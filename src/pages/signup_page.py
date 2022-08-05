from seleniumpagefactory.Pagefactory import PageFactory

from src.resources.locators import SIGNUP_PAGE_LOCATORS


class SignupPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = SIGNUP_PAGE_LOCATORS

    def set_email(self, email):
        self.email.set_text(email)

    def set_password(self, password):
        self.password.set_text(password)

    def signup(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.signup_button.click_button()

    def go_to_login(self):
        self.login.click_button()
