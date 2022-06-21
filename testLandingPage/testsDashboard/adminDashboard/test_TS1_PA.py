import allure
from testLandingPage.testsMethods.admin_dashboard_methods import SearchAdminPanel
import pytest
import time


@pytest.mark.usefixtures("chromeSetup")
class TestPage:

    @allure.title('System Zarzadzania Serwisem Morskim Panel Administracyjny')
    def test_SZSM_page(self, chromeSetup):
        self.driver.get("http://localhost:8000/admin")
        site = SearchAdminPanel(self.driver)
        site.loginToAdminDashboard()
        site.checkSiteAdministrationNameModules()
#         site.addUser()
#         time.sleep(0)



