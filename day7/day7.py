def is_cd_command(split_command: list):
    return split_command[0] == "$" and split_command[1] == "cd"


def is_subdir(split_command: list):
    return split_command[0] == "dir"


def is_ls(split_command: list):
    return split_command[-1] == "ls"


filename = input()
# parte 1
with open(filename, 'r') as file:
    dir_info = dict()
    dir_stack = list()

    for command in file:
        command = command.strip().split()

        if is_cd_command(command):
            if command[-1] != "..":  # deu cd pra um diretório
                dir_info[command[-1]] = {'size': 0, 'subdirs': []}
                dir_stack.append(command[-1])
            else:  # saímos do diretório, calculamos o que tinha pra calcular dentro, podemos calcular o diretório do qual estamos saindo
                current_dir = dir_stack.pop()
                for subdir in dir_info[current_dir]['subdirs']:
                    dir_info[current_dir]['size'] += dir_info[subdir]['size']
        elif is_subdir(command):  # é subdiretório
            dir_info[dir_stack[-1]]['subdirs'].append(command[-1])
        elif is_ls(command):  # ignora ls
            continue
        else:  # é um arquivo
            file_size = int(command[0])
            dir_info[dir_stack[-1]]['size'] += file_size

    # processa os diretório que sobraram
    for current_dir in reversed(dir_stack):
        for subdir in dir_info[current_dir]['subdirs']:
            dir_info[current_dir]['size'] += dir_info[subdir]['size']

    # calcula resultado do desafio
    total_size = 0
    for directory in dir_info:
        info = dir_info[directory]
        total_size += info['size'] if info['size'] <= 100000 else 0
    print(dir_info)
    print(total_size)
