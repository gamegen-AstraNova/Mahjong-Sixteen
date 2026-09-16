# Mahjong Sixteen 封面與 HTML 交付

2026-09-10。使用內建 imagegen，依使用者的 AstraNova 角色參考重新繪製麻將對局封面。Asteria 位於對面出牌、Lumi 與 Nyx 位於左右，前景呈現玩家手牌；使用細緻日系線稿、清晰陰影及日光茶室構圖。Nyx 服裝依遊戲內 `public/common/textures/sym_character_nyx_outfit_1.webp`，為灰色露肩針織衫。角色參考來自使用者的 GameGen/LoRA 目錄，不將既有立繪拼貼成封面。

唯一正式資產為 `public/poster.webp`，建置後位於 `dist/poster.webp`，交付 ZIP 中位於根目錄 `poster.webp`，縱向 9:16。不要把原始碼 ZIP 或包含外層 `dist/` 的 ZIP 上傳為 HTML 遊戲。

## 驗證

- React 19.2.8，`npm test`：13 個測試檔、64 項測試通過。
- `npm run build`：前端與伺服器型別檢查、Vite 正式建置、伺服器建置通過；前端 JS 有既有 500 kB chunk 提示。
- 打包器檢查建置入口、相對入口資源、封面與來源一致、ZIP CRC、唯一項目及全部檔案與 `dist/` 位元組一致。
- HTTP `/dist/` 子路徑的 239 個執行檔案均回傳 200 且位元組一致。Chromium 驗證預載完成、Enter Game、領取獎勵及 Solo 開局成功，未出現 pageerror；未另行重跑四語系互動切換及完整牌局結算。
- 遊戲內圖片為 `common/textures/`，音訊為 `common/audio/`，四語系為 `config/language/`（英文預設）。資源解析保留逐項 style → commonPath → 本地 common → 本地 public 的既有行為。
- 此次更動範圍是封面與交付格式，未修改牌局邏輯或資源解析器。HTML ZIP 不包含多人伺服器；網路多人需另外部署並設定 serverUrl。
- GameGen 後台實際重新上傳尚未驗證。

## 生成提示詞

Edit the FIRST image, the vertical three-character mahjong poster. Change ONLY Nyx's clothing, the black-haired purple-underhair woman at the RIGHT, to faithfully match her actual in-game daily outfit shown in SECOND reference image: a soft light cool-gray off-shoulder knit sweater with a wide straight ribbed neckline, exposed shoulder area, long gray fabric sleeves with ribbed cuffs. Remove the black leather jacket completely and remove the gray tank top. Her torso and both arms must now wear the one coherent gray knit sweater from reference 2. In-game blue high-waisted jeans may remain hidden behind the table, no need to expose them. Do not copy the reference's standing pose or shoulder bag; redraw sweater fabric naturally for her existing seated leaning pose. Preserve Nyx's exact existing face, long black/purple hair, amused expression and hand positions. Preserve Asteria and Lumi, every mahjong tile, table, background, camera, lighting, clean anime linework and portrait 9:16 composition from image1. No added text or watermarks.
