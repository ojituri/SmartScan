# SmartScan Software Architecture

## 1. Overview

SmartScan is a low-cost autonomous/semi-autonomous mobile robotic system designed for indoor mapping and spatial scanning.

The software architecture integrates LiDAR sensing, wheel-encoder data, odometry, SLAM, navigation, obstacle response, visualization, and data storage using ROS 2 as the robotics middleware.

The architecture follows the approved SmartScan project methodology:

**LiDAR + Wheel Encoders → Sensor Data Acquisition → Odometry → SLAM Processing → Localization & Map Generation → Navigation / Obstacle Response → Map Visualization & Storage**

---

## 2. Technology Stack

| Area | Technology |
|---|---|
| Programming | Python, C++ |
| Robotics Middleware | ROS 2 |
| LiDAR / Sensor Processing | LiDAR driver, sensor-data processing |
| Localization / Mapping | SLAM, odometry |
| Embedded Control | Microcontroller, motor driver, encoder interface |
| Visualization | RViz / mapping visualization tools |
| Operating System | Linux |
| Development | VS Code |
| Version Control | Git, GitHub |

---

## 3. High-Level Architecture

The SmartScan software system is divided into the following functional layers:

1. Hardware and Sensor Layer
2. Sensor Data Acquisition Layer
3. Robot Motion and Odometry Layer
4. SLAM and Localization Layer
5. Navigation and Obstacle Response Layer
6. Visualization and Data Storage Layer

---

## 4. Hardware and Sensor Layer

The hardware layer provides the raw data required by the software.

### Components

- 360° LiDAR
- Wheel encoders
- Motors
- Motor driver
- Microcontroller
- Onboard computing unit

The LiDAR provides environmental distance measurements, while wheel encoders provide wheel-motion information.

---

## 5. Sensor Data Acquisition Layer

The sensor-data acquisition layer receives and processes data from the LiDAR and wheel encoders.

### LiDAR Processing

The LiDAR driver acquires 360° scan measurements and makes the scan data available to the ROS 2 software system.

### Encoder Processing

The encoder interface acquires wheel-rotation measurements from the robot.

The acquired data is passed to the odometry-processing layer.

---

## 6. Odometry Layer

The odometry layer uses wheel-encoder measurements to estimate the robot's motion.

The basic processing flow is:

**Wheel Encoder Data → Wheel Motion → Robot Motion Estimate → Odometry**

The odometry output is used together with LiDAR measurements by the SLAM system.

---

## 7. SLAM and Localization Layer

The SLAM layer combines LiDAR measurements and odometry to estimate robot position and generate an indoor map.

Processing flow:

**LiDAR Data + Odometry → SLAM Processing → Robot Localization + Indoor Map Generation**

The generated map represents the selected indoor test environment.

---

## 8. Navigation and Obstacle Response Layer

The navigation layer uses the available map and sensor information to support basic autonomous or semi-autonomous movement.

The obstacle-response function uses LiDAR-based environmental information to identify obstacles and support appropriate robot movement within the selected indoor test environment.

---

## 9. Visualization Layer

RViz / mapping visualization tools are used to visualize the robot's mapping and sensor-processing results.

The visualization layer can display:

- LiDAR scan information
- Robot position/localization
- Generated indoor map
- Mapping progress
- Navigation-related information where applicable

---

## 10. Data Storage Layer

The system stores generated maps and experimental results for later analysis and evaluation.

Stored results may include:

- Generated maps
- LiDAR scan data
- Wheel-encoder measurements
- Experimental measurements
- Mapping results
- Navigation test results

---

## 11. ROS 2 Integration

ROS 2 acts as the communication middleware between the major software components.

The expected logical components include:

- LiDAR data acquisition
- Encoder data acquisition
- Odometry processing
- SLAM processing
- Navigation
- Visualization
- Data storage

ROS 2 enables these components to exchange sensor and processing data as part of the overall robot software system.

---

## 12. Python and C++ Responsibilities

Python and C++ will be used according to the requirements of individual software components.

### Python

Python can be used for:

- Supporting robotics scripts
- Data-processing utilities
- Experimental scripts
- Evaluation and analysis utilities
- Supporting ROS 2 nodes where appropriate

### C++

C++ can be used for:

- Performance-sensitive ROS 2 components
- Sensor-processing components where required
- Low-level or hardware-related integration where appropriate

The exact Python/C++ division will be finalized during implementation based on hardware interfaces and software requirements.

---

## 13. End-to-End Software Flow

```text
360° LiDAR
      ↓
LiDAR Data Acquisition
      ↓
Sensor Processing ──────────────┐
                                │
Wheel Encoders                  │
      ↓                         │
Encoder Data Acquisition        │
      ↓                         │
Odometry ───────────────────────┘
      ↓
SLAM Processing
      ↓
Localization + Map Generation
      ↓
Navigation
      ↓
Obstacle Response
      ↓
Map Visualization
      ↓
Map / Experimental Data Storage
