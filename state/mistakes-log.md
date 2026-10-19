# Mistakes Log

> The most valuable file in the repo. Every important mistake becomes a future exercise. When a
> mental model fails, capture *why* — not just the fix.

## How to use
When you get something wrong (and it matters), add an entry. The agent should also add one when
it corrects a misconception during `TEACH`/`DEBUG`/`REVIEW`. Set a review date so the mistake
comes back as active recall.

## Entries
### Template
```
## YYYY-MM-DD — <topic>
- What I believed:
- Why it was incorrect:
- Correct mental model:
- Example:
- Prevention strategy:
- Review date:
```

---
## 2026-10-19 — Powers of 2 / byte range (off-by-one)
- What I believed: 2⁸ = 255, and that's the largest number a byte holds.
- Why it was incorrect: 2⁸ = **256** (the number of bit *patterns*). Those patterns represent
  values 0–255, so the largest *value* is 255 — but the power itself is 256.
- Correct mental model: N bits → 2ᴺ patterns → values `0 … (2ᴺ − 1)`. One pattern is spent on 0,
  which is why the max is one less than the count.
- Example: 8 bits → 256 patterns → 0…255 (max 255). 4 bits → 16 patterns → 0…15.
- Prevention strategy: whenever I see "how many" vs "the largest", pause — count of things vs
  largest index/value differ by 1. This is the classic off-by-one; it recurs in loops & arrays.
- Review date: 2026-10-24
