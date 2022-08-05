from seleniumpagefactory.Pagefactory import PageFactory

from src.resources.locators import PLP_PAGE_LOCATORS


class PlpPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    ZERO_RESULTS_STR = '"0" resultados'
    NUMBER_OF_RESULTS_STR = 'Productos'

    locators = PLP_PAGE_LOCATORS

    def is_no_results_text_visible(self):
        return self.no_results.visibility_of_element_located(3) \
            and self.ZERO_RESULTS_STR in self.no_results.get_text()

    def is_results_text_visible(self):
        return self.results.visibility_of_element_located(5) \
            and self.NUMBER_OF_RESULTS_STR in self.results.get_text()

    def get_results_number(self):
        if self.is_results_text_visible():
            return self.results.get_text().split()[0]
