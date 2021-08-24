from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from accounts.models import Customer
from accounts.forms import OrderForm, CreateUserForm, CustomerForm
from django.contrib.auth.models import User
#from django.urls import reverse
from time import sleep
import unittest 

browser = webdriver.Chrome('/home/ethan/Downloads/chromedriver_linux64/chromedriver')

#browser.get('http://www.google.com')

class Testlogin(unittest.TestCase):
    def setUp(self):
        print("setUp")
        self.browser = webdriver.Chrome('/home/ethan/Downloads/chromedriver_linux64/chromedriver')

    def tearDown(self):
        self.browser.close

        form = self.browser.find_element_by_class_name('justify-content-center')
        self.assertEquals(
            form.find_element_by_tag_name('h3').text,
            'LOGIN'
        )

        form = self.browser.find_element_by_tag_name('h3').text,
        self.assertIn('LOGIN', form)

        username_inputbox = self.browser.find_element_by_name('username')
        self.assertEqual(
            username_inputbox.get_attribute('placeholder'),
            'Username...'
        )
    
        password_inputbox = self.browser.find_element_by_name('password')
        self.assertEqual(
            password_inputbox.get_attribute('placeholder'),
            'Password...'
        )

        submit_btn = self.browser.find_element_by_class_name('login_btn')


        

sleep(5)
browser.quit()


if __name__ == "__main__":
    unittest.main()