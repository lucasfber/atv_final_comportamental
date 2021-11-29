from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@given("a user with an invalid email")
def given(context):
    context.driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
    context.driver.get('https://test.jasgme.com/pt/login')
    context.driver.maximize_window()


@when('he enters his credentials and click Sign In button a2')
def when(context):
    login_input = context.driver.find_element_by_id('login')
    login_input.send_keys('any_email@mail.com')

    password_input = context.driver.find_element_by_id('inputPassword')
    password_input.send_keys('123')

    login_button = context.driver.find_element_by_id('btnLogin')
    login_button.click()


@then('the platform should show him a error message a2')
def then(context):
    WebDriverWait(context.driver, 20).until(expected_conditions.visibility_of_element_located((
        By.XPATH, '//*[@id="body"]/app-root/app-login/div/div/app-login-form/div[2]/div/div/div/form/div[1]')))
    context.driver.quit()