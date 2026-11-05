---
license: llama2
datasets:
- b-mc2/sql-create-context
language:
- en
metrics:
- accuracy
base_model:
- codellama/CodeLlama-7b-hf
pipeline_tag: text-generation
tags:
- PEFT
- llama
- text-to-sql
- code
- lora
- nlp
- mps
- conversational
model_index:
- name: CodeLlama-7b-SQL-LoRA
  results:
  - task:
      type: text-generation
      name: Text-to-SQL
    dataset:
      name: sql-create-context
      type: b-mc2/sql-create-context
    metrics:
      - type: accuracy
        value: 71.0%
        name: Exact Match
---


# CodeLlama-7b Text-to-SQL-MPS-FineTuned-v4 (Fine-Tuned on Mac MPS)

## Model Description
This is the 4th version of the fine-tuned **CodeLlama-7b-hf** specifically optimized for **Text-to-SQL** tasks. 
It was trained on a **MacBook Pro M3** using **MPS (Metal Performance Shaders)** acceleration.
This version demostrate that MPS fine tuning can achieve **71.0%** accuracy based on **Exact Match**. 

### Origin & Adaptation
This project is adapted from the **Microsoft "Generative AI for Beginners" Course (Chapter 18: Fine-tuning)**.
- Original Source: [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners)
- Old Version: psychologyphd/CodeLlama-7b-Text-to-SQL-mps-finetuned 
- **Modifications**: tons of modifications to achieve this accuracy. 

## Evaluation Results

The model was evaluated on a held-out test set from the `b-mc2/sql-create-context` dataset. 

| Metric | Value |
| --- | --- |
| **Accuracy** | **71.0%** |
| Evaluation Method | **Exact Match** |
| Framework | PEFT (LoRA) |

### Performance Notes:
* **Contextual Understanding:** The model shows strong performance in mapping natural language questions to complex SQL schemas provided in the context.
* **Limitations:** 71% accuracy indicates that while the model handles standard filter and aggregates well,
* eyeballing the results, the model struggles with table that needs to be created(index 10,39) possibly due to lack of such complex training examples,
* quotes (actually those cases should be considered correct because schema is not given),
* and applying correct function in selection (such as count). 
  
### Example Output:
* **Correct Output:**
  
🔹 Index: 0
🎯 Truth: SELECT home FROM table_name_11 WHERE date = "16 april 2008"
🤖 Gen  : select home from table_name_11 where date = '16 april 2008'
----------------------------------------
🔹 Index: 1
🎯 Truth: SELECT MAX(game) FROM table_name_34 WHERE team = "celtics" AND high_assists = "hedo türkoğlu (4)"
🤖 Gen  : select max(game) from table_name_34 where team = 'celtics' and high_assists = 'hedo türkoğlu (4)'
----------------------------------------
🔹 Index: 2
🎯 Truth: SELECT country FROM table_name_17 WHERE score = 72 - 66 - 72 = 210
🤖 Gen  : select country from table_name_17 where score = 72 - 66 - 72 = 210
----------------------------------------
🔹 Index: 3
🎯 Truth: SELECT AVG(gold) FROM table_name_66 WHERE sport = "athletics" AND silver > 42
🤖 Gen  : select avg(gold) from table_name_66 where sport = 'athletics' and silver > 42
----------------------------------------
🔹 Index: 4
🎯 Truth: SELECT club FROM table_name_36 WHERE head_coach = "casemiro mior"
🤖 Gen  : select club from table_name_36 where head_coach = 'casemiro mior'
----------------------------------------
🔹 Index: 5
🎯 Truth: SELECT COUNT(high_points) FROM table_23186738_6 WHERE record = "5-17"
🤖 Gen  : select count(high_points) from table_23186738_6 where record = '5-17'
----------------------------------------
🔹 Index: 6
🎯 Truth: SELECT date FROM table_name_10 WHERE away_team = "st kilda"
🤖 Gen  : select date from table_name_10 where away_team = 'st kilda'
----------------------------------------
🔹 Index: 8
🎯 Truth: SELECT sail_number FROM table_25595209_1 WHERE skipper = "Matt Allen"
🤖 Gen  : select sail_number from table_25595209_1 where skipper = 'matt allen'
----------------------------------------
🔹 Index: 9
🎯 Truth: SELECT venue FROM table_name_74 WHERE home_team = "melbourne"
🤖 Gen  : select venue from table_name_74 where home_team = 'melbourne'
----------------------------------------
🔹 Index: 11
🎯 Truth: SELECT time FROM table_name_1 WHERE event = "k-1 the challenge 1999"
🤖 Gen  : select time from table_name_1 where event = 'k-1 the challenge 1999'
----------------------------------------
🔹 Index: 12
🎯 Truth: SELECT COUNT(gold) FROM table_name_34 WHERE silver = 2 AND total < 7
🤖 Gen  : select count(gold) from table_name_34 where silver = 2 and total < 7
----------------------------------------
🔹 Index: 13
🎯 Truth: SELECT player FROM table_name_92 WHERE team = "chicago bulls"
🤖 Gen  : select player from table_name_92 where team = 'chicago bulls'
----------------------------------------
🔹 Index: 14
🎯 Truth: SELECT player FROM table_2679061_12 WHERE college_junior_club_team = "Litvinov (Czechoslovakia)"
🤖 Gen  : select player from table_2679061_12 where college_junior_club_team = 'litvinov (czechoslovakia)'
----------------------------------------
🔹 Index: 15
🎯 Truth: SELECT DISTINCT name FROM instructor ORDER BY name
🤖 Gen  : select distinct name from instructor order by name
----------------------------------------
🔹 Index: 17
🎯 Truth: SELECT school FROM table_11677691_2 WHERE college = "South Carolina"
🤖 Gen  : select school from table_11677691_2 where college = 'south carolina'
----------------------------------------
🔹 Index: 19
🎯 Truth: SELECT venue FROM table_name_47 WHERE score = "0–0"
🤖 Gen  : select venue from table_name_47 where score = '0–0'
----------------------------------------
🔹 Index: 20
🎯 Truth: SELECT name FROM table_name_88 WHERE nationality = "france" AND lane < 3
🤖 Gen  : select name from table_name_88 where nationality = 'france' and lane < 3
----------------------------------------
🔹 Index: 21
🎯 Truth: SELECT nation FROM table_name_54 WHERE total < 19 AND bronze < 1
🤖 Gen  : select nation from table_name_54 where total < 19 and bronze < 1
----------------------------------------
🔹 Index: 22
🎯 Truth: SELECT record FROM table_name_72 WHERE date = "october 27"
🤖 Gen  : select record from table_name_72 where date = 'october 27'
----------------------------------------
🔹 Index: 23
🎯 Truth: SELECT score FROM table_name_33 WHERE date = "october 17, 2007"
🤖 Gen  : select score from table_name_33 where date = 'october 17, 2007'
----------------------------------------
🔹 Index: 24
🎯 Truth: SELECT nationality FROM table_name_60 WHERE position = "forward" AND years_for_grizzlies = "2011"
🤖 Gen  : select nationality from table_name_60 where position = 'forward' and years_for_grizzlies = '2011'
----------------------------------------
🔹 Index: 25
🎯 Truth: SELECT surface FROM table_name_45 WHERE partner = "galina voskoboeva"
🤖 Gen  : select surface from table_name_45 where partner = 'galina voskoboeva'
----------------------------------------
🔹 Index: 27
🎯 Truth: SELECT rank FROM table_name_96 WHERE bronze < 7 AND nation = "norway"
🤖 Gen  : select rank from table_name_96 where bronze < 7 and nation = 'norway'
----------------------------------------
🔹 Index: 28
🎯 Truth: SELECT sanskrt FROM table_name_38 WHERE japanese = "jayana"
🤖 Gen  : select sanskrt from table_name_38 where japanese = 'jayana'
----------------------------------------
🔹 Index: 32
🎯 Truth: SELECT format FROM table_name_74 WHERE type = "primary" AND call_letters = "kbjs"
🤖 Gen  : select format from table_name_74 where type = 'primary' and call_letters = 'kbjs'
----------------------------------------
🔹 Index: 34
🎯 Truth: SELECT MIN(byes) FROM table_name_3 WHERE against = 1946 AND wins > 2
🤖 Gen  : select min(byes) from table_name_3 where against = 1946 and wins > 2
----------------------------------------
🔹 Index: 36
🎯 Truth: SELECT date FROM table_name_61 WHERE attendance = "79,431"
🤖 Gen  : select date from table_name_61 where attendance = '79,431'
----------------------------------------
🔹 Index: 38
🎯 Truth: SELECT MIN(manhunt_international) FROM table_30018460_1
🤖 Gen  : select min(manhunt_international) from table_30018460_1
----------------------------------------
🔹 Index: 40
🎯 Truth: SELECT COUNT(*) FROM device
🤖 Gen  : select count(*) from device
----------------------------------------
🔹 Index: 42
🎯 Truth: SELECT COUNT(played) FROM table_name_42 WHERE position < 4 AND team = "witton albion"
🤖 Gen  : select count(played) from table_name_42 where position < 4 and team = 'witton albion'
----------------------------------------
🔹 Index: 43
🎯 Truth: SELECT score FROM table_name_98 WHERE loss = "embree (1-2)"
🤖 Gen  : select score from table_name_98 where loss = 'embree (1-2)'
----------------------------------------
🔹 Index: 44
🎯 Truth: SELECT date_of_appointment FROM table_name_91 WHERE manner_of_departure = "sacked"
🤖 Gen  : select date_of_appointment from table_name_91 where manner_of_departure = 'sacked'
----------------------------------------
🔹 Index: 45
🎯 Truth: SELECT catalog FROM table_name_33 WHERE label = "grilled cheese"
🤖 Gen  : select catalog from table_name_33 where label = 'grilled cheese'
----------------------------------------
🔹 Index: 46
🎯 Truth: SELECT medal FROM table_name_48 WHERE games = "2008 beijing" AND sport = "taekwondo"
🤖 Gen  : select medal from table_name_48 where games = '2008 beijing' and sport = 'taekwondo'
----------------------------------------
🔹 Index: 47
🎯 Truth: SELECT engine FROM table_name_49 WHERE team = "arciero racing"
🤖 Gen  : select engine from table_name_49 where team = 'arciero racing'
----------------------------------------
🔹 Index: 49
🎯 Truth: SELECT municipality FROM table_name_53 WHERE station = "benson street"
🤖 Gen  : select municipality from table_name_53 where station = 'benson street'
----------------------------------------

* **Wrong Output:**

🔹 Index: 7
🎯 Truth: SELECT AVG(drawn) FROM table_name_45 WHERE points_1 = "33" AND goals_against = 45 AND played < 28
🤖 Gen  : select avg(drawn) from table_name_45 where points_1 = 33 and goals_against = 45 and played < 28
----------------------------------------
🔹 Index: 10
🎯 Truth: SELECT major, age FROM student WHERE NOT stuid IN (SELECT T1.stuid FROM student AS T1 JOIN has_pet AS T2 ON T1.stuid = T2.stuid JOIN pets AS T3 ON T3.petid = T2.petid WHERE T3.pettype = 'cat')
🤖 Gen  : select t1.major, t1.age from student as t1 join has_pet as t2 on t1.stuid = t2.stuid join pets as t3 on t2.petid = t3.petid where t3.pettype <> 'cat'
----------------------------------------
🔹 Index: 16
🎯 Truth: SELECT COUNT(goals) FROM table_name_49 WHERE goal_ratio < 0.8 AND games = 56
🤖 Gen  : select goals from table_name_49 where goal_ratio < 0.8 and games = 56
----------------------------------------
🔹 Index: 18
🎯 Truth: SELECT SUM(lost) FROM table_name_86 WHERE points = 11 AND drawn > 1
🤖 Gen  : select sum(lost) from table_name_86 where points > 11 and drawn > 1
----------------------------------------
🔹 Index: 26
🎯 Truth: SELECT reward FROM table_1893276_2 WHERE air_date = "October 6, 2005"
🤖 Gen  : select count(reward) from table_1893276_2 where air_date = 'october 6, 2005'
----------------------------------------
🔹 Index: 29
🎯 Truth: SELECT name FROM table_name_19 WHERE dcsf_number = 3373
🤖 Gen  : select name from table_name_19 where dcsf_number = '3373'
----------------------------------------
🔹 Index: 30
🎯 Truth: SELECT COUNT(average) FROM table_12094609_1 WHERE evening_gown = "8.988"
🤖 Gen  : select count(average) from table_12094609_1 where evening_gown = 8.988
----------------------------------------
🔹 Index: 31
🎯 Truth: SELECT writer_s_ FROM table_17810099_3 WHERE episode__number = "14"
🤖 Gen  : select writer_s_ from table_17810099_3 where episode__number = 14
----------------------------------------
🔹 Index: 33
🎯 Truth: SELECT location FROM table_name_65 WHERE round = 3 AND method = "decision"
🤖 Gen  : select location from table_name_65 where round = '3' and method = 'won or loss by a decision'
----------------------------------------
🔹 Index: 35
🎯 Truth: SELECT written_by FROM table_27823359_1 WHERE season__number = "23"
🤖 Gen  : select written_by from table_27823359_1 where season__number = 23
----------------------------------------
🔹 Index: 37
🎯 Truth: SELECT attendance FROM table_name_53 WHERE game_site = "bye"
🤖 Gen  : select count(attendance) from table_name_53 where game_site = 'bye'
----------------------------------------
🔹 Index: 39
🎯 Truth: SELECT T1.fname, T1.lname FROM student AS T1 JOIN lives_in AS T2 ON T1.stuid = T2.stuid WHERE T2.dormid IN (SELECT T3.dormid FROM has_amenity AS T3 JOIN dorm_amenity AS T4 ON T3.amenid = T4.amenid WHERE T4.amenity_name = 'TV Lounge')
🤖 Gen  : select t1.fname, t1.lname from student as t1 join lives_in as t2 on t1.stuid = t2.stuid join has_amenity as t3 on t2.dormid = t3.dormid join dorm_amenity as t4 on t3.amenid = t4.amenid where t4.amenity_name = 'tv lounge' group by t1.st
----------------------------------------
🔹 Index: 41
🎯 Truth: SELECT attendance FROM table_name_65 WHERE tie_no = "4"
🤖 Gen  : select count(attendance) from table_name_65 where tie_no = '4'
----------------------------------------
🔹 Index: 48
🎯 Truth: SELECT home_team AS score FROM table_name_49 WHERE away_team = "hawthorn"
🤖 Gen  : select home_team from table_name_49 where away_team = 'hawthorn'
----------------------------------------


## How to Use
See how_to_use_v4.ipynb. 
- mps pipeline actually works in fine tuning. For this light weighted how to use, I still use model.generate. . 

## Training Details
- **Hardware**: Mac M3 (MPS)
- **Base Model**: [codellama/CodeLlama-7b-hf](https://huggingface.co/codellama/CodeLlama-7b-hf)
- **Dataset**: [b-mc2/sql-create-context](https://huggingface.co/datasets/b-mc2/sql-create-context)
- **Technique**: LoRA (PEFT)