# Layout hints — token-unlock-card (default)

Scope: extracted from cache `501-14570/`, filtered to node `501:14589`
Source: Figma MCP design_context (reference only — see spec.json for authoritative CSS)
Sanitized: 12 raw color value(s) replaced with `[STRIPPED]`
⚠️  1 `src={imgX}` reference(s) unresolved — no matching IMAGE paint with assetUrl in spec.subNodes. Render a neutral placeholder and check spec.subNodes manually.

## DO NOT TRUST from MCP code (use spec.json instead)

This JSX is a **layout scaffold reference**. The values below are unreliable;
use spec.json (or the Tokens block in your prompt) for the truth:

| MCP output | Why unreliable | Use instead |
|---|---|---|
| `bg-[STRIPPED]`, `text-[STRIPPED]` (plus fill/stroke/border/ring/shadow/outline) | Raw color replaced to prevent copy | Tokens from your prompt |
| `from-[STRIPPED]`, `to-[STRIPPED]`, `via-[STRIPPED]` | Gradient-stop raw colors — positions like `to-[98.02%]` are kept as-is | Tokens + the gradient spec from Figma / prompt |
| `leading-[normal]` / `leading-[x%]` | Wrong for INTRINSIC_% line-height | `leading-[<lineHeightPx>px]` from spec.textNodes |
| `<img src={imgX}>` | MCP placeholder var | Pipeline auto-rewrites to the persisted public URL (`/figma-assets/<hash>.ext`) when a matching IMAGE paint is resolved — trust the rewritten `src` below. Unresolved `src={imgX}` stays as-is; look the owning node up in `spec.subNodes` and pick its IMAGE fill manually. |
| Root dimensions in classes (`size-full`, `w-[Npx]`) | May be off-by-1 vs REST API | `spec.dimensions` (root only — descendant sizes stay from this scaffold) |
| `border` styles | Doesn't distinguish gradient strokes from solid | Check spec / Figma stroke type |

⚠️  This component has INTRINSIC_% text nodes. Pin line-heights with `leading-[Npx]` from spec.textNodes (do NOT use `leading-[normal]`).

## Scoped JSX reference

Use this only as a **structural scaffold** — copy the layout (flex, gap,
padding, grid), not the values. Replace anything flagged above.

```jsx
<div className="bg-[var(--dark-2)] content-stretch flex flex-[1_0_0] flex-col gap-[24px] items-start min-w-px p-[18px] relative" data-node-id="501:14589" data-name="section">
        <div className="content-stretch flex gap-[8px] items-start relative shrink-0 w-full" data-node-id="501:14590" data-name="title">
          <div className="content-stretch flex flex-[1_0_0] flex-col gap-[8px] items-start min-w-px relative text-[14px]" data-node-id="603:14544">
            <p className="font-['Nord:Regular',sans-serif] leading-[14.2px] not-italic relative shrink-0 text-[color:var(--white,white)] tracking-[0.84px] whitespace-nowrap" data-node-id="501:14591">
              TOKEN UNLOCK
            </p>
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] min-w-full relative shrink-0 text-[color:var(--grey-1)] w-[min-content]" data-node-id="501:14592" style={{ fontVariationSettings: "'wdth' 100" }}>
              View your token vesting schedule and claim unlocked tokens
            </p>
          </div>
          <div className="bg-[STRIPPED] content-stretch flex items-center justify-center p-[6px] relative rounded-[4px] shrink-0" data-node-id="603:14526" data-name="copy add">
            <div className="overflow-clip relative shrink-0 size-[18px]" data-node-id="603:14538" data-name="arrow-expand-01-sharp">
              <div className="absolute inset-[12.5%]" data-node-id="I603:14538;603:14532" data-name="elements">
                <div className="absolute inset-[-4.17%]">
                  <img alt="" className="block max-w-none size-full" src={imgElements} />
                </div>
              </div>
            </div>
          </div>
        </div>
        <div className="content-stretch flex flex-col gap-[16px] items-start relative shrink-0 w-full" data-node-id="501:14593" data-name="section">
          <div className="content-stretch flex gap-[24px] items-start relative shrink-0 w-full" data-node-id="501:14594">
            <div className="content-stretch flex flex-[1_0_0] flex-col gap-[10px] items-start min-w-px relative" data-node-id="501:14595" data-name="stats">
              <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-[color:var(--grey-2)] w-full" data-node-id="501:14596" style={{ fontVariationSettings: "'wdth' 100" }}>
                Total Amount
              </p>
              <div className="content-stretch flex gap-[8px] items-center relative shrink-0 w-full whitespace-nowrap" data-node-id="501:14597" data-name="Staked Value Container">
                <p className="font-['Instrument_Sans:Medium',sans-serif] font-medium leading-[normal] relative shrink-0 text-[16px] text-white" data-node-id="501:14598" style={{ fontVariationSettings: "'wdth' 100" }}>
                  300,000
                </p>
                <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-[color:var(--grey-1)]" data-node-id="501:14599" style={{ fontVariationSettings: "'wdth' 100" }}>
                  AOLM
                </p>
              </div>
            </div>
            <div className="content-stretch flex flex-[1_0_0] flex-col gap-[10px] items-start min-w-px relative" data-node-id="501:14601" data-name="stats">
              <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-[color:var(--grey-2)] w-full" data-node-id="501:14602" style={{ fontVariationSettings: "'wdth' 100" }}>
                Token Claimed
              </p>
              <div className="content-stretch flex gap-[8px] items-center relative shrink-0 w-full whitespace-nowrap" data-node-id="501:14603" data-name="Staked Value Container">
                <p className="font-['Instrument_Sans:Medium',sans-serif] font-medium leading-[normal] relative shrink-0 text-[16px] text-white" data-node-id="501:14604" style={{ fontVariationSettings: "'wdth' 100" }}>
                  300,000
                </p>
                <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-[color:var(--grey-1)]" data-node-id="501:14605" style={{ fontVariationSettings: "'wdth' 100" }}>
                  AOLM
                </p>
              </div>
            </div>
          </div>
          <div className="bg-[STRIPPED] content-stretch flex gap-[24px] items-center p-[16px] relative shrink-0 w-full" data-node-id="501:14607">
            <div className="content-stretch flex flex-[1_0_0] flex-col gap-[10px] items-start min-w-px relative" data-node-id="501:14608" data-name="stats">
              <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-[color:var(--grey-2)] w-full" data-node-id="501:14609" style={{ fontVariationSettings: "'wdth' 100" }}>
                Unlocked
              </p>
              <div className="content-stretch flex gap-[8px] items-center relative shrink-0 w-full whitespace-nowrap" data-node-id="501:14610" data-name="Staked Value Container">
                <p className="font-['Instrument_Sans:Medium',sans-serif] font-medium leading-[normal] relative shrink-0 text-[16px] text-white" data-node-id="501:14611" style={{ fontVariationSettings: "'wdth' 100" }}>
                  300,000
                </p>
                <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-[color:var(--grey-1)]" data-node-id="501:14612" style={{ fontVariationSettings: "'wdth' 100" }}>
                  AOLM
                </p>
              </div>
            </div>
            <div className="bg-white border-2 border-[STRIPPED] border-solid content-stretch flex h-[36px] items-center justify-center p-[8px] relative rounded-[4px] shrink-0" data-node-id="501:14614" data-name="button">
              <p className="font-['Instrument_Sans:SemiBold',sans-serif] font-semibold leading-[normal] relative shrink-0 text-[STRIPPED] text-[14px] whitespace-nowrap" data-node-id="501:14615" style={{ fontVariationSettings: "'wdth' 100" }}>
                Claim all
              </p>
            </div>
          </div>
        </div>
      </div>
```
