import requests
import json
URL = 'https://openapi.naver.com/v1/datalab/search'
body =json.dumps({
      "startDate": "2017-08-01",
      "endDate": "2017-09-30",
      "timeUnit": "month",
      "keywordGroups": [
        {
            "groupName": "코로나",
            "keywords": [
                "코로나",
                "corona"
            ]
        },
        {
            "groupName": "코로나19",
            "keywords": [
                "코로나19",
                "corona19"
            ]
        }
    ]
      ,
      "device": "pc",
      "gender": "f"
      
    })

headers=({
"X-Naver-Client-Id":"UbTts_4hgkPO2xQb_5nl",
"X-Naver-Client-Secret":"bvmSoaaOAs"
})
print("FINISH")
response = requests.post(URL,headers=headers, data = body)
print(response.json())
###
