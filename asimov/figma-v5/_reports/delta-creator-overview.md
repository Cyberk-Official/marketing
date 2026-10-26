# CSS Measurement Gate — creator-overview (default)
Story: features-creator-ui-creator-overview--default
Spec: figma/components/creator-overview/states/default.spec.json
Date: 2026-04-24T07:43:16.770Z

## Result: ❌ FAIL (2 issues)

## ❌ CSS Failures
- `align-self`: actual=`auto` expected=`stretch`

## ⚠️ Nested-Overflow
Child content overflows the declared root bbox. Fix: widen the component wrapper OR reduce child intrinsic width. Do NOT `overflow: hidden` over this — it hides the real bug.
- `nested_overflow_x: <img.relative.size-6> child box right=1067 exceeds parent content-box right=1059 by 8.0px`

## 📐 Text Node Drift Check
Spec: 13 text nodes, 8 labeled via `data-figma-id` (5 unlabeled — opt-in by adding `data-figma-id="<id>"` on risky nodes)

### ✅ Text Nodes Passing (8 labeled)
- "Overview" `501:14540` — y=0.0px, line-height=14.2px
- "3" `501:14545` — y=74.2px, line-height=24px
- "$500,000" `501:14550` — y=74.2px, line-height=24px
- "$10,000" `501:14560` — y=74.2px, line-height=24px
- "$10,000" `501:14565` — y=74.2px, line-height=24px
- "Claim all" `501:14568` — y=63.7px, line-height=17px
- "10,000" `611:13822` — y=74.2px, line-height=24px
- "Claim all" `611:13825` — y=63.7px, line-height=17px

## ✅ CSS Passing
- `padding-top`: `0px`
- `padding-right`: `0px`
- `padding-bottom`: `0px`
- `padding-left`: `0px`
- `gap`: `12px`
- `display`: `flex`
- `flex-direction`: `column`
- `width`: `1128px`
- `height`: `118.203px`
- `position`: `absolute`