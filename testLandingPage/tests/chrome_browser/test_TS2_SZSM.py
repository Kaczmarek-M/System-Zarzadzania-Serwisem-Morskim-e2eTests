import allure
from testLandingPage.testsMethods.methods import SearchSite
import pytest
import time


@pytest.mark.usefixtures("chromeSetup")
class TestPage:

    @allure.title('System Zarzadzania Serwisem Morskim tests')
    def test_SZSM_page(self, chromeSetup):
        self.driver.get("http://localhost:8080")
        site = SearchSite(self.driver)
        site.properlyLoginAndPassword("Koordynator1", "Maty1234")
        site.checkNavbarForCoordinator()

