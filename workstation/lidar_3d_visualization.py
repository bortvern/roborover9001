import zmq
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Set up ZeroMQ context and subscriber
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5557")  # Connect to the LIDAR data publisher
socket.setsockopt_string(zmq.SUBSCRIBE, "")

def visualize_lidar_3d(points):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title("3D LIDAR Data Visualization")
    
    # Convert polar coordinates to Cartesian coordinates for 3D plotting
    xs = []
    ys = []
    zs = []
    
    for distance, angle in points:
        angle_rad = np.deg2rad(angle)
        x = distance * np.cos(angle_rad)
        y = distance * np.sin(angle_rad)
        z = 0  # Assuming all points lie in the same plane (Z=0)
        
        xs.append(x)
        ys.append(y)
        zs.append(z)
    
    ax.scatter(xs, ys, zs, c='b', marker='o')
    
    ax.set_xlim(-20, 20)  # Adjust based on LIDAR range
    ax.set_ylim(-20, 20)
    ax.set_zlim(-5, 5)  # Adjust the Z limits if you start working with real 3D data
    
    ax.set_xlabel("X (meters)")
    ax.set_ylabel("Y (meters)")
    ax.set_zlabel("Z (meters)")
    
    plt.show()

def main():
    while True:
        message = socket.recv_json()
        if message["sensor"] == "lidar":
            points = message["points"]
            print(f"Received LIDAR data: {points}")
            visualize_lidar_3d(points)

if __name__ == "__main__":
    main()
