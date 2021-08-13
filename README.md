# 철권 대회 조추첨 프로그램







## 개요





철권7 대회에서 조추첨을 수기로 하시는 분들이 계시다고 해서 만든 프로그램입니다.







엑셀 데이터를 기반으로 조추첨을 한 뒤, 결과를 다른 엑셀 파일로 출력합니다.







양식에 맞는 엑셀데이터와 프로그램만 있다면,





인원수가 어떻든, 한 조에 몇명을 넣으실것인지 프로그램에 명시해주신다면





5초도 안되어 조추첨 결과가 엑셀 데이터로 출력됩니다.





참가자 수가 k명으로 딱 떨어지지 않을 떄도 동작합니다.



---



> 원래는 exe파일로 배포하려고 했으나, 윈도우 10 특성상 개인사업자등록증으로 ***전자서명***이라는 것을 하지 않으면.. 배포가 불가능합니다.
>
> 따라서 아래 ***설치 설명서***에 따라서 코드를 사용자 컴퓨터에서 직접 빌드하시면 됩니다.









## 사용 설명서





아래 사진처럼 **인덱스, 플레이어 이름, 스팀 닉네임, 계급 항목**이 필수적으로 들어가야합니다.







계급 상관없이 완전 **무작위**로 돌리고 싶으시면 모든 계급을 1th로 작성하신 뒤, 프로그램을 돌리시면 됩니다.

계급을 영어로 적는게 귀찮으시다면, 숫자로 적으셔도 상관없습니다.
***대신, 프로그램 실행 후에 계급을 숫자로 적었냐, 숫자로 적지 않았냐를 물어볼텐데, 그 때 적절하게 메뉴에 적혀있는 숫자대로 입력해주시면 됩니다.***







계급에 따라 적절하게 인원을 분배하시고 싶으시면, 모든 계급을 아래 이미지에 있는 정식 계급 명칭대로 엑셀을 작성해주신 뒤에 프로그램을 실행시키면 됩니다.







![](https://i.imgur.com/GCXa0cY.png)







프로그램 구동 :





![](https://i.imgur.com/YZdPkkd.jpeg)







프로그램을 돌린 결과 :





![](https://i.imgur.com/NcBK1x1.jpeg)







## 설치 설명서



https://github.com/daumtto53/tekken7_contest_draw 에서 

![사용설명서1](https://github.com/chemicat53/blogging_image/blob/main/img/사용설명서1.jpg?raw=true)





위 사진처럼 **code**를 누르시고, download zip을 해주시면 폴더를 다운할 수 있습니다.



![사용설명서 2](https://github.com/chemicat53/blogging_image/blob/main/img/사용설명서 2.jpg?raw=true)





다운 후에 1_INSTALL 파일을 실행하시면 

알아서 프로그램을 실행시키기 위한 언어와 패키지가 설치됩니다.

> 언어는 python3으로 제작했고, 패키지는 pandas, openxl, numpy 등...으로 제작했습니다.
> 유명한 언어고 전세계인들이 사용하는 언어입니다. :)
>
> 따라서, python3가 없으시다면, pyhon3를 설치하는 과정이 필요해서 그 과정은 스크립트로 만들었습니다.
> 즉, 언어를 설치하는 과정이 있습니다.



![사용설명서 3](https://github.com/chemicat53/blogging_image/blob/main/img/사용설명서 3.jpg?raw=true)

![사용설명서 4](https://github.com/chemicat53/blogging_image/blob/main/img/사용설명서 4.jpg?raw=true)

초기 실행시 이런화면이 뜨신다면 성공하신거고요



최종적으로는 아래와 같은 화면이 뜨신다면 설치에 성공하신겁니다. 



![](https://github.com/chemicat53/blogging_image/blob/main/img/사용설명서 5.jpg?raw=true)







