# butterbot

Autonomous 4-wheel drive robot built on a Raspberry Pi. Uses a servo-mounted ultrasonic sensor to scan for obstacles and navigate around them in real time. All movement and sensor logic is written in Python, interacting directly with GPIO pins and a MotorHat.

---

## Hardware

| Component | Purpose |
|---|---|
| Raspberry Pi | Main controller |
| MotorHat | Motor driver for 4-wheel drive |
| 4x DC wheel motors | Locomotion |
| Servo motor | Rotates ultrasonic sensor for directional scanning |
| Ultrasonic sensor (HC-SR04) | Obstacle distance detection |
| Pi Camera | Visual feed (remote monitoring) |

---

## How It Works

The robot continuously sweeps the ultrasonic sensor left, center, and right via the servo motor. Distance readings determine directional movement — if an obstacle is detected within the threshold, the robot stops, scans to find the clearest path, and steers accordingly.

Threading was implemented to allow servo sweeping and distance measurement to run concurrently, so the robot doesn't pause mid-movement to take a reading.

Motor direction is controlled by passing positive or negative values to each wheel via the MotorHat, enabling forward, reverse, and turning in place.

The robot is operated remotely over SSH for script execution, testing, and updates.

---

## Code Structure

| File | Description |
|---|---|
| `robot3.py` | Main robot controller — movement logic and obstacle response |
| `robot3_behavior1.py` | Behavior module for robot3 — defines how the robot reacts to sensor input |
| `servo_robot.py` | Integrated servo + movement control |
| `simple_avoid.py` | Basic obstacle avoidance without servo sweep |
| `super_sonic.py` | Ultrasonic sensor testing and distance measurement |
| `servo_test1.py` | Servo motor calibration and sweep testing |
| `swivelbot.py` | Servo-mounted sensor sweep prototype |
| `swiveling.py` | Servo sweep logic module |
| `robot2.py` | Earlier iteration of the robot controller |

---

## Usage

1. SSH into the Raspberry Pi
2. Clone the repo or copy scripts to the Pi
3. Install dependencies:
   ```bash
   pip install RPi.GPIO adafruit-circuitpython-motorkit
   ```
4. Run the main controller:
   ```bash
   python3 robot3.py
   ```

---

## What This Demonstrates

- Autonomous navigation with real-time sensor feedback
- Hardware/software integration via GPIO and MotorHat
- Concurrent threading in Python for non-blocking sensor reads
- Iterative hardware development (robot2 → robot3 → behavior modules)
- Remote deployment and testing over SSH
