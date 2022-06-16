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

## Installation
### 虛擬機的前置設定
- 虛擬機要額外安裝一個 Extension Pack 來開啓攝像頭
![](https://i.imgur.com/QCNpZES.png)
- 去打勾啓動攝像頭
![](https://i.imgur.com/IpJrVJZ.png)

### （1）攝像頭拍攝圖像轉換（漸層彩色）
打開 Terinal 去安裝一下套件包
  
    pip3 install colour
    pip3 install pillow
    pip3 install numpy
    pip3 install opencv-python


### （2）動態的攝影機畫面轉 Ascii art
    編寫環境: Virtual Studio Code
    使用語言: Html、一些些CSS
    
- 進到 vscode 裡面，下載這些延伸模組：
    - p5.vscode
    ![](https://i.imgur.com/w3qVJk8.png)
    - HTML CSS Support
    ![](https://i.imgur.com/w1RsWs9.png)
    - Open In Default Browser
    ![](https://i.imgur.com/LghUhA0.png)
## Usage
###  攝像頭拍攝圖像轉換（漸層彩色）
-  photo.py 的程式，（注意裏頭路進設置）
    執行程式
![](https://i.imgur.com/vRrIFZ6.png)
- 這是三個顏色是 （紅 "red" , 綠 "green" , 白 "white"） 
    第一個顔色漸層到第二個顔色，而最後一個顔色為背景顔色
![](https://i.imgur.com/EkpOS1t.png)
- 顔色可以根據需求自己調色
    這裏是調你要的漸層色
![](https://i.imgur.com/FtewDVW.png)
    這裏是 function 呼叫改背景顔色 bgcolor (function 的 默認設定是由黑至藍)
![](https://i.imgur.com/qk8iwsV.png)
- 接著就可以在指定好的路徑看見圖片啦，圖片通常會在你執行 local 路徑裏面找到
- 主程式 main 
   - VideoCaupture 開其攝像頭
   - set (WIDTH) 設定視窗寬度
   - set (HEIGHT) 設定視窗高度
   - imshow 輸出視窗
   - imwrite 產生圖片
![](https://i.imgur.com/mJeLSUl.png)
- 副程式 function 
    - resize 圖片（3寬：4高），計算有多少個 pixel
    - 去計算現需要多少個 ASCII letters
        - widthByLetter = round(img.size[0] * pixel_sampling * WCF) 
        - heightByLetter = round(img.size[1] * pixel_sampling)
    - 把獲取到的每一個 index RGB 用 John D. Cook 的顏色轉換為灰度的平均演算法，然後吧值標準化
![](https://i.imgur.com/HVKb26a.png)
    - 這個由白色（亮）至黑色（暗）說選擇的符號
![](https://i.imgur.com/AdZpAad.png)
    - 根據標準化後的灰度平均演算法去對應光暗的表去做鋪色
    - 用回原來的大小產生一張新的圖片
![](https://i.imgur.com/GSOhc0V.png)
### 動態的攝影機畫面轉 Ascii art
- 流程
  - 首先在你喜歡的位置開一個資料夾
    ``` 
    mkdir Ascii
    ```
  - 到 vscode 把剛剛新建的資料夾拉入工作區
    ![](https://i.imgur.com/IC5WktK.png)
  - 在剛拉過來的工作區中按下 Ctrl + Shift + P ，並選擇 Create p5.js Project，並選擇當前的資料夾。
    ![](https://i.imgur.com/agBm1DA.png)
    ![](https://i.imgur.com/w47HfvY.png)
  - 回到 vscode，選取 index.html 貼入以下程式碼
    ```
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <link rel="stylesheet" type="text/css"     href="style.css">
        <script     src="https://cdnjs.cloudflare.com/ajax/libs/p5    .js/1.4.0/p5.js"></script>
        <script     src="https://cdnjs.cloudflare.com/ajax/libs/p5    .js/1.4.0/addons/p5.sound.min.js"></script>
        <meta charset="utf-8" />
      </head>
      <body>
        
        <main>
        </main>
        <script>
          //const density = '           .:░▒▓█'
          //const density = '█▓▒░:.         '
          //const density = '            .:-    i|=+%O#@'
          //const density = '@#O%+=|i-:.                '
          const density = '                                                       _.,-=+:;cba!?0123456789$W#@Ñ'
          //const density = 'Ñ@#W$9876543210?!abc;:+=-,._                                                       '
          //const density = ' .,:irs?@9B&#'
        let video;
        let asciiDiv;
    
    function setup() {
      noCanvas();
      video = createCapture(VIDEO);
      video.size(275,110);
      // 320,120
      // (275,96)
      // 250,48
      asciiDiv = createDiv();      
    }
    
    
    function draw() {
      video.loadPixels();
      let asciiImage = '';
      for (let j = 0; j < video.height;j++) {
        for (let i = 0;i < video.width; i++) {
          const pixelIndex = (i + j * video.width)     * 4;
          const r = video.pixels[pixelIndex + 0];
          const g = video.pixels[pixelIndex + 1];
          const b = video.pixels[pixelIndex + 2];
          const avg = (r + g + b) / 3;
          const len = density.length;
          const charIndex =     floor(map(avg,0,255,len,0));
          //const charIndex =     floor(map(avg,0,255,0,len));
          
          const c = density.charAt(charIndex);
          if (c == " ") asciiImage += "&nbsp;";
          else asciiImage += c;
        }
        asciiImage  += '<br/>';
      }
      asciiDiv.html(asciiImage);
    }
        </script>
      </body>
    </html>
    ```
  - 存檔後，在 vscode 裡右鍵，選擇 "Open from Default Browser" 
    ![](https://i.imgur.com/N2v2imd.png =60%x)
  - 到網頁裡，選擇 "允許使用相機"（用 VM 的話要照著前面步驟，先開啟攝影機） 
    ![](https://i.imgur.com/VMGr3RV.png =60%x)
  - Ta－Da～


 
     
    
## Job Assignment
- 攝像頭拍攝圖像轉換（漸層彩色）余嘉舜
- 動態的攝影機畫面轉Ascii art 蔡清寶
- github 編寫 5/5 平分
## References
- 期末報告的模板 https://github.com/NCNU-OpenSource/final-project-readme-template/tree/master/template
- 攝像頭拍攝圖像轉換（漸層彩色）https://wshanshan.github.io/python/asciiart/
- Three algorithms for converting color to grayscale https://www.johndcook.com/blog/2009/08/24/algorithms-convert-color-grayscale/
- W3 調色盤 https://www.w3.org/TR/css3-color/#svg-color
- Ascii art 的density參考來源 https://play.ertdfgcvb.xyz/
