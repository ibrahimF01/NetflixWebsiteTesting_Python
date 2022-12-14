import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from src.PageObject.Pages import HomePage
from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.HomePage import HomePage
from selenium.webdriver.support import expected_conditions as EC


class clickAndVerifyTests(WebDriverSetup):

    def test001(self):
        driver = self.driver
        self.driver.get(HomePage.get_base_url())
        home_page = HomePage(driver)
        wait = WebDriverWait(driver, 30)
        home_page.findAndClick("acceptButton_CSS")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-uia='our-story-cta-hero_fuji']")))
        home_page.findAndVerify("heroTitle_CSS", "Sınırsız film")
        home_page.findAndSend("emailInput_ID", "testx@gmail.com")
        home_page.findAndClick("startButton_CSS")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-uia='cta-continue-registration']")))
        home_page.findAndVerify("accountVerify1_CSS", "Hesabınızı oluşturalım")
        home_page.findAndClick("continueButton_CSS")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-uia='cta-registration']")))
        home_page.findAndVerify("accountVerify2_CSS", "Üyeliğinizi başlatmak")
        home_page.findAndVerify("accountVerify3_CSS", "Sadece birkaç adım")
        home_page.findAndVerify("accountVerify4_CSS", "Biz de formaliteyi")
        home_page.findAndClick("passwordInput_ID")
        home_page.findAndSend("passwordInput_ID", "05password009")
        # home_page.findAndVerify("accountVerify5_CSS", "Netflix özel teklifleri")
        # home_page.findAndClick("binaryInput_CSS")
        home_page.findAndClick("continueButton2_CSS")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-uia='continue-button']")))
        home_page.findAndVerify("accountVerify6_XPATH", "Planınızı seçin")
        home_page.findAndVerify("accountVerify7_XPATH", "Taahhüt yok")
        home_page.findAndVerify("accountVerify8_XPATH", "Tek ve düşük bir ücretle")
        home_page.findAndVerify("accountVerify9_XPATH", "Tüm cihazlarınızda")
        home_page.findAndClick("continueButton3_CSS")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-uia='cta-plan-selection']")))
        home_page.findAndVerify("accountVerify11_XPATH", "Canınız neyi isterse")
        home_page.findAndVerify("accountVerify12_XPATH", "Sadece sizin için")
        home_page.findAndVerify("accountVerify13_XPATH", "Planınızı istediğiniz zaman")
        home_page.findAndClick("continueButton4_CSS")
        wait.until(EC.element_to_be_clickable((By.ID, "creditOrDebitCardDisplayStringId")))
        home_page.findAndVerify("accountVerify14_XPATH", "Tercih ettiğiniz ödeme")
        home_page.findAndVerify("accountVerify15_XPATH", "Ödeme yönteminiz")
        home_page.findAndVerify("accountVerify16_XPATH", "Endişelenmeyin")
        home_page.findAndVerify("accountVerify17_XPATH", "İstediğiniz zaman")
        home_page.findAndClick("creditCardButton_ID")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-uia='action-submit-payment']")))
        home_page.findAndVerify("accountVerify18_XPATH", "Ödemenizi ayarlayın")
        home_page.findAndSend("firstNameInput_ID", "test firstName")
        home_page.findAndSend("lastNameInput_ID", "test lastName")
        home_page.findAndSend("creditCardNumberInput_ID", "0000 0000 0000 0000")
        home_page.findAndSend("creditExpirationMonthInput_ID", "0127")
        home_page.findAndSend("creditCardSecurityCodeInput_ID", "000")
        home_page.findAndClick("hasAcceptedInput_XPATH")
        # home_page.findAndClick("continueButton5_CSS") #Bu adım gerçek kullanıcı bilgileri girildiğinde aktif edilmelidir.

    def test002(self):
        driver = self.driver
        self.driver.get(HomePage.get_base_url())
        home_page = HomePage(driver)
        wait = WebDriverWait(driver, 30)
        home_page.findAndClick("acceptButton_CSS")
        home_page.findAndVerify("homepageVerify1_CSS", "Stranger Things")
        home_page.findAndVerify("homepageVerify2_CSS", "İndiriliyor")
        home_page.findAndVerify("homepageVerify3_XPATH", "Çevrimdışı izlemek için")
        home_page.findAndVerify("homepageVerify4_XPATH", "En sevdiğiniz içerikleri")
        home_page.findAndVerify("homepageVerify5_XPATH", "Sıkça Sorulan")
        home_page.findAndClick("faqQuestionButton1_XPATH")
        home_page.findAndVerify("faqAnswerVerify1_XPATH", "Netflix; internet bağlantılı")
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='faq-question'])[2]")))
        home_page.findAndClick("faqQuestionButton2_XPATH")
        home_page.findAndVerify("faqAnswerVerify2_XPATH", "Netflix'i akıllı telefonunuz")
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='faq-question'])[3]")))
        home_page.findAndClick("faqQuestionButton3_XPATH")
        home_page.findAndVerify("faqAnswerVerify3_XPATH", "İstediğiniz yerde, istediğiniz zaman")
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='faq-question'])[4]")))
        home_page.findAndClick("faqQuestionButton4_XPATH")
        home_page.findAndVerify("faqAnswerVerify4_XPATH", "Netflix esnektir")
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='faq-question'])[5]")))
        home_page.findAndClick("faqQuestionButton5_XPATH")
        home_page.findAndVerify("faqAnswerVerify5_XPATH", "Netflix, uzun metrajlı")
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='faq-question'])[6]")))
        home_page.findAndClick("faqQuestionButton6_XPATH")
        home_page.findAndVerify("faqAnswerVerify6_XPATH", "Üyeliğinize dâhil")

    def test003(self):
        driver = self.driver
        self.driver.get(HomePage.get_base_url())
        home_page = HomePage(driver)
        wait = WebDriverWait(driver, 30)
        home_page.findAndClick("acceptButton_CSS")
        home_page.findAndClick("SSSButton_XPATH")
        home_page.findAndVerify("SSSVerify1_CSS", "Netflix nedir?")
        home_page.findAndVerify("SSSVerify2_XPATH", "Diziler ve Filmler")
        home_page.findAndVerify("SSSVerify3_XPATH", "Desteklenen Cihazlar")
        home_page.findAndVerify("SSSVerify4_XPATH", "Planlar ve Ücretler")
        home_page.findAndVerify("SSSVerify5_XPATH", "Başlayın")
        home_page.findAndClick("linkButton1_XPATH")
        home_page.findAndSend("textAreaInput_CSS", "Bu bir test")
        home_page.findAndClick("sendButton_CSS")
        home_page.findAndClick("phoneContactButton_ID")
        home_page.findAndVerify("SSSVerify6_CSS", "Uygulama üzerinden")
        home_page.findAndClick("closeButton1_CSS")
        home_page.findAndClick("chatContactButton_ID")
        driver.switch_to.frame(0)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class^='chat-avatar']+button[class^='chat-end-button']")))
        home_page.findAndVerify("SSSVerify7_XPATH", "Sohbete başlamadan")
        home_page.findAndClick("closeButton2_CSS")
        driver.switch_to.default_content()
        home_page.findAndClick("homePageButton_CSS")

    def test004(self):
        driver = self.driver
        self.driver.get(HomePage.get_base_url())
        home_page = HomePage(driver)
        home_page.findAndClick("acceptButton_CSS")
        home_page.findAndClick("investorsButton_CSS")
        home_page.findAndClick("investorsTitLink1_XPATH")
        home_page.findAndVerify("investorsVerify1_CSS", "Company Profile")
        home_page.findAndClick("investorsTitLink2_XPATH")
        home_page.findAndVerify("investorsVerify2J_CSS", "Quarterly Earnings")
        home_page.findAndClick("investorsTitLink3_XPATH")
        home_page.findAndVerify("investorsVerify2J_CSS", "Financial Releases")
        home_page.findAndClick("investorsTitLink4_XPATH")
        home_page.findAndVerify("investorsVerify2J_CSS", "Stock Quote")
        home_page.findAndClick("investorsTitLink5_XPATH")
        home_page.findAndVerify("investorsVerify2J_CSS", "Leadership & Directors")
        home_page.findAndClick("investorsTitLink6_XPATH")
        home_page.findAndVerify("investorsVerify2J_CSS", "Investor Contacts")

    def test005(self):
        driver = self.driver
        self.driver.get(HomePage.get_base_url())
        home_page = HomePage(driver)
        home_page.findAndClick("acceptButton_CSS")
        home_page.findAndClick("kullanimKosButton_CSS")
        home_page.findAndVerify("SSSVerify1_CSS", "Netflix Kullanım")
        home_page.findAndClick("homePageButton_CSS")

    def test006(self):
        driver = self.driver
        self.driver.get(HomePage.get_base_url())
        home_page = HomePage(driver)
        home_page.findAndClick("acceptButton_CSS")
        home_page.findAndClick("contactUsButton_CSS")
        home_page.findAndVerify("contactUsVerify_XPATH", "Müşteri Hizmetleri")
        home_page.findAndClick("homePageButton_CSS")
