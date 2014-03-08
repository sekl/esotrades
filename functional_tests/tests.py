from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys


class NewVisitorTest(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        LiveServerTestCase.setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            LiveServerTestCase.tearDownClass()

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_guest_can_visit_home_page(self):
        # Guest visits the home page
        self.browser.get(self.server_url)

        # Guest notices the page title and header title
        title = 'Elder Scrolls Online Trades & Auctions'
        self.assertIn(title, self.browser.title)
        header_title = self.browser.find_element_by_tag_name('h1').text
        self.assertIn(title, header_title)

        # Guest notices the register and login buttons
        self.browser.find_element_by_link_text('Register')
        self.browser.find_element_by_link_text('Login')

        # Guest notices the link that lets them browse all trades
        self.browser.find_element_by_link_text('View all trades')


    def test_can_browse_trades(self):
        # Guest browses all trades
        self.browser.get(self.server_url + '/trades/')

        # Guest sees a list of the latest trades

        # Guest can flip to the next page to see more trades

    # Guest looks at a single trade

    # Guest can use the search function

    # Guest sees a list of latest trades on the home page

    # Guest can register and log in
