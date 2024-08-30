import zmq
import time
import random
import json
import logging

def gps_sensor_mock():
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
    socket.bind("tcp://*:5556")

    while True:
        latitude = round(random.uniform(-90.0, 90.0), 6)
        longitude = round(random.uniform(-180.0, 180.0), 6)
        
        # Create a JSON-formatted data string
        data = {
            "sensor": "gps",
            "latitude": latitude,
            "longitude": longitude
        }

        # Serialize the data to JSON
        message = json.dumps(data)
        socket.send_string(message)
        logging.info(f"Sent: {message}")
        time.sleep(2)

if __name__ == "__main__":
    gps_sensor_mock()
