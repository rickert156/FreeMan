from SinCity.colors import GREEN, RESET

counter_number = 0

def ProcessingTXT(base:str):
    number_ru = []
    number_uk = []
    
    global counter_number
    with open(base, 'r') as file:
        for info in file.readlines():
            all_data = info.split()
            phone = None
            for data in all_data:

                if '+' in data:data = data.split('+')[1]
                
                # номера ru и казахстан
                if len(data) == 11:
                    if data[0] == '7'or data[0] == '8':
                        phone = data
                        number_ru+=[phone]
                        counter_number+=1

                # номера украины
                if len(data) == 10:
                    if data[0:3] == '380':
                        phone = data
                        number_uk+=[phone]
                        counter_number+=1
                if phone != None:print(f'[{counter_number}] {base}\t{phone}')
    print(
            f'Номеров РФ: {len(number_ru)}\n'
            f'Номеров Украины: {len(number_uk)}\n'
            )

def ProcessingCSV():
    pass

def ProcessingBase(base:str):
    if '.txt' in base:ProcessingTXT(base=base)
