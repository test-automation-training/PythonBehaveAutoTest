# 本文件中定义behave支持的各种钩子方法，具体作用及用法参考behave文档中的说明

import chromedriver_binary as chrome
from selenium import webdriver

#在测试套件执行之前执行
def before_all(context):
    context.driver = webdriver.Chrome(chrome.chromedriver_filename)
    pass

#在每个feature文件之前执行
def before_feature(context, feature):
    print 'before features'
    pass

#在每个场景执行之前
def before_scenario(context, scenario):
    pass

#在每个步骤之前
def before_step(context, step):
    pass

#在每个步骤之后
def after_step(context, step):
    pass

#在每个场景执行之后
def after_scenario(context, scenario):
    # kec_data_factory.clear_all_kec()
    pass

#在每个feature执行之后
def after_feature(context, feature):
    pass

#在测试套件执行之后
def after_all(context):
    pass
