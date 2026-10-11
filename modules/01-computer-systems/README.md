# Module 01 — Computer Systems

## Purpose
Understand what a computer *is*, from bits and logic gates up to a CPU executing instructions —
the bedrock mental model for everything above it.

## Prerequisites
Module 00.

## Topics
Bits/bytes, binary, hex, two's complement, floating point, char encodings · boolean algebra,
logic gates, transistors (conceptually) · combinational & sequential circuits, adders, flip-flops,
registers, clock cycles · ALU, control unit, CPU · memory hierarchy, cache, RAM, storage · ISA,
machine code, assembly · fetch-decode-execute, interrupts, I/O, buses · stack/heap, virtual
memory, system calls (preview).

## Learning outcomes
- Convert between bases and do two's-complement arithmetic by hand.
- Build a gate-level adder and explain how a CPU runs one instruction.
- Trace a value from binary through the hardware stack to output.

## Exercises
- Binary/hex conversions (by hand, then in code).
- Truth tables → gates → half/full adder.
- Trace the fetch-decode-execute cycle for a toy instruction.

## Projects
#1 number-system converter · #2 logic-gate simulator · #3 tiny CPU/ISA emulator.

## Exit criteria
Working mini-emulator running a small program; can explain each layer.

## Connections
← [00](../00-learning-how-to-learn/) · → [02](../02-programming/) (languages that drive the
machine). See [`../../CONCEPT_MAP.md`](../../CONCEPT_MAP.md) (hardware spine). Phase detail:
[phase-01](../../curriculum/phases/phase-01-computer-systems.md).
