**# 철권 대회 조추첨 프로그램**





git

**## 개요**



철권7 대회에서 조추첨을 수기로 하시는 분들이 계시다고 해서 만든 프로그램입니다.





엑셀 데이터를 기반으로 조추첨을 한 뒤, 결과를 다른 엑셀 파일로 출력합니다.





양식에 맞는 엑셀데이터와 프로그램만 있다면,



인원수가 어떻든, 한 조에 몇명을 넣으실것인지 프로그램에 명시해주신다면



5초도 안되어 조추첨 결과가 엑셀 데이터로 출력됩니다.



**참가자 수가 k명으로 딱 떨어지지 않을 떄도 동작합니다.**





**## 사용 설명서**



아래 사진처럼 ***\*인덱스, 플레이어 이름, 스팀 닉네임, 계급 항목\****이 필수적으로 들어가야합니다.





계급 상관없이 완전 무작위로 돌리고 싶으시면 모든 계급을 1th로 작성하신 뒤, 프로그램을 돌리시면 됩니다.



계급에 따라 적절하게 인원을 분배하시고 싶으시면, 모든 계급을 아래 이미지에 있는 정식 계급 명칭대로 엑셀을 작성해주신 뒤에 프로그램을 실행시키면 됩니다.





![](https://i.imgur.com/GCXa0cY.png)





프로그램 구동 :



![](https://i.imgur.com/YZdPkkd.jpeg)





프로그램을 돌린 결과 :



![](https://i.imgur.com/NcBK1x1.jpeg)











**## 설치 설명서**



https://github.com/daumtto53/tekken7_contest_draw



1. 위 링크에서 download_zip을 하신 뒤에

2. https://somjang.tistory.com/entry/Windows-Windows%EC%97%90-Python-373-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0 링크에 있는대로 파이썬을 까시

3. cmd창 여셔서 아래 명령어 그대로 입력하시고

   ```shell
   pip3 install pandas ;
   pip3 install xlrd ;
   pip3 install openpyxl ;
   ```

4. 다운로드 받으신 zip위치에서

   ```shell
   python tekken.py ;
   ```



입력해주시면 사용 가능합니다 ㅎㅎ...

