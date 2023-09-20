import hashlib
import json
import requests
import time

# 你的请求参数
request = {
    "timestamp": "",
    "format": "json",
    "version": "1.0.0",
    "appName": "fzrivercity",
    "source": "fzrivercity",
    "param": {
        "storeId": 6507,
        "licensePlateNbr": "闽A388QU",
        "isCustomerAcceptPolicy": 1
    },
    "sign": ""
}

# 你的appSecret
appSecret = "C0A5472FB3246B9455CA55563416BD28"

# 生成时间戳
timestamp = str(int(time.time() * 1000))
request["timestamp"] = timestamp

# 按照规则拼接字符串
stringA = appSecret + request["appName"] + request["source"] + request["timestamp"] + request["format"] + request["version"]
stringB = json.dumps(request["param"], sort_keys=True, separators=(',', ':'), ensure_ascii=False)
stringC = stringA + stringB + appSecret

# 使用SHA512算法生成签名
hashed_string = hashlib.sha512(stringC.encode()).hexdigest().upper()
request["sign"] = hashed_string

# 输出签名、时间戳和请求的JSON格式文件
print("Signature:", request["sign"])
print("Timestamp:", timestamp)
print("Request JSON:")
print(json.dumps(request, indent=4))

# 发送POST请求
# 验证能否享受优惠
url = "https://aloha.walmartmobile.cn/members-parking-service/plate/number/free/parking"
# 验证是否为会员
#url = "https://aloha.walmartmobile.cn/members-parking-service/plate/number/binding/member"
headers = {"Content-Type": "application/json"}
response = requests.post(url, json=request, headers=headers)

# 输出响应结果
print("Response:")
print(json.dumps(response.json(), indent=4, ensure_ascii=False))