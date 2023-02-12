from unittest import TestCase
from main import visit_country, geo_id, check_generator
from APIYandex import create_folder
import requests


class TestVisitCountry(TestCase):
    def test_geo_logs(self):
        test_geo_logs = [
            {'visit1': ['Москва', 'Россия']},
            {'visit2': ['Дели', 'Индия']},
            {'visit3': ['Владимир', 'Россия']},
            {'visit4': ['Лиссабон', 'Португалия']},
            {'visit5': ['Париж', 'Франция']},
            {'visit6': ['Лиссабон', 'Португалия']},
            {'visit7': ['Тула', 'Россия']},
            {'visit8': ['Тула', 'Россия']},
            {'visit9': ['Курск', 'Россия']},
            {'visit10': ['Архангельск', 'Россия']}
        ]

        res_list = [{'visit1': ['Москва', 'Россия']},
                    {'visit3': ['Владимир', 'Россия']},
                    {'visit7': ['Тула', 'Россия']},
                    {'visit8': ['Тула', 'Россия']},
                    {'visit9': ['Курск', 'Россия']},
                    {'visit10': ['Архангельск', 'Россия']}]

        res = visit_country(test_geo_logs)
        self.assertEqual(res, res_list)


class TestGeoId(TestCase):
    def test_ids(self):
        ids = {'user1': [213, 213, 213, 15, 213],
               'user2': [54, 54, 119, 119, 119],
               'user3': [213, 98, 98, 35]}

        res_set = {213, 15, 54, 119, 98, 35}

        res = geo_id(ids)
        self.assertEqual(res, res_set)


class TestCheckGenerator(TestCase):
    def test_check_generator(self):
        queries = [
            'смотреть сериалы онлайн',
            'новости спорта',
            'афиша кино',
            'курс доллара',
            'сериалы этим летом',
            'курс по питону',
            'сериалы про спорт'
        ]

        res_list = ['Количество поисковых запросов из 3 слов: 57.14%, кол-во 4',
                    'Количество поисковых запросов из 2 слов: 42.86%, кол-во 3']

        res = check_generator(queries)
        self.assertEqual(res, res_list)


class TestAPIYandex(TestCase):

    def __init__(self, token):
        TestCase.__init__(self, token)
        self.token = ''

    def test_create_folder_positive(self):
        path1 = ''
        response = 201
        res = create_folder(self.token, path1)
        self.assertEqual(res, response)

    def test_create_folder_positive2(self):
        path1 = ''
        response = 409
        res = create_folder(self.token, path1)
        self.assertNotEqual(res, response), 'Такая папка уже существует'

    def test_folder_in_list_positive(self):
        path1 = ''
        response = 200
        headers = {'Authorization': f'OAuth {self.token}'}
        params = {'path': path1}
        create_folder(self.token, path1)
        res1 = requests.get(f'https://cloud-api.yandex.net/v1/disk/resources', headers=headers, params=params)
        self.assertEqual(res1.status_code, response)

    def test_folder_in_list_positive2(self):
        path1 = ''
        response = 404
        headers = {'Authorization': f'OAuth {self.token}'}
        params = {'path': path1}
        create_folder(self.token, path1)
        res1 = requests.get(f'https://cloud-api.yandex.net/v1/disk/resources', headers=headers, params=params)
        self.assertNotEqual(res1.status_code, response), 'Такой папки не существует'

    def test_authorization_positive(self):
        path1 = ''
        response = 401
        res = create_folder(self.token, path1)
        self.assertNotEqual(res, response), 'Вы не авторизованы'

    def test_enough_space_positive(self):
        path1 = ''
        response = 507
        res = create_folder(self.token, path1)
        self.assertNotEqual(res, response), 'Недостаточно свободного места на Диске'