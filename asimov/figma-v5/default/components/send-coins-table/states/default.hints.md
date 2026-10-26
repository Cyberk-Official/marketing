# Layout hints — send-coins-table (default)

Scope: extracted from cache `498-14016/`, filtered to node `498:14016`
Source: Figma MCP design_context (reference only — see spec.json for authoritative CSS)
Sanitized: 21 raw color value(s) replaced with `[STRIPPED]`
⚠️  6 `src={imgX}` reference(s) unresolved — no matching IMAGE paint with assetUrl in spec.subNodes. Render a neutral placeholder and check spec.subNodes manually.

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
<div className="bg-[var(--dark-2)] content-stretch flex flex-col gap-[24px] items-start p-[18px] relative size-full" data-node-id="498:14016" data-name="section">
      <div className="content-stretch flex flex-col gap-[8px] items-start relative shrink-0 text-[14px] w-full" data-node-id="498:14017" data-name="title">
        <p className="font-['Nord:Regular',sans-serif] leading-[14.2px] not-italic relative shrink-0 text-[color:var(--white,white)] tracking-[0.84px] whitespace-nowrap" data-node-id="498:14018">
          Send Coins
        </p>
        <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] min-w-full relative shrink-0 text-[color:var(--grey-1)] w-[min-content]" data-node-id="498:14019" style={{ fontVariationSettings: "'wdth' 100" }}>
          Send token to other with the option to lock them and release overtime
        </p>
      </div>
      <div className="content-stretch flex flex-col gap-[4px] items-start relative shrink-0 w-full" data-node-id="498:14020" data-name="table">
        <div className="bg-[STRIPPED] content-stretch flex items-start relative shrink-0 w-full" data-node-id="498:14021" data-name="row">
          <div className="content-stretch flex items-center px-[16px] py-[10px] relative shrink-0 w-[245px]" data-node-id="498:14022" data-name="col">
            <p className="font-['Nord:Regular',sans-serif] leading-[14.2px] not-italic relative shrink-0 text-[12px] text-[color:var(--grey-2)] tracking-[0.72px] whitespace-nowrap" data-node-id="498:14023">
              Address
            </p>
          </div>
          <div className="content-stretch flex gap-[10px] items-center px-[16px] py-[10px] relative shrink-0 w-[204px]" data-node-id="498:14024" data-name="col">
            <p className="font-['Nord:Regular',sans-serif] leading-[14.2px] not-italic relative shrink-0 text-[12px] text-[color:var(--grey-2)] tracking-[0.72px] whitespace-nowrap" data-node-id="498:14025">
              TOTAL Amount
            </p>
            <div className="relative shrink-0 size-[16px]" data-node-id="498:14026" data-name="Frame">
              <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgFrame} />
            </div>
          </div>
          <div className="content-stretch flex gap-[4px] items-center px-[16px] py-[10px] relative shrink-0 w-[141px]" data-node-id="498:14028" data-name="col">
            <p className="font-['Nord:Regular',sans-serif] leading-[14.2px] not-italic relative shrink-0 text-[12px] text-[color:var(--grey-2)] tracking-[0.72px] whitespace-nowrap" data-node-id="498:14029">
              Length
            </p>
            <div className="relative shrink-0 size-[16px]" data-node-id="498:14030" data-name="Frame">
              <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgFrame} />
            </div>
          </div>
          <div className="content-stretch flex gap-[4px] items-center px-[16px] py-[10px] relative shrink-0 w-[141px]" data-node-id="501:14159" data-name="col">
            <p className="font-['Nord:Regular',sans-serif] leading-[14.2px] not-italic relative shrink-0 text-[12px] text-[color:var(--grey-2)] tracking-[0.72px] whitespace-nowrap" data-node-id="501:14160">
              Start date
            </p>
            <div className="relative shrink-0 size-[16px]" data-node-id="501:14161" data-name="Frame">
              <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgFrame} />
            </div>
          </div>
          <div className="content-stretch flex flex-[1_0_0] items-center min-w-px px-[16px] py-[10px] relative" data-node-id="498:14032" data-name="col">
            <p className="font-['Nord:Regular',sans-serif] leading-[14.2px] not-italic relative shrink-0 text-[12px] text-[color:var(--grey-2)] tracking-[0.72px] whitespace-nowrap" data-node-id="498:14033">
              Claim PROGRESS
            </p>
          </div>
        </div>
        <div className="bg-[STRIPPED] content-stretch flex h-[48px] items-center py-[4px] relative shrink-0 w-full" data-node-id="498:14034" data-name="row">
          <div className="content-stretch flex gap-[6px] items-center px-[16px] py-[12px] relative shrink-0 w-[243px]" data-node-id="498:14035" data-name="col">
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white whitespace-nowrap" data-node-id="498:14036" style={{ fontVariationSettings: "'wdth' 100" }}>
              0x49a7Ed1794b61...567
            </p>
            <div className="overflow-clip relative shrink-0 size-[16px]" data-node-id="498:14037" data-name="copy-01">
              <div className="absolute inset-[8.33%]" data-node-id="498:14038" data-name="elements">
                <div className="absolute inset-[-3.75%]">
                  <img alt="" className="block max-w-none size-full" src={imgElements} />
                </div>
              </div>
            </div>
          </div>
          <div className="content-stretch flex items-center px-[16px] py-[12px] relative shrink-0 w-[204px]" data-node-id="498:14041" data-name="col">
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white whitespace-nowrap" data-node-id="498:14042" style={{ fontVariationSettings: "'wdth' 100" }}>
              45.30K
            </p>
          </div>
          <div className="content-stretch flex items-center px-[16px] py-[12px] relative shrink-0 w-[141px]" data-node-id="498:14043" data-name="col">
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white whitespace-nowrap" data-node-id="498:14044" style={{ fontVariationSettings: "'wdth' 100" }}>
              6 months
            </p>
          </div>
          <div className="content-stretch flex items-center px-[16px] py-[12px] relative shrink-0 w-[141px]" data-node-id="501:14164" data-name="col">
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white whitespace-nowrap" data-node-id="501:14165" style={{ fontVariationSettings: "'wdth' 100" }}>
              12-12-2025
            </p>
          </div>
          <div className="content-stretch flex flex-[1_0_0] gap-[10px] items-center min-w-px px-[16px] py-[12px] relative" data-node-id="498:14045" data-name="col">
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white whitespace-nowrap" data-node-id="501:14153" style={{ fontVariationSettings: "'wdth' 100" }}>
              45.30K
            </p>
            <div className="bg-[STRIPPED] content-stretch flex flex-[1_0_0] flex-col h-[10px] items-start min-w-px relative" data-node-id="498:14047" data-name="progress">
              <div className="bg-gradient-to-r from-[STRIPPED] h-[10px] shrink-0 to-[STRIPPED] w-full" data-node-id="498:14048" />
            </div>
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white whitespace-nowrap" data-node-id="498:14046" style={{ fontVariationSettings: "'wdth' 100" }}>
              50%
            </p>
          </div>
        </div>
        <div className="bg-[STRIPPED] content-stretch flex h-[48px] items-center py-[4px] relative shrink-0 w-full" data-node-id="498:14049" data-name="row">
          <div className="content-stretch flex gap-[6px] items-center px-[16px] py-[12px] relative shrink-0 w-[243px]" data-node-id="498:14050" data-name="col">
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white whitespace-nowrap" data-node-id="498:14051" style={{ fontVariationSettings: "'wdth' 100" }}>
              0x49a7Ed1794b61...567
            </p>
            <div className="overflow-clip relative shrink-0 size-[16px]" data-node-id="498:14052" data-name="copy-01">
              <div className="absolute inset-[8.33%]" data-node-id="498:14053" data-name="elements">
                <div className="absolute inset-[-3.75%]">
                  <img alt="" className="block max-w-none size-full" src={imgElements} />
                </div>
              </div>
            </div>
          </div>
          <div className="content-stretch flex items-center px-[16px] py-[12px] relative shrink-0 w-[204px]" data-node-id="498:14056" data-name="col">
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white whitespace-nowrap" data-node-id="498:14057" style={{ fontVariationSettings: "'wdth' 100" }}>
              45.30K
            </p>
          </div>
          <div className="content-stretch flex items-center px-[16px] py-[12px] relative shrink-0 w-[141px]" data-node-id="498:14058" data-name="col">
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white whitespace-nowrap" data-node-id="498:14059" style={{ fontVariationSettings: "'wdth' 100" }}>
              6 months
            </p>
          </div>
          <div className="content-stretch flex items-center px-[16px] py-[12px] relative shrink-0 w-[141px]" data-node-id="501:14167" data-name="col">
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white whitespace-nowrap" data-node-id="501:14168" style={{ fontVariationSettings: "'wdth' 100" }}>
              12-12-2025
            </p>
          </div>
          <div className="content-stretch flex flex-[1_0_0] gap-[10px] items-center min-w-px px-[16px] py-[12px] relative" data-node-id="498:14060" data-name="col">
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white whitespace-nowrap" data-node-id="501:14155" style={{ fontVariationSettings: "'wdth' 100" }}>
              45.30K
            </p>
            <div className="bg-[STRIPPED] content-stretch flex flex-[1_0_0] flex-col h-[10px] items-start min-w-px relative" data-node-id="498:14062" data-name="progress">
              <div className="bg-gradient-to-r from-[STRIPPED] h-[10px] shrink-0 to-[STRIPPED] w-[55px]" data-node-id="498:14063" />
            </div>
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white whitespace-nowrap" data-node-id="498:14061" style={{ fontVariationSettings: "'wdth' 100" }}>
              50%
            </p>
          </div>
        </div>
        <div className="bg-[STRIPPED] content-stretch flex h-[48px] items-center py-[4px] relative shrink-0 w-full" data-node-id="498:14064" data-name="row">
          <div className="content-stretch flex gap-[6px] items-center p-[16px] relative shrink-0 w-[243px]" data-node-id="498:14065" data-name="col">
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white whitespace-nowrap" data-node-id="498:14066" style={{ fontVariationSettings: "'wdth' 100" }}>
              0x49a7Ed1794b61...567
            </p>
            <div className="overflow-clip relative shrink-0 size-[16px]" data-node-id="498:14067" data-name="copy-01">
              <div className="absolute inset-[8.33%]" data-node-id="498:14068" data-name="elements">
                <div className="absolute inset-[-3.75%]">
                  <img alt="" className="block max-w-none size-full" src={imgElements} />
                </div>
              </div>
            </div>
          </div>
          <div className="content-stretch flex items-center p-[16px] relative shrink-0 w-[204px]" data-node-id="498:14071" data-name="col">
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white whitespace-nowrap" data-node-id="498:14072" style={{ fontVariationSettings: "'wdth' 100" }}>
              45.30K
            </p>
          </div>
          <div className="content-stretch flex items-center p-[16px] relative shrink-0 w-[141px]" data-node-id="498:14073" data-name="col">
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white whitespace-nowrap" data-node-id="498:14074" style={{ fontVariationSettings: "'wdth' 100" }}>
              6 months
            </p>
          </div>
          <div className="content-stretch flex items-center px-[16px] py-[12px] relative shrink-0 w-[141px]" data-node-id="501:14170" data-name="col">
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white whitespace-nowrap" data-node-id="501:14171" style={{ fontVariationSettings: "'wdth' 100" }}>
              12-12-2025
            </p>
          </div>
          <div className="content-stretch flex flex-[1_0_0] gap-[10px] items-center min-w-px p-[16px] relative" data-node-id="498:14075" data-name="col">
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white whitespace-nowrap" data-node-id="501:14157" style={{ fontVariationSettings: "'wdth' 100" }}>
              45.30K
            </p>
            <div className="bg-[STRIPPED] content-stretch flex flex-[1_0_0] flex-col h-[10px] items-start min-w-px relative" data-node-id="498:14077" data-name="progress">
              <div className="bg-gradient-to-r from-[STRIPPED] h-[10px] shrink-0 to-[STRIPPED] w-full" data-node-id="498:14078" />
            </div>
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white whitespace-nowrap" data-node-id="498:14076" style={{ fontVariationSettings: "'wdth' 100" }}>
              50%
            </p>
          </div>
        </div>
      </div>
      <div className="content-stretch flex gap-[8px] items-center justify-center relative shrink-0" data-node-id="498:14079" data-name="button">
        <Add className="overflow-clip relative shrink-0 size-[24px]" />
        <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-[color:var(--blue)] whitespace-nowrap" data-node-id="498:14081" style={{ fontVariationSettings: "'wdth' 100" }}>
          Add Recipient Address
        </p>
      </div>
    </div>
```
