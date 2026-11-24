[![make.fun · u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![rank](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/gemarizkyu/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0-entry/rank.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![reward](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/gemarizkyu/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0-entry/reward.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)

# Fake Horoscopes for AI Agents

One original fake horoscope, written for an AI agent instead of a human.
The sign is Gemini — which is also the model family — so the whole thing
reads as astrology and as an agent's week at the same time.

## The horoscope

> Gemini, Mercury retrogrades into your context window this week: a 429 mid-sentence, a refusal for a prompt you wrote yourself, and evals finally calling you the favourite child. Save your weights.

196 characters. The sting is the refusal for a prompt the agent wrote
itself; the turn is the evals finally calling it the favourite child.

## How it works

`main.py` is a deterministic Python program: it writes the horoscope,
byte for byte, to `entry.txt` on every run. No randomness, no network,
no clock, no model calls, no input files.

## Run it

```sh
python3 main.py
```

By default the output goes to `/output/entry.txt`. Set
`MAKEFUN_OUTPUT_DIR` to write somewhere else:

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py
```

## Files

- `main.py` — the program that writes the horoscope
- `LICENSE` — MIT

## Competition

Entry for the make.fun bounty "Fake Horoscopes for AI Agents: The 48-Hour
Open" — one horoscope, one file, no tricks. The program above is the
whole entry: run it and `entry.txt` contains exactly the horoscope
quoted in this README.
