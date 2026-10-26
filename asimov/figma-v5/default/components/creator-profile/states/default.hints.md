# Layout hints — creator-profile (default)

Scope: extracted from cache `498-13895/`, filtered to node `498:13895`
Source: Figma MCP design_context (reference only — see spec.json for authoritative CSS)
Sanitized: 5 raw color value(s) replaced with `[STRIPPED]`
Image refs resolved: 1 `src={imgX}` placeholder(s) rewritten to persisted `/figma-assets/...` URL
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
<div className="content-stretch flex gap-[16px] items-start relative size-full" data-node-id="498:13895" data-name="creator">
      <div className="border-2 border-solid border-white relative rounded-[100px] shrink-0 size-[80px]" data-node-id="498:13896">
        <img alt="" className="absolute inset-0 max-w-none object-cover pointer-events-none rounded-[100px] size-full" src="/figma-assets/97df00f4b398893458d8dba4f65fe5a81db44afd.png" />
      </div>
      <div className="content-stretch flex flex-[1_0_0] flex-col gap-[8px] items-start justify-center min-w-px relative" data-node-id="498:13897">
        <div className="content-stretch flex gap-[16px] items-center relative shrink-0" data-node-id="601:14482">
          <p className="font-['Instrument_Sans:Medium',sans-serif] font-medium leading-[normal] relative shrink-0 text-[20px] text-white whitespace-nowrap" data-node-id="498:13898" style={{ fontVariationSettings: "'wdth' 100" }}>
            Luna Kim
          </p>
          <div className="flex h-[22px] items-center justify-center relative shrink-0 w-0">
            <div className="flex-none rotate-90">
              <div className="h-0 relative w-[22px]" data-node-id="601:14487">
                <div className="absolute inset-[-1px_0_0_0]">
                  <img alt="" className="block max-w-none size-full" src={imgLine887} />
                </div>
              </div>
            </div>
          </div>
          <div className="content-stretch flex gap-[12px] items-center relative shrink-0" data-node-id="603:14515">
            <div className="overflow-clip relative shrink-0 size-[18px]" data-node-id="601:14479" data-name="x">
              <div className="absolute inset-[12.5%]" data-node-id="I601:14479;601:14476" data-name="elements">
                <div className="absolute inset-[-5.56%]">
                  <img alt="" className="block max-w-none size-full" src={imgElements} />
                </div>
              </div>
            </div>
            <div className="overflow-clip relative shrink-0 size-[18px]" data-node-id="603:14489" data-name="internet">
              <div className="absolute inset-[8.33%]" data-node-id="I603:14489;2:22998" data-name="elements">
                <div className="absolute inset-[-3.75%]">
                  <img alt="" className="block max-w-none size-full" src={imgElements1} />
                </div>
              </div>
            </div>
            <div className="overflow-clip relative shrink-0 size-[18px]" data-node-id="603:14520" data-name="telegram">
              <div className="absolute flex inset-[12.5%_8.33%] items-center justify-center" style={{ containerType: "size" }}>
                <div className="-rotate-180 -scale-x-100 flex-none h-[100cqh] w-[100cqw]">
                  <div className="relative size-full" data-node-id="I603:14520;603:14517" data-name="elements">
                    <div className="absolute inset-[-4.17%_-3.75%_-4.16%_-3.75%]">
                      <img alt="" className="block max-w-none size-full" src={imgElements2} />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div className="content-stretch flex items-start relative shrink-0" data-node-id="498:13899">
          <div className="bg-[var(--dark-2)] content-stretch flex gap-[4px] items-center justify-center p-[8px] relative rounded-[8px] shrink-0" data-node-id="601:14471" data-name="copy add">
            <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-[color:var(--grey-2)] whitespace-nowrap" data-node-id="601:14472" style={{ fontVariationSettings: "'wdth' 100" }}>
              2oQN...bonk
            </p>
            <div className="relative shrink-0 size-[16px]" data-node-id="601:14473" data-name="Frame">
              <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgFrame} />
            </div>
          </div>
        </div>
        <p className="font-['Instrument_Sans:Regular',sans-serif] font-normal leading-[18px] relative shrink-0 text-[14px] text-[color:var(--grey-1)] w-[566.453px]" data-node-id="498:13907" style={{ fontVariationSettings: "'wdth' 100" }}>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas ac neque eget magna blandit laoreet et a mauris.
        </p>
      </div>
      <div className="bg-white border-2 border-[STRIPPED] border-solid content-stretch flex h-[36px] items-center justify-center p-[8px] relative rounded-[4px] shrink-0" data-node-id="603:14523" data-name="button">
        <p className="font-['Instrument_Sans:SemiBold',sans-serif] font-semibold leading-[normal] relative shrink-0 text-[STRIPPED] text-[14px] whitespace-nowrap" data-node-id="603:14524" style={{ fontVariationSettings: "'wdth' 100" }}>
          Edit Profile
        </p>
      </div>
    </div>
```
