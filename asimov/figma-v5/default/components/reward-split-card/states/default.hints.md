# Layout hints — reward-split-card (default)

Scope: extracted from cache `501-14570/`, filtered to node `501:14616`
Source: Figma MCP design_context (reference only — see spec.json for authoritative CSS)
Sanitized: 8 raw color value(s) replaced with `[STRIPPED]`

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

## Scoped JSX reference

Use this only as a **structural scaffold** — copy the layout (flex, gap,
padding, grid), not the values. Replace anything flagged above.

```jsx
<div className="bg-[var(--dark-2)] content-stretch flex flex-[1_0_0] flex-col gap-[24px] h-full items-start min-w-px p-[18px] relative" data-node-id="501:14616" data-name="section">
        <div className="content-stretch flex flex-col gap-[8px] items-start relative shrink-0 text-[14px] w-full" data-node-id="501:14617" data-name="title">
          <p className="font-['Nord:Regular',sans-serif] leading-[14.2px] not-italic relative shrink-0 text-[color:var(--white,white)] tracking-[0.84px] whitespace-nowrap" data-node-id="501:14618">
            Reward Split
          </p>
          <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] min-w-full relative shrink-0 text-[color:var(--grey-1)] w-[min-content]" data-node-id="501:14619" style={{ fontVariationSettings: "'wdth' 100" }}>
            Change the wallet that receivers fees. Split rewards across up to 10 wallets.
          </p>
        </div>
        <div className="content-stretch flex flex-col gap-[12px] items-start relative shrink-0 w-full" data-node-id="501:14620" data-name="list">
          <div className="content-stretch flex font-['Instrument_Sans:Regular',sans-serif] font-normal items-start justify-between leading-[18px] relative shrink-0 text-[14px] text-white w-full whitespace-nowrap" data-node-id="501:14621" data-name="TITEL">
            <p className="relative shrink-0" data-node-id="501:14622" style={{ fontVariationSettings: "'wdth' 100" }}>
              Wallet List (3)
            </p>
            <p className="relative shrink-0" data-node-id="501:14623" style={{ fontVariationSettings: "'wdth' 100" }}>
              Add Wallet
            </p>
          </div>
          <div className="bg-[STRIPPED] content-stretch flex gap-[4px] items-start relative rounded-[8px] shrink-0 w-full" data-node-id="501:14624" data-name="wallet">
            <div className="border-[var(--dark-2)] border-r border-solid content-stretch flex items-center justify-center p-[16px] relative shrink-0" data-node-id="501:14625" data-name="%">
              <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white whitespace-nowrap" data-node-id="501:14626" style={{ fontVariationSettings: "'wdth' 100" }}>
                1
              </p>
            </div>
            <div className="content-stretch flex flex-[1_0_0] items-center min-w-px p-[16px] relative" data-node-id="501:14627" data-name="Wallet">
              <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white w-[310.142px]" data-node-id="501:14628" style={{ fontVariationSettings: "'wdth' 100" }}>
                0x49a7Ed1794b61...567
              </p>
            </div>
            <div className="border-[var(--dark-2)] border-l border-solid content-stretch flex items-center justify-center p-[16px] relative shrink-0" data-node-id="501:14629" data-name="%">
              <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white whitespace-nowrap" data-node-id="501:14630" style={{ fontVariationSettings: "'wdth' 100" }}>
                15%
              </p>
            </div>
          </div>
          <div className="bg-[STRIPPED] content-stretch flex gap-[4px] items-start relative rounded-[8px] shrink-0 w-full" data-node-id="501:14631" data-name="wallet">
            <div className="border-[var(--dark-2)] border-r border-solid content-stretch flex items-center justify-center p-[16px] relative shrink-0" data-node-id="501:14632" data-name="%">
              <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white whitespace-nowrap" data-node-id="501:14633" style={{ fontVariationSettings: "'wdth' 100" }}>
                2
              </p>
            </div>
            <div className="content-stretch flex flex-[1_0_0] items-center min-w-px p-[16px] relative" data-node-id="501:14634" data-name="Wallet">
              <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white w-[310.142px]" data-node-id="501:14635" style={{ fontVariationSettings: "'wdth' 100" }}>
                0x49a7Ed1794b68..567
              </p>
            </div>
            <div className="border-[var(--dark-2)] border-l border-solid content-stretch flex items-center justify-center p-[16px] relative shrink-0" data-node-id="501:14636" data-name="%">
              <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white whitespace-nowrap" data-node-id="501:14637" style={{ fontVariationSettings: "'wdth' 100" }}>
                15%
              </p>
            </div>
          </div>
        </div>
      </div>
```
