import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/banuv/drivers/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()

driver.find_element(By.ID,"Email").clear()
driver.find_element(By.ID,"Email").send_keys("admin@yourstore.com")

driver.find_element(By.ID,"Password").clear()
driver.find_element(By.ID,"Password").send_keys("admin")

driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)

driver.find_element(By.XPATH,"//a[text()='Logout']").click()

'''from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage():
    text_username_id = "Email"
    text_password_id = "Password"
    button_login_xpath = "//button[@type='submit']"
    link_logout_linktext = "Logout"

    def __init__(self,driver):
        self.driver = driver

    def setUsername(self,username):
        self.driver.find_element(By.ID, self.text_username_id).clear()
        self.driver.find_element(By.ID,self.text_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID,self.text_password_id).clear()
        self.driver.find_element(By.ID,self.text_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()'''

