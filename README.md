# 筆畫字級閱讀原型

依每個中文字的筆畫數自動調整字級：筆畫少的字小一級、筆畫多的字大一級、其餘使用標準字級，把原本統一字級的文章改成大、中、小三種字級呈現，以提升文字辨識性與閱讀舒適性。

這是商業 App 開發前的網頁原型，用來確認分級規則與閱讀效果。

## 使用方式

直接用瀏覽器打開 `index.html`，不需要安裝任何東西。

- 在左側貼上文章，右側即時預覽
- 調整小字、大字的筆畫界線（預設 ≤6 畫為小字、≥15 畫為大字）
- 調整標準字級、一個字級的差距、行高
- 切換明體／黑體、橫排／直排、基線／置中對齊
- 與統一字級的原文對照，或用顏色標示小字和大字
- 滑鼠停在字上可看到筆畫數

## 專案結構

```
index.html          建置完成的單一頁面（已內嵌筆畫資料）
src/template.html   頁面原始碼，筆畫資料以 __STROKES__ 佔位
scripts/build.py    產生筆畫資料並輸出 index.html
```

## 重新建置

修改 `src/template.html` 後，重新產生 `index.html`：

```bash
npm pack @mandel59/mojidata
tar xzf mandel59-mojidata-*.tgz
python3 scripts/build.py package/dist/moji.db
```

## 筆畫資料

- 來源：Unicode Unihan 資料庫的 `kTotalStrokes` 欄位，取自 [@mandel59/mojidata](https://www.npmjs.com/package/@mandel59/mojidata) 套件
- 範圍：中日韓統一表意文字基本區（U+4E00–U+9FFF），共 20,992 字
- 不在範圍內的字、標點、英文和數字一律使用標準字級
- 正式產品應以教育部標準字體的筆畫數校對

Unihan 資料 © Unicode, Inc.，依 [Unicode License v3](https://www.unicode.org/license.txt) 使用。

## 待確認

- 依論文研究結果設定分級界線與字級差距
- 第一版 App 支援的輸入方式（貼上文字、電子書、網頁文章）
- 以教育部標準字體筆畫資料校對
