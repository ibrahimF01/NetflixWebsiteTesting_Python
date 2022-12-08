from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from src.PageObject.Pages import HomePage
from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.HomePage import HomePage
from selenium.webdriver.support import expected_conditions as EC


class AssertionOA(WebDriverSetup):

    def test27(self):
        driver = self.driver
        self.driver.get(HomePage.get_base_url())
        home_page = HomePage(driver)
        # wait = WebDriverWait(driver, 30)
        home_page.findAndClick("acceptButton_CSS")
        home_page.findAndVerify("SubLink01", "Medya")
        home_page.findAndVerify("SubLink02", "İzleme")
        home_page.findAndVerify("SubLink03", "Kurumsal")
        home_page.findAndVerify("SubLink04", "Netflix")

    def test28(self):
        driver = self.driver
        self.driver.get(HomePage.get_base_url())
        home_page = HomePage(driver)
        home_page.findAndClick("acceptButton_CSS")
        home_page.findAndClick("SubLink01")
        home_page.findAndVerify("mediaCenterVerify", "Medya Merkezi")

    def test29(self):
        driver = self.driver
        self.driver.get(HomePage.get_base_url())
        home_page = HomePage(driver)
        home_page.findAndClick("acceptButton_CSS")
        home_page.findAndClick("SubLink02")
        home_page.findAndVerify("izlemeYollari", "Favori cihazlarınızla")

    def test30(self):
        driver = self.driver
        self.driver.get(HomePage.get_base_url())
        home_page = HomePage(driver)
        home_page.findAndClick("acceptButton_CSS")
        home_page.findAndClick("SubLink03")
        home_page.findAndVerify("KurumsalInfo", "Netflix Kurumsal Bilgileri")

    def test31(self):
        driver = self.driver
        self.driver.get(HomePage.get_base_url())
        home_page = HomePage(driver)
        home_page.findAndClick("acceptButton_CSS")
        home_page.findAndClick("SubLink04")
        home_page.findAndVerify("OnlyNetflix", "Yalnızca Netflix")