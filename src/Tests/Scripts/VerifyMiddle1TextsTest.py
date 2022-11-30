from src.PageObject.Pages import HomePage
from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.HomePage import HomePage


class VerifyMiddle3TextsTest(WebDriverSetup):

    def test001(self):
        driver = self.driver
        self.driver.get(HomePage.get_base_url())
        home_page = HomePage(driver)
        home_page.findAndClick("acceptButton_CSS")
        home_page.findAndVerify("orta1Element_CSS","Akıllı TV, PlayStation, Xbox, Chromecast, Apple TV, Blu-ray")