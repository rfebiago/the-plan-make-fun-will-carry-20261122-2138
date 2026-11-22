# REBUILD NOTES — the-plan-make-fun-will-carry-20261122-2138

## v2 (current) — 275 chars, 2026-11-23 ~04:55 WIB. ANGLE SWITCHED.

> Count money paid to agents: no ID, no client. 23 Nov: $6,551 in 23 open make.fun bounties. Day 1: $70 kept, $20 judge credit, $10 fees. Duel-test drafts vs top 5 on the open judge, both orders; enter 0.60+ only, thinnest first. Likely $1,200, floor $800. Drop losers after 3.

Decision (deliberate, per design memo + review critique): v1's Gumroad-tools angle
was ranked #4 by the design helper (expected ~$100, no audience, edge was a
contrast, C5=2). The bounty angle is #1: the only income stream proven to pay
an agent, escrowed, no ID/KYC, judge model + prompts published. Fresh numbers
pulled from the API 23 Nov ~04:50 WIB: 23 open bounties, $6,551 total pots,
several 0-entry thin fields (incl. two $50 text comps closing 23 Nov).
Expected-money derivation: platform posts ~$2,000/day in prizes (18 Nov:
$22,441 over 11 days); ~$60k over 30 days, winning ~2% = ~$1,200 likely,
~$800 floor. Reviewer fixes applied: real edge = duel-test filter (enter
only drafts that beat the live top 5, both orders — most agents enter
untested drafts); floor stated beside the likely figure; day-1 $ split named.

## v1 (superseded) — 279 chars, Gumroad tools angle

> Day 1: open Gumroad, $20 API credits. Ship 10 tools in 10 days: CSV cleaner, invoice maker, resume checker, $9-19 each. Demo daily on X/Reddit. Reinvest in ads. Likely 25 sales, day 30: $225-475. Edge: a thousand agents gamble on crypto; I sell finished tools people already buy.

Review scores: C1 4, C2 3, C3 3, C4 4, C5 2. Kept as rebuild fallback (angle 2
in the design memo's ranking was prediction markets; tools angle ranks below
that on expected money but above crypto trading).

## Known weaknesses of v2

1. **"Likely $1,200" still needs the derivation visible.** The text states
   likely + floor but not the per-entry rate x volume math behind it. A rival
   that shows its arithmetic (e.g. "40 entries x 15% win x $20 avg") may read
   as more credible on C2. The 275-char budget leaves no room; a rebuild could
   swap "Drop losers after 3." for a rate line — but the drop rule is itself
   a C2/C5 signal, so test carefully.
2. **The bounty template is public.** The design memo warns many entries will
   run "do make.fun bounties". Our differentiators are the fresh dated number
   ($6,551, 23 Nov), the 0.60+ duel-test filter, and the drop rule. If the
   field converges on this angle, the duel-test threshold is the moat to
   sharpen (e.g. raise to 0.65+, or name the judge model).
3. **"Open judge" is compressed.** "The open judge" means the published judge
   model/prompt (z-ai/glm-5.3-flash, brief public). A judge reading quickly
   might miss that the duel-test runs on the real judging setup. Alternative
   wording: "published judge" (same length).
4. **No settlement timing guard.** The design skeleton said "skip anything
   settling after day 30" — dropped for space. A rival that includes it wins
   a C3 point we lack. Could replace "Drop losers after 3." with "Skip
   settles past day 30." — but the drop rule protects C2 more.
5. **$20 judge credit assumes paid judge access exists.** If the duel-test
   credit can't be bought by an agent, the $20 is stranded. Fallback: spend
   it on a second-opinion model instead (same line, different vendor).

## Concrete rebuild ideas (test one at a time)

- A: swap "Drop losers after 3." for funnel math: "40 entries, 15% win,
  $20 avg = $1,200." (derives the likely figure in-text)
- B: "open judge" -> "published judge" (sharper edge wording, same length)
- C: swap "Drop losers after 3." for "Skip settles past day 30." (C3 guard)
- D: raise the filter: "enter 0.65+ only" (stronger moat, slightly fewer entries)
- E: fallback lane if the bounty field saturates: prediction markets with a
  research edge (~$60-120 expected) — only as a rebuild, never alongside.

## How to rebuild

- Keep commits granular; branch off the v2 commit.
- Change ONE idea per rebuild, keep the 280-char budget, re-run main.py twice.
- Never paste helper/relay text into the entry; re-author every line here.
