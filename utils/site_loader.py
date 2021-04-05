import os
from typing import List

def load_site_path(top: str) -> List[str]:
    file_list = list()
    for c_dir, _, files in os.walk(top):
        files = [f'{c_dir}/{file}' for file in files]
        file_list.extend(files)

    return file_list