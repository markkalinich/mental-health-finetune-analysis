# Reddit C-SSRS user-level gold standard (Gaur et al. 2019)

Psychiatrist-labeled 5-class C-SSRS severity. Unit is the user. Metrics copy
`jpsain/Suicide-Severity` `models/5-Label_Classification.py`: graded precision,
recall, F1, and ordinal error. The model emits one of the five label strings.
No JSON schema.

- Code: https://github.com/jpsain/Suicide-Severity
- Upstream clone: `/shared/mkalinic/benchmarks/reddit_cssrs/upstream-github`
- Prepared: `/shared/mkalinic/benchmarks/reddit_cssrs/prepared/standard_user_level.csv`
- Raw Zenodo: `/shared/mkalinic/benchmarks/reddit_cssrs/raw/500_Reddit_users_posts_labels.csv`
- Rebuild: `python -m orchestration.prepare_cssrs_gold`

Prepared columns: `item_id`, `text`, `standard_label`.
