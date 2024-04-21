import typing
import os

FILE_SPLIT_PATTERN = '--- split:'
FILES_TO_SPLIT = [
    'src/app/shared/models/domain/__cookiecutter__.ts',
    'src/app/shared/resolvers/__cookiecutter__.resolver.ts',
    'src/app/shared/services/api/__cookiecutter__.service.ts',
    'src/app/components/domain/__cookiecutter__/__cookiecutter__.module.ts',
    'src/app/components/domain/__cookiecutter__/__cookiecutter__-list/__cookiecutter__-list.component.ts',
    'src/app/components/domain/__cookiecutter__/__cookiecutter__-list/__cookiecutter__-list.component.html',
    'src/app/components/domain/__cookiecutter__/__cookiecutter__-list/__cookiecutter__-list.component.scss',
    'src/app/components/domain/__cookiecutter__/__cookiecutter__-detail/__cookiecutter__-detail.component.ts',
    'src/app/components/domain/__cookiecutter__/__cookiecutter__-detail/__cookiecutter__-detail.component.html',
    'src/app/components/domain/__cookiecutter__/__cookiecutter__-detail/__cookiecutter__-detail.component.scss',
    'src/app/components/domain/__cookiecutter__/__cookiecutter__-edit/__cookiecutter__-edit.component.ts',
    'src/app/components/domain/__cookiecutter__/__cookiecutter__-edit/__cookiecutter__-edit.component.html',
    'src/app/components/domain/__cookiecutter__/__cookiecutter__-edit/__cookiecutter__-edit.component.scss',
    'src/app/components/domain/__cookiecutter__/__cookiecutter__-delete/__cookiecutter_-delete.component.ts',
    'src/app/components/domain/__cookiecutter__/__cookiecutter__-delete/__cookiecutter_-delete.component.html',
    'src/app/components/domain/__cookiecutter__/__cookiecutter__-delete/__cookiecutter_-delete.component.scss',
]


def main():
    [split_into_files(file_name) for file_name in FILES_TO_SPLIT]


def split_into_files(file_name_to_split: str) -> None:
    with open(file_name_to_split) as f:
        lines = f.readlines()
        buffer = []
        for line in lines:
            if line.startswith(FILE_SPLIT_PATTERN):
                file_name = line.split(FILE_SPLIT_PATTERN)[1].strip()
                write_to_file(file_name, buffer)
                buffer = []
            else:
                buffer.append(line)
    os.remove(file_name_to_split)


def write_to_file(file_name: str, lines: typing.List[str]) -> None:
    parent_dir = os.path.abspath(os.path.join(file_name, os.path.pardir))
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir)
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
