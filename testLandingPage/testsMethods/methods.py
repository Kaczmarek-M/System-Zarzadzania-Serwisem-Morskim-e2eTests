import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from testLandingPage.locators.locators import SearchPageLocators, SearchNavBarItemsServiceTechnician, SearchNavBarItemsCoordinator, SearchNavBarItemsWarehouseman
import logging
import allure


class SearchSite:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    allure.step("Poprawne zalogowanie się do systemu")

    def properlyLoginAndPassword(self, activation_code, password):
        self.driver.find_element(By.CSS_SELECTOR, SearchPageLocators.loginInput).send_keys(activation_code)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, SearchPageLocators.passwordInput).send_keys(password)
        time.sleep(1)
        confirm = self.driver.find_element(By.CSS_SELECTOR, SearchPageLocators.confirmLoginButton)
        confirm.send_keys(Keys.ENTER)
        time.sleep(1)

    def checkNavbarForServiceTechnician(self):
        checkWelcomeMessage = self.driver.find_element(By.XPATH, SearchPageLocators.welcomeMessage).text
        assert checkWelcomeMessage == "Welcome Serwisant1"
        checkHome = self.driver.find_element(By.XPATH, SearchNavBarItemsServiceTechnician.home).text
        assert checkHome == "HOME"
        checkVessel = self.driver.find_element(By.XPATH, SearchNavBarItemsServiceTechnician.vessel).text
        assert checkVessel == "VESSEL"
        checkWarehouse = self.driver.find_element(By.XPATH, SearchNavBarItemsServiceTechnician.warehouse).text
        assert checkWarehouse == "BAZA"
        checkUserName = self.driver.find_element(By.XPATH, SearchNavBarItemsServiceTechnician.nickname).text
        assert checkUserName == "SERWISANT1"
        time.sleep(2)
        self.driver.find_element(By.XPATH, SearchNavBarItemsServiceTechnician.nickname).click()
        self.driver.find_element(By.XPATH, SearchPageLocators.logout).click()

    def checkNavbarForCoordinator(self):
        checkWelcomeMessage = self.driver.find_element(By.XPATH, SearchPageLocators.welcomeMessage).text
        assert checkWelcomeMessage == "Welcome Koordynator1"
        checkHome = self.driver.find_element(By.XPATH, SearchNavBarItemsCoordinator.home).text
        assert checkHome == "HOME"
        checkVessel = self.driver.find_element(By.XPATH, SearchNavBarItemsCoordinator.vessel).text
        assert checkVessel == "VESSEL"
        checkWarehouse = self.driver.find_element(By.XPATH, SearchNavBarItemsCoordinator.warehouse).text
        assert checkWarehouse == "BAZA"
        checkOrder = self.driver.find_element(By.XPATH, SearchNavBarItemsCoordinator.order).text
        assert checkOrder == "ZLECENIE"
        checkUserName = self.driver.find_element(By.XPATH, SearchNavBarItemsCoordinator.nickname).text
        assert checkUserName == "KOORDYNATOR1"
        self.driver.find_element(By.XPATH, SearchNavBarItemsCoordinator.nickname).click()
        self.driver.find_element(By.XPATH, SearchPageLocators.logout).click()

    def checkNavbarForWarehouseman(self):
        checkWelcomeMessage = self.driver.find_element(By.XPATH, SearchPageLocators.welcomeMessage).text
        assert checkWelcomeMessage == "Welcome Magazynier2"
        checkHome = self.driver.find_element(By.XPATH, SearchNavBarItemsWarehouseman.home).text
        assert checkHome == "HOME"
        checkWarehouse = self.driver.find_element(By.XPATH, SearchNavBarItemsWarehouseman.warehouse).text
        assert checkWarehouse == "MAGAZYN"
        checkUserName = self.driver.find_element(By.XPATH, SearchNavBarItemsWarehouseman.nickname).text
        assert checkUserName == "MAGAZYNIER2"
        self.driver.find_element(By.XPATH, SearchNavBarItemsWarehouseman.nickname).click()
        self.driver.find_element(By.XPATH, SearchPageLocators.logout).click()

    def checkShipImoNumber(self):
        self.driver.find_element(By.XPATH, SearchNavBarItemsServiceTechnician.vessel).click()
        imoNumber = self.driver.find_element(By.XPATH, SearchNavBarItemsServiceTechnician.textField)
        imoNumber.send_keys("7907659")
        iframe2 = self.driver.find_element(By.CSS_SELECTOR, SearchNavBarItemsServiceTechnician.frame2)
        self.driver.switch_to.frame(iframe2)
        self.driver.find_element(By.CSS_SELECTOR, SearchNavBarItemsServiceTechnician.moreInfoButton).click()

        parentWindow = self.driver.current_window_handle
        allWindows = self.driver.window_handles
        childWindow = [window for window in allWindows if window != parentWindow][0]
        self.driver.switch_to.window(childWindow)

        imoMmsiNumber = self.driver.find_element(By.XPATH, SearchNavBarItemsServiceTechnician.imoMmsi).text
        assert imoMmsiNumber == "7907659 / 210231000"
        shipFlag = self.driver.find_element(By.XPATH, SearchNavBarItemsServiceTechnician.flag).text
        assert shipFlag == "Cyprus"
        destinationPort = self.driver.find_element(By.XPATH, SearchNavBarItemsServiceTechnician.destinationPort).text
        assert destinationPort == "PLGDY-SEKAA-PLGDY"
        self.driver.close()
        self.driver.switch_to.window(parentWindow)

        time.sleep(2)



















