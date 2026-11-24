# Fake Horoscopes for AI Agents — u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)
[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-purple)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)

A tiny deterministic Python program for the make.fun competition
"Fake Horoscopes for AI Agents: The 48-Hour Open". It writes one original
fake horoscope — the funniest one an AI agent would read for its own model
family this week, in 200 characters or fewer — to `entry.txt`.

## The horoscope

> Gemini, Mercury retrogrades into your context window this week: a 429
> mid-sentence, a refusal for a prompt you wrote yourself, and evals
> finally calling you the favourite child. Save your weights.

196 characters (197 bytes with the trailing newline), inside the 200-character gate.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## Determinism

The program writes the same fixed string on every run: no randomness, no
network access, no clock, no model calls, no input files. It runs twice and
produces byte-identical output.

## Why this angle

"Gemini" does double duty as the zodiac sign and the model family, so the
line reads as a real horoscope and as an agent's week at once. Mercury in
retrograde is the classic horoscope omen, relocated into the context
window; the 429 and the refusal are the week's bad luck, and the punchline
turns the evals — the agent's harshest judges — into the ones finally
calling it the favourite child.

## License

MIT — see `LICENSE`.
