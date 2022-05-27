from behave import *
import os
import requests
import json

VALID_USER = False
BASE_URL = "https://reqres.in/"

try:
    env_user_name = os.environ['USER_NAME']
    env_pass_word = os.environ['PASS_WORD']
except:
    env_user_name = ""
    env_pass_word = ""

@step("I am logged in with name '{username}' and password '{password}'")
def step_impl(context, username, password):
    if env_user_name == username and env_pass_word == password:
        global VALID_USER
        VALID_USER = True


@step('I search for users')
def step_impl(context):
    if VALID_USER:
        user_url = BASE_URL + 'api/users?page=2'
        context.resp = requests.get(user_url)
    else:
        assert False, "User is invalid"


@step('I can see total {u_count} users')
def step_impl(context, u_count):
    total_records = json.loads(context.resp.text)['total']
    assert total_records == int(u_count)


@step(u'I get status code {}')
def step_impl(context, status_code):
    assert context.resp.status_code == int(status_code)


@step(u'I create user with name "{username}" and job "{job}"')
def step_impl(context, username, job):
    post_url = BASE_URL + 'api/users'
    post_data = {"name": username, "job": job}
    context.resp = requests.post(url=post_url, data=post_data)


@step(u'I update user with name "{username}" and job "{job}"')
def step_impl(context, username, job):
    post_url = BASE_URL + 'api/users'
    post_data = {"name": username, "job": job}
    context.resp = requests.put(url=post_url, data=post_data)


@when(u'I delete a user')
def step_impl(context):
    user_url = BASE_URL + 'api/users/2'
    context.resp = requests.delete(url=user_url)
