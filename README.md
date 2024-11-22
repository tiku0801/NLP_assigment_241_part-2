# NLP_assigment_241_part-2 HCMUT

## 1. Description
This project is a reply system about tour informaton using NLP.

Inputs are question in natural language. They will be analyzed to logical forms, and then the logical structures are parsed into query sentences.

The system will execute the query and return the result by looking up in the database

The simple CFG used in this project is quite simple which is located in `nlp/input/data/grammar.fcfg`

## 2. Requirement
- python 3.8
- NLTK 3.9

## 3. Structure
4 python files:
- [main.py](main.py): The main function of the program (run from this).
- [query_parser.py](query_parser.py): Parser module - includes functions to parse from natural language to logical form
- [query_process.py](query_process.py): Query execution module - includes functions to translate from logical form to query form, execute queries to get the data in the database
- [utils.py](utils.py): Utility module - includes functions to read/write data to .txt file

Other folders:
- input: contains 2 folders
    - data: 
        - [database.json](database.json): database of the system
        - [grammar.fcfg](grammar.fcfg): simple cfg of the project
    - question: input questions
- output: contains answers of the former which are divided into 2 folders 
    - answer: final answers of the system
    - parse-tree: logical forms of the questions

## 4. Running
Windows env (in `/nlp`):
```
python main.py
```
Or:
```
sh util.sh test
```

## 5. Result:
Question:
```
How long does it take to travel from Ho Chi Minh to Nha Trang?
```
Logical form:
```
WHQUERY(HOWLONG(?t),(ARRVIE(?v3,TIME(?t)) & FROM(?v3,NAME(hcm1,'HCM')) & TO(?v3,NAME(nt1,'NT'))))
```
Answer:
```
It takes 5:00 HR to travel to Nha Trang
```

## 6. Future work:
- Make the grammar more general, now is specified with some situations
- Clearer grammar rules
- Dependency grammar?
- Vietnamese support
