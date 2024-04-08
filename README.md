1. 自动登录
2. 环境变量控制不同环境地址
3. resultClient封装
4. 测试环境执行的注解
5. 测试报告

## 安装依赖
```shell
pip3 install -r requeirments.txt
```

## 环境变量BASE_HOST
```shell
## 指定运行的apiHost默认: http://192.168.0.129:31000
export BASE_HOST=''
```
## 运行
```shell
pytest -s --env=pro
# --env=pro指定环境，可选，如果不写默认是--env=test
```

## 注解说明
1. 指定运行环境所有说明
```py
@pytest.mark.runALL
```

## 代码生成地址
http://192.168.0.14:7070

## 测试报告
```shell
pytest -s  --alluredir=./allure-report
```
```
allure serve  ./allure-report
```

## 用例数据格式说明
```ts
type casesItem = {
  /** 用例标题 */
  title: string,
  /** 是否在生产环境运行 */
  runPro?: "true" | "false",
  /** 路径参数 activity/changeActivity/{id} 传入{id: 1}输出activity/changeActivity/1*/
  pathParams?: Dictionary,
  /** 接口参数 */
  data?: Dictionary,
  /** 期望的结果 */
  expected: {
      header: Dictionary
      body?: Dictionary
  }
},

type DataCases = {
  /** 用例分类 */
  feature: string,
  /** 用例函数名称 */
  funcNameSpace: string,
  /** 重要等级 */
  funcNameSpace: 'BLOCKER' | 'CRITICAL' | 'NORMAL' | 'MINOR' | 'TRIVIAL',
  /** 用例数据相对路径 */
  casePath: string,
  /** 接口路径 */
  path: string
  /** 详细用例数据 */
  casesList: casesItem[]
}

```
