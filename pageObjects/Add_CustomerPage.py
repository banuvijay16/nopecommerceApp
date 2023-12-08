import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:
    link_Customers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    link_Customers_menu_item_xpath = "//a[@href='/Admin/Customer/List']"
    button_Addnew_xpath = "//a[@class='btn btn-primary']"
    text_Email_xpath = "//input[@id='Email']"
    text_Password_xpath = "//input[@id='Password']"
    text_Firstname_xpath = "//input[@name='FirstName']"
    text_Lastname_xpath = "//input[@name='LastName']"
    radio_MaleGender_id = "Gender_Male"
    radio_FemaleGender_id = "Gender_Female"
    text_DoB_xpath = "//input[@id='DateOfBirth']"
    text_CompanyName_xpath = "//input[@id='Company']"
    checkbox_Tax_xpath = "//input[@id='IsTaxExempt']"
    text_Newsletter_xpath = "(//div[@role='listbox'])[1]"
    lstitem1_Newsletter_YourStoreName_xpath = "//span[normalize-space()='Your store name']"
    lstitem1_Newsletter_TestStore2_xpath = "//span[normalize-space()='Test store 2']"
    text_CustomerRoles_xpath = "(//div[@role='listbox'])[2]"
    lstitem2_Administrators_xpath = "//span[normalize-space()='Administrators']"
    lstitem2_ForumModerators_xpath = "//span[normalize-space()='Forum Moderators']"
    lstitem2_Guests_xpath = "//span[contains(normalize-space(),'Guests')]"
    lstitem2_Registered_xpath = "//span[normalize-space()='Registered']"
    lstitem2_Vendors = "//span[normalize-space()='Vendors']"
    dropdown_VendorID_xpath = "//select[@id='VendorId']"
    checkbox_Active_xpath = "//input[@id='Active']"
    text_AdminComment_xpath = "//textarea"
    button_save_xpath = "//button[@name='save']"

    def __init__(self,driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH,self.link_Customers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH, self.link_Customers_menu_item_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH, self.button_Addnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.text_Email_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.text_Password_xpath).send_keys(password)


    '''def setcustomerRoles(self,role):
        self.driver.find_element(By.XPATH, self.text_CustomerRoles_xpath).click()
        self.driver.implicitly_wait(20)

        if role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem2_Registered_xpath)
        elif role == "Adminstartors":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem2_Administrators_xpath)
        elif role == "Guests":
            time.sleep(20)
            self.listitem = self.driver.find_element(By.XPATH,"//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem2_Guests_xpath)
        elif role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem2_Registered_xpath)
        elif role == "Vendors":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem2_Vendors)
        elif role == "Forum Moderators":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem2_ForumModerators_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem2_Guests_xpath)
        time.sleep(20)
        #self.listitem.click()
        self.driver.execute_script("argument[0].click();", self.listitem)'''

    def setManageOfVendor(self,value):
        drpDown = Select(self.driver.find_element(By.XPATH, self.dropdown_VendorID_xpath))
        drpDown.select_by_visible_text(value)

    def setGender(self,gender):
        if gender == "Male":
            self.driver.find_element(By.ID,self.radio_MaleGender_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID,self.radio_FemaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.radio_MaleGender_id).click()

    def setFirstName(self,fname):
        self.driver.find_element(By.XPATH,self.text_Firstname_xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.XPATH,self.text_Lastname_xpath).send_keys(lname)

    def setDoB(self, DoB):
        self.driver.find_element(By.XPATH, self.text_DoB_xpath).send_keys(DoB)

    def setCompanyName(self,companyname):
        self.driver.find_element(By.XPATH, self.text_CompanyName_xpath).send_keys(companyname)

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH, self.text_AdminComment_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.button_save_xpath).click()


















