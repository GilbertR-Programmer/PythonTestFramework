from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@given('I open the Google homepage')
def step_impl(context):
    context.browser = webdriver.Chrome()  # Ensure that ChromeDriver is available
    context.browser.get("https://www.google.com")

@when('I search for "{query}"')
def step_impl(context, query):
    search_box = context.browser.find_element(By.NAME, 'q')
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

@then('the results page should display results for "{query}"')
def step_impl(context, query):
    assert query in context.browser.title
    context.browser.quit()
