from src.PageObject.Pages import HomePage
from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.HomePage import HomePage


class clickAndVerifyTests(WebDriverSetup):

    def test001(self):
        driver = self.driver
        self.driver.get(HomePage.get_base_url())
        home_page = HomePage(driver)
        home_page.findAndClick("acceptButton_CSS")
        home_page.findAndVerify("heroTitle_CSS", "Sınırsız film")
        home_page.findAndSend("emailInput_ID", "fixtests@gmail.com")
        home_page.findAndClick("startButton_CSS")
        home_page.findAndVerify("accountVerify1_CSS", "Hesabınızı oluşturalım")
        home_page.findAndClick("continueButton_CSS")








