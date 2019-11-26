# coding=utf-8
from behave import Step

import page_object.BingHomePage as BingHomePage
import page_object.SignInPage as SignInPage


@Step('我已经登录到系统中')
def step_impl(context):
    # 登录步骤
    BingHomePage.sign_in_link(context).click()
    SignInPage.username_textbox(context).clear()
    SignInPage.username_textbox(context).send_keys("pollyan212@hotmail.com")
    SignInPage.submit_button(context).click()
    SignInPage.password_textbox(context).clear()
    SignInPage.password_textbox(context).send_keys("Shunlian05")
    SignInPage.submit_button(context).click()
