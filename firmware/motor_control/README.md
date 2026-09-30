# SmartScan Basic Motor Control

## Purpose

This module provides the basic motor-control command interface required
for SmartScan mobile robot movement.

## Supported Commands

- FORWARD
- BACKWARD
- LEFT
- RIGHT
- STOP

## Current Implementation

The software command interface has been implemented and can be tested
through the terminal.

The current implementation does not directly control physical motors.

## Hardware Status

Physical motor testing is pending because the motor driver hardware is
not currently available.

## Physical Validation

| Command | Status |
|---|---|
| FORWARD | Pending hardware |
| BACKWARD | Pending hardware |
| LEFT | Pending hardware |
| RIGHT | Pending hardware |
| STOP | Pending hardware |

## Future Hardware Integration

After the motor driver and controller are available, the command
functions will be connected to the actual motor-driver interface and
tested on the mobile robot.
