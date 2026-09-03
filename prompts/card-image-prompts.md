# 79 張卡圖生成提示詞

給 ChatGPT / Midjourney / Stable Diffusion 之類的圖像生成工具用。每張卡一個提示詞，對應現有的 `assets/cards/` 檔名，生完直接覆蓋同名檔案即可，網站不用改任何程式碼。

## 為什麼不是「照抄原圖」

這裡刻意沒有寫成「畫出一模一樣的構圖」，而是保留每張牌的**核心意象與象徵**（花朵在石縫中開花＝勇氣、水面漂浮＝隨波逐流……這些是塔羅牌本身的通用視覺語言，不是特定畫家的獨創表達），但指定了一套跟原版奧修禪卡不同的畫風（見下方 Art Direction）。這樣生出來的圖在概念上忠於原本的牌意，視覺呈現上是一套新的、風格統一的原創插畫，而不是對受版權保護畫作的再製——這也是這份提示詞存在的意義：讓網站未來能光明正大公開。

如果生出來的某張圖意外地跟原卡長得太像（構圖、角色特徵、色彩配置幾乎一致），建議重新生成一次，或在提示詞後面加一句 `different composition from any existing tarot deck artwork`。

## Art Direction（每張都要套用，貼在每個 prompt 後面）

```
Style: modern symbolic spiritual illustration, digital painting with soft luminous
gradients and glowing light, dreamlike meditative mood, rich jewel-tone color palette,
single centered subject, atmospheric glowing background (stars / mist / aura),
minimalist and uncluttered, stylized non-photorealistic figures.
Aspect ratio 2:3 portrait. No text, no logo, no watermark, no border/frame.
Negative: text, letters, numbers, watermark, signature, photorealistic skin,
cluttered background, low quality, blurry, extra limbs, frame, border
```

用法：把下面每張卡的 Prompt 那行，接上這段 Art Direction 一起丟給生圖工具。79 張共用同一套風格描述，這樣生出來的整副牌才會像同一個人畫的、風格統一。

---

## 主牌 Major Arcana（ccard1.jpg – ccard23.jpg）

深邃、宇宙感的珠寶色調（深藍、紫、金）為主基調，依每張牌主題微調。

1. **ccard1.jpg — 存在 Existence**
   Prompt: A serene figure sitting cross-legged on a large glowing lotus leaf, gazing up at a vast cosmic night sky filled with stars and a shooting comet. Deep indigo-to-violet gradient. A feeling of belonging to the whole universe.

2. **ccard2.jpg — 內在之聲 Inner Voice**
   Prompt: A meditating figure with a crescent-moon halo, calm face emerging from swirling silver water, two dolphins gliding gently around them symbolizing intuition. Cool blue-white palette, quiet inner listening.

3. **ccard3.jpg — 創造力 Creativity**
   Prompt: A radiant open hand releasing colorful ribbons of light and paint that swirl upward into abstract joyful shapes. Warm magenta-orange glow, playful creative energy flowing outward.

4. **ccard4.jpg — 叛逆者 The Rebel**
   Prompt: A lone figure standing tall on a cliff edge holding a torch high, cloak blown backward by wind, a broken chain lying at their feet. Fiery red-black palette, defiant freedom.

5. **ccard5.jpg — 空無 No-Thingness**
   Prompt: A vast empty dark void with a single soft glowing point of light at the center, the faint dissolving silhouette of a seated figure. Deep black-violet gradient, spacious potential rather than emptiness.

6. **ccard6.jpg — 戀人 The Lovers**
   Prompt: Two intertwined figures made of soft light, foreheads gently touching, hearts connected by a thread of golden light. Soft pink-lavender palette, tender mutual recognition rather than possession.

7. **ccard7.jpg — 覺察 Awareness**
   Prompt: A calm meditating figure with a single luminous eye glowing at the center of the chest, faint thought-forms drifting away like unattached smoke. Teal-gold palette.

8. **ccard8.jpg — 勇氣 Courage**
   Prompt: A small delicate flower blooming through a crack in grey stone, reaching toward a single shaft of golden light from above. Muted grey background, warm golden highlight.

9. **ccard9.jpg — 獨處 Aloneness**
   Prompt: A single figure sitting peacefully inside a soft glowing circle of light in an otherwise dark space, serene expression, self-contained and whole. Deep blue-violet palette.

10. **ccard10.jpg — 變化 Change**
    Prompt: A great luminous wheel turning in space, a small figure standing still at its center while the outer rim blurs with motion. Gold-orange-blue gradient.

11. **ccard11.jpg — 突破 Breakthrough**
    Prompt: Cracks of golden light bursting outward through a dark stone wall, energy radiating in dramatic beams. Deep purple-black background, brilliant golden fracture light.

12. **ccard12.jpg — 新視野 New Vision**
    Prompt: A figure standing at a mountain summit, one hand reaching toward bright sunrise light above, the other resting on rocky roots below. Balanced light-and-shadow composition.

13. **ccard13.jpg — 蛻變 Transformation**
    Prompt: A figure mid-transformation — one half dissolving into falling petals of ash, the other half emerging luminous and phoenix-like. Deep red-violet-gold palette.

14. **ccard14.jpg — 整合 Integration**
    Prompt: Two flowing forms — one sharp and angular, one soft and curved — merging together into a single balanced glowing figure. Teal-rose gradient.

15. **ccard15.jpg — 制約 Conditioning**
    Prompt: A lion-shaped figure standing among a flock of sheep, faint ghostly bars of an invisible cage around it, a hint of golden mane light breaking through. Muted earth tones.

16. **ccard16.jpg — 雷電 Thunderbolt**
    Prompt: A dramatic bolt of white-gold lightning shattering an old rigid tower into fragments against a dark storm-blue sky. Sense of sudden necessary upheaval.

17. **ccard17.jpg — 寂靜 Silence**
    Prompt: A solitary figure sitting cross-legged in deep meditation inside a vast quiet dark-blue space, faint ripples of stillness radiating outward like visible sound waves. Minimal composition.

18. **ccard18.jpg — 前世 Past Lives**
    Prompt: A figure gazing into a pool of water reflecting faint layered echoes of past selves fading into mist. Sepia-violet palette, an old repeating pattern.

19. **ccard19.jpg — 純真 Innocence**
    Prompt: A childlike figure with arms outstretched in soft golden light, surrounded by floating simple flowers and bubbles. Warm pastel palette, open uncomplicated wonder.

20. **ccard20.jpg — 超越幻象 Beyond Illusion**
    Prompt: A figure gently removing a translucent veil to reveal clearer light behind it, layered semi-transparent shapes dissolving away. Cool violet-silver palette.

21. **ccard21.jpg — 完成 Completion**
    Prompt: A circle of golden light closing seamlessly, a figure bowing gently at its center in a soft exhale. Warm amber-rose gradient, gentle closure.

22. **ccard22.jpg — 大師 The Master**
    Prompt: A luminous bearded figure seated in deep meditation, roots of light extending downward and a single star glowing above the crown of the head. Deep midnight-blue and silver palette, quiet authority.

23. **ccard23.jpg — 愚者 The Fool**
    Prompt: A joyful figure leaping off a cliff edge into open sky at dawn, arms outstretched holding a small flower, mountains and a river below bathed in warm sunrise colors. Trust and new beginning.

---

## 火 Fire（fcard1.jpg – fcard14.jpg）

暖色調為主：紅、橙、金，太陽與火焰意象。

1. **fcard1.jpg — 本源 The Source**
   Prompt: A radiant sun-like sphere of concentrated red-orange-gold energy pulsing at the center of the frame, rings of fire and light emanating outward. Untapped inner power.

2. **fcard2.jpg — 可能 Possibilities**
   Prompt: A figure standing on a high peak, an eagle soaring above toward an open golden horizon. Wide sense of expanding opportunity.

3. **fcard3.jpg — 體驗 Experiencing**
   Prompt: A figure with arms wrapped fully around a glowing tree trunk, eyes closed, warm amber light passing between them both ways. Direct lived experience over analysis.

4. **fcard4.jpg — 參與 Participation**
   Prompt: A circle of glowing figures each holding out a beam of colored light that weaves together into one larger radiant pattern above them. Warm collective energy.

5. **fcard5.jpg — 全然 Totality**
   Prompt: Three figures mid-motion passing glowing orbs of light between each other in a triangular formation, dynamic warm-toned light trails. Full present-moment focus.

6. **fcard6.jpg — 成功 Success**
   Prompt: A triumphant figure riding a powerful tiger through a shower of golden confetti and ribbons, joyful expression. Warm celebratory orange-gold palette.

7. **fcard7.jpg — 壓力 Stress**
   Prompt: A frantic juggler figure balancing on a rolling ball while juggling too many glowing objects at once, strained expression. Warm but chaotic reds and oranges.

8. **fcard8.jpg — 旅程 Traveling**
   Prompt: A lone traveler walking a winding misty mountain path, the destination hidden in soft fog, warm dawn light glowing at the edges. Journey over destination.

9. **fcard9.jpg — 耗竭 Exhaustion**
   Prompt: A figure entangled in mechanical gears and tubes, slumped but still trying to keep moving. Dulled warm tones fading toward grey, burnout needing rest.

10. **fcard10.jpg — 壓抑 Suppression**
    Prompt: A glowing figure tightly bound by coils of dark rope, faint light straining to escape through the bindings. Deep red-black palette, a single crack of gold light.

11. **fcard11.jpg — 玩心 Playfulness**
    Prompt: A figure dancing freely under a sky full of stars, limbs loose and joyful, trailing sparks of golden light like laughter made visible.

12. **fcard12.jpg — 熾烈 Intensity**
    Prompt: A figure's form elongated into a single streak of pure blazing energy shooting forward, minimal background. Dramatic red-gold motion blur, total focused momentum.

13. **fcard13.jpg — 分享 Sharing**
    Prompt: A generous figure holding a glowing candle and an overflowing basket of fruit and light outward toward the viewer. Warm golden radiance, abundance given freely.

14. **fcard14.jpg — 創造者 The Creator**
    Prompt: A serene robed figure seated in soft inner firelight, hands cupped around a small glowing flame at the heart. Warm orange-gold aura, integrated creative power.

---

## 水 Water（wcard1.jpg – wcard14.jpg）

冷色調為主：藍、青、水色，流水與情感意象。

1. **wcard1.jpg — 隨波逐流 Going With The Flow**
   Prompt: A figure floating peacefully on their back on a calm turquoise water surface, eyes closed, gentle ripples carrying them along. Cool blue-teal palette, complete surrender and trust.

2. **wcard2.jpg — 知己之交 Friendliness**
   Prompt: Two trees growing side by side, branches touching lightly overhead without tangling, roots independent in soft earth. Cool green-blue palette, quiet companionship.

3. **wcard3.jpg — 歡慶 Celebration**
   Prompt: Three joyful figures dancing barefoot in the rain among trees, laughing with arms raised, splashes of water catching soft light. Lively blue-violet palette.

4. **wcard4.jpg — 內觀 Turning In**
   Prompt: A seated figure with eyes closed in meditation, faint translucent faces and thoughts drifting and dissolving behind them like ripples on water. Calm indigo palette.

5. **wcard5.jpg — 放不下 Clinging To The Past**
   Prompt: A hunched figure clutching an ornate heavy chest that glows faintly with old memories. Cool grey-blue tones, weight of longing for what has passed.

6. **wcard6.jpg — 幻夢 The Dream**
   Prompt: A figure gazing longingly at a glowing, semi-transparent idealized silhouette in the distance. Soft dreamy blue-violet mist, romantic illusion rather than solid reality.

7. **wcard7.jpg — 投射 Projections**
   Prompt: Two faces overlapping in shifting light and shadow, blurring into one another. Ambiguous cool-toned mist, seeing one's own feelings mirrored onto another.

8. **wcard8.jpg — 放手 Letting Go**
   Prompt: A single water droplet sliding off a lotus leaf into calm water, gentle expanding ripples, a faint figure walking softly away in the background mist. Soft blue-grey palette.

9. **wcard9.jpg — 安逸 Laziness**
   Prompt: A figure reclining on a lounge chair sipping a drink, unaware the mirror behind them is quietly cracked. Cool blues with a subtle uneasy fracture of light.

10. **wcard10.jpg — 和諧 Harmony**
    Prompt: A serene figure with closed eyes and a gentle smile, a stream of soft dolphin-like light flowing between heart and crown. Cool aqua-violet palette, inner balance.

11. **wcard11.jpg — 理解 Understanding**
    Prompt: A bird flying freely past the loosely open bars of a cage, the bars rendered translucent and unlocked. Soft blue-white palette, realizing the limit was never solid.

12. **wcard12.jpg — 信任 Trust**
    Prompt: A figure leaping joyfully off a cliff into open sky above calm water, arms wide open, no visible safety net. Warm light breaking through cool blue tones.

13. **wcard13.jpg — 接納 Receptivity**
    Prompt: Two open hands gently cupping a glowing blooming lotus flower, soft starlight and water reflections around them. Cool blue-lavender palette, quiet openness.

14. **wcard14.jpg — 療癒 Healing**
    Prompt: Two hands wrapped gently around a luminous glowing figure at the heart, old faint cracks of light softening and dissolving. Warm-cool blended blue-rose palette.

---

## 雲 Clouds / Air（ucard1.jpg – ucard14.jpg）

冷灰、藍紫、白，天空與心智意象。

1. **ucard1.jpg — 意識之光 Consciousness**
   Prompt: A meditating silhouette made entirely of stars and soft mist against a deep midnight-blue sky. Quiet luminous clarity emerging from stillness.

2. **ucard2.jpg — 拉鋸 Schizophrenia**
   Prompt: A figure suspended midair, pulled by two glowing opposing forces on either side, unable to land. Cool grey-violet palette, torn between two choices.

3. **ucard3.jpg — 封凍 Ice-olation**
   Prompt: A face frozen inside a block of pale blue ice, a single tear suspended mid-fall. Cool icy palette, protective numbness hiding old hurt.

4. **ucard4.jpg — 拖延 Postponement**
   Prompt: A figure gazing wistfully out a window at a vivid colorful landscape while standing inside a dim grey fog-filled room. Vibrant possibility versus grey hesitation.

5. **ucard5.jpg — 比較 Comparison**
   Prompt: A rough old tree trunk and a tall slender bamboo standing side by side in soft light, neither better nor worse. Muted green-brown palette.

6. **ucard6.jpg — 重擔 The Burden**
   Prompt: A bent figure climbing a steep hill carrying many faint ghostly passengers and packages on their back. Muted grey-violet tones, weight of unspoken obligation.

7. **ucard7.jpg — 心機 Politics**
   Prompt: Two overlapping masks, one smiling and one scowling, neither showing a real face beneath. Cool grey-green palette, calculated social performance.

8. **ucard8.jpg — 自責 Guilt**
   Prompt: A figure clutching their head as translucent hands reach in from all directions. Faint grey-violet tones, the heavy weight of self-blame pressing inward.

9. **ucard9.jpg — 悲傷 Sorrow**
   Prompt: A hooded figure sitting in quiet contemplation, head bowed, a single thin beam of soft light breaking through darkness behind them. Deep blue-grey palette.

10. **ucard10.jpg — 重生 Rebirth**
    Prompt: A small child playing a flute while standing atop a sleeping lion and camel, dawn light breaking behind them. Soft gold-blue gradient, gentle emergence of a renewed self.

11. **ucard11.jpg — 紛亂之心 Mind**
    Prompt: A head-shaped form built from tangled gears, dice, and mechanical fragments, faint light struggling to shine through the clutter. Cool grey-metallic palette.

12. **ucard12.jpg — 備戰 Fighting**
    Prompt: A figure encased in heavy armor, fists clenched, a small vulnerable glow barely visible through a crack in the chestplate. Cool steel-blue palette.

13. **ucard13.jpg — 教條 Morality**
    Prompt: A figure boxed in by rigid geometric bars and layered stiff collars. Muted grey-beige palette, vitality dimmed by external rules.

14. **ucard14.jpg — 掌控 Control**
    Prompt: A tense figure surrounded by sharp radiating spikes of self-made light, rigid posture. Cool blue-white palette with an undertone of strain.

---

## 彩虹 Rainbow（rcard1.jpg – rcard14.jpg）

暖色調＋多彩，豐盛與大地意象。

1. **rcard1.jpg — 圓熟 Maturity**
   Prompt: A calm figure standing serenely under a blossoming tree in soft spring light, roots visible and deep beneath them. Warm golden-green palette, earned stability.

2. **rcard2.jpg — 當下 Moment To Moment**
   Prompt: A figure stepping lightly across stones in a flowing stream, focused only on the next step, warm multicolor light reflecting off the water's surface.

3. **rcard3.jpg — 指引 Guidance**
   Prompt: A luminous rainbow-winged figure of light standing gently beside a small seated figure. Warm prismatic glow, inner guidance rather than external authority.

4. **rcard4.jpg — 守財者 The Miser**
   Prompt: A hunched figure surrounded by heaps of glowing jewels, hands clutched tightly shut, a cool shadowed corner despite the wealth around them.

5. **rcard5.jpg — 局外人 The Outsider**
   Prompt: A small child standing before a tall gate believing it locked, while a chain lies loosely broken at their feet. Warm-cool contrast between imagined and real barriers.

6. **rcard6.jpg — 妥協 Compromise**
   Prompt: Two figures standing side by side each quietly holding a small blade behind their back, forced smiles. Muted warm-grey palette, uneasy peace.

7. **rcard7.jpg — 耐心 Patience**
   Prompt: A pregnant figure sitting peacefully as moon phases arc gently overhead in a cycle. Soft warm amber-violet gradient, quiet trust in natural timing.

8. **rcard8.jpg — 平凡 Ordinariness**
   Prompt: A figure walking a simple country path carrying a basket of flowers, no audience. Warm soft earth-tone palette, quiet dignity in everyday simplicity.

9. **rcard9.jpg — 熟成 Ripeness**
   Prompt: A single fully ripe fruit hanging heavy and glowing on a branch, about to fall on its own without force. Warm golden-orange palette, readiness.

10. **rcard10.jpg — 世界一家 We Are The World**
    Prompt: A circle of many different glowing figures holding hands, dancing gently around a small luminous globe. Warm multicolor prismatic palette, joyful collective celebration.

11. **rcard11.jpg — 冒險 Adventure**
    Prompt: A small figure standing at the edge of a misty forest facing a glowing, uncertain rainbow-colored light ahead, no map. Warm-cool contrast, quiet courage.

12. **rcard12.jpg — 放慢腳步 Slowing Down**
    Prompt: A turtle carrying a glowing shell-home calmly along a quiet path, unhurried. Warm muted earth tones, contentment already carried within.

13. **rcard13.jpg — 綻放 Flowering**
    Prompt: A figure seated on a fully blooming lotus, surrounded by radiating warm multicolor light and floating petals. Uninhibited open joy.

14. **rcard14.jpg — 豐盛 Abundance**
    Prompt: A grounded figure with one hand touching the earth and one reaching toward the sky, warm full-bodied glow. Harmony between physical enjoyment and inner depth.

---

## 卡背 Card Back（back.jpg）

Prompt: An elegant symmetrical mandala-like pattern in deep indigo and gold, softly glowing at the center, no text, no figure — abstract and mysterious. Same Art Direction style as above, aspect ratio 2:3.
