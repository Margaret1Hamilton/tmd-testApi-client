
class AssertUtils():
  @classmethod
  def checkReqSuccess(self, res):
    assert res['header']['code'] == '0000'
  def checkSectionException(res, exceptResult):
    resData = {
      'code': res['header']['code'],
      'messageDetails': res['header']['messageDetails']
    }
    assert resData == exceptResult

  def checkGlobalException(res, exceptResult):
    resData = {
      'code': res['header']['code'],
      'message': res['header']['message']
    }
    assert resData == exceptResult
