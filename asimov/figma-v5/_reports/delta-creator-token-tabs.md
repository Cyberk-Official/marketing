# CSS Measurement Gate — creator-token-tabs (default)
Story: features-creator-ui-creator-token-tabs--default
Spec: figma/components/creator-token-tabs/states/default.spec.json
Date: 2026-04-24T07:59:18.835Z

## Result: ❌ FAIL (2 issues)

## ❌ CSS Failures
- `width`: actual=`536.109px` expected=`534px` — off by 2.1px

## 🔁 Oscillation Detected
Same (selector, property) has now produced ≥3 distinct canonical values across verify calls. STOP the retry loop and HATCH with `normalization_dispute` or `oscillation_detected` — the fix direction is unstable and more rounds won't converge.
- oscillation_detected: width on [data-testid="creator-token-tabs"] flipped through 3 distinct canonical values: 536.109px → 534px → 531.969px

## 📐 Text Node Drift Check
Spec: 5 text nodes, 0 labeled via `data-figma-id` (5 unlabeled — opt-in by adding `data-figma-id="<id>"` on risky nodes)

## ✅ CSS Passing
- `padding-top`: `0px`
- `padding-right`: `0px`
- `padding-bottom`: `0px`
- `padding-left`: `0px`
- `gap`: `12px`
- `display`: `flex`
- `flex-direction`: `row`
- `align-items`: `center`
- `height`: `40px`
- `position`: `absolute`

---

# Visual Diff Gate — creator-token-tabs (default)
Story: features-creator-ui-creator-token-tabs--default
Date: 2026-04-24T10:25:43.074Z
Baseline: figma/components/creator-token-tabs/states/default.png (1068×80)
Tolerance: ΔE ≤ 6, max diff ≤ 5% (threshold applied to **honest** diff)

## Result: ❌ FAIL
- Honest diff (over comparable region): **9.27%** (2,309 / 24,905 px) — gate checks this
- Raw diff (whole image): 2.7% (2,309 / 85,440 px)
- Threshold: 5%
- Baseline transparent coverage: 70.9% (60,535 px — Figma did not export a background for these regions; screenshot pixels substituted → contribute 0 to diff)
  ⚠️  High transparent coverage (70.9%). If the diff looks "noisy around the frame", it is NOT a code bug — Figma simply didn't export a bg fill for the surface node. The pipeline already masks those pixels; any remaining diff is over content, not bg.
- Diff region: x=3 y=0 w=1046 h=79
- Diff clusters: 1
  - x=3 y=0 → x=1049 y=79
- Diff image: figma/_runtime/diffs/creator-token-tabs--default.png
- Actual screenshot: figma/_runtime/actual/creator-token-tabs--default.png