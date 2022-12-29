def is_cd_command(split_command: list):
    return split_command[0] == "$" and split_command[1] == "cd"


def is_subdir(split_command: list):
    return split_command[0] == "dir"


def is_ls(split_command: list):
    return split_command[-1] == "ls"


def build_dir_name(path: list, directory: str):
    return ''.join(path) + directory


def calculate_dir_size(dir_infos: dict, directory: str):
    info = dir_infos[directory]
    if len(info['subdirs']) == 0:
        return info['size']
    for sub_dir in info['subdirs']:
        info['size'] += calculate_dir_size(dir_infos, sub_dir)
    return info['size']


filename = input()
# parte 1
with open(filename, 'r') as file:
    dir_info = dict()
    dir_stack = list()

    # calcular primeiro os tamanhos dos arquivos e os subdiretórios
    for command in file:
        command = command.strip().split()

        current_dir = build_dir_name(dir_stack, '') if len(dir_stack) > 0 else ''
        if is_cd_command(command):
            if command[-1] != "..":  # deu cd pra um diretório, guarda na pilha pra saber onde estamos
                dir_stack.append(command[-1])
            else:  # voltamos pro diretório anterior, só dar pop na pilha pra gente se situar
                current_dir = dir_stack.pop()
        elif is_ls(command):  # vai listar conteúdo do diretório atual, então inicializa as informações dele
            dir_info[current_dir] = {'size': 0, 'subdirs': []}
        elif is_subdir(command):  # adiciona subdiretório na lista de subdiretórios do diretório atual
            dir_info[current_dir]['subdirs'].append(build_dir_name(dir_stack, command[-1]))
        else:  # é um arquivo, soma tamanho dele
            file_size = int(command[0])
            dir_info[current_dir]['size'] += file_size

    # calcula resultado do desafio
    calculate_dir_size(dir_info, '/')
    result = 0
    for directory in dir_info:
        info = dir_info[directory]
        if info['size'] <= 100000:
            result += info['size']

    # parte 2
    dir_sizes = list()
    for directory in dir_info:
        dir_sizes.append((directory, dir_info[directory]['size']))
    dir_sizes.sort(key=lambda x: x[1]) #ordena ascendente comparando tamanhos dos diretorios
    needed_space = 30000000 - (70000000 - dir_info['/']['size'])
    for size in dir_sizes:
        if size[1] >= needed_space:
            print(size)
            break

