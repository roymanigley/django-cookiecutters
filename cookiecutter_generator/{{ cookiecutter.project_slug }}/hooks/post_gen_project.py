import typing
import os

FILE_SPLIT_PATTERN = '--- split:'
FILES_TO_SPLIT = []


def main():
    [split_into_files(file_name) for file_name in FILES_TO_SPLIT]


def split_into_files(file_name_to_split: str) -> None:
    with open(file_name_to_split) as f:
        lines = f.readlines()
        buffer = []
        for line in lines:
            if line.startswith(FILE_SPLIT_PATTERN):
                file_name = line.split(FILE_SPLIT_PATTERN)[1].strip()
                print(file_name)
                write_to_file(file_name, buffer)
                buffer = []
            else:
                buffer.append(line)
    os.remove(file_name_to_split)


def write_to_file(file_name: str, lines: typing.List[str]) -> None:
    with open(file_name, 'w') as f:
        [f.write(line) for line in lines]


if __name__ == '__main__':
    try:
        print('[+] post_gen_project.py started')
        main()
        print('[+] post_gen_project.py completed')
    except Exception as e:
        print(f'[+] post_gen_project.py failed: {e}')
        raise e
