from multiprocessing.connection import Client
from unittest import TestCase
import unittest
from urllib import response
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from mywatchlist.models import MyWatchlistItem
from mywatchlist.views import show_html, show_json, show_xml
from mywatchlist.urls import urlpatterns

# class TestUrls(SimpleTestCase):
#     def test_url_html(self):
#         url = reverse('show_html')
#         print(resolve(url))

class UrlTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()

    def test_url_html(self):
        response = self.client.get('/mywatchlist/html/')
