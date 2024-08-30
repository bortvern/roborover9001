import zmq
import time
import random
import json
import logging

def camera_sensor_mock():
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
    socket.bind("tcp://*:5558")

    while True:
        # Simulate camera data as an image ID (e.g., for different frames)
        image_id = random.randint(1, 1000)
        
        # Create a JSON-formatted data string
        data = {
            "sensor": "camera",
            "image_id": f"image_{image_id}"
        }

        # Serialize the data to JSON
        message = json.dumps(data)
        socket.send_string(message)
        logging.info(f"Sent: {message}")
        time.sleep(1)

if __name__ == "__main__":
    camera_sensor_mock()
