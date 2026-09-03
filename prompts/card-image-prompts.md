# 79 張卡圖生成提示詞

給 ChatGPT / Midjourney / Stable Diffusion 之類的圖像生成工具用，也可以直接用 `scripts/generate_cards.py` 自動批次生（見專案 README）。每張卡一個提示詞，對應現有的 `assets/cards/` 檔名，生完直接覆蓋同名檔案即可，網站不用改任何程式碼。

## 為什麼不是「照抄原圖」，也盡量不畫人形

保留每張牌的**核心意象與象徵**（花朵在石縫中開花＝勇氣、水面漂浮＝隨波逐流……這些是塔羅牌本身的通用視覺語言，不是特定畫家的獨創表達），但指定了一套跟原版奧修禪卡不同的畫風（見下方 Art Direction），概念忠於牌意、視覺是全新的原創插畫。

另外這版刻意把大部分「人形主角」改成物件、動物、植物、光影等抽象意象——測試時發現免費生圖模型（Pollinations）對冥想／水中人形這類主題常常會擅自畫成裸體，怎麼調提示詞都壓不住，所以乾脆從構圖上避開真人身體，只在少數幾張真的需要「人的存在感」時，用「遠景剪影、背光、看不清五官身體細節」的安全寫法（這種寫法實測沒問題）。

## Art Direction（每張都要套用，貼在每個 prompt 後面）

```
Style: symbolic spiritual illustration, digital painting with soft luminous gradients
and glowing light, dreamlike meditative mood, rich jewel-tone color palette, atmospheric
background (stars / mist / aura). The described subject must be clearly rendered and
easily recognizable as itself — show its actual identifying shape and details; do not
reduce it to a generic glowing circle, ring, orb, or featureless blob. If a human
presence appears, render it ONLY as a small distant silhouette with no visible facial
or body detail, or as an abstract light-being with no anatomy — never a close-up
realistic body, never bare skin. Family-friendly, SFW. Aspect ratio 2:3 portrait.
No text, no logo, no watermark, no border/frame.
Negative: nudity, nude, bare skin, sexual, suggestive, photorealistic skin, realistic
human anatomy, close-up body, generic empty glowing circle with no subject, featureless
blob, text, letters, numbers, watermark, signature, cluttered background, low quality,
blurry, extra limbs, frame, border
```

用法：把下面每張卡的 Prompt 那行，接上這段 Art Direction 一起丟給生圖工具。79 張共用同一套風格描述，這樣生出來的整副牌才會像同一個人畫的、風格統一。

---

## 主牌 Major Arcana（ccard1.jpg – ccard23.jpg）

深邃、宇宙感的珠寶色調（深藍、紫、金）為主基調，依每張牌主題微調。

1. **ccard1.jpg — 存在 Existence**
   Prompt: Abstract botanical illustration, no figure, no person, no human anatomy: a single glowing lotus-shaped flower made purely of starlight and soft mist petals, floating alone above a still dark cosmic ocean beneath a sky full of stars and a shooting comet. Deep indigo-to-violet gradient. Pure abstract light and floral form only, like a logo or icon.

2. **ccard2.jpg — 內在之聲 Inner Voice**
   Prompt: Two silver-blue dolphins leaping and circling gracefully around a large glowing white crescent moon, spiral splashes of water below them, star-filled night sky. Cool blue-white palette, quiet inner listening.

3. **ccard3.jpg — 創造力 Creativity**
   Prompt: A single glowing paintbrush, clearly visible with bristles and handle, mid-stroke, trailing vivid rainbow-colored ribbons of wet paint through the air in swirling curved shapes. Warm magenta-orange glow.

4. **ccard4.jpg — 叛逆者 The Rebel**
   Prompt: A single blazing torch standing upright on a wind-swept cliff edge at dusk, a broken chain lying beside it, flames whipping like a cloak in the wind. Fiery red-black palette.

5. **ccard5.jpg — 空無 No-Thingness**
   Prompt: A single tiny white feather, clearly visible with individual barbs, slowly dissolving into sparkling dust as it floats alone in a vast empty dark void. Deep black-violet gradient, spacious silence rather than emptiness.

6. **ccard6.jpg — 戀人 The Lovers**
   Prompt: Two glowing ribbons of light, one pink and one gold, weaving and intertwining together in the air until they form the clear recognizable shape of a heart. Soft pink-lavender palette, tender mutual connection.

7. **ccard7.jpg — 覺察 Awareness**
   Prompt: A wise owl with large round glowing eyes, perched perfectly still on a branch, watching calmly and alertly, soft light surrounding it. Teal-gold palette. No person.

8. **ccard8.jpg — 勇氣 Courage**
   Prompt: A small delicate flower blooming through a crack in grey stone, reaching toward a single shaft of golden light from above. Muted grey background, warm golden highlight.

9. **ccard9.jpg — 獨處 Aloneness**
   Prompt: A single lit candle standing alone at the center of a large dark round room, its flame the only light source, curved stone walls surrounding it in a circle. Deep blue-violet palette, self-contained and whole.

10. **ccard10.jpg — 變化 Change**
    Prompt: A great luminous wheel turning in space, a small steady point of light glowing at its center while the outer rim blurs with motion. Gold-orange-blue gradient.

11. **ccard11.jpg — 突破 Breakthrough**
    Prompt: Cracks of golden light bursting outward through a dark stone wall, energy radiating in dramatic beams. Deep purple-black background, brilliant golden fracture light.

12. **ccard12.jpg — 新視野 New Vision**
    Prompt: A single tree growing at a mountain summit, its upper branches reaching into bright sunrise light, its roots gripping rocky ground below. Balanced light-and-shadow composition.

13. **ccard13.jpg — 蛻變 Transformation**
    Prompt: A phoenix-like form made of falling ash and petals on one side, dissolving into luminous rising light and feathers on the other. Deep red-violet-gold palette.

14. **ccard14.jpg — 整合 Integration**
    Prompt: A glowing yin-yang symbol, one half made of golden light, one half made of silver light, swirling together in perfect balance. Clearly the classic yin-yang shape. Teal-rose gradient. No person.

15. **ccard15.jpg — 制約 Conditioning**
    Prompt: A lion-shaped figure standing among a flock of sheep, faint ghostly bars of an invisible cage around it, a hint of golden mane light breaking through. Muted earth tones.

16. **ccard16.jpg — 雷電 Thunderbolt**
    Prompt: A dramatic bolt of white-gold lightning striking and shattering a tall crumbling stone tower into fragments, stone debris flying outward, dark storm-blue sky. Sense of sudden necessary upheaval.

17. **ccard17.jpg — 寂靜 Silence**
    Prompt: A single pink lotus flower, clearly recognizable with visible petals, blooming perfectly still on dark calm water, faint ripple rings spreading outward around it in a vast quiet dark-blue space. No figure, no person.

18. **ccard18.jpg — 前世 Past Lives**
    Prompt: An old ornate hourglass filled with glowing sand, clearly detailed glass and wood frame, with faint translucent echoes of the same hourglass repeating and fading away behind it into the past. Sepia-violet palette. No person.

19. **ccard19.jpg — 純真 Innocence**
    Prompt: Abstract illustration, no figure, no person, no human anatomy: a cluster of simple daisy flowers and floating soap bubbles glowing in soft golden light, like a botanical icon. Warm pastel palette, open uncomplicated wonder.

20. **ccard20.jpg — 超越幻象 Beyond Illusion**
    Prompt: A kaleidoscope toy lying on a dark table, colorful fractured glass and mirror patterns clearly visible through its lens end. No people, no faces, just the object. Cool violet-silver palette.

21. **ccard21.jpg — 完成 Completion**
    Prompt: A single ripe pomegranate, split open, glowing jewel-like seeds clearly visible inside catching warm light, sitting alone on a dark surface. Warm amber-rose gradient. No person.

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
   Prompt: Many colorful prayer flags on a long string, fluttering together in a strong wind against a bright sky. No people. Warm collective energy.

5. **fcard5.jpg — 全然 Totality**
   Prompt: A small clothed silhouette of a person sitting cross-legged, floating and balanced perfectly still in mid-air, calm and focused, one hand holding a single glowing point of light steady before them. Dynamic warm-toned dusk sky.

6. **fcard6.jpg — 成功 Success**
   Prompt: A small silhouette of a person standing triumphantly on a mountain peak, both arms raised high in victory, golden confetti and ribbons swirling around them in celebration. Warm celebratory orange-gold palette.

7. **fcard7.jpg — 壓力 Stress**
   Prompt: A frantic cascade of many distinct circus juggling balls, rings, and flaming torches all tumbling in mid-air at once above a single spinning circus ball on the ground. Warm but chaotic reds and oranges, motion blur.

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
   Prompt: Close-up of two tree trunks growing side by side, bark texture clearly visible, their upper branches visibly touching overhead. Empty forest, absolutely no people anywhere in the frame. Cool green-blue palette.

3. **wcard3.jpg — 歡慶 Celebration**
   Prompt: Three small silhouettes of women dancing barefoot and joyfully in the rain among trees, arms raised, splashing through puddles, warm light scattering through raindrops. Lively blue-violet palette.

4. **wcard4.jpg — 內觀 Turning In**
   Prompt: A small distant silhouette of a person sitting cross-legged in meditation, wearing a simple full-length modest robe with a high neckline, faint translucent ripples of thought-forms drifting around them. The figure is small and far away, not a close-up portrait. Calm indigo palette.

5. **wcard5.jpg — 放不下 Clinging To The Past**
   Prompt: Abstract object illustration, no figure, no person: an ornate antique wooden treasure trunk with a curved lid, glowing faintly from within with old sepia-toned memories, rusty chains and padlocks wrapped tightly around it, like a product photo of an object. Cool grey-blue tones, weight of longing for what has passed.

6. **wcard6.jpg — 幻夢 The Dream**
   Prompt: A large iridescent soap bubble floating above still water, its curved surface clearly reflecting a tiny rainbow-colored castle floating inside it like a mirage. No people. Soft dreamy blue-violet mist.

7. **wcard7.jpg — 投射 Projections**
   Prompt: A pair of antique brass binoculars resting on a windowsill, each lens clearly reflecting a different colorful distorted scene. No people, no faces — just metal and glass. Ambiguous cool-toned mist.

8. **wcard8.jpg — 放手 Letting Go**
   Prompt: A single water droplet sliding off a lotus leaf into calm water, gentle expanding ripples fading into stillness. Soft blue-grey palette, quiet release.

9. **wcard9.jpg — 安逸 Laziness**
   Prompt: A fluffy cat lounging lazily and stretched out on a cushioned lounge chair, eyes half-closed in total contentment, unaware that the ornate mirror behind it is quietly cracked. No people. Cool blues with a subtle uneasy fracture of light.

10. **wcard10.jpg — 和諧 Harmony**
    Prompt: Abstract illustration, no figure, no person, no human anatomy: two dolphins made of soft light swimming in a gentle figure-eight/infinity loop around each other, like a minimalist logo. Cool aqua-violet palette, inner balance.

11. **wcard11.jpg — 理解 Understanding**
    Prompt: A bird flying freely past the loosely open bars of a cage, the bars rendered translucent and unlocked. Soft blue-white palette, realizing the limit was never solid.

12. **wcard12.jpg — 信任 Trust**
    Prompt: A small bird diving fearlessly off a cliff edge into open sky above calm water, wings folded back, trusting the fall completely. No figure, no person. Warm light breaking through cool blue tones.

13. **wcard13.jpg — 接納 Receptivity**
    Prompt: A pair of open cupped hands, disembodied and floating with no arms or body attached, gently holding a glowing blooming pink lotus flower between the palms. Soft starlight and water reflections around them. Cool blue-lavender palette.

14. **wcard14.jpg — 療癒 Healing**
    Prompt: A small distant silhouette of a person gently cradling a softly glowing bird against their chest, warm healing light flowing between them. Warm-cool blended blue-rose palette.

---

## 雲 Clouds / Air（ucard1.jpg – ucard14.jpg）

冷灰、藍紫、白，天空與心智意象。

1. **ucard1.jpg — 意識之光 Consciousness**
   Prompt: A meditating silhouette made entirely of stars and soft mist against a deep midnight-blue sky. Quiet luminous clarity emerging from stillness.

2. **ucard2.jpg — 拉鋸 Schizophrenia**
   Prompt: A close-up of an old brass compass with a spinning needle unable to settle, pointing wildly between two opposite directions, glowing dial markings clearly visible. No people, no body, just the compass object. Cool grey-violet palette.

3. **ucard3.jpg — 封凍 Ice-olation**
   Prompt: A single red rose completely encased inside a thick block of cracked, frosted ice, visible ice crystals covering the petals, a single drop of water frozen mid-fall beside it. Cool icy palette. No person.

4. **ucard4.jpg — 拖延 Postponement**
   Prompt: A window glowing with a vivid colorful landscape outside, while the room on this side stays dim and grey with fog. Vibrant possibility versus grey hesitation.

5. **ucard5.jpg — 比較 Comparison**
   Prompt: A rough gnarled old tree trunk standing directly next to a tall slender green bamboo stalk, both clearly visible growing side by side in a garden. No people, no animals. Muted green-brown palette.

6. **ucard6.jpg — 重擔 The Burden**
   Prompt: A small distant silhouette of a person bent forward under the weight of a huge overloaded backpack stacked high with boxes and sacks, struggling up a steep rocky mountain path. Muted grey-violet tones.

7. **ucard7.jpg — 心機 Politics**
   Prompt: Two ornate wooden masks mounted on wooden poles stuck into the ground, one carved with a smiling expression, one carved with a scowling expression, carved wood grain and paint clearly visible. No living faces. Cool grey-green palette.

8. **ucard8.jpg — 自責 Guilt**
   Prompt: A small distant silhouette of a person in a dark hooded cloak, fully covered, sitting hunched over with their head down in their hands, faint translucent ghostly hands reaching in from the darkness around them. The figure is small and far away, not a close-up portrait. Faint grey-violet tones.

9. **ucard9.jpg — 悲傷 Sorrow**
   Prompt: A small hooded silhouette sitting in quiet contemplation, head bowed, a single thin beam of soft light breaking through darkness behind them. Deep blue-grey palette.

10. **ucard10.jpg — 重生 Rebirth**
    Prompt: A small faceless child silhouette playing a flute, standing balanced on top of a sleeping lion, which itself lies resting on top of a camel — all three clearly stacked and visible — dawn light breaking behind them. Soft gold-blue gradient.

11. **ucard11.jpg — 紛亂之心 Mind**
    Prompt: A large human head silhouette entirely constructed out of visible clockwork gears, spinning dice, nuts, bolts and mechanical scrap metal fused together — a steampunk sculpture, not a real face or skin. Cool grey-metallic palette.

12. **ucard12.jpg — 備戰 Fighting**
    Prompt: A suit of heavy armor standing alone, fists clenched empty inside, a small vulnerable glow barely visible through a crack in the chestplate. Cool steel-blue palette.

13. **ucard13.jpg — 教條 Morality**
    Prompt: An empty rigid birdcage made of straight geometric metal bars, with several stiff formal shirt-collars stacked and hanging inside it like rungs. No person, no face inside. Muted grey-beige palette.

14. **ucard14.jpg — 掌控 Control**
    Prompt: A glowing orb surrounded by sharp radiating spikes of self-made light, tightly contained. Cool blue-white palette with an undertone of strain.

---

## 彩虹 Rainbow（rcard1.jpg – rcard14.jpg）

暖色調＋多彩，豐盛與大地意象。

1. **rcard1.jpg — 圓熟 Maturity**
   Prompt: A blossoming tree standing serenely in soft spring light, its roots glowing deep and visible beneath the earth. Warm golden-green palette, earned stability.

2. **rcard2.jpg — 當下 Moment To Moment**
   Prompt: A row of flat stepping stones crossing a shallow flowing stream, close-up, each stone catching warm multicolor light reflecting off the water, a splash of water on the nearest stone. No people.

3. **rcard3.jpg — 指引 Guidance**
   Prompt: A small luminous angel figure with large feathered rainbow-colored wings, clearly visible, hovering gently in the air beside a tiny glowing seed of light resting on the ground below. Warm prismatic glow.

4. **rcard4.jpg — 守財者 The Miser**
   Prompt: A large glowing heap of gold coins and colorful gemstones piled in a dark shadowy corner, with two bony hands gripping a fistful of coins tightly, refusing to let go. Cool shadow despite the wealth around them.

5. **rcard5.jpg — 局外人 The Outsider**
   Prompt: A small silhouette of a child standing before a tall gate believing it locked, while a chain lies loosely broken at their feet. Warm-cool contrast between imagined and real barriers.

6. **rcard6.jpg — 妥協 Compromise**
   Prompt: Two ornate wooden chess king pieces, faceless and abstract like real chess pieces, standing close together on a chessboard as if in a truce, each with a tiny hidden dagger tucked at its base. Warm candlelight. Muted warm-grey palette. No people, no faces.

7. **rcard7.jpg — 耐心 Patience**
   Prompt: A small silhouette of a pregnant woman sitting peacefully, hands resting on her belly, as eight phases of the moon arc gently overhead in the night sky. Soft warm amber-violet gradient.

8. **rcard8.jpg — 平凡 Ordinariness**
   Prompt: A small silhouette walking a simple country path carrying a basket of flowers, no audience. Warm soft earth-tone palette, quiet dignity in everyday simplicity.

9. **rcard9.jpg — 熟成 Ripeness**
   Prompt: A single fully ripe fruit hanging heavy and glowing on a branch, about to fall on its own without force. Warm golden-orange palette, readiness.

10. **rcard10.jpg — 世界一家 We Are The World**
    Prompt: Many small glowing figures of different colors, clearly distinct individuals, standing together in a large circle holding hands, forming an unbroken ring around a small glowing globe of the Earth at the center. Warm multicolor prismatic palette.

11. **rcard11.jpg — 冒險 Adventure**
    Prompt: A small silhouette standing at the edge of a misty forest facing a glowing, uncertain rainbow-colored light ahead, no map. Warm-cool contrast, quiet courage.

12. **rcard12.jpg — 放慢腳步 Slowing Down**
    Prompt: A large turtle, with clearly visible head, four legs and tail, carrying a glowing patterned shell on its back, walking slowly and calmly along a quiet forest path. Warm muted earth tones.

13. **rcard13.jpg — 綻放 Flowering**
    Prompt: A fully blooming lotus radiating warm multicolor light and floating petals outward in every direction. Uninhibited open joy.

14. **rcard14.jpg — 豐盛 Abundance**
    Prompt: A small silhouette of a person kneeling, one hand touching the glowing earth, the other hand reaching up into a glowing sky, connecting both. Warm full-bodied light. Harmony between physical and spiritual.

---

## 卡背 Card Back（back.jpg）

Prompt: An elegant symmetrical mandala-like pattern in deep indigo and gold, softly glowing at the center, no text, no figure — abstract and mysterious. Same Art Direction style as above, aspect ratio 2:3.
