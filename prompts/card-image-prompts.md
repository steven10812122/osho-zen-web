# 79 張卡圖生成提示詞

給 ChatGPT / Midjourney / Stable Diffusion 之類的圖像生成工具用，也可以直接用 `scripts/generate_cards.py` 自動批次生（見專案 README）。每張卡一個提示詞，對應現有的 `assets/cards/` 檔名，生完直接覆蓋同名檔案即可，網站不用改任何程式碼。

## 為什麼不是「照抄原圖」，也盡量不畫人形

保留每張牌的**核心意象與象徵**（花朵在石縫中開花＝勇氣、水面漂浮＝隨波逐流……這些是塔羅牌本身的通用視覺語言，不是特定畫家的獨創表達），但指定了一套跟原版奧修禪卡不同的畫風（見下方 Art Direction），概念忠於牌意、視覺是全新的原創插畫。

另外這版刻意把大部分「人形主角」改成物件、動物、植物、光影等抽象意象——測試時發現免費生圖模型（Pollinations）對冥想／水中人形這類主題常常會擅自畫成裸體，怎麼調提示詞都壓不住，所以乾脆從構圖上避開真人身體，只在少數幾張真的需要「人的存在感」時，用「遠景剪影、背光、看不清五官身體細節」的安全寫法（這種寫法實測沒問題）。

## Art Direction（每張都要套用，貼在每個 prompt 後面）

```
Style: modern symbolic spiritual illustration, digital painting with soft luminous
gradients and glowing light, dreamlike meditative mood, rich jewel-tone color palette,
single centered subject, atmospheric glowing background (stars / mist / aura),
minimalist and uncluttered. If a human presence appears, render it ONLY as a small
distant silhouette with no visible facial or body detail, or as an abstract light-being
with no anatomy — never a close-up realistic body, never bare skin. Family-friendly, SFW.
Aspect ratio 2:3 portrait. No text, no logo, no watermark, no border/frame.
Negative: nudity, nude, bare skin, sexual, suggestive, photorealistic skin, realistic
human anatomy, close-up body, text, letters, numbers, watermark, signature,
cluttered background, low quality, blurry, extra limbs, frame, border
```

用法：把下面每張卡的 Prompt 那行，接上這段 Art Direction 一起丟給生圖工具。79 張共用同一套風格描述，這樣生出來的整副牌才會像同一個人畫的、風格統一。

---

## 主牌 Major Arcana（ccard1.jpg – ccard23.jpg）

深邃、宇宙感的珠寶色調（深藍、紫、金）為主基調，依每張牌主題微調。

1. **ccard1.jpg — 存在 Existence**
   Prompt: Abstract botanical illustration, no figure, no person, no human anatomy: a single glowing lotus-shaped flower made purely of starlight and soft mist petals, floating alone above a still dark cosmic ocean beneath a sky full of stars and a shooting comet. Deep indigo-to-violet gradient. Pure abstract light and floral form only, like a logo or icon.

2. **ccard2.jpg — 內在之聲 Inner Voice**
   Prompt: A glowing crescent moon cradling a swirling spiral of silver water, two dolphins circling gently around it symbolizing intuition. Cool blue-white palette, quiet inner listening.

3. **ccard3.jpg — 創造力 Creativity**
   Prompt: A single glowing paintbrush trailing colorful ribbons of light that swirl upward into abstract joyful shapes. Warm magenta-orange glow, playful creative energy flowing outward.

4. **ccard4.jpg — 叛逆者 The Rebel**
   Prompt: A single blazing torch standing upright on a wind-swept cliff edge at dusk, a broken chain lying beside it, flames whipping like a cloak in the wind. Fiery red-black palette.

5. **ccard5.jpg — 空無 No-Thingness**
   Prompt: A vast empty dark void with a single soft glowing point of light slowly dissolving at the center, no solid form. Deep black-violet gradient, spacious potential rather than emptiness.

6. **ccard6.jpg — 戀人 The Lovers**
   Prompt: Two spirals of soft light intertwining and touching at their centers, connected by a thread of golden light. Soft pink-lavender palette, tender mutual connection.

7. **ccard7.jpg — 覺察 Awareness**
   Prompt: A single luminous eye glowing softly at the center of an expanding calm circle of light, faint thought-forms drifting away like unattached smoke. Teal-gold palette.

8. **ccard8.jpg — 勇氣 Courage**
   Prompt: A small delicate flower blooming through a crack in grey stone, reaching toward a single shaft of golden light from above. Muted grey background, warm golden highlight.

9. **ccard9.jpg — 獨處 Aloneness**
   Prompt: A single glowing orb of soft light resting peacefully inside a larger circle of light in an otherwise dark space, self-contained and whole. Deep blue-violet palette.

10. **ccard10.jpg — 變化 Change**
    Prompt: A great luminous wheel turning in space, a small steady point of light glowing at its center while the outer rim blurs with motion. Gold-orange-blue gradient.

11. **ccard11.jpg — 突破 Breakthrough**
    Prompt: Cracks of golden light bursting outward through a dark stone wall, energy radiating in dramatic beams. Deep purple-black background, brilliant golden fracture light.

12. **ccard12.jpg — 新視野 New Vision**
    Prompt: A single tree growing at a mountain summit, its upper branches reaching into bright sunrise light, its roots gripping rocky ground below. Balanced light-and-shadow composition.

13. **ccard13.jpg — 蛻變 Transformation**
    Prompt: A phoenix-like form made of falling ash and petals on one side, dissolving into luminous rising light and feathers on the other. Deep red-violet-gold palette.

14. **ccard14.jpg — 整合 Integration**
    Prompt: Two flowing forms — one sharp and angular, one soft and curved — merging together into a single balanced glowing shape. Teal-rose gradient.

15. **ccard15.jpg — 制約 Conditioning**
    Prompt: A lion-shaped figure standing among a flock of sheep, faint ghostly bars of an invisible cage around it, a hint of golden mane light breaking through. Muted earth tones.

16. **ccard16.jpg — 雷電 Thunderbolt**
    Prompt: A dramatic bolt of white-gold lightning shattering an old rigid tower into fragments against a dark storm-blue sky. Sense of sudden necessary upheaval.

17. **ccard17.jpg — 寂靜 Silence**
    Prompt: Abstract illustration, no figure, no person: a single glowing lotus-shaped icon resting motionless in a vast quiet dark-blue empty space, faint ripples of stillness radiating outward like visible sound waves. Minimal composition, like a logo.

18. **ccard18.jpg — 前世 Past Lives**
    Prompt: A pool of water reflecting faint layered echoes of ghostly shapes fading into mist. Sepia-violet palette, an old repeating pattern.

19. **ccard19.jpg — 純真 Innocence**
    Prompt: Abstract illustration, no figure, no person, no human anatomy: a cluster of simple daisy flowers and floating soap bubbles glowing in soft golden light, like a botanical icon. Warm pastel palette, open uncomplicated wonder.

20. **ccard20.jpg — 超越幻象 Beyond Illusion**
    Prompt: Abstract illustration, no figure, no person: a translucent veil of fabric dissolving away in mid-air over an empty glowing light source, layered semi-transparent cloth forms fading into mist, like a surreal object study. Cool violet-silver palette.

21. **ccard21.jpg — 完成 Completion**
    Prompt: A circle of golden light closing seamlessly around a single softly fading star at its center. Warm amber-rose gradient, gentle closure.

22. **ccard22.jpg — 大師 The Master**
    Prompt: A tall ancient tree with roots of light extending deep into the earth and a single star glowing above its crown. Deep midnight-blue and silver palette, quiet enduring authority.

23. **ccard23.jpg — 愚者 The Fool**
    Prompt: A small silhouette leaping off a cliff edge into open sky at dawn, arms outstretched holding a small flower, wearing simple colorful clothing, mountains and a river below bathed in warm sunrise colors. Trust and new beginning.

---

## 火 Fire（fcard1.jpg – fcard14.jpg）

暖色調為主：紅、橙、金，太陽與火焰意象。

1. **fcard1.jpg — 本源 The Source**
   Prompt: A radiant sun-like sphere of concentrated red-orange-gold energy pulsing at the center of the frame, rings of fire and light emanating outward. Untapped inner power.

2. **fcard2.jpg — 可能 Possibilities**
   Prompt: An eagle soaring high above a mountain peak toward an open golden horizon. Wide sense of expanding opportunity, warm gold-orange sky.

3. **fcard3.jpg — 體驗 Experiencing**
   Prompt: A glowing tree trunk with warm amber light flowing through its bark like a heartbeat, roots and branches pulsing gently together. Direct lived experience over abstract thought.

4. **fcard4.jpg — 參與 Participation**
   Prompt: A circle of glowing colored light-beams weaving together into one larger radiant pattern above a warm central glow. Warm collective energy.

5. **fcard5.jpg — 全然 Totality**
   Prompt: Three flames of light passing a glowing orb between each other in a triangular dance, dynamic warm-toned light trails. Full present-moment focus.

6. **fcard6.jpg — 成功 Success**
   Prompt: A powerful tiger leaping through a shower of golden confetti and ribbons, triumphant motion. Warm celebratory orange-gold palette.

7. **fcard7.jpg — 壓力 Stress**
   Prompt: Too many glowing orbs, rings, and flames being juggled at once in frantic motion above a single spinning ball. Warm but chaotic reds and oranges, strain visible in the motion blur.

8. **fcard8.jpg — 旅程 Traveling**
   Prompt: A small silhouette walking a winding misty mountain path, the destination hidden in soft fog, warm dawn light glowing at the edges. Journey over destination.

9. **fcard9.jpg — 耗竭 Exhaustion**
   Prompt: Abstract mechanical illustration, no figure, no person, no human anatomy: a flickering candle flame trapped inside a cage of rusted mechanical gears, chains and tubes, struggling to keep burning, like a steampunk icon. Dulled warm tones fading toward grey, burnout needing rest.

10. **fcard10.jpg — 壓抑 Suppression**
    Prompt: A glowing orb of light tightly bound by coils of dark rope, faint light straining to escape through the bindings. Deep red-black palette, a single crack of gold light escaping.

11. **fcard11.jpg — 玩心 Playfulness**
    Prompt: A small silhouette dancing freely under a sky full of stars, limbs loose and joyful, trailing sparks of golden light like laughter made visible.

12. **fcard12.jpg — 熾烈 Intensity**
    Prompt: A single streak of pure blazing energy shooting forward like a comet, minimal background. Dramatic red-gold motion blur, total focused momentum.

13. **fcard13.jpg — 分享 Sharing**
    Prompt: A glowing candle beside an overflowing basket of fruit and light, warmth spreading outward freely toward the viewer. Warm golden radiance, abundance given freely.

14. **fcard14.jpg — 創造者 The Creator**
    Prompt: A small silhouette seated peacefully in soft inner firelight, hands cupped around a small glowing flame at the heart. Warm orange-gold aura, integrated creative power.

---

## 水 Water（wcard1.jpg – wcard14.jpg）

冷色調為主：藍、青、水色，流水與情感意象。

1. **wcard1.jpg — 隨波逐流 Going With The Flow**
   Prompt: A single white feather floating peacefully on a calm turquoise water surface, drifting gently with the current. Cool blue-teal palette, complete surrender and trust.

2. **wcard2.jpg — 知己之交 Friendliness**
   Prompt: Two trees growing side by side, branches touching lightly overhead without tangling, roots independent in soft earth. Cool green-blue palette, quiet companionship.

3. **wcard3.jpg — 歡慶 Celebration**
   Prompt: Three glowing lanterns swaying and dancing together in the rain among trees, light scattering joyfully through raindrops. Lively blue-violet palette.

4. **wcard4.jpg — 內觀 Turning In**
   Prompt: Abstract illustration, no figure, no person: a single still point of glowing light at the center of calm dark water, faint translucent geometric ripple-patterns drifting and dissolving outward like sonar waves, like a minimalist icon. Calm indigo palette.

5. **wcard5.jpg — 放不下 Clinging To The Past**
   Prompt: Abstract object illustration, no figure, no person: an ornate antique wooden treasure trunk with a curved lid, glowing faintly from within with old sepia-toned memories, rusty chains and padlocks wrapped tightly around it, like a product photo of an object. Cool grey-blue tones, weight of longing for what has passed.

6. **wcard6.jpg — 幻夢 The Dream**
   Prompt: Abstract illustration, no figure, no person, no human anatomy: a single glowing soap-bubble orb reflecting a distorted rainbow mirage inside it, floating just out of reach above still water, like a surreal object study. Soft dreamy blue-violet mist, romantic illusion rather than solid reality.

7. **wcard7.jpg — 投射 Projections**
   Prompt: Abstract illustration, no figure, no person, no face, no human anatomy: two translucent theater masks overlapping in shifting light and shadow, blurring into one another, like an object study. Ambiguous cool-toned mist, seeing one's own feelings mirrored onto another.

8. **wcard8.jpg — 放手 Letting Go**
   Prompt: A single water droplet sliding off a lotus leaf into calm water, gentle expanding ripples fading into stillness. Soft blue-grey palette, quiet release.

9. **wcard9.jpg — 安逸 Laziness**
   Prompt: An empty lounge chair beside a half-finished drink, the mirror behind it quietly cracked. Cool blues with a subtle uneasy fracture of light, comfort mistaken for stillness.

10. **wcard10.jpg — 和諧 Harmony**
    Prompt: Abstract illustration, no figure, no person, no human anatomy: two dolphins made of soft light swimming in a gentle figure-eight/infinity loop around each other, like a minimalist logo. Cool aqua-violet palette, inner balance.

11. **wcard11.jpg — 理解 Understanding**
    Prompt: A bird flying freely past the loosely open bars of a cage, the bars rendered translucent and unlocked. Soft blue-white palette, realizing the limit was never solid.

12. **wcard12.jpg — 信任 Trust**
    Prompt: A small bird diving fearlessly off a cliff edge into open sky above calm water, wings folded back, trusting the fall completely. No figure, no person. Warm light breaking through cool blue tones.

13. **wcard13.jpg — 接納 Receptivity**
    Prompt: Two open hands gently cupping a glowing blooming lotus flower, soft starlight and water reflections around them. Cool blue-lavender palette, quiet openness.

14. **wcard14.jpg — 療癒 Healing**
    Prompt: Two hands gently cupping a small luminous glowing orb, old faint cracks of light on its surface softening and dissolving. Warm-cool blended blue-rose palette, tender healing.

---

## 雲 Clouds / Air（ucard1.jpg – ucard14.jpg）

冷灰、藍紫、白，天空與心智意象。

1. **ucard1.jpg — 意識之光 Consciousness**
   Prompt: A meditating silhouette made entirely of stars and soft mist against a deep midnight-blue sky. Quiet luminous clarity emerging from stillness.

2. **ucard2.jpg — 拉鋸 Schizophrenia**
   Prompt: A glowing orb suspended midair, pulled taut by two opposing beams of light on either side, unable to settle. Cool grey-violet palette, torn between two choices.

3. **ucard3.jpg — 封凍 Ice-olation**
   Prompt: A face frozen inside a block of pale blue ice, a single tear suspended mid-fall. Cool icy palette, protective numbness hiding old hurt.

4. **ucard4.jpg — 拖延 Postponement**
   Prompt: A window glowing with a vivid colorful landscape outside, while the room on this side stays dim and grey with fog. Vibrant possibility versus grey hesitation.

5. **ucard5.jpg — 比較 Comparison**
   Prompt: A rough old tree trunk and a tall slender bamboo standing side by side in soft light, neither better nor worse. Muted green-brown palette.

6. **ucard6.jpg — 重擔 The Burden**
   Prompt: A small bent silhouette climbing a steep hill carrying many faint ghostly packages and shapes on their back. Muted grey-violet tones, weight of unspoken obligation.

7. **ucard7.jpg — 心機 Politics**
   Prompt: Two overlapping masks, one smiling and one scowling, neither showing a real face beneath. Cool grey-green palette, calculated social performance.

8. **ucard8.jpg — 自責 Guilt**
   Prompt: A glowing head-shaped form with translucent hands reaching in from all directions. Faint grey-violet tones, the heavy weight of self-blame pressing inward.

9. **ucard9.jpg — 悲傷 Sorrow**
   Prompt: A small hooded silhouette sitting in quiet contemplation, head bowed, a single thin beam of soft light breaking through darkness behind them. Deep blue-grey palette.

10. **ucard10.jpg — 重生 Rebirth**
    Prompt: A small distant silhouette, no visible facial detail, playing a flute while standing atop a sleeping lion and camel, dawn light breaking behind them. Soft gold-blue gradient.

11. **ucard11.jpg — 紛亂之心 Mind**
    Prompt: A head-shaped form built from tangled gears, dice, and mechanical fragments, faint light struggling to shine through the clutter. Cool grey-metallic palette.

12. **ucard12.jpg — 備戰 Fighting**
    Prompt: A suit of heavy armor standing alone, fists clenched empty inside, a small vulnerable glow barely visible through a crack in the chestplate. Cool steel-blue palette.

13. **ucard13.jpg — 教條 Morality**
    Prompt: A rigid geometric cage of bars and layered stiff collars stacked upon each other, empty at the center. Muted grey-beige palette, vitality dimmed by external rules.

14. **ucard14.jpg — 掌控 Control**
    Prompt: A glowing orb surrounded by sharp radiating spikes of self-made light, tightly contained. Cool blue-white palette with an undertone of strain.

---

## 彩虹 Rainbow（rcard1.jpg – rcard14.jpg）

暖色調＋多彩，豐盛與大地意象。

1. **rcard1.jpg — 圓熟 Maturity**
   Prompt: A blossoming tree standing serenely in soft spring light, its roots glowing deep and visible beneath the earth. Warm golden-green palette, earned stability.

2. **rcard2.jpg — 當下 Moment To Moment**
   Prompt: A small silhouette stepping lightly across stones in a flowing stream, focused only on the next step. Warm multicolor light reflecting off the water's surface.

3. **rcard3.jpg — 指引 Guidance**
   Prompt: A luminous rainbow-winged shape of light hovering gently beside a small glowing seed of light. Warm prismatic glow, inner guidance rather than external authority.

4. **rcard4.jpg — 守財者 The Miser**
   Prompt: A heap of glowing jewels in a shadowed corner, two clutched hands barely visible gripping them tightly shut. Cool shadow despite the wealth around them.

5. **rcard5.jpg — 局外人 The Outsider**
   Prompt: A small silhouette of a child standing before a tall gate believing it locked, while a chain lies loosely broken at their feet. Warm-cool contrast between imagined and real barriers.

6. **rcard6.jpg — 妥協 Compromise**
   Prompt: Two shapes of light standing side by side, each quietly hiding a small blade behind them, forced smiles painted on simple mask-like faces. Muted warm-grey palette, uneasy peace.

7. **rcard7.jpg — 耐心 Patience**
   Prompt: A glowing seed resting peacefully as moon phases arc gently overhead in a cycle, quiet growth happening unseen within. Soft warm amber-violet gradient.

8. **rcard8.jpg — 平凡 Ordinariness**
   Prompt: A small silhouette walking a simple country path carrying a basket of flowers, no audience. Warm soft earth-tone palette, quiet dignity in everyday simplicity.

9. **rcard9.jpg — 熟成 Ripeness**
   Prompt: A single fully ripe fruit hanging heavy and glowing on a branch, about to fall on its own without force. Warm golden-orange palette, readiness.

10. **rcard10.jpg — 世界一家 We Are The World**
    Prompt: A circle of many different glowing lights linked hand to hand in an unbroken ring, dancing gently around a small luminous globe. Warm multicolor prismatic palette, joyful collective celebration.

11. **rcard11.jpg — 冒險 Adventure**
    Prompt: A small silhouette standing at the edge of a misty forest facing a glowing, uncertain rainbow-colored light ahead, no map. Warm-cool contrast, quiet courage.

12. **rcard12.jpg — 放慢腳步 Slowing Down**
    Prompt: A turtle carrying a glowing shell-home calmly along a quiet path, unhurried. Warm muted earth tones, contentment already carried within.

13. **rcard13.jpg — 綻放 Flowering**
    Prompt: A fully blooming lotus radiating warm multicolor light and floating petals outward in every direction. Uninhibited open joy.

14. **rcard14.jpg — 豐盛 Abundance**
    Prompt: A tree with roots deep in glowing earth and branches reaching into a glowing sky, warm full-bodied light connecting both. Harmony between physical enjoyment and inner depth.

---

## 卡背 Card Back（back.jpg）

Prompt: An elegant symmetrical mandala-like pattern in deep indigo and gold, softly glowing at the center, no text, no figure — abstract and mysterious. Same Art Direction style as above, aspect ratio 2:3.
