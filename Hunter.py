from SinCity.colors import RED, GREEN, BLUE, RESET, YELLOW
from module.miniTools import StartProject
from module.checker import CheckBase
from module.processing_base import ProcessingBase
from manifest import version, dir_base, archive_base
import os, shutil


def DataHunter():
    print(f'{RED}Data Hunter: {version}{RESET}')
    dir_base = StartProject()

    all_base, base_txt, base_csv = CheckBase()
    input(f'\n{GREEN}click enter...{RESET}')
    for base in all_base:
        print(f'Processing base: {base}...')
        ProcessingBase(base=base)
        input('...')

        file = base.split('/')[1]
        shutil.move(base, f'{archive_base}/{file}')

try: 
    DataHunter()
except KeyboardInterrupt:print(f'{RED}\nExit...{RESET}')
