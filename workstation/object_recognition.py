import cv2
import zmq
import requests
import numpy as np

# ZeroMQ setup
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5560")  # Port for publishing recognition events

# URL of the Raspberry Pi video feed
video_feed_url = "http://<raspberry-pi-ip>:5000/video_feed"

def perform_object_recognition(frame):
    # Stub to apply your object recognition logic
    # For example, using a pre-trained model like YOLO, SSD, etc.
    # The following is a placeholder for where recognition would occur.
    # recognition_results = your_model.detect_objects(frame)
    recognition_results = ["object1", "object2"]  # Placeholder result
    return recognition_results

def main():
    stream = requests.get(video_feed_url, stream=True)
    bytes_data = b''
    
    for chunk in stream.iter_content(chunk_size=1024):
        bytes_data += chunk
        a = bytes_data.find(b'\xff\xd8')
        b = bytes_data.find(b'\xff\xd9')
        if a != -1 and b != -1:
            jpg = bytes_data[a:b+2]
            bytes_data = bytes_data[b+2:]

            # Decode the frame
            frame = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
            
            # Perform object recognition
            recognition_results = perform_object_recognition(frame)
            
            # Publish recognition events via ZeroMQ
            data = {"sensor": "camera", "recognition_results": recognition_results}
            socket.send_json(data)
            print(f"Sent recognition event: {data}")

if __name__ == "__main__":
    main()
