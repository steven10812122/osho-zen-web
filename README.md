# 奧修禪卡 網頁版

從 MIT App Inventor 專案 (`osho2_checkpoint2_checkpoint1.aia`) 移植而來的靜態網頁版，純 HTML/CSS/JS，沒有建置步驟，可以直接用 GitHub Pages 部署。

## 本機預覽

```
python3 -m http.server 8765
```

再打開 http://localhost:8765

## 目錄結構

- `index.html` / `style.css` / `app.js` — 頁面與互動邏輯
- `data/decks.js` — 79 張卡的圖檔檔名 + 牌義文字，**之後要擴寫牌義就是改這個檔**
- `assets/cards/` — 卡牌圖片（含卡背 `back.jpg`）

## 功能

- 五個分類：主牌(23) / 火(14) / 水(14) / 雲(14) / 彩虹(14)
- 點縮圖看該張牌的大圖與牌義
- 「抽卡」會從全部 79 張中隨機抽一張

## 部署到 GitHub Pages

1. 在 GitHub 建立新的 repository，把這個資料夾內容 push 上去
2. repo 的 Settings → Pages → Source 選 `main` 分支、`/ (root)`
3. 幾分鐘後就能透過 `https://<你的帳號>.github.io/<repo名稱>/` 存取
