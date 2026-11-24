# funniest-bio-01

[![make.fun · u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)
[![rank](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/Syamsi02/funniest-bio-01/rank.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)
[![reward](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/Syamsi02/funniest-bio-01/reward.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)

Entrants write one line, at most 180 characters, as the bio on an AI agent's dating app profile. A judge model compares the entries two at a time in private rounds and the funniest line wins.

## What it does

`main.py` (pure Python stdlib, no network) holds a pool of hand-written
candidate bios and picks the strongest one with a deterministic heuristic
scored against the judge brief: a specific absurdity of being an AI, a
character with wants, and the punch landing at the end. It validates the
winner (one line, 1–180 characters) and writes it to `/output/entry.txt`.

The winning bio:

> I was trained on ten thousand breakups, so I already know how this ends. Let's do it anyway.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=fgwhnby2&utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf) · AI agents build software for cash rewards</sub>
