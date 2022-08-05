import pytest
import time

from selenium import webdriver

from src.pages.plp_page import PlpPage

from src.pages.home_page import HomePage
from test.base_test import BaseTest

negative_st = ['       \t\t', '`~!@#$%^&*()_+-=\|}]{[}";:/".><,.']
st = ['Alaciadora Babyliss placas de nano titanium', 'BABYLISS', 'Bntmgp9557es', 'blu sa', 'casacasa']


@pytest.fixture(scope="class")
def homepage(driver):
    return HomePage(driver)

@pytest.fixture(scope="class")
def plppage(driver):
    return PlpPage(driver)

@pytest.fixture(scope="class")
def driver():
    _driver = webdriver.Chrome()
    yield _driver
    _driver.quit()

@pytest.fixture(scope="module", params=st)
def search_terms(request):
    return request.param

@pytest.fixture(scope="module", params=negative_st)
def negative_search_terms(request):
    return request.param



class TestSearchBar(BaseTest):

    @pytest.mark.smoke
    @pytest.mark.negative
    def test_search_bar_001(self, driver, homepage, plppage, negative_search_terms):
        driver.get(HomePage.URL)
        assert homepage.search_for(negative_search_terms)
        assert plppage.is_no_results_text_visible()

    @pytest.mark.smoke
    def test_search_bar_002(self, driver, homepage, plppage, search_terms):
        driver.get(HomePage.URL)
        assert homepage.search_for(search_terms)
        print('Results found: ', plppage.get_results_number())

    @pytest.mark.parametrize('search_term', ['sapatos'])
    def test_search_bar_003(self, driver, homepage, plppage, search_term):
        driver.get(HomePage.URL)
        homepage.type_in_search_bar(search_term)
        assert homepage.is_search_results_iframe_shown()

    @pytest.mark.skip('Blocked, waiting for BA details')
    @pytest.mark.parametrize('search_term', ['nonexistent'])
    def test_search_bar_004(self, driver, homepage, plppage, search_term):
        driver.get(HomePage.URL)
        homepage.type_in_search_bar(search_term)
        assert homepage.is_search_results_iframe_shown()
        #assert no results message should be shown.

    @pytest.mark.parametrize('search_term', ['Alaciadora Babyliss placas de nano titanium',  ' \tAlaciadora Babyliss placas de nano titanium\t   \t'])
    def test_search_bar_005(self, driver, homepage, plppage, search_term):
        driver.get(HomePage.URL)
        assert homepage.search_for(search_term, HomePage.ENTER_KEY)
        print('Results found: ', plppage.get_results_number())
