import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Page_object_model.Login_page import Loginpage
from Utilities.readproperties import Readconfig
from Utilities.custom_Logger import LogGen


class Test_001_login():
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getuseremail()
    password = Readconfig.getpassword()

    logger = LogGen.loggen()



    # @pytest.marks.sanity
    # @pytest.marks.regression
    def test_login(self, setup):
        self.logger.info("*****************test_login***********")
        self.logger.info("*****************verifying_home page***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*****************Home page title is passed***********")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_login.png")
            self.logger.error("*****************Home page title is Failed***********")
            assert False

    # @pytest.marks.regression
    def test_homepage(self, setup):
        # self.logger.info("*****************test_homepage***********")
        self.logger.info("*****************verify dashboard page***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Loginpage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.click_on_login()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("*****************Home page title is passed***********")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_homepage.png")
            self.driver.close()
            self.logger.error("*****************Home page title got failed***********")
            assert False
