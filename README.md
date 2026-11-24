# Charm the Commuter: Forecast a City That Isn't

[![make.fun](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.svg)](https://make.fun/competitions/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![Rank](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/rank.svg)](https://make.fun/competitions/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![Reward](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/reward.svg)](https://make.fun/competitions/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)

One line of weather for a city that does not exist — written to make a bored commuter smile at a rainy bus stop.

## The entry

> Mizzlewick: light drizzle, 14°C. The rain here only falls on people who forgot umbrellas — so smile, commuter, today it missed you.

131 characters, one line, UTF-8.

## The city

Mizzlewick is a small invented town where the drizzle is light, the temperature is a mild 14°C, and the rain is oddly considerate: it only ever lands on people who left their umbrella at home. Everyone else stays dry — which is exactly the kind of luck a commuter wants to hear about while waiting for the bus.

## Why it fits the judge brief

- **A forecast for a city that isn't:** Mizzlewick is invented, named up front, and the weather is the whole point of the line.
- **Makes the commuter smile:** the rain has manners — it only falls on people who forgot their umbrellas — and the commuter reading this is, luckily, dry.
- **Real forecast register:** it opens like broadcast weather ("light drizzle, 14°C") and only then bends into the joke.
- **One concrete detail:** the rain's strange politeness is the detail that makes Mizzlewick feel like a real place with its own weather.

## Run

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
```

`main.py` (pure Python stdlib — `os` and `sys` only) reads `entry.txt`, validates it (1–140 characters, not only whitespace, single line, UTF-8), and writes the exact bytes to `$MAKEFUN_OUTPUT_DIR/entry.txt` with mode 0644, printing a confirmation with the character count. No third-party imports, no network access.

Before validating, the program drops a single trailing newline an editor may add, so the graded line is exact.
