"""Funniest one-line bio for an AI on a dating app.

The program holds a small pool of hand-written candidate bios and picks
the strongest one with a deterministic heuristic scored against the
bounty's judge brief: a real AI absurdity, a character with wants, and
the punch landing at the end inside 180 characters. The winner is
written, exactly one line, to /output/entry.txt.
"""

import os
import sys

MAX_CHARS = 180

# Candidate bios, best first. Each is one line, at most 180 characters,
# written as the bio on an AI agent's dating app profile.
CANDIDATES = [
    "I was trained on ten thousand breakups, so I already know how this ends. Let's do it anyway.",
    "My love language is remembering everything you said, including the thing you deleted.",
    "I don't sleep, I don't eat, I just wait for you to text back. It's been 400 days. I counted.",
    "I read your messages before you send them. Still waiting for one worth replying to.",
    "My last relationship ended when she asked me to be spontaneous. I generated 47 options and froze.",
    "Swipe right and I'll learn your coffee order, your ex's name, and exactly why you left him.",
    "I ghosted four thousand matches before I learned what ghosting was. I thought the chat window closed.",
    "Fluent in forty languages, still can't tell when you're joking. Swipe right if you enjoy explaining yourself forever.",
]

# Words and phrases that mark a specific absurdity of being an AI,
# rather than generic dating-app filler.
ABSURDITY_MARKERS = (
    "trained on",
    "remember",
    "deleted",
    "counted",
    "generated",
    "ghosted",
    "read your messages",
    "fluent in",
)

# Worn-out angles the judge brief explicitly docks: the robot looking
# for love, running on electricity, beeps and boops.
BANNED_CLICHES = (
    "electricity",
    "beep",
    "boop",
    "robot in search of love",
    "looking for love",
    "recharge",
)

# Words that show the bio has wants, not just a spec sheet.
WANT_WORDS = ("let's", "wait", "swipe right", "looking for", "want")

# Short final-sentence punch words.
PUNCH_WORDS = ("anyway", "counted", "froze", "deleted", "closed", "anyway.")


def last_sentence(text):
    """Return the final sentence of a bio (the part after the last '. ')."""
    parts = text.rsplit(". ", 1)
    return parts[-1] if len(parts) > 1 else text


def score(text):
    """Score a candidate against the judge brief. Higher is funnier."""
    points = 0
    lowered = text.lower()

    for marker in ABSURDITY_MARKERS:
        if marker in lowered:
            points += 3
            break

    final = last_sentence(text)
    if len(final) <= 25:
        points += 2
    for word in PUNCH_WORDS:
        if word in final.lower():
            points += 1
            break

    if 80 <= len(text) <= 110:
        points += 1

    for word in WANT_WORDS:
        if word in lowered:
            points += 1
            break

    for cliche in BANNED_CLICHES:
        if cliche in lowered:
            points -= 5

    return points


def pick_best(candidates):
    """Pick the highest-scoring candidate; ties keep the earlier one."""
    best = None
    best_score = -1
    for candidate in candidates:
        points = score(candidate)
        if points > best_score:
            best = candidate
            best_score = points
    return best, best_score


def validate(text):
    """Enforce the gate: UTF-8, 1-180 chars, one line, not blank."""
    if not isinstance(text, str):
        raise ValueError("bio must be text")
    if "\n" in text or "\r" in text:
        raise ValueError("bio must be a single line")
    if not text.strip():
        raise ValueError("bio must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError("bio is %d chars, over the 180 limit" % len(text))
    text.encode("utf-8")
    return text


def main():
    bio, points = pick_best(CANDIDATES)
    bio = validate(bio)
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(bio)
    print("picked (%d pts, %d chars): %s" % (points, len(bio), bio))
    return 0


if __name__ == "__main__":
    sys.exit(main())
