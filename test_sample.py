import unittest
import os
import requests
import json


class TestRest(unittest.TestCase):
    VALID_USER = False
    BASE_URL = "https://reqres.in/"

    # Get username and password from command line
    # here we can verify user from DB

    def setUp(self):
        self.env_user_name = os.environ['USER_NAME']
        self.env_pass_word = os.environ['PASS_WORD']
        if self.env_user_name == '1234' and self.env_pass_word == '1234':
            self.VALID_USER = True

    # GET method, Verify there should be 12 records and response 200
    def test_get_request(self):
        if not self.VALID_USER:
            assert False
        else:
            user_url = self.BASE_URL + 'api/users?page=2'
            resp = requests.get(user_url)
            total_records = json.loads(resp.text)['total']
            assert resp.status_code == 200
            assert total_records == 12

    # POST method, Verify a record is created with status code 201
    def test_post_request(self):
        if not self.VALID_USER:
            assert False
        else:
            post_url = self.BASE_URL + 'api/users'
            post_data = {"name": "Ahsan", "job": "IT"}
            resp = requests.post(url=post_url, data=post_data)
            assert resp.status_code == 201

    # PUT method, Record updated with response code 200
    def test_put_request(self):
        if not self.VALID_USER:
            assert False
        else:
            user_url = self.BASE_URL + 'api/users/2'
            put_data = {"name": "Ahsan1", "job": "IT1"}
            resp = requests.put(url=user_url, data=put_data)
            assert resp.status_code == 200

    # DELETE method, Verify record deleted with status code 204
    def test_delete_request(self):
        if not self.VALID_USER:
            assert False
        else:
            user_url = self.BASE_URL + 'api/users/2'
            resp = requests.delete(url=user_url)
            assert resp.status_code == 204
