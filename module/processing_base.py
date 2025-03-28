from SinCity.colors import GREEN, RESET
from module.Recording import recordingResult

counter_number = 0

def ProcessingTXT(base:str):
    number_ru = set()
    number_uk = set()
    number_by = set()
    
    global counter_number
    with open(base, 'r') as file:
        for info in file.readlines():
            all_data = info.split()
            if '[' in info:all_data = info.replace('[', ' ')
            if ']' in info:all_data = info.replace(']', ' ')
            if ':' in info:all_data = info.split(':')
            if '|' in info:all_data = info.split('|')
            phone = None
            for data in all_data:
                if '\n' in data:data = data.split('\n')[0]

                if '+' in data:data = data.split('+')[1]
                
                # номера ru и казахстан
                if len(data) == 11:
                    if data[0] == '7'or data[0] == '8':
                        phone = data
                        number_ru.add(phone)
                        recordingResult(location='ru', phone=phone)
                        counter_number+=1

                # номера украины
                if len(data) == 10:
                    if data[0:3] == '380':
                        phone = data
                        number_uk.add(phone)
                        recordingResult(location='uk', phone=phone)
                        counter_number+=1
                
                # номера беларуси
                if len(data) == 12:
                    if data[0:3] == '375':
                        phone = data
                        number_by.add(phone)
                        recordingResult(location='be', phone=phone)
                        counter_number+=1
                
                if phone != None:print(f'[{counter_number}] {base}\t{phone}')
    print(
            f'Номеров РФ: {len(number_ru)}\n'
            f'Номеров Украины: {len(number_uk)}\n'
            f'Номеров Беларусии: {len(number_by)}'
            )

def ProcessingCSV():
    pass

def ProcessingBase(base:str):
    if '.txt' in base:ProcessingTXT(base=base)
