
import os
import time
import requests
from pathlib import *
import yadisk
from tqdm import tqdm

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

y = yadisk.YaDisk(token=Ytoken)

for file in res:
    # time.sleep(1.5)
    size = file['sizes'][-1]['type']
    photo_url = file['sizes'][-1]['url']
    file_name = file['likes']['count']
    download_foto = requests.get(photo_url)
    with open(f'{Path.cwd() / "Folder"}/{file_name}.jpg', 'wb') as f:
        f.write(download_foto.content)
    print(f"{file_name} загружен на диск.")


def run(path):
    y.mkdir('folder')
    for address, dirs, files in os.walk(path):
        for file in files:
            for i in tqdm(range(len(files))):
                time.sleep(0.5)
            print(f'Файл {file} загружен на Яндекс.Диск')
            y.upload(f'{address}/{file}', f'/folder/{file}')


if __name__ == '__main__':
    run(path_to_file)
