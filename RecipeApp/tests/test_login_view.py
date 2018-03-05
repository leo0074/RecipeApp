from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import TestCase
from django.test import Client
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class Login_view_test(StaticLiveServerTestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_login_page(self):
		client = Client()
		
		driver = self.driver
		driver.get(self.live_server_url + "/RecipeApp/login")
		assert "Invalid username or password" not in driver.page_source
		username = driver.find_element_by_name('username')
		password = driver.find_element_by_name('password')
		username.send_keys = 'leo0074'
		password.send_keys = 'Somepassword'	
		submit = driver.find_element_by_name('login')
		submit.submit()
		assert "Invalid username or password" in driver.page_source

	def tearDown(self):
		self.driver.close()