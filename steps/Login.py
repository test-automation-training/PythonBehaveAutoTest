# coding=utf-8
from behave import *

import pageObject.BingHomePage as BingHomePage
import pageObject.SignInPage as SignInPage


@Step('我已经登录到系统中')
def step_impl(context):
    BingHomePage.Signin_Link(context).click()
    SignInPage.Username_TextBox(context).clear()
    SignInPage.Username_TextBox(context).send_keys("pollyan212@hotmail.com")
    SignInPage.Submit_Button(context).click()
    SignInPage.Password_TextBox(context).clear()
    SignInPage.Password_TextBox(context).send_keys("Shunlian05")
    SignInPage.Submit_Button(context).click()
