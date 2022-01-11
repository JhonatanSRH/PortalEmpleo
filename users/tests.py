from django.test import TestCase

# Create your tests here.

from users.models import User
from django.urls import reverse

class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        User.objects.create(email='test@test.com', password='testingAnApp123')

    def test_email_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')

    def test_password_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('password').verbose_name
        self.assertEquals(field_label, 'password')

    def test_other_first_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('other_first_name').max_length
        self.assertEquals(max_length, 50)

class UserViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(email='test@test.com', password='testingAnApp123')

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('signup'))
        self.assertEqual(resp.status_code, 200)

    def test_resp_type_list(self):
        resp = self.client.get(reverse('signup'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(isinstance(resp.json(), list))

    def test_lists_all_users(self):
        resp = self.client.get(reverse('signup'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(isinstance(resp.json(), list))
        self.assertTrue(len(resp.json()) == 1)