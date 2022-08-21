from django.test import TestCase

from drogasil.views import get_search_url


class GetSearchUrl(TestCase):
    def test_get_search_url(self):
        url = get_search_url('https://any_url?term={term}', 'dorflex')
        self.assertEqual(url, 'https://any_url?term=dorflex')

    def test_should_be_return_term_in_lowercase(self):
        url = get_search_url('https://any_url?term={term}', 'DORFLEX')
        self.assertEqual(url, 'https://any_url?term=dorflex')
        
    def test_should_be_strip_term(self):
        url = get_search_url('https://any_url?term={term}', 'dorflex ')
        self.assertEqual(url, 'https://any_url?term=dorflex')
