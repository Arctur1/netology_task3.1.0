import requests
import json
import time
from tqdm import tqdm


class VkUser:
    url = 'https://api.vk.com/method/'

    def __init__(self, token, version):
        self.token = token
        self.version = version
        self.params = {
            'access_token': self.token,
            'v': self.version
        }
        self.owner_id = requests.get(self.url + 'users.get', self.params).json()['response'][0]['id']

    def get_photos(self, user_id=None): # Загружает фото из профиля в файл import.txt
        if user_id is None:
            user_id = self.owner_id
        photos_url = self.url + 'photos.get'
        photos_params = {
            'owner_id': user_id,
            'album_id': 'profile',
            'extended': 1
        }
        res = requests.get(photos_url, params={**self.params, **photos_params})
        with open('import.txt', 'w') as f:
            json.dump(res.json(), f)
        return res.json()


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, amount=5): # Загружает фото по ссылкам из файла import.txt в папку import
        with open('import.txt') as f:
            lastimport = json.load(f)
            for i in tqdm(range(amount)):
                requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                             params={'path': f'disk:/import'},
                             headers={'Authorization': f'OAuth {ytoken}'}
                             )
                requests.post('https://cloud-api.yandex.net:443/v1/disk/resources/upload',
                              params={'path': f'disk:/import/{lastimport["response"]["items"][i]["likes"]["count"]}',
                                      'url': lastimport['response']['items'][i]['sizes'][-1]['url']},
                              headers={'Authorization': f'OAuth {ytoken}'})
                time.sleep(1)


token = ''
ytoken = ''


VkUser(token, '5.126').get_photos(552934290)
YaUploader(ytoken).upload(5)

