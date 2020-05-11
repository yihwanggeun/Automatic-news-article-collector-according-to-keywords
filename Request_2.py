import requests
import json
URL = 'https://openapi.naver.com/v1/datalab/shopping/category/keyword/device'
body =json.dumps({
      "startDate": "2017-08-01",
      "endDate": "2017-09-30",
      "timeUnit": "month",
      "category": "50000000",
      "keyword": "정장",
      "device": "",
      "gender": "",
      "ages": [ ]
    })

headers=({
"X-Naver-Client-Id":"UbTts_4hgkPO2xQb_5nl",
"X-Naver-Client-Secret":"bvmSoaaOAs"
})
print("FINISH")
response = requests.post(URL,headers=headers, data = body)
print(response.content)
