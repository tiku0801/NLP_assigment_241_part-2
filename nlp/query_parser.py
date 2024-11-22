import nltk
import os
from nltk import load_parser
from query_process import QueryDatabase
class Parser:
    def __init__(self,mode = 'standard') -> None:
        if mode == 'docker':
            self.cfg = load_parser(os.getcwd() +'/nlp/input/data/grammar.fcfg')
            self.query_proccesor = QueryDatabase('docker')
        else:
            self.cfg = load_parser('input/data/grammar.fcfg')
            self.query_proccesor = QueryDatabase()
    
    def parse(self,query):
        '''
        programm.parse('How many types of transportation from Ho Chi Minh to Phu Quoc')
        programm.parse('How long does it take to travel to Ho Chi Minh')
        programm.parse('Can you repeat all the tours to Da Nang')
        programm.parse('How many types of transportation for the Phu Quoc tour')
        programm.parse('What type of transportation is used for the Nha Trang tour')

        WHQUERY(HOWMANY(?v),(TYPE(?v) & OF(?v,(TRANSPORTATION(?v4) & FROM(?v4,NAME(hcm1,'HCM')) & TO(?v4,NAME(pq1,'PQ'))))))
        WHQUERY(HOWLONG(?t),(ARRVIE(?v3,TIME(?t)) & TO(?v3,NAME(hcm1,'HCM'))))
        QUERY(DO(LIST(ALL(DET((TOUR(?v3) & TO(?v3,NAME(dn1,'DN'))))),YOU)))
        WHQUERY(HOWMANY(?v),(TYPE(?v) & OF(?v,(TRANSPORTATION(?v6) & FOR(?v6,DET(NAME(pq1,'PQ',TOUR(?v4))))))))
        WHQUERY(WHAT(?v),BE(USE(FOR(?v,DET(NAME(nt1,'NT',TOUR(?v4))))),(TYPE(?v) & OF(?v,TRANSPORTATION(?v6)))))
        '''
        try:
            trees = self.cfg.parse_one(query.replace('?','').split())
            parsed_sen = str(trees.label()['SEM'])
        except:
            # cannot parse
            return None
        return parsed_sen


    def answer(self, query):
        return self.query_proccesor.answer(self.parse(query))