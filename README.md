# Python Behave Auto Test
## 一、使用工具、依赖
1. [Behave](https://github.com/behave/behave)
2. Selenium Webdriver


## 二、运行
代码运行请使用命令：`$ behave`

## 三、内容
这是一个基于Python，[Behave](https://github.com/behave/behave)以及PageObject的一个UI自动化测试实例。
他包含如下场景:
1. 用Bing搜索引擎搜索关键字。
2. 使用微软用户名密码登录
3. 使用Scenario outline进行多次查询

你可以使用关键字:
1. `功能`表示`Feature`
2. `场景`表示`Scenario`
3. `场景大纲`表示`Scenario outline`或`Scenario template`
4. `当`表示`Given`
5. `假如`表示`When`
6. `那么`表示`Then`
7. `例子`表示`Examples`

## 四、规范

### 案例设计

1. 业务方向
* 需要包含主干功能案例。
* 需要包含必要的反案例。
* 案例需要有业务含义，描述用户业务行为，注意不要描述用户操作步骤。
* 案例以用户场景的方式组织，保持场景适当的粒度，新功能或新项目可尝试先在现有场景中添加步骤。
* 测试断言完整。
* 参数中有限取值参数如用户类型，状态等。需要分析等价类并针对性设计案例。
* 需要参考团队的启发式测试列表设计案例。

2. 技术方向
* 界面元素需要以PageObject形式封装，以节省案例维护成本。
* 参数有取值范围时需要设计[边界条件](https://baike.baidu.com/item/%E8%BE%B9%E7%95%8C%E5%80%BC%E6%B5%8B%E8%AF%95/2511553?fr=aladdin)案例。
* 页面元素优先用ID方式获取，除特殊情况，避免XPath方式。
* 页面元素在操作之前有适当的检查机制保证可访问。
* 上述所有条件的组合，在符合业务含义的情况下应适当考虑组合测试。

### 请按照以下提交规范提交代码：
* br: 此项特别针对bug号，用于向测试反馈bug列表的bug修改情况 
* feat：新功能（feature） 
* fix：修补bug 
* docs：文档（documentation） 
* style： 格式（不影响代码运行的变动） 
* refactor：重构（即不是新增功能，也不是修改bug的代码变动） 
* test：增加测试 
* chore：构建过程或辅助工具的变动 
* revert: feat(pencil): add 'graphiteWidth' option (撤销之前的commit) 

⚠️示例提交规范：
* `refactor: rename files`
* `feat(#12): add search multi keywords test scenario`

### 度量指标
* 案例覆盖率（按优先级，正反案例）
