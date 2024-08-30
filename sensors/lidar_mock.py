import zmq
import time
import random
import json
import logging

def lidar_sensor_mock():
    # Set up logging
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=[
            logging.StreamHandler(),        # Log to console
            logging.FileHandler("roborover9001.log", mode='a')  # Log to file
        ]
    )

    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:5557")

    while True:
        # Simulate a simple LIDAR point cloud with random distances
        points = [(round(random.uniform(0.5, 20.0), 2), round(random.uniform(-180, 180), 2)) for _ in range(10)]
        data = {
            "sensor": "lidar",
            "points": points
        }

        # Serialize the data to JSON
        message = json.dumps(data)
        socket.send_string(message)
        logging.info(f"Sent: {message}")
        time.sleep(1)

if __name__ == "__main__":
    lidar_sensor_mock()
