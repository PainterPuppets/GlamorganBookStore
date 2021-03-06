# coding: utf-8
from rest_framework.test import APIClient
from testing.testcases import TestCase

import json


class BookApiTests(TestCase):

    def setUp(self):
        self.client = APIClient(enforce_csrf_checks=True)

        self.user = self.createUser('authenticated@jz.com')
        self.user_client = APIClient(enforce_csrf_checks=True)
        self.user_client.force_authenticate(user=self.user)

        admin = self.createUser('admin@jz.com', is_superuser=True)
        self.admin_client = APIClient(enforce_csrf_checks=True)
        self.admin_client.force_authenticate(user=admin)
    
    def test_get_book_api(self):
        book = self.createBook('他改变了中国')

        # list
        response = self.client.get('/api/book/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json.loads(response.content)['results']), 1)

    def test_create_book_api(self):
        data = {
            'name': 'test',
            'price': '1',
            'discount': '1',
            'introduce': 'hhh',
            'count': '1',
            'author': '佚名'
        }
        
        response = self.client.post('/api/book/', data, format='json')
        self.assertEqual(response.status_code, 403)

        response = self.user_client.post('/api/book/', data, format='json')
        self.assertEqual(response.status_code, 403)

        response = self.admin_client.post('/api/book/', data, format='json')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/api/book/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json.loads(response.content)['results']), 1)
