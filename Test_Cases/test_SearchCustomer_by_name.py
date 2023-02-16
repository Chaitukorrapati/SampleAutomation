import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Page_object_model.Login_page import Loginpage
from Page_object_model.Search_Customers_Page import SearchCustomer
from Utilities.readproperties import Readconfig
from Utilities.custom_Logger import LogGen
from Page_object_model.Add_Customer import AddCustomer_name


class Search_CustomerByEmail_004:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getuseremail()
    password = Readconfig.getpassword()

    logger = LogGen.loggen()


    @pytest.marks.sanity
    def test_SearchCustomerByName(self, setup):
        self.logger.info("*****************test_AddCustomer***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Loginpage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.click_on_login()
        self.logger.info("********************Login Was Successfully****************************")

        self.logger.info("*********************SearchCustomer By Name***********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstname("victoria")
        searchcust.setlastname("Terces")
        searchcust.click_on_search_button()
        time.sleep(5)
        status = searchcust.SearchCustomerByName("victoria_victoria@nopCommerce.com")
        assert True == status
        self.logger.info("**********************Search_Customer_Finally_Closed*******************************")
