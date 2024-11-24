from selenium.webdriver.common.by import By

class loginPage():
    #object name
    usrname = 'user-name'
    passw = "//input[@id='password']"
    login_btn = "//input[@id='login-button']"
    error_msg = '[data-test="error"]'
    cart = 'shopping_cart_link'
    
    #object locator
    findUsername = (By.CSS_SELECTOR, '[data-test="username"]')
    findPass = (By.XPATH, "//input[@id='password']")
    findLogin = (By.XPATH, "//input[@id='login-button']")
    findError = (By.CSS_SELECTOR, '[data-test="error"]')