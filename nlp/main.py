import os
import json
from query_parser import Parser
from utils import *
input = {'1': 'Can you repeat all the tours?',
         '2': 'How long does it take to travel from Ho Chi Minh to Nha Trang?',
         '3': 'How many tours to Phu Quoc?',
         '4': 'How many types of transportation?',
         '5': 'How many types of transportation to Phu Quoc?',
         '6': 'What type of transportation is used for the Nha Trang tour?',
         '7': 'Can you repeat all the tours to Da Nang?',
         '8': 'Hi',
         '9': 'How long does it take to travel from Ho Chi Minh?'
         }
class Main:
    def __init__(self) -> None:
        self.parser = Parser()

    def parse_to_answer(self,query):
        return self.parser.answer(query)

    def parse_to_tree(self,query):
        tree = self.parser.parse(query)
        if tree is None : return ''
        return tree
    
if __name__ == '__main__':
    programm = Main()
    create_input_file(input,'input/question')
    write_to_file_with_func('input/question','output/answer',programm.parse_to_answer)
    write_to_file_with_func('input/question','output/parse-tree',programm.parse_to_tree)