import time

import pytest
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC


class Test_002_DDT_Login():
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    #username = ReadConfig.getUserEmail()
    #password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_LoginPage(self,setup):
        self.logger.info("***************Test_002_DDT_Login****************")
        self.logger.info("***************Verifying Login DDT Test**************")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of rows in excel:", self.rows)

        lst_status = []

        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path,'Sheet1',r,2)
            self.exp = XLUtils.readData(self.path,'Sheet1',r, 3)

            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            self.driver.implicitly_wait(10)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "pass":
                    self.logger.info("****Passed***")
                    self.lp.clickLogout()
                    lst_status.append("pass")
                elif self.exp == "fail":
                    self.logger.info("****Failed***")
                    self.lp.clickLogout()
                    lst_status.append("fail")
            elif act_title != exp_title:
                if self.exp == "pass":
                    self.logger.info("****Failed***")
                    lst_status.append("fail")
                elif self.exp == "fail":
                    self.logger.info("****Passed***")
                    lst_status.append("pass")
        if "fail" not in lst_status:
            self.logger.info("******Login DDT test case passed*********")
            self.driver.close()
            assert True
        else:
            self.logger.info("******Login DDT test case Failed*********")
            self.driver.close()
            assert False

        self.logger.info("**********End of LoginTestcase002_DDT*********")
        self.logger.info("*****completed Testcase_002********")



