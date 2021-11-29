from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@given("a user with a valid password")
def given(context):
    context.driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
    context.driver.get('https://test.jasgme.com/pt/login')
    context.driver.maximize_window()


@when('he enters only his password')
def when(context):
    password_input = context.driver.find_element_by_id('inputPassword')
    password_input.send_keys('wrongPa55w0rd')


@then('the Sign In button should remain disabled a6')
def then(context):
    WebDriverWait(context.driver, 20).until(expected_conditions.element_attribute_to_include((
        By.ID, 'btnLogin'), 'disabled'))
    context.driver.quit()