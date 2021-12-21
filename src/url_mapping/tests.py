from django.test import TestCase

from django.urls import reverse
from url_mapping.views import RecoveryUrlView


class TestHomePageView(TestCase):

    def test_url_shortener(self):
        # resolve root path
        print('start testing...')
        test_url = "www.google.com"
        data = {"url" : test_url}
        response = self.client.post(reverse('get_shorted_url'),data=data)
        url = response.data.get('result_data').get('short_url')
        # check url match
        self.assertEqual(self.client.get(url).url, test_url)
