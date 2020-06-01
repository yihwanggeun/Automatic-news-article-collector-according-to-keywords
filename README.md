# Automatic news article collector according to keywords<br>(희망 키워드 별 자동 뉴스 기사 수집기)

# Development

**Developer : HwangGeun Yi, a sophomore in the Department of Software at Sungkyunkwan University**<br>
**Contributor : SoYoung Park**

# Description
관심있는 기사가 있고 그리고 자신이 검색해보고 싶은 기사가 있을 경우 네이버, 구글 같은 웹 사이트에 들어가서 검색하는 것에 대한 불편함을 줄이기 위해 이 프로젝트를 진행하게 되었다.
자신이 관심 있어하는 키워드를 입력하면 자동으로 네이버 API를 이용하여 기사를 수집하여 웹서버에 보여주는 기능을 함으로써 불편함을 한 단계 줄일 수 있다.


## Setup
자동 뉴스 수집기의 설치를 매우 간단하게 진행된다. 우선 New_Collector라는 이름의 폴더를 컴퓨터에 저장을 한 후 `terminal` 에서 `News_Collector` 
폴더로 이동한 후 `pip freeze requirements.txt` 또는 `pip3 freeze requirements.txt`를 이용하여 필요한 `module`을 구비한다.
그 이후 `app.py`를 시작하게 되면 웹 서버가 시작되게 될 것이고 이후 `terminal`에 나와있는 웹 서버의 주소로 접속하면 된다.

## Commands
`termianl` 창에서 `app.py`에서 실행된 웹 서버에 접속하게 되면 `원하는 뉴스명` 그리고 `원하는 수량`을 입력한 후 `검색` 버튼을 누르게 되면 기사의 제목, 기사의 링크, 기사의 내용 등
여러가지 정보가 나오게 된다.<br>
![image](https://user-images.githubusercontent.com/63749140/83417222-c22e9280-a45c-11ea-9f9f-97a94c43fcd0.png)<br>
그리고 기사의 기간까지 정하고 싶다면 초기 웹 서버의 주소에서 `/query`를 추가후 접속하면 된다. ex) `localhost:5000/query` <br>
접속한 이후에는 원하는 기사의 제목 뿐만 아니라 기사의 기간도 지정하여 검색할 수 있다. 단, 기사의 기간을 입력할 때는 `Year.Month.Day`의 형식을 맞춰야된다. ex)2020.01.20<br>
![image](https://user-images.githubusercontent.com/63749140/83417383-f609b800-a45c-11ea-8e0f-761ba8d3c7d5.png)



