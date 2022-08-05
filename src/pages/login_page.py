from seleniumpagefactory.Pagefactory import PageFactory

from src.resources.locators import LOGIN_PAGE_LOCATORS


class LoginPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = LOGIN_PAGE_LOCATORS

    def set_email(self, email):
        self.email.set_text(email)

    def set_password(self, password):
        self.password.set_text(password)

    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.login_button.click_button()

    def go_to_signup(self):
        self.signup.click_button()
