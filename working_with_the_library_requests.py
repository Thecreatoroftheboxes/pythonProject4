"""
Task № 2
"""

import requests
import os

# current = os.getcwd()
# filename = 'test_uploader.txt'
file_list = ['test_uploader.txt', 'test_uploader.txt']
# file_path = os.path.join(current, filename)

TOKEN =


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        """
        Функция получает заголовки
        """
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, disk_file_path):
        """
        Функция получает ссылку для загрузки файла
        """
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        link_dict = response.json()
        href = link_dict.get('href')
        return href

    def upload_file_to_disk(self, disk_file_path, file_list):
        """
        Функция загружает файлы по списку file_list на яндекс диск
        """
        for file in file_list:
            href = self._get_upload_link(disk_file_path=disk_file_path)
            response = requests.put(href, data=open(file, 'rb'))
        if response.status_code == 201:
            print('Success')


if __name__ == '__main__':
    ya = YaUploader(token=TOKEN)
    ya.upload_file_to_disk('Тест для загрузки файла/test_10.04.23.txt', file_list)
