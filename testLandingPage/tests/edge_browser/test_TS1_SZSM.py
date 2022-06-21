import allure
from testLandingPage.testsMethods.methods import SearchSite
import pytest

@pytest.mark.usefixtures("edgeSetup")
class TestPage:

    @allure.title('System Zarzadzania Serwisem Morskim tests')
    def test_SZSM_page(self, edgeSetup):
        self.driver.get("http://localhost:8080")
        site = SearchSite(self.driver)
        site.properlyLoginAndPassword("Serwisant1", "PJATK1234")
        site.checkNavbarForServiceTechnician()
