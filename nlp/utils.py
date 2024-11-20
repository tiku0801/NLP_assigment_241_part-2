import os

def create_input_file(q_dict,path_to_folder,mode = 'standard'):
    if mode == 'standard':
        for index,question in q_dict.items():
            with open(f'{path_to_folder}/p2-q-{index}.txt','w') as f:
                f.write(question)

def write_to_file_with_func(path_to_q_folder,path_to_a_folder,func,mode ='standard'): 
    if mode == 'standard':
        for file_path in os.listdir(path_to_q_folder):
            if os.path.isfile(os.path.join(path_to_q_folder, file_path)):
                question = ''
                with open(f'{path_to_q_folder}/{file_path}','r') as q_f:
                    question = q_f.read()
                with open(f'{path_to_a_folder}/{file_path}','w') as a_f:
                    a_f.write(func(question))