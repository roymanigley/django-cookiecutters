import typing
import os

FILE_SPLIT_PATTERN = '--- split:'
FILES_TO_SPLIT = [
    '__cookiecutter__/model.ts',
    '__cookiecutter__/resolver.ts',
    '__cookiecutter__/service.ts',
    '__cookiecutter__/component.module.ts',
    '__cookiecutter__/list-component/list.component.ts',
    '__cookiecutter__/list-component/list.component.html',
    '__cookiecutter__/list-component/list.component.scss',
    '__cookiecutter__/detail-component/detail.component.ts',
    '__cookiecutter__/detail-component/detail.component.html',
    '__cookiecutter__/detail-component/detail.component.scss',
    '__cookiecutter__/edit-component/edit.component.ts',
    '__cookiecutter__/edit-component/edit.component.html',
    '__cookiecutter__/edit-component/edit.component.scss',
    '__cookiecutter__/delete-component/delete.component.ts',
    '__cookiecutter__/delete-component/delete.component.html',
    '__cookiecutter__/delete-component/delete.component.scss',
]


def main():
    [split_into_files(file_name) for file_name in FILES_TO_SPLIT]
    os.remove('__cookiecutter__')


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
        main()
    except Exception as e:
        print(f'[!] post_gen_project.py failed: {e}')
        raise e
