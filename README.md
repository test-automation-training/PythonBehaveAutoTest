# Python Behave Auto Test
This is an example repo for using Python [Behave](https://github.com/behave/behave), and we use so called "PageObject"
to implement an auto UI end to end test for:
1. Using Bing to search one keyword
2. Using my Microsoft user name and password to login Bing
3. After I login to Bing, and I can use `Scenario outline` or `Scenario template` to create a template for `Examples`

---

代码运行请使用命令：`$ behave`

---

你可以使用关键字:
1. `功能`表示`Feature`
2. `场景`表示`Scenario`
3. `场景大纲`表示`Scenario outline`或`Scenario template`
4. `当`表示`Given`
5. `假如`表示`When`
6. `那么`表示`Then`
7. `例子`表示`Examples`

---

请按照以下提交规范提交代码：
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
