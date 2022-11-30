from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


base_url = "https://www.netflix.com/tr/"

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.acceptButton_CSS = "button[data-uia='cookie-disclosure-button-accept']"
        self.heroTitle_CSS = "h1[data-uia='hero-title']"
        self.emailInput_ID = "id_email_hero_fuji"
        self.startButton_CSS = "button[data-uia='our-story-cta-hero_fuji']"
        self.accountVerify1_CSS = "h1[data-uia='stepTitle']"
        self.continueButton_CSS = "button[data-uia='cta-continue-registration']"
        self.accountVerify2_CSS = "h1[data-uia='stepTitle']"
        self.oturumAcBtn_CSS = "a[data-uia='header-login-link']"
        self.userLogin_ID = "id_userLoginId"
        self.userPassword_ID = "id_password"
        self.oturumAcBtn2_CSS = "button[data-uia='login-submit-button']"
        self.loginNegativeVerifyMessage = "div[data-uia='text']"
        self.loginEmptyVerifyMessage1 = "div[data-uia='login-field+error']"
        self.loginEmptyVerifyMessage2 = "div[data-uia='password-field+error']"
        self.orta3Element = "div[data-uia-nmhp='watchOnDevice']"


    def get_acceptButton_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.acceptButton_CSS)
    def get_heroTitle_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.heroTitle_CSS)
    def get_emailInput_ID(self):
        return self.driver.find_element(By.ID, self.emailInput_ID)
    def get_startButton_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.startButton_CSS)
    def get_accountVerify1_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.accountVerify1_CSS)
    def get_continueButton_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.continueButton_CSS)
    def get_oturumAcBtn_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.oturumAcBtn_CSS)
    def get_userLogin_ID(self):
        return self.driver.find_element(By.ID, self.userLogin_ID)
    def get_userPassword_ID(self):
        return self.driver.find_element(By.ID, self.userPassword_ID)
    def get_oturumAcBtn2_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.oturumAcBtn2_CSS)
    def get_loginNegativeVerifyMessage(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.loginNegativeVerifyMessage)
    def get_loginEmptyVerifyMessage1(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.loginEmptyVerifyMessage1)
    def get_loginEmptyVerifyMessage2(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.loginEmptyVerifyMessage2)
    def get_orta3(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.orta3Element)

    def scrollToElementMid(self, element):
        scrollElementIntoMiddle = "var viewPortHeight = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);"
        "var elementTop = arguments[0].getBoundingClientRect().top;"
        "window.scrollBy(0, elementTop-(viewPortHeight/2));"
        self.driver.execute_script(scrollElementIntoMiddle, element)

    def scrollToElement(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def moveToElement(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def scrollHeight(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def findAndClick(self, strElement):
        match strElement:
            case "acceptButton_CSS": self.myElement = self.get_acceptButton_CSS()
            case "startButton_CSS": self.myElement = self.get_startButton_CSS()
            case "continueButton_CSS": self.myElement = self.get_continueButton_CSS()
            case "oturumAcBtn_CSS": self.myElement = self.get_oturumAcBtn_CSS()
            case "oturumAcBtn2_CSS": self.myElement = self.get_oturumAcBtn2_CSS()
        self.scrollToElementMid(self.myElement)
        EC.element_to_be_clickable(self.myElement)
        self.myElement.click()

    def findAndSend(self, strElement, strText):
        match strElement:
            case "emailInput_ID": self.myElement = self.get_emailInput_ID()
            case "userLogin_ID": self.myElement = self.get_userLogin_ID()
            case "userPassword_ID": self.myElement = self.get_userPassword_ID()
        self.scrollToElementMid(self.myElement)
        EC.visibility_of(self.myElement)
        self.myElement.send_keys(strText)

    def findAndVerify(self, strElement, textElement):
        match strElement:
            case "heroTitle_CSS": self.myElement = self.get_heroTitle_CSS()
            case "accountVerify1_CSS": self.myElement = self.get_accountVerify1_CSS()
            case "loginNegativeVerifyMessage": self.myElement = self.get_loginNegativeVerifyMessage()
            case "loginEmptyVerifyMessage1": self.myElement = self.get_loginEmptyVerifyMessage1()
            case "loginEmptyVerifyMessage2": self.myElement = self.get_loginEmptyVerifyMessage2()
            case "orta3Element": self.myElement = self.get_orta3()
        self.scrollToElementMid(self.myElement)
        EC.visibility_of(self.myElement)
        assert textElement in self.myElement.text

    @staticmethod
    def get_base_url():
        return base_url
