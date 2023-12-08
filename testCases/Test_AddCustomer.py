import string
import random

import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from pageObjects.LoginPage import LoginPage
from pageObjects.Add_CustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_AddCustomer(self,setup):
        self.logger.info("***************Test__003__AddCustomer***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.driver.implicitly_wait(20)

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**********Login successful**********")

        self.logger.info("***********Starting Add Customer**********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.addcust.clickOnAddNew()

        self.logger.info("*********Providing customer info***********")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        #self.addcust.setcustomerRoles("Administrators")
        self.addcust.setManageOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Banu")
        self.addcust.setLastName("Mathi")
        self.addcust.setDoB("03/28/1983")
        self.addcust.setCompanyName("Academy")
        self.addcust.setAdminContent("This is for testing purpose")
        self.addcust.clickOnSave()

        self.logger.info("********Saving customer info**********")

        self.logger.info("**********Adding customer validation started***********")

        self.msg = self.driver.find_element(By.TAG_NAME,"body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("********Add Customer test Passed*********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_AddCustomer_scr.png")
            self.logger.error("********Add Customer test Failed*********")
            assert True == False

            #self.driver.close()
            self.logger.info("********Ending Add Customer Test Case*******")

def random_generator(size=8, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
