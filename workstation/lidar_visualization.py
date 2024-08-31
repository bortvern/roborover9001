import zmq
import matplotlib.pyplot as plt
import numpy as np

# Set up ZeroMQ context and subscriber
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5557")  # Connect to the LIDAR data publisher
socket.setsockopt_string(zmq.SUBSCRIBE, "")

def visualize_lidar(points):
    plt.figure()
    plt.title("LIDAR Data Visualization")
    plt.xlabel("X (meters)")
    plt.ylabel("Y (meters)")
    
    # Convert polar coordinates to Cartesian coordinates for plotting
    for distance, angle in points:
        angle_rad = np.deg2rad(angle)
        x = distance * np.cos(angle_rad)
        y = distance * np.sin(angle_rad)
        plt.plot(x, y, 'bo')  # Plot the point as a blue dot
    
    plt.xlim(-20, 20)  # Adjust the limits based on LIDAR range
    plt.ylim(-20, 20)
    plt.grid(True)
    plt.show()

def main():
    while True:
        message = socket.recv_json()
        if message["sensor"] == "lidar":
            points = message["points"]
            print(f"Received LIDAR data: {points}")
            visualize_lidar(points)

if __name__ == "__main__":
    main()
