# 奧修禪卡 網頁版

線上塔羅牌占卜小工具，收錄完整 79 張奧修禪卡。可以自由瀏覽五個牌組，也可以隨機抽卡看牌義。

**🔮 立即使用：https://steven10812122.github.io/osho-zen-web/**

## 功能

- 五個牌組：主牌（23張）／火／水／雲／彩虹（各14張）
- 點卡片縮圖看大圖與完整牌義解讀
- 「抽卡」隨機從 79 張中抽出一張
- 響應式設計，手機、平板、電腦都能用

## 開發

純 HTML/CSS/JS，沒有建置流程。本機跑起來：

```
python3 -m http.server 8765
```

打開 http://localhost:8765 即可。

想調整牌義文字，改 `data/decks.js`；想換卡牌圖片，`prompts/card-image-prompts.md` 有現成的 AI 生圖提示詞可以用 `scripts/generate_cards.py` 批次生成。
