import time
import zmq
import json
import logging
from ..motor_servo_control import set_motor, set_servo

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("roborover9001.log", mode='a')
    ]
)

# Initialize ZeroMQ context and socket for subscribing to sensor data
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")  # Ultrasonic
socket.connect("tcp://localhost:5556")  # GPS
socket.connect("tcp://localhost:5557")  # LIDAR
socket.connect("tcp://localhost:5558")  # Camera
socket.setsockopt_string(zmq.SUBSCRIBE, "")

# Initialize variables for navigation
obstacle_detected = False
current_direction = "forward"
map_data = []

def process_ultrasonic_data(data):
    global obstacle_detected
    distance = data["distance"]
    if distance < 20:  # Threshold for obstacle detection
        obstacle_detected = True
    else:
        obstacle_detected = False
    logging.info(f"Processed ultrasonic data: {distance} cm")

def process_gps_data(data):
    latitude = data["latitude"]
    longitude = data["longitude"]
    logging.info(f"Processed GPS data: Latitude {latitude}, Longitude {longitude}")
    map_data.append({"type": "gps", "lat": latitude, "lon": longitude})

def process_lidar_data(data):
    points = data["points"]
    logging.info(f"Processed LIDAR data: {points}")
    map_data.append({"type": "lidar", "points": points})

def process_camera_data(data):
    image_id = data["image_id"]
    logging.info(f"Processed Camera data: {image_id}")
    map_data.append({"type": "camera", "image_id": image_id})

def scout_mode():
    try:
        while True:
            message = socket.recv_string()
            data = json.loads(message)
            sensor_type = data["sensor"]

            if sensor_type == "ultrasonic":
                process_ultrasonic_data(data)
            elif sensor_type == "gps":
                process_gps_data(data)
            elif sensor_type == "lidar":
                process_lidar_data(data)
            elif sensor_type == "camera":
                process_camera_data(data)

            # Decision making based on sensor data
            if obstacle_detected:
                logging.info("Obstacle detected! Turning...")
                set_motor(50, 'backward')  # Example action: back up
                set_servo(45)  # Turn the rover
                time.sleep(1)
            else:
                logging.info("Path is clear, moving forward.")
                set_motor(50, 'forward')  # Example action: move forward
                set_servo(90)  # Straight ahead
                time.sleep(1)

    except KeyboardInterrupt:
        logging.info("Scout mode terminated by user.")
        set_motor(0, 'forward')  # Stop the rover

if __name__ == "__main__":
    scout_mode()
