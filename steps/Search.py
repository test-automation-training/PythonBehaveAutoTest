# coding=utf-8
from behave import Step
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

import page_object.BingHomePage as BingHomePage
import page_object.SearchResultPage as SearchResultPage


@Step('我在bing主页')
def step_impl(context):
    BingHomePage.open(context)


@Step('我搜索“{keyword}”')
def step_impl(context, keyword):
    # 输入搜索内容并提交，注意最好每次输入之前先清除内容。
    BingHomePage.search_textbox(context).clear()
    BingHomePage.search_textbox(context).send_keys(keyword)
    BingHomePage.submit_button(context).click()


@Step('我应该看见包含“{keyword}”的搜索结果')
def step_impl(context, keyword):
    # 等待机制也可在step中使用
    WebDriverWait(context.driver, 10).until(ec.presence_of_all_elements_located)
    assert context.driver.title.__contains__(keyword)
