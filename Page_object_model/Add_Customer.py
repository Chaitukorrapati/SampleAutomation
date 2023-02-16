from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.by import By

class AddCustomer_name:
    Click_on_customer_main_menu_xpath = "//a[@href ='#']//p[contains(text(), 'Customers' )]"
    click_on_customer_sub_menu_xpath = "//a[@href='/Admin/Customer/List']"
    click_on_add_new_button_xpath = "//a[@class='btn btn-primary']"
    click_on_Email_xpath = "//input[@id='Email']"
    click_on_Password_xpath = "//input[@id='Password']"
    click_on_first_name_xpath = "//input[@id='FirstName']"
    click_on_last_name_xpath = "//input[@id='LastName']"
    click_on_gender_male_xpath = "//input[@id='Gender_Male']"
    click_on_gender_female_xpath = "//input[@id='Gender_Female']"
    click_on_date_picker_xpath = "//input[@id='DateOfBirth']"
    click_on_news_letter_xpath = "//div[@class='input-group-append']//div[@role='listbox']"
    click_on_test_store2_xpath = "//li[text()='Test store 2']"
    click_on_company_name_xpath = "//input[@id='Company']"
    click_on_Customers_role_xpath = "(//div[@role='listbox'])[1]"
    click_on_cross_xpath = "//ul[@id='SelectedCustomerRoleIds_taglist']/li/span[2]"
    click_on_Administrator_xpath = "//li[text()='Administrators']"
    click_on_Guests_xpath = "//li[text()='Guests']"
    click_on_Registered_xpath = "//li[text()='Registered']"
    click_on_vendors_xpath = "//li[text()='Vendors']"
    click_on_manager_vendor_xpath = "//select[@id='VendorId']"
    click_on_Admin_content_xpath = "//textarea[@id='AdminComment']"
    click_on_save_button_xpath = "//button[@name='save']"


    def __init__(self,driver):
        self.driver = driver

    def clickoncustomer1(self):
        self.driver.find_element(By.XPATH,self.Click_on_customer_main_menu_xpath).click()

    def click_on_sub_menu(self):
        self.driver.find_element(By.XPATH,self.click_on_customer_sub_menu_xpath).click()

    def clickonaddnew(self):
        self.driver.find_element(By.XPATH,self.click_on_add_new_button_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.click_on_Email_xpath).send_keys(email)

    def setpassword(self,password):
        self.driver.find_element(By.XPATH,self.click_on_Password_xpath).send_keys(password)

    def click_on_news_letter(self,value):
        drp = Select(self.driver.find_element(By.XPATH,self.click_on_news_letter_xpath).click())
        drp.select_by_visible_text(value)

    def setcustomerrole(self,role):
        # self.driver.find_element(By.XPATH, self.click_on_Customers_role_xpath).click()
        if role =="Registered":
            listitems = self.driver.find_element(By.XPATH,self.click_on_Registered_xpath).click()

        elif role == "Administrators":
            listitems = self.driver.find_element(By.XPATH,self.click_on_Administrator_xpath).click()

        elif role == "Guests":
            # self.driver.find_element(By.XPATH,self.click_on_cross_xpath).click()
            # time.sleep(5)
            listitems = self.driver.find_element(By.XPATH,self.click_on_Guests_xpath).click()


        elif role == "Registered":
            listitems = self.driver.find_element(By.XPATH,self.click_on_Registered_xpath).click()

        elif role == "Vendors":
            listitems = self.driver.find_element(By.XPATH,self.click_on_vendors_xpath).click()

        else:
            listitems = self.driver.find_element(By.XPATH, self.click_on_Guests_xpath).click()
        # listitems.click();
        self.driver.execute_script("arguments[0].click:",listitems)

    def setmangerVendor(self,value):
        drp = Select(self.driver.find_element(By.XPATH, self.click_on_manager_vendor_xpath))
        drp.select_by_visible_text(value)


    def setgender(self,gender):
        if gender == "male":
            self.driver.find_element(By.XPATH, self.click_on_gender_male_xpath).click()

        elif gender == "Female":
            self.driver.find_element(By.XPATH, self.click_on_gender_female_xpath).click()

        else:
            self.driver.find_element(By.XPATH, self.click_on_gender_male_xpath).click()

    def setfirstname(self,firstname):
        self.driver.find_element(By.XPATH, self.click_on_first_name_xpath).send_keys(firstname)

    def setlastname(self,lastname):
        self.driver.find_element(By.XPATH, self.click_on_last_name_xpath).send_keys(lastname)

    def setdob(self,date):
        self.driver.find_element(By.XPATH, self.click_on_date_picker_xpath).send_keys(date)

    def setcompanyname(self,Companyname):
        self.driver.find_element(By.XPATH, self.click_on_company_name_xpath).send_keys(Companyname)

    def setAdmncontent(self,description):
        self.driver.find_element(By.XPATH,self.click_on_Admin_content_xpath).send_keys(description)

    def save_button(self):
        self. driver.find_element(By.XPATH,self.click_on_save_button_xpath).click()