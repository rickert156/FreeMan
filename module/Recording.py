import csv, os, time
from manifest import base_name, dir_result

def CreateNewDoc(file_name:str):
    if not os.path.exists(file_name):
        with open(file_name, 'a+') as file:
            write = csv.writer(file)
            write.writerow(['Phone', 'Location', 'UserID', 'Date'])


def recordingResult(phone:str=None, location:str=None, userId:str=None):
    global base_name
    if ' ' in base_name:base_name = base_name.replace(' ', '_')
    if ' ' in location:location = location.replace(' ', '_')
    file_name = f'{location}_{base_name}.csv'
    path_file_base = f'{dir_result}/{file_name}'
    CreateNewDoc(file_name=path_file_base)

    current_time = time.strftime("%d/%m/%Y %H:%M")

    with open(path_file_base, 'a+') as file:
        write = csv.writer(file)
        write.writerow([phone, location, userId, current_time])
