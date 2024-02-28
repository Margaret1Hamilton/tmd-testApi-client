import json
import requests
import consts.env
import conftest

initHeaders = {
    "lang": "en-US",
    "Content-Type": "application/json",
    "platform": "WEB_CLIENT",
}

baseUrl = consts.env.baseHost


def getRequestParamsMap(path, pathParams, data, headers):
    urlTemplate = baseUrl + path
    url = urlTemplate.format(**pathParams)
    resultHeaders = {**headers, **initHeaders}
    resultData = json.dumps(data)
    if conftest.loginUserInfo:
        resultHeaders["token"] = conftest.loginUserInfo["token"]

    resultParamsMap = {"url": url, "headers": resultHeaders, "data": resultData}

    return resultParamsMap


class RequestClient:
    @classmethod
    def get(self, path, pathParams={}, data={}, headers={}, **kwargs):
        requestParamsMap = getRequestParamsMap(
            path=path, pathParams=pathParams, data=data, headers=headers
        )

        response = requests.get(
            url=requestParamsMap["url"],
            headers=requestParamsMap["headers"],
            params=requestParamsMap["data"],
            **kwargs
        )
        return response.json()

    @classmethod
    def post(self, path, pathParams={}, data={}, headers={}, **kwargs):
        requestParamsMap = getRequestParamsMap(
            path=path, pathParams=pathParams, data=data, headers=headers
        )

        print("response", requestParamsMap)

        response = requests.post(
            url=requestParamsMap["url"],
            headers=requestParamsMap["headers"],
            data=requestParamsMap["data"],
            **kwargs
        )
        return response.json()

    @classmethod
    def put(self, path, pathParams={}, data={}, headers={}, **kwargs):
        requestParamsMap = getRequestParamsMap(
            path=path, pathParams=pathParams, data=data, headers=headers
        )
        response = requests.put(
            url=requestParamsMap["url"],
            headers=requestParamsMap["headers"],
            data=requestParamsMap["data"],
            **kwargs
        )
        return response.json()

    @classmethod
    def delete(self, path, pathParams={}, data={}, headers={}, **kwargs):
        requestParamsMap = getRequestParamsMap(
            path=path, pathParams=pathParams, data=data, headers=headers
        )
        response = requests.delete(
            url=requestParamsMap["url"],
            headers=requestParamsMap["headers"],
            data=requestParamsMap["data"],
            **kwargs
        )
        return response.json()

    @classmethod
    def request(self, method, path, pathParams={}, data={}, headers={}, **kwargs):
        requestParamsMap = getRequestParamsMap(
            path=path, pathParams=pathParams, data=data, headers=headers
        )

        if method == "get":
            response = requests.get(
                url=requestParamsMap["url"],
                headers=requestParamsMap["headers"],
                params=requestParamsMap["data"],
                **kwargs
            )
            return response.json()
        if method in ["post", "put", "delete"]:
            response = requests.request(
                method=method,
                url=requestParamsMap["url"],
                headers=requestParamsMap["headers"],
                data=requestParamsMap["data"],
            )

            return response.json()
