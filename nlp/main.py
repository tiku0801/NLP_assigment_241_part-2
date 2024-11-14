import os
import json
from query_process import QueryDatabase
from query_parser import Parser

class Main:
    def __init__(self) -> None:
        self.querydb = QueryDatabase()
        self.parser = Parser()
    
    def query(self,query): 
        self.querydb.answer(query)

    def parse(self,query):
        self.parser.parse(query)


if __name__ == '__main__':
    programm = Main()  
    programm.parse('How many types of transportation from Ho Chi Minh to Phu Quoc')
    programm.parse('How long does it take to travel to Ho Chi Minh')
    
    programm.parse('Can you repeat all the tours to Da Nang')
    programm.parse('How many types of transportation for the Phu Quoc tour')
