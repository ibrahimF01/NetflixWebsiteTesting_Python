from src.PageObject.Pages import HomePage
from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.HomePage import HomePage


class negativeLoginTest(WebDriverSetup):

    def test001(self):
        driver = self.driver
        self.driver.get(HomePage.get_base_url())
        home_page = HomePage(driver)
        home_page.findAndClick("acceptButton_CSS")
        home_page.findAndClick("oturumAcBtn_CSS")
        home_page.findAndSend("userLogin_ID","testMail@hotmail.com")
        home_page.findAndSend("userPassword_ID","1234567890")
        home_page.findAndClick("oturumAcBtn2_CSS")
        home_page.findAndVerify("loginNegativeVerifyMessage","Bu e‑posta adresi ile bağlantılı bir hesap bulamadık.")


    def test002(self):
        driver = self.driver
        self.driver.get(HomePage.get_base_url())
        home_page = HomePage(driver)
        home_page.findAndClick("acceptButton_CSS")
        home_page.findAndClick("oturumAcBtn_CSS")
        home_page.findAndClick("oturumAcBtn2_CSS")
        home_page.findAndVerify("loginEmptyVerifyMessage1","Lütfen geçerli bir telefon numarası veya e‑posta adresi girin.")
        home_page.findAndVerify("loginEmptyVerifyMessage2","Parolanız 4 ila 60 karakter olmalıdır.")
