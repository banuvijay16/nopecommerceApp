from selenium.webdriver.common.by import By


class SearchCustomer:
    text_Email_id = "SearchEmail"
    text_firstname_id = "SearchFirstName"
    text_lastname_id = "SearchLastName"
    button_search_xpath = "//button[@id='search-customers']"

    table_xpath = "(//div[@class='col-md-12'])[1]"
    tablerows_xpath = "(//div[@class='col-md-12'])[1]//tbody//tr"
    tablecolumns_xpath = "(//div[@class='col-md-12'])[1]//tbody//tr//td"

    def __init__(self,driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element(By.ID,self. text_Email_id).clear()
        self.driver.find_element(By.ID,self.text_Email_id).send_keys(email)

    def setFirstName(self, fname):
        self.driver.find_element(By.ID,self.text_firstname_id).clear()
        self.driver.find_element(By.ID,self.text_firstname_id).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.ID,self.text_lastname_id).clear()
        self.driver.find_element(By.ID,self.text_lastname_id).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(By.XPATH,self.button_search_xpath).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH,self.tablerows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH,self.tablecolumns_xpath))

    def searchCustomerByEmail(self,email):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element(By.XPATH,self.table_xpath)
            emailid = table.find_element(By.XPATH,"(//div[@class='col-md-12'])[1]//tbody//tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
            return flag

    def searchCustomerByName(self,Name):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name = table.find_element(By.XPATH,"(//div[@class='col-md-12'])[1]//tbody//tr[" + str(r) + "]/td[3]").text
            if name == Name:
                flag = True
                break
            return flag





