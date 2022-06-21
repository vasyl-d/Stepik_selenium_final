from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_EMAIL = (By.NAME, "login-username")
    LOGIN_PASS = (By.NAME, "login-password")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators():
    PRODUCT_ADD_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    BASKET_VIEW = (By.CSS_SELECTOR, ".basket-mini>span>a")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    ALERT_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
