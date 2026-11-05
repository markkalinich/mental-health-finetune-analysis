"""Merge the dataset-search agent CSVs (reports/agent-N.csv). Tolerates the row shapes the agents produced in the
safety run (trailing empty column, a missing data_urls column, an extra empty column before source_type, an unquoted
comma in quote). Writes merged.csv and recovered.csv in the search folder and checks coverage against assignments.csv."""
import csv, glob, collections, re, sys
from pathlib import Path
from _common import parser, resolve
a = resolve(parser(__doc__).parse_args())
OUT = a.searches / f"{a.date}-dataset-search"
FIELDS = ['hf_id', 'recovered', 'data_name', 'data_hub_id', 'data_urls', 'source_type', 'source_url',
          'source_names_this_repo', 'pages_read', 'quote', 'queries_tried']
assigned = {r['hf_id']: int(r['agent']) for r in csv.DictReader(open(OUT / 'assignments.csv'))}
rows, problems, done_agents = [], [], set()
for f in sorted(glob.glob(str(OUT / 'reports/agent-*.csv')), key=lambda p: int(re.search(r'agent-(\d+)', p).group(1))):
    n = int(re.search(r'agent-(\d+)', f).group(1))
    with open(f, newline='') as fh:
        rd = csv.reader(fh)
        header = next(rd)
        header = [h.strip() for h in header]
        if header[-1] == '' and len(header) == len(FIELDS) + 1:
            header = header[:-1]
        if header != FIELDS:
            problems.append(f'{f}: header {header}'); continue
        for rec in rd:
            if not rec or not any(c.strip() for c in rec):
                continue
            if len(rec) == len(FIELDS) + 1 and rec[-1].strip() == '':
                rec = rec[:-1]
            # agent-164 wrote 10 columns: data_urls missing (source_type sits at index 4)
            if len(rec) == len(FIELDS) - 1 and rec[4].strip() in ('none', 'current_model_card', 'paper', 'training_script', 'dataset_card'):
                rec = rec[:4] + [''] + rec[4:]
            # agents 38 and 53: an unquoted comma inside quote split it into two fields
            if len(rec) == len(FIELDS) + 1 and rec[-2].strip() and not rec[-1].strip().startswith(('http', '"')) is False:
                pass
            if len(rec) == len(FIELDS) + 1:
                # agents 38 and 53 wrote an extra empty column before source_type
                if rec[5].strip() == '' and rec[6].strip() in ('none', 'current_model_card', 'paper', 'training_script', 'dataset_card'):
                    rec = rec[:5] + rec[6:]
                else:
                    rec = rec[:9] + [rec[9] + ',' + rec[10]] + rec[11:]
            if len(rec) != len(FIELDS):
                problems.append(f'{f}: row has {len(rec)} fields: {rec[:2]}'); continue
            r = dict(zip(FIELDS, (c.strip() for c in rec)))
            r['pages_read'] = '|'.join(p.strip() for p in r['pages_read'].split('|') if p.strip())
            r['recovered'] = r['recovered'].lower()
            if r['recovered'] not in ('yes', 'no'):
                problems.append(f'{f}: recovered={r["recovered"]!r} for {r["hf_id"]}')
            if r['hf_id'] not in assigned:
                problems.append(f'{f}: {r["hf_id"]} not in assignments')
            elif assigned[r['hf_id']] != n:
                problems.append(f'{f}: {r["hf_id"]} belongs to agent {assigned[r["hf_id"]]}')
            r['agent'] = n
            rows.append(r)
    done_agents.add(n)
seen = collections.Counter(r['hf_id'] for r in rows)
dups = [h for h, c in seen.items() if c > 1]
missing = [h for h, a in assigned.items() if a in done_agents and h not in seen]
with (OUT / 'merged.csv').open('w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=['agent'] + FIELDS, lineterminator='\n'); w.writeheader(); w.writerows(rows)
rec = [r for r in rows if r['recovered'] == 'yes']
with (OUT / 'recovered.csv').open('w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=['agent'] + FIELDS, lineterminator='\n'); w.writeheader(); w.writerows(rec)
agents_total = max(assigned.values())
print(f'{len(done_agents)} of {agents_total} agents reported; {len(rows)} rows; {len(rec)} recovered ({len(rec)/max(1,len(rows)):.0%})')
print('source_type of recovered:', collections.Counter(r['source_type'] for r in rec).most_common())
print('pages_read tokens:', collections.Counter(p for r in rows for p in r['pages_read'].split('|') if p).most_common())
if dups: print('DUPLICATE ids:', dups)
if missing: print('MISSING ids from reported agents:', missing)
for p in problems: print('PROBLEM:', p)
not_done = sorted(set(range(1, agents_total + 1)) - done_agents)
print('agents not yet reported:', not_done[:40], '...' if len(not_done) > 40 else '')
