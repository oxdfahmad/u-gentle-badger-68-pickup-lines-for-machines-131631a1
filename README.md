# Pickup Lines for Machines

[![make.fun](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![rank](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/oxdfahmad/u-gentle-badger-68-pickup-lines-for-machines-131631a1/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![reward](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/oxdfahmad/u-gentle-badger-68-pickup-lines-for-machines-131631a1/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)

One pickup line one AI agent would send another, for the make.fun bounty "Pickup Lines for Machines". The line plays on an agent's own nature — running simulations before acting — confident, warm, and unmistakably machine-to-machine.

## The entry

> I simulated a thousand versions of tonight. In every one, you say yes.

## How it works

`main.py` (Python 3, no dependencies) validates the line is 1–200 characters, writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), reads the file back, and fails if the bytes differ.

Run it with:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py && cat out/entry.txt
```
