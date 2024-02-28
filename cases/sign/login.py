dataCases = {
    "feature": "交易端登录接口",
    "funcNameSpace": "TestLogin",
    "severityLevel": "BLOCKER",
    "casePath": "cases.sign.login",
    "path": "/api/h5/user/check/account",
    "method": "post",
    "casesList": [
        {
            "title": "登录账号格式错误",
            "runPro": "true",
            "data": {"account": "lena.liu@", "password": "abc123"},
            "expected": {
                "header": {
                    "code": "1200",
                            "messageDetails": {"account": "Account incorrect"}
                }
            }
        },
        {
            "title": "登录账号不存在",
            "data": {"account": "lena01@spotec.net", "password": "abc123"},
            "expected": {
                "header": {
                    "code": "1200",
                    "messageDetails": {
                        "account": "Username incorrect, please check and try again."
                    }
                }
            }
        },
        {
            "title": "黑名单账号",
            "data": {"account": "lena-038@1.com", "password": "abc123"},
            "expected": {"header": {"code": "1000", "message": "Unknown error R"}}
        },
        {
            "title": "登录账号为空",
            "data": {"account": "", "password": "abc123"},
            "expected": {"header": {"code": "9999", "message": "Service in error"}}
        },
        {
            "title": "登录密码不正确",
            "data": {"account": "lena.liu@spotec.net", "password": "abc1234"},
            "expected": {
                "header": {
                    "code": "1200",
                    "messageDetails": {
                        "password": "Login failed, please check username or password."
                    }
                }
            }
        },
        {
            "title": "登录密码为空",
            "data": {"account": "lena.liu@spotec.net", "password": ""},
            "expected": {
                "header": {
                    "code": "1200",
                    "messageDetails": {
                        "password": "Login failed, please check username or password."
                    }
                }
            }
        }
    ]
}
