import json
import os
class QueryDatabase:
    def __init__(self,mode = 'standard') -> None:
        if mode == 'docker':
            with open(os.getcwd() +'/nlp/input/data/database.json','r') as database_file:
                self.db = json.load(database_file)['database']
        else:
            with open('input/data/database.json','r') as database_file:
                self.db = json.load(database_file)['database']
    def parse_query(self,sen):
        '''
        INPUT: PARSED SENTENCE
        WHQUERY(HOWMANY(?v),(TYPE(?v) & OF(?v,(TRANSPORTATION(?v4) & FROM(?v4,NAME(hcm1,'HCM')) & TO(?v4,NAME(pq1,'PQ'))))))
        -> SELECT PQ IN BY
        WHQUERY(HOWLONG(?t),(ARRVIE(?v3,TIME(?t)) & TO(?v3,NAME(hcm1,'HCM'))))
        -> SELECT HCM IN RUNTIME
        QUERY(DO(LIST(ALL(DET((TOUR(?v3) & TO(?v3,NAME(dn1,'DN'))))),YOU)))
        -> SELECT DN IN DTIME
        WHQUERY(HOWMANY(?v),(TYPE(?v) & OF(?v,(TRANSPORTATION(?v6) & FOR(?v6,DET(NAME(pq1,'PQ',TOUR(?v4))))))))
        -> SELECT PQ IN BY
        WHQUERY(WHAT(?v),BE(USE(FOR(?v,DET(NAME(nt1,'NT',TOUR(?v4))))),(TYPE(?v) & OF(?v,TRANSPORTATION(?v6)))))
        -> SELECT NT IN BY
        OUTPUT: query_code, query_table
        EXAMPLE:
            - SELECT PQ IN BY -> PQ,BY
            - SELECT HCM IN RUNTIME -> HCM,RUNTIME
        '''
        if sen is None: 
            return 'UNKNOWN','UNKNOWN'
        dest = 'ALL'
        table = 'UNKNOWN'

        to_str = sen.find('TO')
        for_str = sen.find('FOR')
        if to_str >= 0:
            dest_str = sen[to_str:]
            if 'NAME' in dest_str:
                if "'DN'" in dest_str: dest = 'DN'
                elif "'PQ'" in dest_str: dest = 'PQ' 
                elif "'NT'" in dest_str: dest = 'NT' 
                else: dest = 'unknown'
        if for_str >= 0:
            dest_str = sen[for_str:]
            if 'NAME' in dest_str:
                if "'DN'" in dest_str: dest = 'DN'
                elif "'PQ'" in dest_str: dest = 'PQ' 
                elif "'NT'" in dest_str: dest = 'NT' 
                else: dest = 'unknown'
        if 'WHQUERY' in sen:
            if 'HOWLONG' in sen:
                table = 'RUNTIME'
            elif 'HOWMANY' in sen or 'WHAT' in sen:
                if 'HOWMANY' in sen:
                    variable = sen[sen.find('HOWMANY'):]
                elif 'WHAT' in sen:
                    variable = sen[sen.find('WHAT'):]
                variable = variable[variable.find('(')+1:variable.find(')')]
                if 'TYPE' in sen and 'TRANSPORTATION' in sen and 'OF' in sen:
                    var_type = sen[sen.find('TYPE'):]
                    var_type = var_type[var_type.find('(')+1:var_type.find(')')]
                    if var_type == variable: 
                        table = 'BY'
                        return dest,table
                if 'TOUR' in sen:
                    var_tour = sen[sen.find('TOUR'):]
                    var_tour = var_tour[var_tour.find('(')+1:var_tour.find(')')]
                    if var_tour == variable:
                        table = 'DTIME'
                        return dest,table
        elif 'QUERY' in sen:
            if 'TOUR' in sen:
                table = 'DTIME'
            elif 'TYPE' in sen and 'TRANSPORTATION' in sen and 'OF' in sen:
                table = 'BY'
        return dest, table

    def query_excute(self, parsed_query):
        qcode, qtable = parsed_query

        qtable = qtable.upper()
        qcode = qcode.upper()
        name = self.db['TOURS']
        print(parsed_query)
        answer = ''
        if qcode == 'UNKNOWN' and qtable == 'UNKNOWN': 
            return "I can not understand! :'("
        if qcode == 'UNKNOWN': return 'There are not any tours to travel to this destination!'
        if qtable == 'UNKNOWN': return 'I do not have any information about this!'
        if qcode == 'ALL':
            if qtable == 'BY':
                data = self.db['BY']
                answer = f'There are {len(data)} types of transportation:'
                answer_list = ''
                for dest,trans in data.items():
                    answer_list += f', {trans} used for {name[dest]} tours'
                answer_list = answer_list[1:] + '.'
                answer += answer_list
            elif qtable == 'RUNTIME':
                data = self.db['RUNTIME']
                answer = f'It takes'
                answer_list = ''
                for dest,time in data.items():
                    answer_list += f', {time} to travel to {name[dest]}'
                answer_list = answer_list[1:] + '.'
                answer += answer_list
            elif qtable == 'DTIME':
                data = self.db['DTIME']
                answer = f'There are'
                answer_tour = ''
                for dest,tour_list in data.items():
                    answer_list = ''
                    tour_num = len(tour_list)
                    if tour_num >= 2:
                        answer_tour = f', {len(tour_list)} tours to travel to {name[dest]}:'
                    else: 
                        answer_tour = f', {len(tour_list)} tour to travel to {name[dest]}:'
                    for tour in tour_list:
                        answer_list += f', {tour}'
                    answer_list = answer_list[1:] # delete ','
                    answer_tour += answer_list
                    answer_tour = answer_tour[1:] + ';' # delete ','
                    answer += answer_tour
                answer = answer[:-1] + '.' #delete ';' and add '.'
        else:
            if qtable == 'BY':
                data = self.db['BY'][qcode]
                answer = f'{data} is used to travel to {name[qcode]}' 
            elif qtable == 'DTIME':
                data = self.db['DTIME'][qcode]
                answer = f'There are {len(data)} to travel to {name[qcode]}: {data}'
            elif qtable == 'RUNTIME':
                data = self.db['RUNTIME'][qcode]
                answer = f'It takes {data} to travel to {name[qcode]}'
        return answer

    def answer(self, query):
        return self.query_excute(self.parse_query(query))
    