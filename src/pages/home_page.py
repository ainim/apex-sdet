from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from src.resources.locators import HOME_PAGE_LOCATORS


class HomePage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    URL = 'https://www.liverpool.com.mx/tienda/home'
    SEARCH_BUTTON = 'SB'
    ENTER_KEY = Keys.ENTER

    locators = HOME_PAGE_LOCATORS


    def go_to_login(self):
        self.login.click_button()


    def search_for(self, text, search_trigger = SEARCH_BUTTON):
        self.search_bar.set_text(text)

        if search_trigger == self.SEARCH_BUTTON:
            self.search_button.click_button()
        else:
            self.search_bar.send_keys(Keys.ENTER)
        return self.wait_for_title_to_contain_text(text.strip())

    def wait_for_title_to_contain_text(self, text):
        return WebDriverWait(self.driver, 3).until(EC.title_contains(text))

    def is_search_results_iframe_shown(self):
        return self.search_results.visibility_of_element_located(3)

    def type_in_search_bar(self, text):
        self.search_bar.set_text(text)


    def click_search_button(self):
        self.search_button.click_button()


    def go_to_screens_plp(self):
        self.screens_category.click_button()
