from django.test import TestCase
from django.http import response
from django.urls import reverse

# Create your tests here.
class ThingsTest(TestCase):

    def test_main_page_status(self):
        url = reverse('boba_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_main_page_template(self):
        url = reverse('boba_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'boba/boba_list.html')

    def test_base_page_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'pages/home.html')

    def test_about_page_status(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about_page_template(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'pages/about.html')