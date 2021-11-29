from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@given("a user is logged and the high contrast is enabled c4")
def given(context):
    context.driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
    context.driver.get('https://test.jasgme.com/pt/login')
    context.driver.maximize_window()

    login_input = context.driver.find_element_by_id('login')
    login_input.send_keys('lucas.bertoldo@dellead.com')

    password_input = context.driver.find_element_by_id('inputPassword')
    password_input.send_keys('123')

    login_button = context.driver.find_element_by_id('btnLogin')
    login_button.click()

    WebDriverWait(context.driver, 50).until(expected_conditions.visibility_of_element_located((
        By.XPATH, '//*[@id="sidebar"]/div/div[1]/div/div[1]/img')))


@when('the user clicks on disable it and logs out c4')
def when(context):
    WebDriverWait(context.driver, 50).until(expected_conditions.visibility_of_element_located((
        By.ID, 'bt-autocontraste')))

    toggle_high_contrast(context)

    WebDriverWait(context.driver, 50).until(expected_conditions.visibility_of_element_located((
        By.XPATH, '//*[@id="sidebar"]/div/div[1]/div/div[1]/img')))

    logout_btn = context.driver.find_element_by_xpath('//*[@id="navbarSupportedContent atalhos"]/ul/ul/li[2]/button')
    logout_btn.click()


@then('High Contrast should be disabled when the user logs in again c4')
def then(context):
    WebDriverWait(context.driver, 50).until(expected_conditions.visibility_of_element_located((
        By.ID, 'login')))

    login_input = context.driver.find_element_by_id('login')
    login_input.send_keys('lucas.bertoldo@dellead.com')

    password_input = context.driver.find_element_by_id('inputPassword')
    password_input.send_keys('123')

    login_button = context.driver.find_element_by_id('btnLogin')
    login_button.click()

    WebDriverWait(context.driver, 50).until(expected_conditions.visibility_of_element_located((
        By.XPATH, '//*[@id="sidebar"]/div/div[1]/div/div[1]/img')))

    body = context.driver.find_element_by_id('body')
    print(body.get_attribute('class'))
    assert 'high-contrast' not in body.get_attribute('class').split()
    context.driver.quit()


def toggle_high_contrast(context):
    high_contrast_btn = context.driver.find_element_by_id('bt-autocontraste')
    high_contrast_btn.click()


def check_if_high_contrast_is_enabled(context):
    body = context.driver.find_element_by_id('body')
    if 'high-contrast' in body.get_attribute('class').split():
        return True
    else:
        return False
