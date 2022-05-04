from django.test import TestCase
from django.contrib.auth.models import User


class UserTestCase(TestCase):
    def test_user(self):
        username = "shetu"
        password = "hello"
        u = User(username=username)
        u.set_password(password)
        u.save()
        print(u)
        self.assertEqual(u.username, username)
        self.assertTrue(u.check_password(password))
        print("test finished")
        print("TEST 5")


# try CI CD
