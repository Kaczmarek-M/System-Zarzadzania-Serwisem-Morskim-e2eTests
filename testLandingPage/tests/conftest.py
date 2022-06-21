import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import allure
from testLandingPage.utils.driver_factory import DriverFactory

# @pytest.fixture()
# def setup(request):
#     driver = webdriver.Chrome(ChromeDriverManager().install())
#     driver.implicitly_wait(5)
#     driver.maximize_window()
#     request.cls.driver = driver
#     before_failed = request.session.testsfailed
#     yield
#     if request.session.testsfailed != before_failed:
#         allure.attach(driver.get_screenshot_as_png(), name="Test failed", attachment_type=AttachmentType.PNG)
#     driver.quit()

@pytest.fixture()
def chromeSetup(request):
    driver = DriverFactory.get_driver('chrome')
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    before_failed = request.session.testsfailed
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name="Test failed", attachment_type=AttachmentType.PNG)
    driver.close()

@pytest.fixture()
def edgeSetup(request):
    driver = DriverFactory.get_driver('edge')
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    before_failed = request.session.testsfailed
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name="Test failed", attachment_type=AttachmentType.PNG)
    driver.quit()

@pytest.fixture()
def firefoxSetup(request):
    driver = DriverFactory.get_driver('firefox')
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    before_failed = request.session.testsfailed
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name="Test failed", attachment_type=AttachmentType.PNG)
    driver.quit()
