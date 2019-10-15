#-*- coding:utf-8 -*-
from selenium import webdriver

def before_all(context):
    context.driver = webdriver.Chrome()
    pass
def before_feature(context,feature):
    print 'before features'
    pass
def before_scenario(context,scenario):
    pass
def before_step(context,step):
    pass
def after_step(context,step):
    pass
def after_scenario(context,scenario):
    #kec_datafactory.clear_all_kec()
    pass
def after_feature(context,feature):
    pass
def after_all(context):
    pass