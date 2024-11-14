import nltk
from nltk import load_parser

class Parser:
    def __init__(self) -> None:
        self.cfg = load_parser('input/data/grammar.fcfg')

    def parse(self,query):
        trees = self.cfg.parse_one(query.replace('?','').split())
        answer = str(trees.label()['SEM']).replace(',',' ')


        # --------------------------------------------------------------
        trees = list(self.cfg.parse(query.split()))
        answer = trees[0].label()['SEM']
        print(type(answer))
        print(answer)

        # answer = [s for s in answer if s]
        # q = ' '.join(answer)
        # print(q)
        # # --------------------------------------------------------------
        # answer = [s for s in answer if s]
        # answer = answer.replace('(',' ').replace(')',' ').split()
        # q = ' '.join(answer)
        # print(answer)
    

        # cp = self.cfg
        # # query = 'What cities are located in China'
        # trees = list(cp.parse(query.split()))
        # answer = trees[0].label()['SEM']
        # answer = [s for s in answer if s]
        # q = ' '.join(answer)
        # print(q)
