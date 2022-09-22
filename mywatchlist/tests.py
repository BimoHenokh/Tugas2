from unittest import TestCase
from django.test import Client
from mywatchlist.models import MyWatchlistItem
from mywatchlist.views import show_html, show_json, show_xml

class UrlTest(TestCase):

    def test_url_html(self):
        client = Client()
        response = client.get('/mywatchlist/html/')
        response.status_code

    def test_url_xml(self):
        client = Client()
        response = client.get('/mywatchlist/xml/')
        response.status_code

    def test_url_json(self):
        client = Client()
        response = client.get('/mywatchlist/json/')
        response.status_code
