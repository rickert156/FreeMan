from manifest import dir_base, archive_base
from SinCity.colors import RED, RESET
import os

def StartProject():
    status_base_dir = False
    if not os.path.exists(dir_base):
        os.makedirs(dir_base)
        print(f'{RED}Создана директория для хранения баз{RESET}')
    else:status_base_dir = False

    if not os.path.exists(archive_base):os.makedirs(archive_base)


    return status_base_dir

