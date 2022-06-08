import requests
import os
import configparser
import json


class AtlassianConnection(object):

    def __init__(self):
        current_file_path = os.path.dirname(__file__)

        abs_file_path = os.path.join(current_file_path, 'defaults.cfg')
        config = configparser.ConfigParser()
        config.read_file(open(abs_file_path))
        self.base_url, self.organization_id, self.new_user_email = "", "", ""
        try:
            self.base_url = config['DEFAULT']['BASE_URL']
            self.organization_id = config['DEFAULT']['ORGANIZATION_ID']
            self.new_user_email = config['DEFAULT']['NEW_USER_EMAIL']
        except KeyError:
            pass

        self.headers = {
            'Content-Type': 'application/json', 'origin': 'https://admin.atlassian.com',
            'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty',
            'referer': 'https://admin.atlassian.com/o/{}/users'.format(self.organization_id)}
        self.cookies = {'cloud.session.token': self.get_organization_session_token()}

        request_apis = os.path.join(current_file_path, 'request_apis.json')
        f_read_json = open(request_apis)
        self.requests_data = json.load(f_read_json)

    @staticmethod
    def get_organization_session_token():
        script_dir = os.path.dirname(__file__)
        abs_file_path = os.path.join(script_dir, 'session_token.txt')
        with open(abs_file_path) as f:
            for line in f:
                return line

    def fetch_all_users(self):
        url = self.requests_data['fetch_all_users'].format(
            self.base_url, self.organization_id)
        headers = {'Content-Type': 'application/json'}
        resp = requests.get(url, cookies=self.cookies, headers=headers)
        return resp.status_code, resp.json()["total"]

    def invite_user(self):
        url = self.requests_data['create_user'].format(self.base_url, self.organization_id)
        data = {"emails": [self.new_user_email], "permissionRules": [], "additionalGroups": [],
                "sendNotification": True}
        resp = requests.post(url, json=data, cookies=self.cookies, headers=self.headers)
        return resp.status_code, resp.json()[0]

    def delete_user(self, user_id):
        url = self.requests_data['delete_user'].format(
            self.base_url, self.organization_id, user_id)
        resp = requests.post(url, cookies=self.cookies, headers=self.headers)
        return resp.status_code
