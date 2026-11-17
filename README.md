# tiny-chess-01

The strongest chess engine in 4 KB of Python — a make.fun entry.

`main.py` (4,094 bytes) is a self-contained chess engine: 0x88 board,
alpha-beta search with iterative deepening, a transposition table,
MVV-LVA + killer move ordering, quiescence search with check evasions,
and a material + piece-square-table evaluation (pawn/knight/bishop/king)
with a bishop-pair bonus. Fixed 40,000 nodes per move, deterministic
(no clock, no randomness), so every position always gives the same move.

It talks to the make.fun env at `MAKEFUN_ENV_URL` (`/game`, `/move`),
plays the house gauntlet, and was verified locally with perft
(startpos d4 = 197,281; Kiwipete d3 = 97,862) and practice trials.

## Usage

```
MAKEFUN_ENV_URL=http://127.0.0.1:18080 python3 main.py
```

## License

MIT — see `LICENSE`.
