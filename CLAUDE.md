# SUS304 資料庫（不鏽鋼焊道酸洗膏）

每次開啟 Code 自動讀取。本檔只放「規則」與「目前狀態」；進度用 git commit 記錄。
詳細交接內容見 `交接_焊道酸洗膏.md`。

## 一、工作規則
- 每次回覆開頭先寫「郭阿貴，」再接內容；回應一律繁體中文。
- 指令不清楚先列選項；有更簡單做法先提出；大量重複工作先做樣品。
- 問問題一次只給 2 題（手機看），每題：問題一句、選項、建議。
- 使用者說「先暫停」：更新交接檔＋commit＋push 後停止。
- 每完成一項就 commit＋push；成果同步一份到 Google Drive「SUS304 資料庫」資料夾。
- **測試照片（2026-11-27 船主）**：船主傳來的白鐵片／配方測試照片，一律：①壓縮到 ≤3 MB（長邊 1600 px）存 `photos/日期_配方_內容.jpg`；②上傳 Drive「SUS304 資料庫」資料夾（不轉 Google 文件）；③在 Drive「E4 系列配方」總表最下方「測試照片」區加一列快速連結（=HYPERLINK，欄位：照片名稱／日期／說明）；④記進 `data/試驗紀錄.csv` 與交接檔。
- **只照實際記錄**：設計目標值不可寫成實測值；船主給的數字照原樣記，不自行改。

## 二、Repo 結構
```
交接_焊道酸洗膏.md        交接檔（目前狀態、配方摘要、待辦）
docs/問答紀錄_2026-11-21.md  原始問答紀錄全文（Drive Doc 匯出）
data/配方.csv              A～D 配方（B 氟化鎂已拿掉）（每 100 kg／1 kg 小批）
data/配方_甲基磺酸.csv      加甲基磺酸版本
data/現行配方.csv、修正配方.csv  現行配方、E2–E5 修正配方（不用氟化鈉、氟化鎂粉）
data/E4系列配方.csv  主配方 E4／E4-2（500／2000 mL 換算、黏度記錄）
data/試驗紀錄.csv           小批試驗結果（試完填這裡）
tools/配方計算.py           完全反應理論值計算
photos/                    試驗照片
```

## 三、Google Drive
- 配方比對總表「E4 系列配方」（含黏度紀錄、測試照片連結）：1RKPuKw5i3fCia0pWYvHuP3meXNL6gAJH9KaIAJyfwOM
- 資料夾「SUS304 資料庫」：1jPRDF3X6tDC2FUGQZ57i0vs8xSs_VKd-
- 問答紀錄 Doc：1lDl_jH17LwyZXXenEnTksNLaBtkQIwKP78p94usJErQ
- 配方試算表：1aq7-kwos2pnzhrFsrbtWccgZmXdPiuuafRxU_dqHhWI
