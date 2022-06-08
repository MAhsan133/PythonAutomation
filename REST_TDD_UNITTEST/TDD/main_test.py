import unittest
from http import HTTPStatus
from AppIntegration.atlassian_integration import AtlassianConnection


class TddAttlassianIntegration(unittest.TestCase):
    user_count = 0
    new_user_id = None
    test_type = None

    def setUp(self):
        self.atlassian_obj = AtlassianConnection()

    def test_1_get_all_atlassian_users(self):
        status_code, count = self.atlassian_obj.fetch_all_users()
        self.__class__.user_count = count
        self.assertEqual(status_code, HTTPStatus.OK)

    def test_2_create_atlassian_user(self):
        status_code, user_id = self.atlassian_obj.invite_user()
        self.__class__.user_count += 1
        self.__class__.new_user_id = user_id
        self.assertEqual(status_code, HTTPStatus.OK)

    def test_3_verify_count_after_user_add(self):
        status_code, count = self.atlassian_obj.fetch_all_users()
        self.assertEqual(status_code, HTTPStatus.OK)
        self.assertEqual(self.__class__.user_count, count)

    def test_4_remove_atlassian_user(self):
        status_code = self.atlassian_obj.delete_user(self.__class__.new_user_id)
        self.__class__.user_count -= 1
        self.assertEqual(status_code, HTTPStatus.NO_CONTENT)

    def test_5_verify_count_after_user_remove(self):
        status_code, count = self.atlassian_obj.fetch_all_users()
        self.assertEqual(status_code, HTTPStatus.OK)
        self.assertEqual(self.__class__.user_count, count)


if __name__ == "__main__":
    unittest.main()
