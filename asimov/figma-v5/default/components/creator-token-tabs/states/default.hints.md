# Layout hints — creator-token-tabs (default)

Scope: extracted from cache `498-13932/`, filtered to node `498:13932`
Source: Figma MCP design_context (reference only — see spec.json for authoritative CSS)
Sanitized: 5 raw color value(s) replaced with `[STRIPPED]`
Image refs resolved: 4 `src={imgX}` placeholder(s) rewritten to persisted `/figma-assets/...` URL

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
<div className="content-stretch flex gap-[12px] items-center relative size-full" data-node-id="498:13932" data-name="tabs">
      <p className="font-['Nord:Regular',sans-serif] leading-[14.2px] not-italic relative shrink-0 text-[14px] text-white tracking-[0.84px] whitespace-nowrap" data-node-id="498:13933">
        Created:
      </p>
      <div className="bg-[STRIPPED] content-stretch flex gap-[8px] items-center justify-center p-[8px] relative shrink-0" data-node-id="498:13934" data-name="tab">
        <div className="relative rounded-[100px] shrink-0 size-[24px]" data-node-id="498:13935">
          <img alt="" className="absolute inset-0 max-w-none object-cover pointer-events-none rounded-[100px] size-full" src="/figma-assets/97df00f4b398893458d8dba4f65fe5a81db44afd.png" />
        </div>
        <p className="font-['Nord:Regular',sans-serif] leading-[14.2px] not-italic relative shrink-0 text-[14px] text-white tracking-[0.84px] whitespace-nowrap" data-node-id="498:13936">
          AOLM
        </p>
      </div>
      <div className="content-stretch flex gap-[8px] items-center justify-center p-[8px] relative shrink-0" data-node-id="498:13937" data-name="tab">
        <div className="relative rounded-[100px] shrink-0 size-[24px]" data-node-id="498:13938">
          <img alt="" className="absolute inset-0 max-w-none object-cover pointer-events-none rounded-[100px] size-full" src="/figma-assets/ba5f50a3a407381d3b4092ec49187ad097e44870.png" />
        </div>
        <p className="font-['Nord:Regular',sans-serif] leading-[14.2px] not-italic relative shrink-0 text-[14px] text-[color:var(--grey-2)] tracking-[0.84px] whitespace-nowrap" data-node-id="498:13939">
          valor
        </p>
      </div>
      <div className="content-stretch flex gap-[8px] items-center justify-center p-[8px] relative rounded-[4px] shrink-0" data-node-id="498:13940" data-name="tab">
        <div className="border-2 border-[STRIPPED] border-solid relative rounded-[100px] shrink-0 size-[24px]" data-node-id="498:13941">
          <img alt="" className="absolute inset-0 max-w-none object-cover pointer-events-none rounded-[100px] size-full" src="/figma-assets/2c0ac919ed147b1b78e70c626e2dfb21eb161f36.png" />
        </div>
        <p className="font-['Nord:Regular',sans-serif] leading-[14.2px] not-italic relative shrink-0 text-[14px] text-[color:var(--grey-2)] tracking-[0.84px] whitespace-nowrap" data-node-id="498:13942">
          burger
        </p>
      </div>
      <div className="content-stretch flex gap-[8px] items-center justify-center p-[8px] relative shrink-0" data-node-id="498:13943" data-name="tab">
        <div className="relative rounded-[100px] shrink-0 size-[24px]" data-node-id="498:13944">
          <img alt="" className="absolute inset-0 max-w-none object-cover pointer-events-none rounded-[100px] size-full" src="/figma-assets/97df00f4b398893458d8dba4f65fe5a81db44afd.png" />
        </div>
        <p className="font-['Nord:Regular',sans-serif] leading-[14.2px] not-italic relative shrink-0 text-[14px] text-[color:var(--grey-2)] tracking-[0.84px] whitespace-nowrap" data-node-id="498:13945">
          abcd
        </p>
      </div>
    </div>
```
