from selenium.webdriver.common.by import By
from testLandingPage.locators.locators import SearchAdminDashboard
import logging
import allure

class SearchAdminPanel:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    @allure.step("Logowanie do panelu administracyjnego")
    def loginToAdminDashboard(self):
        inputUsername = self.driver.find_element(By.XPATH, SearchAdminDashboard.username)
        inputUsername.send_keys('admin')
        inputPassword = self.driver.find_element(By.XPATH, SearchAdminDashboard.password)
        inputPassword.send_keys('admin123')
        self.driver.find_element(By.CSS_SELECTOR, SearchAdminDashboard.loginButton).click()

    @allure.step("Sprawdzanie czy wszystkie nazwy modułów wyświetlają się poprawnie")
    def checkSiteAdministrationNameModules(self):
        accountsModuleName = self.driver.find_element(By.CSS_SELECTOR, SearchAdminDashboard.accountsNameModule).text
        assert accountsModuleName == "ACCOUNTS"
        authenticationAndAuthorizationModuleName = self.driver.find_element(By.CSS_SELECTOR,
               SearchAdminDashboard.authenticationAndAuthorizationModule).text
        assert authenticationAndAuthorizationModuleName == "AUTHENTICATION AND AUTHORIZATION"
        ordersModuleName = self.driver.find_element(By.CSS_SELECTOR, SearchAdminDashboard.ordersModule).text
        assert ordersModuleName == "ORDERS"
        shipsModuleName = self.driver.find_element(By.CSS_SELECTOR, SearchAdminDashboard.shipsModule).text
        assert shipsModuleName == "SHIPS"
        tokenBlacklistModuleName = self.driver.find_element(By.CSS_SELECTOR, SearchAdminDashboard.tokenBlacklistModule).text
        assert tokenBlacklistModuleName == "TOKEN BLACKLIST"
        warehouseModuleName = self.driver.find_element(By.CSS_SELECTOR, SearchAdminDashboard.warehouseModule).text
        assert warehouseModuleName == "WAREHOUSE"

    @allure.step("dodawanie użytkownika do systemu")
    def addUser(self):
        self.driver.find_element(By.XPATH, SearchAdminDashboard.addButtonAccounts).click()
        addUsername = self.driver.find_element(By.CSS_SELECTOR, SearchAdminDashboard.usernameTextField)
        addUsername.send_keys('Serwisant1')
        addPassword = self.driver.find_element(By.CSS_SELECTOR, SearchAdminDashboard.passwordTextField)
        addPassword.send_keys('PJATK1234')
        confirmPassword = self.driver.find_element(By.CSS_SELECTOR, SearchAdminDashboard.confirmationPasswordTextField)
        confirmPassword.send_keys('PJATK1234')
        addFirstName = self.driver.find_element(By.CSS_SELECTOR, SearchAdminDashboard.firstNameTextField)
        addFirstName.send_keys('Marek')
        addLastName = self.driver.find_element(By.CSS_SELECTOR, SearchAdminDashboard.lastNameTextField)
        addLastName.send_keys('Kowalik')
        addMail = self.driver.find_element(By.CSS_SELECTOR, SearchAdminDashboard.mailTextField)
        addMail.send_keys('Kowalik@gmail.com')
        self.driver.find_element(By.CSS_SELECTOR, SearchAdminDashboard.roleOptions).click()
        self.driver.find_element(By.XPATH, SearchAdminDashboard.serwisantRole).click()
        self.driver.find_element(By.XPATH, SearchAdminDashboard.saveButton).click()
        successAddUserMessage = self.driver.find_element(By.XPATH, SearchAdminDashboard.addUserSuccessMessage).text
        assert successAddUserMessage == "The user “Serwisant1” was added successfully. You may edit it again below."


