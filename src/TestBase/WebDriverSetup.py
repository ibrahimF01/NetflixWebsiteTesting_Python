import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import urllib3


class WebDriverSetup(unittest.TestCase):
    def setUp(self):
        print("Test başladı...")
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        service = Service("drivers/chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()


    def tearDown(self):
        print("Test sonlandı...")
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()