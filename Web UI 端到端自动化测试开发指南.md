## 一、案例设计规范

### 1. 业务方向
* 需要包含主干功能案例。比如：测试用户登录，作为正案例必须测试用户登录成功。
* 需要包含必要的反案例。比如：测试用户登录，作为反案例必须测试用户登录失败，但失败分多钟情况导致失败，需用多个反案例覆盖。
* 案例需要有业务含义，描述用户业务行为，注意不要描述用户操作步骤。比如：“用户成功登录”可以是用户业务场景，但“打开首页，输入用户名密码，点击登录按钮”就属于操作步骤。
* 案例以用户场景的方式组织，保持场景适当的粒度，新功能或新项目可尝试先在现有场景中添加步骤，具体粒度标准因业务复杂度和team实际情况而定。案例示例：有用户注册，登录和更新用户信息三个功能，应该是以流程方式组织测试案例：先注册，之后登录再修改信息。
* 测试断言完整。比如测试用户登录，应该保证用户能够langding到登录后的页面。
* 对于诸如如用户类型，状态等有限取值类型因素。需要分析等价类并针对性设计案例。
* 需要参考团队的启发式测试列表设计案例。
* 上述所有条件的组合，在符合业务含义的情况下应适当考虑组合测试。

### 2. 技术方向
* 界面元素需要以PageObject形式封装，以节省案例维护成本。
* 参数有取值范围时需要设计[边界条件](https://baike.baidu.com/item/%E8%BE%B9%E7%95%8C%E5%80%BC%E6%B5%8B%E8%AF%95/2511553?fr=aladdin)案例。
* 页面元素优先用ID方式获取，除特殊情况，尽量避免XPath方式。
* 页面元素在操作之前有适当的检查机制保证可访问。


## 二、代码实现规范
### 1. 依赖管理
使用 pipenv & Pipfile 管理代码依赖，保证每个测试开发人员都可以在自己的电脑中快速构建起依赖环境

### 2. 命名
团队应共同制定测试用例的命名规范，且命名应当具有业务含义，由于 Behave 使用 Gherkin 语法，因此建议命名采用如
"As a user I want to ..."

### 3. 案例 scenario 的结构规范
请使用 Behave 推荐的 Given、When、Then 的形式组织代码

* Given -- 准备数据
* When -- 被测内容
* Then -- 断言内容

同时应使用 PageObject 模式对整个代码结构管理

### 4. 包结构设计
请按照 page_object / steps / cases 的方式设计包结构

### 5. 案例编写
1. 请参见示例代码中，`bing_search_background.feature`

在案例编写中，务必对每个案例都要进行断言，断言内容：
* 元素是否加载成功
* 想要得到的元素/内容是否存在
* 流程是否跑的通

### 6. 重构
请在修改/编写 Web UI 测试的时候，一直保持重构的心态：
#### a. 去掉无用的内容
* 删掉 Scenario 中无用代码
* 删掉在提交代码前将代码中测试用的 log 信息
* 删掉在书写过程中使用的 sleep(time)
* 删掉无实际意义的注释代码
* 删掉无实际意义的描述代码

#### b. 添加有意义的内容
* 赋予变量有意义的名称
* 添加有描述意义的代码测试场景描述

### 7. 小步提交 & 七步提交法
一般来说，建议 小步提交，即按自己的 Tasking 步骤来的提交，每一小步都有对应的提交信息。这样做的主要目的是：防止一次修改中，修改过多的文件，导致后期修改、维护、撤销等等困难。

请按照以下提交规范提交代码：
* br: 此项特别针对 bug 号，用于向测试反馈 bug 列表的 bug 修改情况
* feat：新功能（feature）
* fix：修补 bug
* docs：文档（documentation）
* style： 格式（不影响代码运行的变动）
* refactor：重构（即不是新增功能，也不是修改 bug 的代码变动）
* test：增加测试
* chore：构建过程或辅助工具的变动
* revert: 撤销之前的 commit

⚠️示例提交规范：

refactor: rename files
feat(#12): add search multi keywords test scenario
