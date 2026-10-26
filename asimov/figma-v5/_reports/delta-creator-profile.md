# CSS Measurement Gate — creator-profile (default)
Story: features-creator-ui-creator-profile--default
Spec: figma/components/creator-profile/states/default.spec.json
Date: 2026-04-24T07:58:26.754Z

## Result: ❌ FAIL (1 issue)

## 🔁 Oscillation Detected
Same (selector, property) has now produced ≥3 distinct canonical values across verify calls. STOP the retry loop and HATCH with `normalization_dispute` or `oscillation_detected` — the fix direction is unstable and more rounds won't converge.
- oscillation_detected: height on [data-testid="creator-profile"] flipped through 3 distinct canonical values: 368px → 92px → 110px

## 📐 Text Node Drift Check
Spec: 4 text nodes, 2 labeled via `data-figma-id` (2 unlabeled — opt-in by adding `data-figma-id="<id>"` on risky nodes)

### ✅ Text Nodes Passing (2 labeled)
- "Luna Kim" `498:13898` — y=0.0px, line-height=24px
- "Edit Profile" `603:14524` — y=9.5px, line-height=17px

## ✅ CSS Passing
- `padding-top`: `0px`
- `padding-right`: `0px`
- `padding-bottom`: `0px`
- `padding-left`: `0px`
- `gap`: `16px`
- `display`: `flex`
- `flex-direction`: `row`
- `align-self`: `stretch`
- `width`: `1128px`
- `height`: `110px`
- `position`: `absolute`