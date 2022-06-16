# ACSII_REAL_TIME_OR_PHOTO

## Concept Development
- 每次看駭客電影中，將自己轉換成為 code 的樣子感覺這玩意好酷哦
- 所以我們嘗試 Real-time 轉換和 圖像轉換

## Implementation Resources
- Python
- JS
- Html

## Existing Library/Software
- 文字圖像轉換（github）
  https://www.youtube.com/watch?v=kaDtdOB-ixY&ab_channel=BabinMeitei
- 圖像轉換（直接 apt install 套件）
  https://www.youtube.com/watch?v=9wFINaz7-I8&ab_channel=SSTecTutorials

## Implementation Process

## Knowledge from Lecture

## Installation
### 攝像頭拍攝圖像轉換（漸層彩色）
- 虛擬機要額外安裝一個 Extension Pack 來開啓攝像頭
![](https://i.imgur.com/QCNpZES.png)
- 去打勾啓動攝像頭
![](https://i.imgur.com/IpJrVJZ.png)

打開 Terinal 去安裝一下套件包
  
    pip3 install colour
    pip3 install Pillow
    pip3 install opencv-python


### 動態的攝影機畫面轉Ascii art
    編寫環境: Virtual Studio Code
    使用語言: Html、一些些CSS
    
- 進到vscode裡面，下載p5.vscode的package
    
## Usage
###  攝像頭拍攝圖像轉換（漸層彩色）

- 去複製 photo.py 的程式，（注意裏頭路進設置）
    跑程式去拍攝
![](https://i.imgur.com/vRrIFZ6.png)
- 這是三個顏色是 （紅 "red" , 綠 "green" , 白 "white"） 
    第一個顔色漸層到第二個顔色，而最後一個顔色為背景顔色
![](https://i.imgur.com/EkpOS1t.png)
- 顔色可以根據需求自己調色
    這裏是調你要的漸層色
![](https://i.imgur.com/0ryhHcf.png)
    這裏是 function 呼叫改背景顔色 bgcolor (function 的 默認設定是由黑至藍)
![](https://i.imgur.com/ab23q5C.png)
- 接著就可以在指定好的路徑看見圖片啦，圖片通常會在你執行 local 路徑裏面找到



## Job Assignment
攝像頭拍攝圖像轉換（漸層彩色）余嘉舜
動態的攝影機畫面轉Ascii art 蔡清寶
我們
## References
https://github.com/NCNU-OpenSource/final-project-readme-template/tree/master/template
https://wshanshan.github.io/python/asciiart/
https://www.w3.org/TR/css3-color/#svg-color
