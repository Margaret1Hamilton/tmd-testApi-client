import json
import requests
import consts.env

initHeaders = {
    "lang": "en-US",
    "Content-Type": "application/json",
    "platform": "WEB_CLIENT",
}


def get_request_params_map(path, pathParams, data, headers):
    baseUrl = consts.env.baseHost
    urlTemplate = baseUrl + path
    url = urlTemplate.format(**pathParams)
    resultHeaders = {**headers, **initHeaders}
    resultData = json.dumps(data)
    resultParamsMap = {"url": url, "headers": resultHeaders, "data": resultData}

    return resultParamsMap


class RequestClient:
    def __init__(self, token):
        self.session = requests.Session()
        self.session.headers.update({'token': token})

    def request(self, method, path, pathParams={}, data={}, headers={}, **kwargs):
        requestParamsMap = get_request_params_map(
            path=path, pathParams=pathParams, data=data, headers=headers
        )

        if method.lower() == "get":
            response = self.session.get(
                url=requestParamsMap["url"],
                headers=requestParamsMap["headers"],
                params=requestParamsMap["data"],
                **kwargs
            )
            return response.json()
        if method.lower() in ["post", "put", "delete"]:
            response = self.session.request(
                method=method,
                url=requestParamsMap["url"],
                headers=requestParamsMap["headers"],
                data=requestParamsMap["data"],
            )

            return response.json()


def login(account, password):
    baseHost = consts.env.baseHost
    url = baseHost + '/api/h5/user/check/account'
    headers = {
        'platform': 'WEB_CLIENT',
        'Content-Type': 'application/json',
        'lang': 'zh-CN'
    }
    data = {"account": account, "password": password}

    accountInfo = requests.post(url=url, headers=headers, data=json.dumps(data)).json()

    token = accountInfo['body']['appLoginVO']['token']
    return {'rest_client_func': RequestClient(token=token), 'accountInfo': accountInfo}
