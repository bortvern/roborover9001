RoboRover 9001
Overview
RoboRover 9001 is an autonomous rover project designed to navigate and map its environment using various sensors. The rover uses a Raspberry Pi as its core processor and interacts with multiple sensors such as ultrasonic sensors, GPS, LIDAR, and a camera. The project is structured to allow flexibility in switching out sensors and applying the correct processing logic.

Project Structure
bash
Copy code
roborover9001/
│
├── sensors/               # Mock servers simulating sensor data
│   ├── ultrasonic_mock.py
│   ├── gps_mock.py
│   ├── lidar_mock.py
│   └── camera_mock.py
│
├── sensor_parsing/        # Processing layer for actual sensor data
│   ├── ultrasonic_processor.py
│   ├── gps_processor.py
│   ├── lidar_processor.py
│   └── camera_processor.py
│
├── rover/                 # Rover control and data handling
│   ├── rover_subscriber.py
│   ├── motor_servo_control.py   # Motor and steering control
│
└── README.md              # Project documentation
Components
Hardware:
Traxxas Slash 4x4 VXL Brushless 1/10 4WD RTR Short Course Truck: The base platform for the rover.
Raspberry Pi 5 (8GB RAM): The central processor for the rover, handling sensor data and decision-making.
Pololu G2 High-Power Motor Driver 24v21: Controls the motors for movement.
Traxxas EZ-Peak 3S "Completer Pack" with Two Power Cell Batteries: Power supply and battery management.
Various Sensors: Including ultrasonic sensors, GPS, LIDAR, and a camera, for environmental awareness and mapping.
Software:
Python: The primary programming language used for the project's software components.
ZeroMQ: A messaging library used for communication between the rover's components and mock servers.
RPi.GPIO: Library used to control GPIO pins on the Raspberry Pi, for motor and servo control.
Current Features
Scout Mode:
The rover operates in a "scout" mode where it builds a map of its environment using data from the various sensors.
Sensor data is continuously received, processed, and used to update the rover's internal map and make navigation decisions.
Mock Sensors:
The sensors/ folder contains mock servers that simulate the behavior of actual sensors, allowing you to test the system without hardware.
Ultrasonic: Simulates distance measurement data.
GPS: Simulates location data.
LIDAR: Simulates point cloud data for mapping.
Camera: Simulates image capture data.
Processing Layer:
The sensor_parsing/ folder contains scripts that handle the conversion of raw sensor data to a structured JSON format. This allows for easy integration of different sensors and ensures consistent data handling across the system.
Ultrasonic Processor: Converts raw distance data into JSON.
GPS Processor: Converts raw GPS data into JSON.
LIDAR Processor: Converts point cloud data into JSON.
Camera Processor: Converts camera data into JSON.
Rover Subscriber:
The rover_subscriber.py script in the rover/ folder listens for data from all sensors (real or mock) and processes it to make navigation decisions or update the map.
Motor and Steering Control:
The motor_servo_control.py script in the rover/ folder handles the control of the motors and steering servos, enabling the rover to move and navigate based on processed sensor data.
Getting Started
Prerequisites:
Python 3.6+
ZeroMQ (pyzmq)
RPi.GPIO (for Raspberry Pi)
Any required libraries for specific sensors or hardware components
Installation:
Clone this repository:

bash
Copy code
git clone https://github.com/yourusername/roborover9001.git
cd roborover9001
Install the necessary Python libraries:

bash
Copy code
pip install pyzmq RPi.GPIO
Set up your hardware and ensure all connections are correct.

Running the Mock Servers:
To simulate sensor data:

bash
Copy code
python sensors/ultrasonic_mock.py
python sensors/gps_mock.py
python sensors/lidar_mock.py
python sensors/camera_mock.py
Running the Rover Subscriber:
To start receiving and processing sensor data:

bash
Copy code
python rover/rover_subscriber.py
Contributing
Feel free to submit issues or pull requests if you have suggestions or improvements. This is an open project, and contributions are welcome!

License
This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0). See the LICENSE file for details.

Acknowledgments
Thanks to the open-source community for providing tools and libraries that make projects like this possible. Special thanks to Bort Vern for developing RoboRover 9001.

Parts list acquired from Amazon, AMain Hobbies, and Pololu 
1. Traxxas Slash 4x4 VXL Brushless 1/10 4WD RTR Short Course Truck (Orange) w/TSM & TQi 2.4GHz Radio
2. Pololu G2 High-Power Motor Driver 24v21
3. Raspberry Pi 5 8GB RAM Broadcom BCM2712 Arm Cortex-A76 2.4GHz Quad-core 64-bit Single Board Computer
4. Traxxas EZ-Peak 3S "Completer Pack" Dual Multi-Chemistry Battery Charger w/Two Power Cell Batteries (5000mAh)
5. CSE010-0004-00 - Castle Creations 10 Amp Adjustable BEC
6. RaceTek Matek HUBOSD8 H-Type PDB & OSD
7. XT60 Connector Male-Female Pair, Black x 10
8. JST RCY Connector Pack, Female x 10
9. Fermerry Wire, 14AWG Silicone Stranded Tinned Copper, 6 Colors 10Ft Each, Includes Heat Shrink Tubings & Wire Ties
10. Fermerry Wire Spool, 18AWG Silicone Electrical Kit, 150ft 6 Colors, Wide Range of Applications, Super Flexible, 13A, CN
11. Fermerry 22 AWG Stranded Wire Spool 25ft Each 6 Colors Flexible 22 Gauge Silicone Hook up Wire Kit Electrical Tinned Copper Wire
12. Ginsco 580 pcs 2:1 Heat Shrink Tubing Kit 6 Colors 11 Sizes Assorted Sleeving Tube Wrap Cable Wire Kit for DIY
13. 63-37 Tin Lead Rosin Core Solder Wire for Electrical Soldering (0.8mm 50g)
14. iCrimp SN-28B Dupont Terminal Ratchet Crimper
15. 620pcs 2.54mm Pitch 1/2/3/4/5/6 Pin JST SM Housing Dupont Connector Kit and 2.54 mm JST XH Male/Female Crimp Pins Adaptor Assortment Kit
16. ProTek RC Futaba Style Servo Connectors (4 Pair)
17. Saiper 300pcs M3 Nylon Male Female Hex Spacers Standoff Screw Nut Assortment Kit for PCB FPV RC Quadcopter Drone Arduino Circuit Board and DIY Use with Plastic Box
18. Adafruit Perma-Proto Half-sized Breadboard PCB - 3 Pack
19. Genuine 1/2" (12mm) x 15 Ft VHB Double Sided Foam Adhesive Tape 5952 Grey Automotive Mounting Very High Bond Strong Industrial Grade (1/2" (w) x 15 ft)
20. Raspberry Pi 5 Official Raspberry Pi 5 Active Cooler, Pi5 Active Cooler Combines Temperature-Controlled Blower Fan and Aluminium Heatsink, Comes with Thermal Tapes for Better Heat Dissipation
21. 5pcs Ultrasonic Module HC-SR04 Distance Sensor with 2pcs Mounting Bracket for Arduino R3 MEGA Mega2560 Duemilanove Nano Robot XBee ZigBee
22. HiLetgo 3pcs GY-521 MPU-6050 MPU6050 3 Axis Accelerometer Gyroscope Module 6 DOF 6-axis Accelerometer Gyroscope Sensor Module 16 Bit AD Converter Data Output IIC I2C for Arduino
23. Arducam for Raspberry Pi HQ Camera, 12.3MP IMX477 High Sensitivity CMOS Raspberry Pi 5 Camera, Comes with C-CS Adapter and Tripod Mount for Raspberry Pi 4 Model B, Pi 3/3B+, and Pi Zero 2W
24. yueton Rc 1-8s Lipo Battery Tester Monitor Low Voltage Buzzer Alarm Voltage Checker with LED Indicator for Lipo LiFe LiMn Li-ion Battery
25. 2Pack GPS Module,Navigation Satellite Positioning NEO-6M,Arduino GPS, Drone Microcontroller, GPS Receiver Compatible with 51 Microcontroller STM32 Arduino UNO R3 with Antenna High Sensitivity
26. RPLIDAR A1M8 2D 360 Degree 12 Meters Scanning Radius LIDAR Sensor Scanner
27. 5Pcs DC 5V 1 Channel Relay Module Board Shield with Optocoupler Isolation Support High or Low Level Compatible Development Board Trigger
28. APIELE Waterproof Round Rocker Toggle Switch 2 Position DC 12V 20A ON-Off with LED Light SPST 3 Pins 4Pcs KCD1-8-101NW (Four Color Pack)
29. 6 Pack 10 Gauge Inline Fuse Holder 12V - 10AWG Automotive Blade Fuse Holder with 6pcs 40 AMP ATC/ATO Standard Fuses