# Layout hints — gradual-sell-table (default)

Scope: extracted from cache `498-14082/`, filtered to node `498:14082`
Source: Figma MCP design_context (reference only — see spec.json for authoritative CSS)
Sanitized: 12 raw color value(s) replaced with `[STRIPPED]`
⚠️  7 `src={imgX}` reference(s) unresolved — no matching IMAGE paint with assetUrl in spec.subNodes. Render a neutral placeholder and check spec.subNodes manually.

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
<div className="bg-[var(--dark-2)] content-stretch flex flex-col gap-[24px] items-start p-[18px] relative size-full" data-node-id="498:14082" data-name="section">
      <div className="content-stretch flex flex-col gap-[8px] items-start relative shrink-0 w-full" data-node-id="498:14083" data-name="title">
        <p className="font-['Nord:Regular',sans-serif] leading-[14.2px] not-italic relative shrink-0 text-[14px] text-[color:var(--white,white)] tracking-[0.84px] whitespace-nowrap" data-node-id="498:14084">
          Gradual sell strategy
        </p>
        <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] min-w-full relative shrink-0 text-[14px] text-[color:var(--grey-1)] w-[min-content]" data-node-id="498:14085" style={{ fontVariationSettings: "'wdth' 100" }}>
          Reduce market impact by selling as a liquidity provider.
        </p>
        <div className="absolute content-stretch flex gap-[8px] items-center justify-center right-[0.5px] top-0" data-node-id="498:14086" data-name="button">
          <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-[color:var(--blue)] whitespace-nowrap" data-node-id="498:14087" style={{ fontVariationSettings: "'wdth' 100" }}>
            History
          </p>
          <Restore className="overflow-clip relative shrink-0 size-[20px]" />
        </div>
      </div>
      <div className="content-stretch flex flex-col gap-[4px] items-start relative shrink-0 w-full" data-node-id="498:14089" data-name="table">
        <div className="bg-[STRIPPED] content-stretch flex items-start relative shrink-0 w-full" data-node-id="498:14090" data-name="row">
          <div className="content-stretch flex h-[44px] items-center px-[12px] py-[10px] relative shrink-0 w-[458px]" data-node-id="498:14091" data-name="col">
            <p className="font-['Nord:Regular',sans-serif] leading-[14.2px] not-italic relative shrink-0 text-[12px] text-[color:var(--grey-2)] tracking-[0.72px] whitespace-nowrap" data-node-id="498:14092">
              Price range
            </p>
          </div>
          <div className="content-stretch flex h-[44px] items-center px-[16px] py-[10px] relative shrink-0 w-[206px]" data-node-id="498:14093" data-name="col">
            <p className="font-['Nord:Regular',sans-serif] leading-[14.2px] not-italic relative shrink-0 text-[12px] text-[color:var(--grey-2)] tracking-[0.72px] whitespace-nowrap" data-node-id="498:14094">
              SELL Amount
            </p>
          </div>
          <div className="content-stretch flex gap-[4px] h-[44px] items-center px-[16px] py-[10px] relative shrink-0 w-[142px]" data-node-id="498:14095" data-name="col">
            <p className="font-['Nord:Regular',sans-serif] leading-[14.2px] not-italic relative shrink-0 text-[12px] text-[color:var(--grey-2)] tracking-[0.72px] whitespace-nowrap" data-node-id="498:14096">
              Remaining
            </p>
            <div className="relative shrink-0 size-[16px]" data-node-id="498:14097" data-name="Frame">
              <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgFrame} />
            </div>
          </div>
          <div className="content-stretch flex h-[44px] items-center justify-end px-[16px] py-[10px] relative shrink-0 w-[286px]" data-node-id="498:14099" data-name="col">
            <p className="font-['Nord:Regular',sans-serif] leading-[14.2px] not-italic relative shrink-0 text-[12px] text-[color:var(--grey-2)] tracking-[0.72px] whitespace-nowrap" data-node-id="498:14100">
              Action
            </p>
          </div>
        </div>
        <div className="bg-[STRIPPED] content-stretch flex h-[48px] items-center py-[4px] relative shrink-0 w-full" data-node-id="498:14101" data-name="row">
          <div className="content-stretch flex gap-[6px] items-center p-[12px] relative shrink-0 w-[458px]" data-node-id="498:14102" data-name="col">
            <div className="relative shrink-0 size-[16px]" data-node-id="498:14103" data-name="Frame">
              <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgFrame} />
            </div>
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white whitespace-nowrap" data-node-id="498:14105" style={{ fontVariationSettings: "'wdth' 100" }}>
              3601.345 - 3601.345
            </p>
          </div>
          <div className="content-stretch flex items-center px-[16px] py-[12px] relative shrink-0 w-[207px]" data-node-id="498:14106" data-name="col">
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white whitespace-nowrap" data-node-id="498:14107" style={{ fontVariationSettings: "'wdth' 100" }}>
              45.30K
            </p>
          </div>
          <div className="content-stretch flex items-center px-[16px] py-[12px] relative shrink-0 w-[146px]" data-node-id="498:14108" data-name="col">
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white whitespace-nowrap" data-node-id="498:14109" style={{ fontVariationSettings: "'wdth' 100" }}>
              30.1K
            </p>
          </div>
          <div className="content-stretch flex flex-[1_0_0] gap-[8px] items-center justify-end min-w-px px-[16px] py-[8px] relative rounded-[4px]" data-node-id="498:14110" data-name="button">
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white whitespace-nowrap" data-node-id="498:14111" style={{ fontVariationSettings: "'wdth' 100" }}>
              Remove LP
            </p>
            <div className="flex h-[19.221px] items-center justify-center relative shrink-0 w-0">
              <div className="flex-none rotate-90">
                <div className="h-0 relative w-[19.221px]" data-node-id="498:14112">
                  <div className="absolute inset-[-1px_0_0_0]">
                    <img alt="" className="block max-w-none size-full" src={imgLine872} />
                  </div>
                </div>
              </div>
            </div>
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white whitespace-nowrap" data-node-id="498:14113" style={{ fontVariationSettings: "'wdth' 100" }}>
              Claim USD
            </p>
          </div>
        </div>
        <div className="bg-[STRIPPED] content-stretch flex h-[48px] items-center py-[4px] relative shrink-0 w-full" data-node-id="498:14114" data-name="row">
          <div className="content-stretch flex gap-[6px] items-center p-[12px] relative shrink-0 w-[458px]" data-node-id="498:14115" data-name="col">
            <div className="relative shrink-0 size-[16px]" data-node-id="498:14116" data-name="Frame">
              <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgFrame} />
            </div>
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white whitespace-nowrap" data-node-id="498:14118" style={{ fontVariationSettings: "'wdth' 100" }}>
              3601.345 - 3601.345
            </p>
          </div>
          <div className="content-stretch flex items-center px-[16px] py-[12px] relative shrink-0 w-[207px]" data-node-id="498:14119" data-name="col">
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white whitespace-nowrap" data-node-id="498:14120" style={{ fontVariationSettings: "'wdth' 100" }}>
              45.30K
            </p>
          </div>
          <div className="content-stretch flex items-center px-[16px] py-[12px] relative shrink-0 w-[146px]" data-node-id="498:14121" data-name="col">
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white whitespace-nowrap" data-node-id="498:14122" style={{ fontVariationSettings: "'wdth' 100" }}>
              30.1K
            </p>
          </div>
          <div className="content-stretch flex flex-[1_0_0] gap-[8px] items-center justify-end min-w-px px-[16px] py-[8px] relative rounded-[4px]" data-node-id="498:14123" data-name="button">
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white whitespace-nowrap" data-node-id="498:14124" style={{ fontVariationSettings: "'wdth' 100" }}>
              Remove LP
            </p>
            <div className="flex h-[19.221px] items-center justify-center relative shrink-0 w-0">
              <div className="flex-none rotate-90">
                <div className="h-0 relative w-[19.221px]" data-node-id="498:14125">
                  <div className="absolute inset-[-1px_0_0_0]">
                    <img alt="" className="block max-w-none size-full" src={imgLine872} />
                  </div>
                </div>
              </div>
            </div>
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white whitespace-nowrap" data-node-id="498:14126" style={{ fontVariationSettings: "'wdth' 100" }}>
              Claim USD
            </p>
          </div>
        </div>
        <div className="bg-[STRIPPED] content-stretch flex h-[48px] items-center py-[4px] relative shrink-0 w-full" data-node-id="498:14127" data-name="row">
          <div className="content-stretch flex gap-[6px] items-center p-[12px] relative shrink-0 w-[458px]" data-node-id="498:14128" data-name="col">
            <div className="relative shrink-0 size-[16px]" data-node-id="498:14129" data-name="Frame">
              <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgFrame} />
            </div>
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white whitespace-nowrap" data-node-id="498:14131" style={{ fontVariationSettings: "'wdth' 100" }}>
              3601.345 - 3601.345
            </p>
          </div>
          <div className="content-stretch flex items-center px-[16px] py-[12px] relative shrink-0 w-[207px]" data-node-id="498:14132" data-name="col">
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white whitespace-nowrap" data-node-id="498:14133" style={{ fontVariationSettings: "'wdth' 100" }}>
              45.30K
            </p>
          </div>
          <div className="content-stretch flex items-center px-[16px] py-[12px] relative shrink-0 w-[146px]" data-node-id="498:14134" data-name="col">
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white whitespace-nowrap" data-node-id="498:14135" style={{ fontVariationSettings: "'wdth' 100" }}>
              30.1K
            </p>
          </div>
          <div className="content-stretch flex flex-[1_0_0] gap-[8px] items-center justify-end min-w-px px-[16px] py-[8px] relative rounded-[4px]" data-node-id="498:14136" data-name="button">
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white whitespace-nowrap" data-node-id="498:14137" style={{ fontVariationSettings: "'wdth' 100" }}>
              Remove LP
            </p>
            <div className="flex h-[19.221px] items-center justify-center relative shrink-0 w-0">
              <div className="flex-none rotate-90">
                <div className="h-0 relative w-[19.221px]" data-node-id="498:14138">
                  <div className="absolute inset-[-1px_0_0_0]">
                    <img alt="" className="block max-w-none size-full" src={imgLine872} />
                  </div>
                </div>
              </div>
            </div>
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-white whitespace-nowrap" data-node-id="498:14139" style={{ fontVariationSettings: "'wdth' 100" }}>
              Claim USD
            </p>
          </div>
        </div>
      </div>
      <div className="content-stretch flex gap-[8px] items-center justify-center relative shrink-0" data-node-id="498:14140" data-name="button">
        <Add className="overflow-clip relative shrink-0 size-[24px]" />
        <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-[color:var(--blue)] whitespace-nowrap" data-node-id="498:14142" style={{ fontVariationSettings: "'wdth' 100" }}>
          Add Sell Token
        </p>
      </div>
    </div>
```
