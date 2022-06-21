import allure

from testLandingPage.testsMethods.methods import SearchSite
import pytest
import time


@pytest.mark.usefixtures("firefoxSetup")
class TestPage:

    @allure.title('System Zarzadzania Serwisem Morskim tests')
    def test_SZSM_page(self, firefoxSetup):
        self.driver.get("http://localhost:8080")
        site = SearchSite(self.driver)
        site.properlyLoginAndPassword("Magazynier2", "Kicha1234!")
        site.checkNavbarForWarehouseman()