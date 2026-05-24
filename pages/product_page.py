from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART).click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_added_product_message(self, product_name):
        added_product_message = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_MESSAGE).text
        assert product_name in added_product_message

    def should_be_added_product_price_message(self, product_price):
        added_product_price_message = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE_MESSAGE).text
        assert product_price == added_product_price_message


