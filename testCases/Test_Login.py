import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login():
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_HomepageTitle(self,setup):
        print("executing testcases")
        self.logger.info("***************Test__001__Login***************")
        self.logger.info("****************Verifying Homepage Title*************")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title

        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("************Homepage title test is passed************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_HomepageTitle.png")
            self.driver.close()
            self.logger.error("***********Homepage title is failed**********")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_LoginPage(self,setup):
        self.logger.info("***************Verifying LoginTest**************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("**********Login Test passed*********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_LoginpageTitle.png")
            self.driver.close()
            self.logger.error("*********Login Test failed*********")
            assert False


