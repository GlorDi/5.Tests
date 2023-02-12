import requests


def create_folder(token, path):
    headers = {'Authorization': f'OAuth {token}'}
    params = {'path': path}
    r = requests.put('https://cloud-api.yandex.net/v1/disk/resources', headers=headers, params=params)
    return r.status_code