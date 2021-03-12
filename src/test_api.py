#!/usr/bin/python3
import unittest

import requests


class TestApi(unittest.TestCase):
    @classmethod 
    def setUp(cls):
        cls.test_host = '10.128.35.79'

    def test01_get_max_records_count(self):
        response = requests.get(f'http://127.0.0.1:5000/top10vulnerabilities?hostip={self.test_host}')
        response_json = response.json()
        self.assertLessEqual(len(response_json), 10)

    def test02_get_max_records_count(self):
        response = requests.get(f'http://127.0.0.1:5000/top10vulnerabilities?hostip={self.test_host}&page=1')
        response_json = response.json()
        self.assertLessEqual(len(response_json), 10)

    def test03_get_max_records_count(self):
        response = requests.get(f'http://127.0.0.1:5000/top10vulnerabilities?hostip={self.test_host}&page=1')
        response_json = response.json()
        self.assertLessEqual(len(response_json), 10)
        response = requests.get(f'http://127.0.0.1:5000/top10vulnerabilities?hostip={self.test_host}&page=2')
        response_json = response.json()  
        self.assertLessEqual(len(response_json),10)      

    def test04_get_max_records_count(self):
        for page_num in range(1,15):
            response = requests.get(f'http://127.0.0.1:5000/top10vulnerabilities?hostip={self.test_host}&page={page_num}')
            response_json = response.json()
            self.assertLessEqual(len(response_json),10)

    def test05_get_max_records_count(self):
        response = requests.get(f'http://127.0.0.1:5000/top10vulnerabilities?hostip={self.test_host}&page=0')
        response_json = response.json()
        self.assertEqual(len(response_json), 0)

    def test06_get_max_records_count(self):
        response = requests.get('http://127.0.0.1:5000/top10vulnerabilities')
        response_json = response.json()
        print(response_json)
        self.assertEqual(response_json["message"],"hostip is mandatory")
        
if __name__ == '__main__':
    unittest.main()
