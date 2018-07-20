# SimpleMenuRestApi

Server Url ec2-13-125-219-166.ap-northeast-2.compute.amazonaws.com:8080/

How Use?

ec2-13-125-219-166.ap-northeast-2.compute.amazonaws.com:8080/api/store?key_number=1
이런식으로 정보를 요청 할 수 있습니다.

Mac 접속방법 
ssh -i thonz.pem ubuntu@ec2-13-125-219-166.ap-northeast-2.compute.amazonaws.com
(thonz.pem 인증 키의 경로를 입력하면 되고, 사용자 이름 ubuntu 그 다음 서버 주소를 입력하면 된다.)

Server File Address

/srv 에 관련 파일 전부 있습니다.

(서버 구동 방법)

/srv/ec2_depoly/bin/source 를 activate source 이런식으로 활성화 시킵니다. Python 가상환경을 실행 시켜가지고, Django 파일을 돌릴 수 있게 합니다.

그 다음 srv 의 파일 폴더로 들어가서 nohub python manage.py runserver 0:8080 식으로 서버를 구동하면 됩니다. 
현재 서버가 돌아가는 중이라, 끄고 실행시키고 싶다면 lsof -i 로 실행중인 파일을 찾아 kill -9 (portNumber) 로 종료 시킨 후 구동 시키면 됩니다.

파일에 정보를 보내는 방법은 python_code 에 Request 로 파일을 보내고, GetRequest로 잘 보내졌는지 확인 할 수 있습니다.

localhost 에서 테스트 해보는걸 권장하고, localhost 에서는 그냥 python manage.py runserver 로 구동해면 127.0.0.1:8000 주소에서 실행되는걸 확인
할 수 있습니다.
