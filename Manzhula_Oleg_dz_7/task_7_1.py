import os


def create_path(mk_path: str):
    if not os.path.exists(mk_path):
        os.makedirs(mk_path, exist_ok=True)


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))
    paths_config = ['my_project/settings',
                    'my_project/mainapp',
                    'my_project/adminapp',
                    'my_project/authapp']
    for name in paths_config:
        create_path(os.path.join(base_dir, name))
