from django.test.testcases import TransactionTestCase
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from accounts.models import Customer
from accounts.forms import OrderForm, CreateUserForm, CustomerForm
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestRegister(TransactionTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.browser.get("http://127.0.0.1:8000/login")

def test_login(self):
        try:
            self.username = WebDriverWait(self.browser, 50).until(EC.presence_of_element_located((By.ID, "username")))
            self.username.send_keys("Ethan")
            self.password = self.browser.find_element_by_id("********")
            self.password.send_keys("********")
            
        except Exception as err:
            print(err)

        try:
            self.registerButton = self.browser.find_element_by_class_name("btn")
            self.registerButton.click()
        except Exception as err:
            print(err)

        try:
            self.setLink = WebDriverWait(self.browser, 50).until(EC.presence_of_element_located((By.ID, "username")))
            self.setLink.click()
        except Exception as err:
            print(err)

        try:
            self.PhoneNum = self.browser.find_element_by_class_name("id_phone")
            self.PhoneNum.send_keys("01234567")
            self.email = self.browser.find_element_by_id("id_email")
            self.email.send_keys("ethan@gmail.com")
        except Exception as err:
            print(err)
        
        try:
            self.settingButton = self.browser.find_element_by_class_name("btn")
            self.settingButton.click()
            time.sleep(50)
        except Exception as err:
            print(err)
