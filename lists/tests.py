
from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string

class HomePageTest(TestCase):

    def test_url_resolve(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_return_html(self):

        # request = HttpRequest()
        # response = home_page(request)
        # html = response.content.decode('utf8')
        # self.assertTrue(html.startswith('<html>'))
        # self.assertIn('<title>To-Do lists</title>', html)
        # self.assertTrue(html.endswith('</html>'))

        response = self.client.get('/')
        # html = response.content.decode('utf8')
        # self.assertTrue(html.startswith('<html>'))
        # self.assertIn('<title>To-Do lists</title>', html)
        # self.assertTrue(html.strip().endswith('</html>'))
        self.assertTemplateUsed(response, 'home.html')