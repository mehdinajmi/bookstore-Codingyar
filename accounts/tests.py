from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class SignUpTest( TestCase):
    def test_signup_page_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code,200)

    def test_signup_page_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code,200)

    def test_signup_form(self):
        user=get_user_model().objects.create_user('myUesrname','myUsername@gmail.com')
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, 'myUesrname' )
        self.assertEqual(get_user_model().objects.all()[0].email, 'myUsername@gmail.com')


