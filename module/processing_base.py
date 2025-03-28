from SinCity.colors import GREEN, RESET, RED
from module.Recording import recordingResult
import csv

counter_number = 0

number_ru = set()
number_uk = set()
number_by = set()

def CheckPhone(data:str):
    global number_ru, number_uk, number_by
    phone = None

    # номера ru и казахстан
    if len(data) == 11:
        if data[0] == '7'or data[0] == '8':
            phone = data
            number_ru.add(phone)
            recordingResult(location='ru', phone=phone)

    # номера украины
    if len(data) == 10:
        if data[0:3] == '380':
            phone = data
            number_uk.add(phone)
            recordingResult(location='uk', phone=phone)
                
    # номера беларуси
    if len(data) == 12:
        if data[0:3] == '375':
            phone = data
            number_by.add(phone)
            recordingResult(location='be', phone=phone)
    
    return phone

def ProcessingTXT(base:str):
    global number_ru, number_uk, number_by
    global counter_number
    with open(base, 'r') as file:
        for info in file.readlines():
            all_data = info.split()
            if ',' in info:all_data = info.replace(',', ' ')
            if '.' in info:all_data = info.replace('.', ' ')
            if '[' in info:all_data = info.replace('[', ' ')
            if ']' in info:all_data = info.replace(']', ' ')
            if ':' in info:all_data = info.split(':')
            if '|' in info:all_data = info.split('|')
            phone = None
            for data in all_data:
                if '\n' in data:data = data.split('\n')[0]

                if '+' in data:data = data.split('+')[1]
                 
                phone = CheckPhone(data=data)
                if phone != None:
                    counter_number+=1
                    print(f'[{counter_number}] {base}\t{phone}')


    print(
            f'Номеров РФ: {len(number_ru)}\n'
            f'Номеров Украины: {len(number_uk)}\n'
            f'Номеров Беларусии: {len(number_by)}'
            )

def ProcessingCSV(base:str):
    global number_ru, number_by, number_uk
    global counter_number
    with open(base, 'r') as file:
        for info in file.readlines():
            all_data = info.split()
            if ':' in info:all_data = info.split(':')
            if '|' in info:all_data = info.split('|')
            phone = None
            for data in all_data:
                string_csv = data.split(',') 
                for data in string_csv:

                    if '\n' in data:data = data.split('\n')[0]

                    if '+' in data:data = data.split('+')[1]
                 
                    phone = CheckPhone(data=data)
                    if phone != None:
                        counter_number+=1
                        print(f'[{counter_number}] {base}\t{phone}')

    print(
            f'Номеров РФ: {len(number_ru)}\n'
            f'Номеров Украины: {len(number_uk)}\n'
            f'Номеров Беларусии: {len(number_by)}'
            )

def ProcessingBase(base:str):
    try:
        if '.txt' in base:ProcessingTXT(base=base)
        if '.csv' in base:ProcessingCSV(base=base)
    except UnicodeDecodeError:print(
            f'{RED}Поменяй кодировку, ублюдок!{RESET}\n'
            f'{RED}Для слепых показываю файл: "{base}"{RESET}'
            )
