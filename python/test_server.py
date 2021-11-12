from server import app

import unittest
import json

class TestUrlApp(unittest.TestCase):

    def test_home_page_works(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['Page'], 'Home')

    def test_valid_url_with_slash(self):
        tester = app.test_client(self)
        url = "/urlinfo/1/worksgreat.it:8080/"
        response = tester.get(url, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['isSafe'], True)

    def test_valid_url_without_slash(self):
        tester = app.test_client(self)
        url = "/urlinfo/1/worksgreat.it:8080"
        response = tester.get(url, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['isSafe'], True)

    def test_invalid_url(self):
        tester = app.test_client(self)
        url = "/urlinfo/1/noturl"
        response = tester.get(url, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_valid_url_missing_from_db(self):
        tester = app.test_client(self)
        url = "/urlinfo/1/missing.it:8080/"
        response = tester.get(url, content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_unsafe_url(self):
        tester = app.test_client(self)
        url = "/urlinfo/1/terrible.com:80/foo/?sortBy=dependency&order=asc&page=1&perPage=500"
        response = tester.get(url, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['isSafe'], False)

    def test_safe_url(self):
        tester = app.test_client(self)
        url = "/urlinfo/1/worksgreat.it:8080/foo/?sortBy=dependency&order=asc&page=1&perPage=500"
        response = tester.get(url, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['isSafe'], True)

if __name__ == '__main__':
    unittest.main()