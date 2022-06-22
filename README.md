# Nginx Load balacing ASCII real-time
[TOC]
## Concept Development
- 每次看駭客電影中，將自己轉換成為 code 的樣子感覺這玩意好酷哦！所以我們想嘗試看看：相片的圖像轉換，以及 Real-time 的畫面轉換
    ![](https://i.imgur.com/hpbHEms.jpg)

- 所以我們想弄一個 Real-time 轉換成為 code 的樣子，把該服務假設在 Nginx Web Server 上再由 Nginx 去做一 Load balancing 服務資源
![](https://i.imgur.com/8yVcFpI.png)
- DEMO 環節
[影片連結點我](https://drive.google.com/file/d/1XA2AYVIKD9lGg15OxQYGUp4FH1F4FA9e/view?usp=sharing)


## Implementation Resources
- JavaScript
- HTML
- Nginx

## Existing Library/Software
- 文字圖像轉換（github）
  https://www.youtube.com/watch?v=kaDtdOB-ixY&ab_channel=BabinMeitei
- 圖像轉換（直接 apt install 套件）
  https://www.youtube.com/watch?v=9wFINaz7-I8&ab_channel=SSTecTutorials

## Installation
- 虛擬機要額外安裝一個 Extension Pack 來開啓攝像頭
![](https://i.imgur.com/QCNpZES.png)
- 去打勾啓動攝像頭
![](https://i.imgur.com/IpJrVJZ.png)

- 先更新一下軟件

        sudo apt update
        sudo apt upgrade
    
- 下載 Nginx

        sudo apt-get install nginx
   
- 下載 p5.js 檔案
[點擊這裡](https://p5js.org/download/)
![](https://i.imgur.com/lK0DAYS.png)


## Implementation Process
- 首先在你喜歡的位置開一個資料夾存放網頁資料
    ```
    1. cd /var/www
    2. mkdir lsa
    3. sudo vim ascii_1.html
    ```

    - 貼以下 HTML 的程式碼

    ```
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <link rel="stylesheet" type="text/css"     href="style.css">
        <script     src="p5.js"></script>
        <meta charset="utf-8" />
        <h1>This Is Server 1.</h1>
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
        
    // 開啟一個攝影機、並看到預覽
    function setup() {
      noCanvas();
      video = createCapture(VIDEO);
      video.size(275,110);
      asciiDiv = createDiv();      
    }
    
    
    function draw() {
      video.loadPixels();
      // 要印出的結果
      let asciiImage = '';
      for (let j = 0; j < video.height;j++) {
        for (let i = 0;i < video.width; i++) {
          // pixelIndex = (r,g,b,alpha) alpha：處理透明度(此處不考慮)
          const pixelIndex = (i + j * video.width)     * 4;
          // 抓取單一像素的 RGB 數值，rgb 數字越大越亮。 (0,0,0)->黑；(255,255,255)->白
          const r = video.pixels[pixelIndex + 0];
          const g = video.pixels[pixelIndex + 1];
          const b = video.pixels[pixelIndex + 2];
          // 為了知道該給這格pixel什麼樣的 ascii 符號 (有怎樣的亮度)，固取平均值
          const avg = (r + g + b) / 3;
          const len = density.length;
          // 將該 pixel 的亮度，由 0~255，投到 0 ~ density.length中，來找出該用哪一個 ascii 符號來代表這格pixel
          const charIndex = floor(map(avg,0,255,len,0));
          
          
          // 確保空格能夠正確的被印出來
          const c = density.charAt(charIndex);
          if (c == " ") asciiImage += "&nbsp;";
          else asciiImage += c;
        }
        asciiImage  += '<br/>';
      }
      // 刷新含有儲存 ascii art 的 div
      asciiDiv.html(asciiImage);
    }
        </script>
      </body>
    </html>
    ```
    
    - 複製多一個 HTML 給第二個 web server 用，（記得把裡面的 h1 改成 This Is Web Server 2.）
    ```
    4. sudo cp ascii_1.html ascii_2.html
    5. sudo vim style.css
    ```
    - 貼以下 CSS 的程式碼
    ```
    html, body {
      margin: 0;
      padding: 0;
      background-color: #FFF;
      /* color:#FFF; */
      font-family: 'Courier';
      font-size: 6pt;
      line-height: 4pt;
      color: blue;
    }
    
    canvas {
      display: block;
    }
    ```
    - 從 Download 的檔案裡面把 p5.js 放入 /var/www/lsa
    ```
    6. cd /Downloads
    7. sudo mv p5.js /var/www/lsa
    ```
    - 去 Nginx 架設一個 Load Balancer 和兩個 Web Servers
    ```
    8. cd /etc/nginx/sites-available
    9. sudo vim loadbalancer.conf
    ``` 
    - 貼以下程式碼
    ```
    upstream lsa{
        random;
        server localhost:8081;
        server localhost:8082;
    }
    server{
        listen 8080;
        listen [::]:8080;
        
        location / {
            proxy_pass http://lsa;
        }
    }
    ```
    ```
    10. sudo vim lsa_1.conf
    ``` 
    - 貼以下程式碼
    ```
    server{
        listen 8081;
        listen [::]:8081;
        
        root /var/www/lsa;
        index ascii_1.html
        
        location / {
            try_files $uri $uri/ =404;
        }
    }
    ```
    ```
    11. sudo vim lsa_2.conf
    ``` 
    - 貼以下程式碼
    ```
    server{
        listen 8082;
        listen [::]:8082;
        
        root /var/www/lsa;
        index ascii_2.html
        
        location / {
            try_files $uri $uri/ =404;
        }
    }
    ```
    - 把 loadbalancer.conf 和兩個 Web Server.conf Softlink 到 /etc/nginx/sities-enabled
    ```
    12. sudo ln -s /etc/nginx/sites-available/loadbalancer.conf /etc/nginx/sites-enabled
    13. sudo ln -s /etc/nginx/sites-available/lsa_1.conf /etc/nginx/sites-enabled
    14. sudo ln -s /etc/nginx/sites-available/lsa_2.conf /etc/nginx/sites-enabled
    15. sudo service nginx restart
    ``` 
    - 開啓網頁輸入 127.0.0.1:8080 (loadBalancer) 點擊 Allow
![](https://i.imgur.com/OJ7azCK.png)

    - Ta Da~ 大功告成~
![](https://i.imgur.com/Nf0wA0q.png)

## Usage
- 主要還是用於興趣開發的範疇，沒有什麽特別的商業價值
- 可用於視頻中做一個濾鏡特效

## 碰到的問題
- 因爲 p5.js 的套件它只能在本地端 localhost 下可以使用 getusermedia, 到了其他的私人 ip 下它無法使用即使對 Web Browser 手動開起攝像頭或是權限都無法根治 
    - 問題: "navigator.mediaDevices.getUserMedia is not implemented in this browser"
    - 嘗試寫了一個 navigator.mediaDevices.getUserMedia 的 Web APIs 也沒被辦法啟用

## Job Assignment
- Nginx Web Server & Load Balancer：余嘉舜
- 動態的攝影機畫面轉 Ascii art：蔡清寶
- github 編寫 5/5 平分

## 感謝名單
- 資管三 沈佳龍 同學
## References
- 期末報告的模板 https://github.com/NCNU-OpenSource/final-project-readme-template/tree/master/template
- W3 調色盤 https://www.w3.org/TR/css3-color/#svg-color
- Ascii art 的density參考來源 https://play.ertdfgcvb.xyz/
- ASCII Video - The Coding Train https://www.youtube.com/watch?v=55iwMYv8tGI&ab_channel=TheCodingTrain
