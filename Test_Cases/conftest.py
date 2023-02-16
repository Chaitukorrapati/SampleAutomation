from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "Chrome":
        driver = webdriver.Chrome()
        print("application launch in chrome")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("application launch in firefox ")
    else:
        driver = webdriver.Chrome()
        # driver = webdriver.Ie()            # internet explorer
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

###############GENERATE HTML REPORTS############################


def pytest_configure(config):
    config._metadata['project Name'] = 'nopCommerce'
    config._metadata['Module Name'] = 'customers'
    config._metadata['Tester'] = 'chaitanya'


def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("plugins",None)

