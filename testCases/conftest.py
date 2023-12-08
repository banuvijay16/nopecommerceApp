from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launchin chrome browser................")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launchin firefox browser.................")
    else:
        driver = webdriver.ie()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

##pytest HTML reports###

def pytest_configure(config):
    config.my_metadata = {'Project name': 'nop commerce'}
    #config.metadata['Project name'] = 'nop commerce'
    config.my_metadata = {'Module name': 'Customers'}
    config.my_metadata = {'Tester': 'Banu'}
    #config.metadata['Module name'] = 'Customers'
    #config.metadata['Tester'] = 'Banu'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


