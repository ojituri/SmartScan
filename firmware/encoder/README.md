# SmartScan Encoder Data Acquisition

## Purpose

This module provides the software interface for acquiring wheel encoder
data for the SmartScan mobile robot.

## Current Implementation

The current implementation provides a software encoder interface and
simulated pulse input for development and testing.

It supports:

- Left encoder pulse counting
- Right encoder pulse counting
- Encoder count reading
- Encoder count reset
- Input validation
- Automated software testing

## Commands

The test interface supports:

- `LEFT <pulses>`
- `RIGHT <pulses>`
- `READ`
- `RESET`
- `EXIT`

## Hardware Status

Physical encoder hardware is currently unavailable.

Therefore, real encoder signal acquisition has not yet been validated.

The current implementation is designed so that a hardware-specific
encoder input layer can be added later without changing the higher-level
encoder interface.

## Software Test Status

| Test | Status |
|---|---|
| Initial encoder counts | PASS |
| Left encoder counting | PASS |
| Right encoder counting | PASS |
| Left/right counting | PASS |
| Count accumulation | PASS |
| Count reset | PASS |
| Invalid input handling | PASS |

## Physical Validation

| Test | Status |
|---|---|
| Real left encoder signal | Pending hardware |
| Real right encoder signal | Pending hardware |
| Encoder signal during wheel rotation | Pending hardware |
