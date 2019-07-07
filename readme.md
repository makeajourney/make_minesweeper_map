# 지뢰찾기

## 개요

게임을 제작한다고 가정. 
각 사각형에 표시될 숫자를 입력하는 코드 작성.  

지뢰찾기의 각 사각형이 나타내는 숫자는 자신을 제외한 주변 8개 사각형에 포함된 폭탄의 갯수를 의미.    
사각형은 가로 10개, 세로 10개.  
지뢰의 갯수는 10개로 가정, 랜덤하게 배치함.  

## 개발환경

Python 3.7.0  

## 실행 방법

Python 3.7.0, pip3 이 설치된 환경에서 실행한다고 가정.  

~~~
git clone https://github.com/makeajourney/make_minesweeper_map.git
pip install -r requirements.txt
python minesweeper.py
~~~