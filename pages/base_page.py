class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.error_msg = ''
        self.browser.implicitly_wait(timeout)

    def open(self): 
        # ваша реализация
        self.browser.get(self.url)        

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except Exception as ex:
            self.error_msg = f"An exception of type {type(ex).__name__} случилось."
            return False
        return True
