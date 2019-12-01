from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User


class UserTest(TestCase): 
    def setUp(self):
        self.c = Client()
        User.objects.create(
            username = 'Zeus',
            first_name = 'Sara',
            last_name = 'Kamali'
        )

    def test_user_check(self):
        response = self.c.get('/users/list')
        self.assertEqual(
            response.status_code, 200
            )
        self.assertNotEqual(
            response.status_code, 400
            )