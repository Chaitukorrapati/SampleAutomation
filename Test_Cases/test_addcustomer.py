import random
import string

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Page_object_model.Login_page import Loginpage
from Utilities.readproperties import Readconfig
from Utilities.custom_Logger import LogGen
from Page_object_model.Add_Customer import AddCustomer_name


class Test_003_login():
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getuseremail()
    password = Readconfig.getpassword()

    logger = LogGen.loggen()

    @pytest.marks.sanity
    @pytest.marks.regression
    def test_AddCustomer(self, setup):
        self.logger.info("*****************test_AddCustomer***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.lp = Loginpage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.click_on_login()
        self.logger.info("********************Login Was Successfully****************************")

        self.addcust = AddCustomer_name(self.driver)
        self.addcust.clickoncustomer1()
        self.addcust.click_on_sub_menu()
        self.addcust.clickonaddnew()
        self.logger.info("************Providing Customer info****************")
        self.email = self.random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setpassword("Amma**17")
        self.addcust.click_on_news_letter_xpath("Test store 2")
        self.addcust.setcustomerrole("Guests")
        self.addcust.setmangerVendor("vendor 2")
        self.addcust.setgender("male")
        self.addcust.setfirstname("chaitanya")
        self.addcust.setlastname("Korrapati")
        self.addcust.setdob("07/02/1996")
        self.addcust.setcompanyname("Capgemini")
        self.addcust.setAdmncontent("This is Testing of............")
        self.addcust.save_button()
        self.logger.info("************Saving customer Info****************")

        self.logger.info("*******************Add Customer Validation**********")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text()
        print(self.msg)
        if "customer has been successfully." in self.msg:
            assert True == True
            self.logger.info("add Customer test case are passed")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "AddCustomer.png")
            self.logger.error("add customer are failed")
            assert True == False
            self.driver.close()
        self.logger.info("**********Ending Home page Title test***************")

    def random_generator(size=8,chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(8))




















