from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')

class ProductPageLocators():
    ADD_TO_CART = (By.CLASS_NAME, 'btn-add-to-basket')
    PRODUCT_NAME = (By.TAG_NAME, 'h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    ADDED_PRODUCT_MESSAGE = (By.CSS_SELECTOR, '#messages .alert:nth-child(1) strong')
    ADDED_PRODUCT_PRICE_MESSAGE = (By.CSS_SELECTOR, '.alert-info strong')