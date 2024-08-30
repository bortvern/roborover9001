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