from SinCity.colors import YELLOW, RED, RESET, BLUE, GREEN 
from manifest import dir_base
import os

def ListBase():
    list_txt = []
    list_csv = []
    
    for base in os.listdir(dir_base):
        base = f'{dir_base}/{base}'
        if '.txt' in base:list_txt.append(base)
        if '.csv' in base:list_csv.append(base)

    return list_txt, list_csv
    
def CheckBase():
    list_txt, list_csv = ListBase()
    
    all_base = []

    if len(list_txt) > 0:print(f'\n{YELLOW}BASE TXT{RESET}')
    number_txt = 0
    for base_txt in list_txt:
        number_txt+=1
        all_base.append(base_txt)
        print(f'{GREEN}[{number_txt}]{RESET} {BLUE}{base_txt}{RESET}')
    
    if len(list_csv) > 0:print(f'\n{YELLOW}BASE CSV{RESET}')
    number_csv = 0
    for base_csv in list_csv:
        number_csv+=1
        all_base.append(base_csv)
        print(f'{GREEN}[{number_csv}]{RESET} {RED}{base_csv}{RESET}')

    return all_base, list_txt, list_csv
