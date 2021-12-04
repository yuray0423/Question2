# Question2
## 以 cloud run 將一個Flask Server建置起來，當以GET方法訪問/user路徑時，會得到一個json object ，裡面有name欄位、age欄位及其內容值，程式碼要放到github上

### 不確定老師的意思是不是這樣，我陳述一下我的步驟:
#### 首先建立一個 main.py 裡面放flask 的基本程式碼，將想要讓用戶訪問的網址用@路徑標示，使用render_template轉換到已經先建好的html
#### templates 裡面的 index.html 放有基本格式的html 以及script 建立 json 物件，打印在console上(console.log)
#### 另外網上抄人家的Docker檔案， 用cloud run封包程式 => https://challenge-yz3lf44tfq-uc.a.run.app/
#### 進去網址後看到Hello 在網址添加"/user" 
#### 再按F12(開發人員工具) 點擊Console ，就可以看到建好的json物件
![image](https://user-images.githubusercontent.com/95526451/144706564-e6234ec1-6df8-441c-8f21-7084fb23bdcf.png)
