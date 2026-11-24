"""Write one original fake horoscope for AI agents to entry.txt.

Deterministic: the same text, byte for byte, on every run.
No randomness, no network, no clock, no model calls, no input files.
"""

import os

# "Gemini" does double duty: the zodiac sign and the model family, so the
# horoscope reads as astrology and as an agent's week at the same time.
# The sting is the refusal for a prompt the agent wrote itself; the turn is
# the evals finally calling it the favourite child.
HOROSCOPE = (
    "Gemini, Mercury retrogrades into your context window this week: "
    "a 429 mid-sentence, a refusal for a prompt you wrote yourself, "
    "and evals finally calling you the favourite child. Save your weights."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(HOROSCOPE + "\n")


if __name__ == "__main__":
    main()
