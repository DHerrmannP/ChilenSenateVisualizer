import unittest

from website_reader import read_website

class TestHttpGet(unittest.TestCase):
    def test_http_get_request_with_valid_url(self):
        from pydantic import HttpUrl
        url = HttpUrl(url='https://www.google.com',scheme='https',host='www.google.com')
        assert read_website.http_get_request(url).lower().startswith('<!doctype html>')