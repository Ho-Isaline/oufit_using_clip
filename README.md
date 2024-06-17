### 專案目標:
結合語音輸入輸出爬取網路衣服型式資料，為視障者做篩選及推薦。
### 專案簡介:
1. 網路爬蟲衣服資訊 -> (如hm&prada)
  -  名稱
  -  顏色
  -  材質
  -  簡介
  -  圖樣
  -  圖片
2. 將圖片利用clipp轉成向量做儲存
3. 利用chat create將衣服資訊做為prompt生成人性化的語音推薦
4. openai texttovoice 將擬人化後的推薦輸出
5. google recognizer 將使用者輸入語音轉成文字
