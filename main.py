import json
import os
import time
import requests
from pathlib import *
from progress.bar import Bar

Ytoken = ''


access_token = ''
user_id = '47535255'
album_id = 'profile'
extended = '1'
url = 'https://api.vk.com/method/photos.get'
params = {'access_token': access_token, 'v': '5.131', 'user_id': user_id, 'album_id': album_id, 'extended': extended, 'photo_sizes': '1'}
response = requests.get(url, params=params).json()
res = response['response']['items']

Path.mkdir(Path.cwd() / "Folder")
path_to_file = Path.cwd() / "Folder"

log_list = []

for file in res:
    time.sleep(1.5)
    size = file['sizes'][-1]['type']
    photo_url = file['sizes'][-1]['url']
    file_name = file['likes']['count']
    download_foto = requests.get(photo_url)
    with open(f'{Path.cwd() / "Folder"}/{file_name}.jpg', 'wb') as f:
        f.write(download_foto.content)
    print(f"{file_name} загружен.")

file_list = os.listdir(Path.cwd() / "Folder")

urly = 'https://cloud-api.yandex.net/v1/disk/resources'
requests.get(urly)
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {Ytoken}'}


# def create_folder(path):
#     """Создание папки. \n path: Путь к создаваемой папке."""
#     requests.put(f'{urly}?path={path}', headers=headers)


def upload_file(loadfile, savefile, replace=False):
    """Загрузка файла.
    savefile: Путь к файлу на Диске
    loadfile: Путь к загружаемому файлу
    replace: true or false Замена файла на Диске"""
    res = requests.get(f'{urly}/upload?path={savefile}&overwrite={replace}', headers=headers).json()
    with open(loadfile, 'rb') as f:
        try:
            requests.put(res['href'], files={'file': f})
        except KeyError:
            print(res)

# def backup(savepath, loadpath):
#     """Загрузка папки на Диск. \n savepath: Путь к папке на Диске для сохранения \n loadpath: Путь к загружаемой папке"""
#     date_folder = '{0}_{1}'.format(loadpath.split('\\')[-1], datetime.now().strftime("%Y.%m.%d-%H.%M.%S"))
#     create_folder(savepath)
#     for address, _, files in os.walk(loadpath):
#         create_folder('{0}/{1}/{2}'.format(savepath, date_folder, address.replace(loadpath, "")[1:].replace("\\", "/")))
#         bar = Bar('Loading', fill='X', max=len(files))
#         for file in files:
#             bar.next()
#             upload_file('{0}\{1}'.format(address, file), '{0}/{1}{2}/{3}'.format(savepath, date_folder, address.replace(loadpath, "").replace("\\", "/"), file))
#     bar.finish()
# create_folder('Folder')
upload_file(path_to_file, 'Folder')
