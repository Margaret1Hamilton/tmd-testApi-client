# import allure
# import pytest
# import pydash
# from utils.restClient import RequestClient
# from cases.sign.login import dataCases
#
# @allure.severity(getattr(allure.severity_level, dataCases['severityLevel']))
# @allure.feature(dataCases['feature'])
# class TestLoginPageAPI:
#
#     @pytest.mark.runALL
#     @allure.story("登录账号格式错误")
#     def testTestLoginCase1(self):
#         res = RequestClient.request(
#             method=dataCases['method'],
#             path=dataCases['path'],
#             data=dataCases["casesList"][0]['data'],
#         )
#
#         if 'header' in dataCases['casesList'][0]['expected']:
#             exceptHeaderResult = dataCases['casesList'][0]['expected']['header']
#             resHeaderData = res["header"]
#             del resHeaderData["traceId"]
#             assert resHeaderData == exceptHeaderResult
#
#         if 'body' in dataCases['casesList'][0]['expected']:
#             exceptBodyResult = dataCases['casesList'][0]['expected']['body']
#             restBoyData = pydash.pick(res["body"], pydash.keys(exceptBodyResult) )
#             assert exceptBodyResult == restBoyData
#
#     @allure.story("登录账号不存在")
#     def testTestLoginCase2(self):
#         res = RequestClient.request(
#             method=dataCases['method'],
#             path=dataCases['path'],
#             data=dataCases["casesList"][1]['data'],
#         )
#
#         if 'header' in dataCases['casesList'][1]['expected']:
#             exceptHeaderResult = dataCases['casesList'][1]['expected']['header']
#             resHeaderData = res["header"]
#             del resHeaderData["traceId"]
#             assert resHeaderData == exceptHeaderResult
#
#         if 'body' in dataCases['casesList'][1]['expected']:
#             exceptBodyResult = dataCases['casesList'][1]['expected']['body']
#             restBoyData = pydash.pick(res["body"], pydash.keys(exceptBodyResult) )
#             assert exceptBodyResult == restBoyData
#
#     @allure.story("黑名单账号")
#     def testTestLoginCase3(self):
#         res = RequestClient.request(
#             method=dataCases['method'],
#             path=dataCases['path'],
#             data=dataCases["casesList"][2]['data'],
#         )
#
#         if 'header' in dataCases['casesList'][2]['expected']:
#             exceptHeaderResult = dataCases['casesList'][2]['expected']['header']
#             resHeaderData = res["header"]
#             del resHeaderData["traceId"]
#             assert resHeaderData == exceptHeaderResult
#
#         if 'body' in dataCases['casesList'][2]['expected']:
#             exceptBodyResult = dataCases['casesList'][2]['expected']['body']
#             restBoyData = pydash.pick(res["body"], pydash.keys(exceptBodyResult) )
#             assert exceptBodyResult == restBoyData
#
#     @allure.story("登录账号为空")
#     def testTestLoginCase4(self):
#         res = RequestClient.request(
#             method=dataCases['method'],
#             path=dataCases['path'],
#             data=dataCases["casesList"][3]['data'],
#         )
#
#         if 'header' in dataCases['casesList'][3]['expected']:
#             exceptHeaderResult = dataCases['casesList'][3]['expected']['header']
#             resHeaderData = res["header"]
#             del resHeaderData["traceId"]
#             assert resHeaderData == exceptHeaderResult
#
#         if 'body' in dataCases['casesList'][3]['expected']:
#             exceptBodyResult = dataCases['casesList'][3]['expected']['body']
#             restBoyData = pydash.pick(res["body"], pydash.keys(exceptBodyResult) )
#             assert exceptBodyResult == restBoyData
#
#     @allure.story("登录密码不正确")
#     def testTestLoginCase5(self):
#         res = RequestClient.request(
#             method=dataCases['method'],
#             path=dataCases['path'],
#             data=dataCases["casesList"][4]['data'],
#         )
#
#         if 'header' in dataCases['casesList'][4]['expected']:
#             exceptHeaderResult = dataCases['casesList'][4]['expected']['header']
#             resHeaderData = res["header"]
#             del resHeaderData["traceId"]
#             assert resHeaderData == exceptHeaderResult
#
#         if 'body' in dataCases['casesList'][4]['expected']:
#             exceptBodyResult = dataCases['casesList'][4]['expected']['body']
#             restBoyData = pydash.pick(res["body"], pydash.keys(exceptBodyResult) )
#             assert exceptBodyResult == restBoyData
#
#     @allure.story("登录密码为空")
#     def testTestLoginCase6(self):
#         res = RequestClient.request(
#             method=dataCases['method'],
#             path=dataCases['path'],
#             data=dataCases["casesList"][5]['data'],
#         )
#
#         if 'header' in dataCases['casesList'][5]['expected']:
#             exceptHeaderResult = dataCases['casesList'][5]['expected']['header']
#             resHeaderData = res["header"]
#             del resHeaderData["traceId"]
#             assert resHeaderData == exceptHeaderResult
#
#         if 'body' in dataCases['casesList'][5]['expected']:
#             exceptBodyResult = dataCases['casesList'][5]['expected']['body']
#             restBoyData = pydash.pick(res["body"], pydash.keys(exceptBodyResult) )
#             assert exceptBodyResult == restBoyData
#
