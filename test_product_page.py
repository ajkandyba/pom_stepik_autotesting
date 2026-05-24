from pages.product_page import ProductPage


def test_add_project_to_cart(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_added_product_message(product_name)
    page.should_be_added_product_price_message(product_price)