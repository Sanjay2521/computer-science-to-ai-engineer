# Phase 1 — Computer Systems Foundations

**Timeline:** ~6–10 weeks · **Module:** [01-computer-systems](../../modules/01-computer-systems/)

## Goal
Understand what a computer *is*, from binary and gates up to a CPU executing instructions.

## Prerequisites
Phase 0.

## Topics & required depth
- **Numbers:** bits/bytes, binary, hexadecimal, unsigned & signed integers, two's complement,
  floating point (IEEE 754 conceptually), character encodings (ASCII, Unicode/UTF-8).
- **Logic:** boolean algebra; logic gates (AND/OR/NOT/NAND/NOR/XOR); transistors conceptually.
- **Circuits:** combinational (adders, multiplexers, decoders); sequential (flip-flops,
  registers, counters); clock cycles.
- **CPU:** ALU, control unit, datapath; memory hierarchy, cache, RAM, persistent storage;
  ISA, machine code, assembly; fetch-decode-execute; interrupts, I/O, buses.
- **Just enough OS preview:** stack/heap, virtual memory, system calls (full depth in Phase 4).

Depth: enough to *implement* a gate-level adder and a tiny instruction emulator and to *trace*
a value through the whole stack.

## Mathematics thread
Number bases; boolean algebra. (Vectors begin late in this phase as a bridge to Phase 3.)

## DSA thread
Complexity *intuition* only; no formal problems yet.

## Hands-on labs
Truth-table simulations; build a half/full adder from gates; model registers; a simulated
instruction cycle.

## From-scratch implementation
- Number-system converter (dec/bin/hex, signed).
- Logic-gate simulator (gates → adder).
- Tiny CPU / instruction-set emulator (small ISA, fetch-decode-execute loop).

## Mini-project
Logic-gate simulator computing binary addition.

## Major project
Project #3 — tiny CPU / instruction-set emulator.

## Recommended resources
Nand2Tetris (core); CS:APP (selective); CrashCourse CS. (See [`../../RESOURCES.md`](../../RESOURCES.md).)

## Assessment
Trace a value binary→gates→register→output; explain fetch-decode-execute; implement an adder
and run a program on your emulator.

## Exit criteria
- Convert between bases and do two's-complement arithmetic by hand.
- Build a gate-level adder; explain how a CPU runs one instruction.
- A working mini-emulator executing a small program.

## Common mistakes
- Treating floating point as exact (it isn't — connects to DL numerical issues later).
- Memorizing gate truth tables without building circuits.
- Skipping two's complement and getting signed-overflow bugs later.

## Connection to next phase
You understand the machine → learn the languages that drive it (Phase 2), starting with Python
and a taste of C.
