import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.PageObject.Pages import HomePage
from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.HomePage import HomePage


class submenuControl2(WebDriverSetup):

    def test001(self):
        driver = self.driver
        self.driver.get(HomePage.get_base_url())
        home_page = HomePage(driver)
        home_page.findAndClick("acceptButton_CSS")
        home_page.findAndClick("yardimMerkeziBtn_XPATH")
        assert "help" in driver.current_url
        home_page.findAndVerify("yardimMerkeziVerify_CSS","Yardım Merkezi")
        home_page.findAndClick("popularTopicsBtn1_XPATH")
        home_page.findAndVerify("popularTopicsBtnsVerify_CSS","Netflix'e nasıl kaydolunur?")
        home_page.findAndVerify("platformVerify1_XPATH","Android")
        home_page.findAndVerify("platformVerify2_XPATH","Bilgisayar")
        home_page.findAndVerify("platformVerify3_XPATH","iPhone, iPad veya iPod Touch")
        home_page.findAndVerify("platformVerify4_XPATH","Akıllı TV ve Medya Oynatıcıları")
        home_page.findAndVerify("platformVerify5_XPATH","Alıcı Kutusu")
        driver.back()
        home_page.findAndClick("popularTopicsBtn2_XPATH")
        home_page.findAndVerify("popularTopicsBtnsVerify_CSS","Planlar ve Ücretler")
        home_page.findAndVerify("netflixPlansChart1_XPATH","Netflix Planları")
        home_page.findAndVerify("netflixPlansChart2_XPATH","Temel")
        home_page.findAndVerify("netflixPlansChart3_XPATH","Standart")
        home_page.findAndVerify("netflixPlansChart4_XPATH","Özel")
        driver.back()
        home_page.findAndClick("popularTopicsBtn3_XPATH")
        home_page.findAndVerify("popularTopicsBtnsVerify_CSS","Netflix'te oturum açamıyorum")
        home_page.findAndVerify("platformVerify1_XPATH", "Oturum açarken bir hata mesajıyla karşılaşıyorsanız")
        home_page.findAndVerify("platformVerify2_XPATH", "Bir cihazda oturum açamıyorsanız")
        home_page.findAndVerify("platformVerify3_XPATH", "Bir cihazda oturum açarken diğerinde açamıyorsanız")


    def test002(self):
        driver = self.driver
        self.driver.get(HomePage.get_base_url())
        home_page = HomePage(driver)
        home_page.findAndClick("acceptButton_CSS")
        home_page.findAndClick("isImkanlariBtn_XPATH")
        assert "jobs" in driver.current_url
        home_page.findAndVerify("isImkanlariVerify_CSS","A great workplace combines exceptional colleagues and hard problems.")
        home_page.findAndVerify("isImkanlariTitleVerify1_XPATH","Freedom and Responsibility")
        home_page.findAndVerify("isImkanlariTitleMsgVerify1_XPATH","Our core philosophy is people over process.")
        home_page.findAndVerify("isImkanlariTitleVerify2_XPATH","Streaming entertainment.")
        home_page.findAndVerify("isImkanlariTitleMsgVerify2_XPATH","Our first original series debuted in 2013.")


    def test003(self):
        driver = self.driver
        self.driver.get(HomePage.get_base_url())
        home_page = HomePage(driver)
        home_page.findAndClick("acceptButton_CSS")
        home_page.findAndClick("gizlilikBtn_XPATH")
        assert "privacy" in driver.current_url
        home_page.findAndVerify("popularTopicsBtnsVerify_CSS","Gizlilik Bildirimi")
        home_page.findAndVerify("gizlilikVerify_XPATH","kişisel bilgileriniz dâhil olmak üzere belli bazı bilgilerin Netflix hizmetiyle ilişkili olarak toplanması, kullanılması ve ifşasına dair seçeneklerinizi")


    def test004(self):
        driver = self.driver
        self.driver.get(HomePage.get_base_url())
        home_page = HomePage(driver)
        home_page.findAndClick("acceptButton_CSS")
        home_page.findAndClick("hizTestiBtn_XPATH")
        assert "fast" in driver.current_url
        home_page.findAndClick("hizTestiDetails_ID")
        print("Kullanıcıya ait internet hız bilgisi= "+home_page.get_hizTestiSpeedValue_ID().text)
        WebDriverWait(driver, 45).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,"span[class$='refresh']")))
        zaman = datetime.datetime.now().strftime("%d" + "-" + "%m" + "-" + "%Y" + "_saat_" + "%H" + "_" + "%M" + "_ve_" + "%S" + "_saniye")
        driver.save_screenshot("ScreenShots/" + zaman + ".png")
