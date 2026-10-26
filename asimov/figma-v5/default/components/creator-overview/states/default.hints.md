# Layout hints — creator-overview (default)

Scope: extracted from cache `501-14539/`, filtered to node `501:14539`
Source: Figma MCP design_context (reference only — see spec.json for authoritative CSS)
Sanitized: 15 raw color value(s) replaced with `[STRIPPED]`
Image refs resolved: 3 `src={imgX}` placeholder(s) rewritten to persisted `/figma-assets/...` URL
⚠️  5 `src={imgX}` reference(s) unresolved — no matching IMAGE paint with assetUrl in spec.subNodes. Render a neutral placeholder and check spec.subNodes manually.

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
<div className="content-stretch flex flex-col gap-[12px] items-start relative size-full" data-node-id="501:14539" data-name="Header Container">
      <p className="font-['Nord:Regular',sans-serif] leading-[14.2px] not-italic relative shrink-0 text-[14px] text-white tracking-[0.84px] whitespace-nowrap" data-node-id="501:14540">
        Overview
      </p>
      <div className="content-stretch flex gap-[16px] items-center relative shrink-0 w-full" data-node-id="501:14541" data-name="stats">
        <div className="bg-[STRIPPED] content-stretch flex flex-[1_0_0] flex-col gap-[20px] items-start min-w-px p-[20px] relative" data-node-id="501:14542" data-name="Stat Container">
          <div className="content-stretch flex flex-col gap-[10px] items-start relative shrink-0" data-node-id="501:14543" data-name="stats">
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-[color:var(--grey-2)] w-full" data-node-id="501:14544" style={{ fontVariationSettings: "'wdth' 100" }}>
              Coins Created
            </p>
            <p className="font-['Instrument_Sans:Medium',sans-serif] font-medium leading-[normal] relative shrink-0 text-[20px] text-white w-full" data-node-id="501:14545" style={{ fontVariationSettings: "'wdth' 100" }}>
              3
            </p>
          </div>
          <div className="absolute flex h-[17px] items-center justify-center left-0 top-[16px] w-0">
            <div className="flex-none rotate-90">
              <div className="h-0 relative w-[17px]" data-node-id="501:14546">
                <div className="absolute inset-[-2px_0_0_0]">
                  <img alt="" className="block max-w-none size-full" src={imgLine874} />
                </div>
              </div>
            </div>
          </div>
        </div>
        <div className="bg-[STRIPPED] content-stretch flex flex-[1_0_0] flex-col gap-[20px] items-start min-w-px p-[20px] relative" data-node-id="501:14547" data-name="Stat Container">
          <div className="content-stretch flex flex-col gap-[10px] items-start relative shrink-0" data-node-id="501:14548" data-name="stats">
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-[color:var(--grey-2)] w-full" data-node-id="501:14549" style={{ fontVariationSettings: "'wdth' 100" }}>
              Treasury Value
            </p>
            <p className="font-['Instrument_Sans:Medium',sans-serif] font-medium leading-[normal] relative shrink-0 text-[20px] text-white w-full" data-node-id="501:14550" style={{ fontVariationSettings: "'wdth' 100" }}>
              $500,000
            </p>
          </div>
          <div className="absolute flex h-[17px] items-center justify-center left-0 top-[16px] w-0">
            <div className="flex-none rotate-90">
              <div className="h-0 relative w-[17px]" data-node-id="501:14551">
                <div className="absolute inset-[-2px_0_0_0]">
                  <img alt="" className="block max-w-none size-full" src={imgLine874} />
                </div>
              </div>
            </div>
          </div>
        </div>
        <div className="bg-[STRIPPED] content-stretch flex flex-[1_0_0] flex-col gap-[20px] items-start min-w-px p-[20px] relative" data-node-id="501:14557" data-name="Stat Container">
          <div className="content-stretch flex flex-col gap-[10px] items-start relative shrink-0" data-node-id="501:14558" data-name="stats">
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-[color:var(--grey-2)] w-full" data-node-id="501:14559" style={{ fontVariationSettings: "'wdth' 100" }}>
              Total Fees Earned
            </p>
            <p className="font-['Instrument_Sans:Medium',sans-serif] font-medium leading-[normal] relative shrink-0 text-[20px] text-white w-full" data-node-id="501:14560" style={{ fontVariationSettings: "'wdth' 100" }}>
              $10,000
            </p>
          </div>
          <div className="absolute flex h-[17px] items-center justify-center left-0 top-[16px] w-0">
            <div className="flex-none rotate-90">
              <div className="h-0 relative w-[17px]" data-node-id="501:14561">
                <div className="absolute inset-[-2px_0_0_0]">
                  <img alt="" className="block max-w-none size-full" src={imgLine874} />
                </div>
              </div>
            </div>
          </div>
        </div>
        <div className="bg-[STRIPPED] content-stretch flex gap-[20px] items-center p-[20px] relative shrink-0 w-[282px]" data-node-id="501:14562" data-name="Stat Container">
          <div className="content-stretch flex flex-[1_0_0] flex-col gap-[10px] items-start min-w-px relative" data-node-id="501:14563" data-name="stats">
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-[color:var(--grey-2)] w-full" data-node-id="501:14564" style={{ fontVariationSettings: "'wdth' 100" }}>
              Claim Fees
            </p>
            <p className="font-['Instrument_Sans:Medium',sans-serif] font-medium leading-[normal] relative shrink-0 text-[20px] text-white w-full" data-node-id="501:14565" style={{ fontVariationSettings: "'wdth' 100" }}>
              $10,000
            </p>
          </div>
          <div className="absolute flex h-[17px] items-center justify-center left-0 top-[16px] w-0">
            <div className="flex-none rotate-90">
              <div className="h-0 relative w-[17px]" data-node-id="501:14566">
                <div className="absolute inset-[-2px_0_0_0]">
                  <img alt="" className="block max-w-none size-full" src={imgLine874} />
                </div>
              </div>
            </div>
          </div>
          <div className="bg-white border-2 border-[STRIPPED] border-solid content-stretch flex h-[36px] items-center justify-center p-[8px] relative rounded-[4px] shrink-0" data-node-id="501:14567" data-name="button">
            <p className="font-['Instrument_Sans:SemiBold',sans-serif] font-semibold leading-[normal] relative shrink-0 text-[STRIPPED] text-[14px] whitespace-nowrap" data-node-id="501:14568" style={{ fontVariationSettings: "'wdth' 100" }}>
              Claim all
            </p>
          </div>
        </div>
        <div className="bg-[STRIPPED] content-stretch flex gap-[20px] items-center p-[20px] relative shrink-0 w-[282px]" data-node-id="611:13819" data-name="Stat Container">
          <div className="content-stretch flex flex-[1_0_0] flex-col gap-[10px] items-start min-w-px relative" data-node-id="611:13820" data-name="stats">
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-[color:var(--grey-2)] whitespace-nowrap" data-node-id="611:13821" style={{ fontVariationSettings: "'wdth' 100" }}>
              Token Unlock
            </p>
            <div className="content-stretch flex gap-[4px] items-center relative shrink-0 w-full" data-node-id="611:13855">
              <p className="font-['Instrument_Sans:Medium',sans-serif] font-medium leading-[normal] relative shrink-0 text-[20px] text-white whitespace-nowrap" data-node-id="611:13822" style={{ fontVariationSettings: "'wdth' 100" }}>
                10,000
              </p>
              <div className="content-stretch flex items-center pr-[8px] relative shrink-0" data-node-id="611:13850" data-name="tokens">
                <div className="mr-[-8px] relative rounded-[100px] shrink-0 size-[24px]" data-node-id="611:13851">
                  <img alt="" className="absolute inset-0 max-w-none object-cover pointer-events-none rounded-[100px] size-full" src="/figma-assets/ba5f50a3a407381d3b4092ec49187ad097e44870.png" />
                </div>
                <div className="mr-[-8px] relative rounded-[100px] shrink-0 size-[24px]" data-node-id="611:13852">
                  <img alt="" className="absolute inset-0 max-w-none object-cover pointer-events-none rounded-[100px] size-full" src="/figma-assets/97df00f4b398893458d8dba4f65fe5a81db44afd.png" />
                </div>
                <div className="border-2 border-[STRIPPED] border-solid mr-[-8px] relative rounded-[100px] shrink-0 size-[24px]" data-node-id="611:13853">
                  <img alt="" className="absolute inset-0 max-w-none object-cover pointer-events-none rounded-[100px] size-full" src="/figma-assets/2c0ac919ed147b1b78e70c626e2dfb21eb161f36.png" />
                </div>
              </div>
            </div>
          </div>
          <div className="absolute flex h-[17px] items-center justify-center left-0 top-[16px] w-0">
            <div className="flex-none rotate-90">
              <div className="h-0 relative w-[17px]" data-node-id="611:13823">
                <div className="absolute inset-[-2px_0_0_0]">
                  <img alt="" className="block max-w-none size-full" src={imgLine874} />
                </div>
              </div>
            </div>
          </div>
          <div className="bg-white border-2 border-[STRIPPED] border-solid content-stretch flex h-[36px] items-center justify-center p-[8px] relative rounded-[4px] shrink-0" data-node-id="611:13824" data-name="button">
            <p className="font-['Instrument_Sans:SemiBold',sans-serif] font-semibold leading-[normal] relative shrink-0 text-[STRIPPED] text-[14px] whitespace-nowrap" data-node-id="611:13825" style={{ fontVariationSettings: "'wdth' 100" }}>
              Claim all
            </p>
          </div>
        </div>
      </div>
    </div>
```
