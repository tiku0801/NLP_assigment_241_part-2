import os

def create_input_file(q_dict,path_to_folder):
    for index,question in q_dict.items():
        with open(f'{path_to_folder}/p2-q-{index}.txt','w') as f:
            f.write(question)

def write_to_file_with_func(path_to_q_folder,path_to_a_folder,func): 
    for file_path in os.listdir(path_to_q_folder):
        if os.path.isfile(os.path.join(path_to_q_folder, file_path)):
            question = ''
            with open(f'{path_to_q_folder}/{file_path}','r') as q_f:
                question = q_f.read()
            if 'answer' in path_to_a_folder:
                with open(f'{path_to_a_folder}/answer-{file_path}','w') as a_f:
                    a_f.write(func(question))
            if 'parse-tree' in path_to_a_folder:
                with open(f'{path_to_a_folder}/tree-{file_path}','w') as a_f:
                    a_f.write(func(question))
