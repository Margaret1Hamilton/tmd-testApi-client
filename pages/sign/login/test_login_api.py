import allure
import pytest
from utils.restClient import RequestClient
from cases.sign.login import dataCases

@allure.severity(getattr(allure.severity_level, dataCases['severityLevel']))
@allure.feature(dataCases['feature'])
class TestLoginPageAPI:

    @pytest.mark.runALL
    @allure.story("登录账号格式错误")
    def testTestLoginCase1(self):
        res = RequestClient.request(
            method=dataCases['method'],
            path=dataCases['path'],
            data=dataCases["casesList"][0]['data'],
        )
        exceptHeaderResult = dataCases['casesList'][0]['expected']['header']
        resData = res["header"]
        del resData["traceId"]

        assert resData == exceptHeaderResult

    @allure.story("登录账号不存在")
    def testTestLoginCase2(self):
        res = RequestClient.request(
            method=dataCases['method'],
            path=dataCases['path'],
            data=dataCases["casesList"][1]['data'],
        )
        exceptHeaderResult = dataCases['casesList'][1]['expected']['header']
        resData = res["header"]
        del resData["traceId"]

        assert resData == exceptHeaderResult

    @allure.story("黑名单账号")
    def testTestLoginCase3(self):
        res = RequestClient.request(
            method=dataCases['method'],
            path=dataCases['path'],
            data=dataCases["casesList"][2]['data'],
        )
        exceptHeaderResult = dataCases['casesList'][2]['expected']['header']
        resData = res["header"]
        del resData["traceId"]

        assert resData == exceptHeaderResult

    @allure.story("登录账号为空")
    def testTestLoginCase4(self):
        res = RequestClient.request(
            method=dataCases['method'],
            path=dataCases['path'],
            data=dataCases["casesList"][3]['data'],
        )
        exceptHeaderResult = dataCases['casesList'][3]['expected']['header']
        resData = res["header"]
        del resData["traceId"]

        assert resData == exceptHeaderResult

    @allure.story("登录密码不正确")
    def testTestLoginCase5(self):
        res = RequestClient.request(
            method=dataCases['method'],
            path=dataCases['path'],
            data=dataCases["casesList"][4]['data'],
        )
        exceptHeaderResult = dataCases['casesList'][4]['expected']['header']
        resData = res["header"]
        del resData["traceId"]

        assert resData == exceptHeaderResult

    @allure.story("登录密码为空")
    def testTestLoginCase6(self):
        res = RequestClient.request(
            method=dataCases['method'],
            path=dataCases['path'],
            data=dataCases["casesList"][5]['data'],
        )
        exceptHeaderResult = dataCases['casesList'][5]['expected']['header']
        resData = res["header"]
        del resData["traceId"]

        assert resData == exceptHeaderResult

