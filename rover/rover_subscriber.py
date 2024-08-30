import zmq
import json

def rover_subscriber():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://localhost:5555")  # Ultrasonic
    socket.connect("tcp://localhost:5556")  # GPS
    socket.connect("tcp://localhost:5557")  # LIDAR
    socket.connect("tcp://localhost:5558")  # Camera
    socket.setsockopt_string(zmq.SUBSCRIBE, "")

    while True:
        message = socket.recv_string()

        if not message.strip():  # Check if the message is empty
            continue  # Skip processing this message
        
        try:
            # Deserialize the JSON data
            data = json.loads(message)
        except json.JSONDecodeError as e:
            print(f"Failed to decode JSON: {e}")
            continue  # Skip this iteration and wait for the next message

        sensor_type = data.get("sensor")
        
        if sensor_type == "ultrasonic":
            distance = data["distance"]
            print(f"Received ultrasonic data: {distance} meters")
        elif sensor_type == "gps":
            latitude = data["latitude"]
            longitude = data["longitude"]
            print(f"Received GPS data: {latitude}, {longitude}")
        elif sensor_type == "lidar":
            points = data["points"]
            print(f"Received LIDAR data: {points}")
        elif sensor_type == "camera":
            image_id = data["image_id"]
            print(f"Received camera data: {image_id}")

if __name__ == "__main__":
    rover_subscriber()
