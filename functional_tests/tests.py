from selenium import webdriver
from django.test import LiveServerTestCase

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_visiting_page(self):
        self.browser.get(self.live_server_url)
        self.assertIn('EOL homepage', self.browser.title)
