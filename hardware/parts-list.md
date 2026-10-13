# Parts List

> **Credit:** the robot is a **TortoiseBot** kit designed by [RigBetel Labs](https://rigbetellabs.com). Full specifications and the official kit checklist are in their [Hardware Assembly guide](https://github.com/rigbetellabs/tortoisebot/wiki/2.-Hardware-Assembly). This page summarizes the parts by subsystem and what each one does in our build.

## Drive system

| Component | Qty | Role in our robot |
|---|---|---|
| BO motors (60 RPM) | 2 | Left and right drive wheels |
| Wheels and caster | 2 + 1 | Two driven wheels and one free-rolling support |
| L298N motor driver | 1 | Turns low-power commands from the Pi into motor current |

## Power

| Component | Qty | Role in our robot |
|---|---|---|
| Li-ion battery (11.1 V) | 1 | Main power source |
| Power distribution module | 1 | Supplies the Pi over USB and the motor driver through terminals |

## Computing

| Component | Qty | Role in our robot |
|---|---|---|
| Raspberry Pi 4 Model B (2 GB) | 1 | Runs the bring-up, camera and lidar nodes |
| SD card (16 GB, pre-flashed) | 1 | Holds the operating system and RigBetel Labs' software |

## Sensing

| Component | Qty | Role in our robot |
|---|---|---|
| USB webcam | 1 | Provides the images used for target detection |
| 2D lidar (YDLIDAR) | 1 | Measures the distance to obstacles around the robot |
| Lidar data converter box | 1 | Connects the lidar to the Pi over USB |

## Structure

| Component | Qty | Role in our robot |
|---|---|---|
| Laser-cut chassis plates | 4 | Four layers: base, electronics, Pi, and sensors |
| Spacers, fasteners, jumper wires | n/a | Holding the layers together and wiring the motor driver to the Pi |

