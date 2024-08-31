# ZeroMQ Port Mappings

This document lists all the ports used in the RoboRover 9001 project for ZeroMQ communication, along with their purposes and any relevant notes.

## Port Assignments

| Port  | Purpose                         | Description                                         |
|-------|---------------------------------|-----------------------------------------------------|
| 5555  | Ultrasonic Sensor Data          | Publishes distance measurements from the ultrasonic sensor. |
| 5556  | GPS Data                        | Publishes GPS coordinates.                          |
| 5557  | LIDAR Data                      | Publishes point cloud data from the LIDAR sensor.   |
| 5558  | Camera Data                     | Publishes image data from the camera sensor.        |
| 5560  | Object Recognition Results      | Publishes object recognition results from the workstation. |

## Notes

- **Port 5555:** Used by the `ultrasonic_processor.py` to publish processed ultrasonic sensor data.
- **Port 5556:** Used by the `gps_processor.py` to publish GPS coordinates.
- **Port 5557:** Used by the `lidar_processor.py` to publish LIDAR sensor data.
- **Port 5558:** Used by the `camera_processor.py` to publish image data.
- **Port 5560:** Used by the `object_recognition.py` script on the workstation to publish object recognition events.

## Adding New Ports

When adding a new port for ZeroMQ communication:
1. Choose an available port number that doesn't conflict with existing ones.
2. Update this document with the new port, its purpose, and the relevant details.
3. Ensure that all related code and documentation reflect the new port assignment.

