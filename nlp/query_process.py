import json

class QueryDatabase:
    def __init__(self) -> None:
        with open('input/data/database.json','r') as database_file:
            self.db = json.load(database_file)['database']
    
    def parse_query(self, query):
        '''
        return (type_query, table, tour_code)
        Example:
            1. SELECT ALL IN TOURS
                table: TOURS
                tour_code: all
        '''
        tokens = query.lower().split()
    
        return tokens[-1], tokens[1]

    def query_excute(self, parsed_query):
        qtable, qcode = parsed_query

        qtable = qtable.upper()
        qcode = qcode.upper()

        if qcode == 'ALL':
            return self.db[qtable]
        else:
            return self.db[qtable][qcode]
    
    def print_answer(self, excuted_query):
        answer = ''
        if excuted_query is not None:
            if type(excuted_query) is list:
                for item in excuted_query:
                    answer += str(item) + ', '
                answer = answer[:-2]
            else:
                answer = excuted_query
            print(answer)
        else:
            print("I can not understand! :'(")

    def answer(self, query):
        self.print_answer(self.query_excute(self.parse_query(query)))
    