# Region analysis — creator-token-tabs (state: default)
Generated: 2026-04-24T10:25:43.145Z

6 candidate(s) analyzed. 6 actionable verdict(s) surfaced; 0 AA_NOISE silenced; 0 low-signal STRUCTURAL kept (0 dropped).

Read **Top diff regions** in order. Fix the highest-confidence non-DYNAMIC issue first. DYNAMIC_ tag is **advisory** — flag indicates the region MAY reflect mock data / dynamic state (progress bars, lorem ipsum, generated values). Inspect baseline vs actual structure (font, padding, border, layout) before treating it as a bug.

## Top diff regions

### #1 COLOR_ONLY(ΔRGB=58) — MEDIUM confidence
- Region: TEXT "burger" — "burger" (id=498:13942)
- Bbox: (704,25,138,30)
- Density: exclusive=1230px / total=1230px (30%)
- Expected font: Nord Regular 14px
- Expected fill: #5e698b
- Reason: palette-level shift (ΔRGB=58); edgeSim=0.43 not required
- Raw signals: shift=(2,1) impr=37% | missing.edgeRatio=1.02 | ΔRGB=58 | edgeSim=0.43

### #2 COLOR_ONLY(ΔRGB=53) — MEDIUM confidence
- Region: TEXT "abcd" — "abcd" (id=498:13945)
- Bbox: (962,25,90,30)
- Density: exclusive=797px / total=797px (30%)
- Expected font: Nord Regular 14px
- Expected fill: #5e698b
- Reason: palette-level shift (ΔRGB=53); edgeSim=0.42 not required
- Raw signals: shift=(3,1) impr=40% | missing.edgeRatio=0.98 | ΔRGB=53 | edgeSim=0.42

### #3 COLOR_ONLY(ΔRGB=51) — MEDIUM confidence
- Region: TEXT "valor" — "valor" (id=498:13939)
- Bbox: (476,25,108,30)
- Density: exclusive=818px / total=818px (25%)
- Expected font: Nord Regular 14px
- Expected fill: #5e698b
- Reason: palette-level shift (ΔRGB=51); edgeSim=0.40 not required
- Raw signals: shift=(2,1) impr=40% | missing.edgeRatio=0.99 | ΔRGB=51 | edgeSim=0.40

### #4 MISSING — HIGH confidence
- Region: RECTANGLE "Rectangle 8" (id=498:13941)
- Bbox: (640,16,48,48)
- Density: exclusive=418px / total=418px (18%)
- Reason: baseline strong-edges=58% → actual 19% (ratio=0.33)
- Raw signals: shift=(12,0) impr=19% [bnd] | missing.edgeRatio=0.33 | ΔRGB=77 | edgeSim=0.34

### #5 WRONG_CONTENT — HIGH confidence
- Region: FRAME "tab" (id=498:13940)
- Bbox: (624,0,234,80)
- Density: exclusive=368px / total=2016px (11%)
- Reason: edges diverge (sim=0.38) at same position
- Raw signals: shift=(2,1) impr=17% | missing.edgeRatio=0.63 | ΔRGB=20 | edgeSim=0.38

### #6 SUBTLE_DRIFT(ΔRGB=16) — MEDIUM confidence
- Region: TEXT "AOLM" — "AOLM" (id=498:13936)
- Bbox: (270,25,86,30)
- Density: exclusive=110px / total=110px (4%)
- Expected font: Nord Regular 14px
- Expected fill: #ffffff
- Reason: small region (86×30) with subtle palette/edge drift
- Raw signals: shift=(1,1) impr=66% | missing.edgeRatio=1.04 | ΔRGB=16 | edgeSim=0.75
