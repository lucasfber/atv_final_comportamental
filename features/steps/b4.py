from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@given("a user is on the Profile page and clicks on the Change Password button b4")
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

    context.driver.get('https://test.jasgme.com/en/profile')


@when('he enters a new password and a password confirmation')
def when(context):
    WebDriverWait(context.driver, 60).until(expected_conditions.visibility_of_element_located((
        By.ID, 'change')))

    change_password_btn = context.driver.find_element_by_id('change')
    change_password_btn.click()

    password_input = context.driver.find_element_by_xpath('//*[@id="password"]/div/div[1]/div/input')
    password_input.send_keys('1234')

    confirm_password_input = context.driver.find_element_by_xpath(
        '//*[@id="password"]/div/div[2]/div/input')
    confirm_password_input.send_keys('1234')

    context.driver.find_element_by_id('save').click()


@then('the platform should show him a success message')
def then(context):
    WebDriverWait(context.driver, 30).until(expected_conditions.visibility_of_element_located((
        By.ID, 'profileUpdated')))
    context.driver.quit()
    # profileUpdated