from behave import *
import pageObject.BingHomePage as BingHomePage
import pageObject.SearchResultPage as SearchResultPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@Step ('我在bing主页')
def step_impl(context):
    BingHomePage.Open(context)

@Step ('我搜索“{keyword}”')
def step_impl(context,keyword):
    BingHomePage.Search_TextBox(context).clear()
    BingHomePage.Search_TextBox(context).send_keys(keyword)
    BingHomePage.Submit_Button(context).click()

@Step ('我应该看见包含“{keyword}”的搜索结果')
def step_impl(context,keyword):
    print "here is result:"
    print SearchResultPage.Search_TextBox(context)
    print context.driver.title
    WebDriverWait(context.driver, 10).until(EC.presence_of_all_elements_located)
    assert context.driver.title.__contains__(keyword)