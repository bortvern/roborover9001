import zmq
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Set up ZeroMQ context and subscriber
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5557")  # Replace with your Raspberry Pi's IP address
socket.setsockopt_string(zmq.SUBSCRIBE, "")

def visualize_lidar_3d_real_time():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title("Real-Time 3D LIDAR Data Visualization")
    ax.set_xlabel("X (meters)")
    ax.set_ylabel("Y (meters)")
    ax.set_zlabel("Z (meters)")

    ax.set_xlim(-20, 20)  # Adjust based on LIDAR range
    ax.set_ylim(-20, 20)
    ax.set_zlim(-5, 5)  # Adjust the Z limits if you start working with real 3D data

    plt.ion()  # Enable interactive mode

    while True:
        message = socket.recv_json()
        if message["sensor"] == "lidar":
            points = message["points"]
            print(f"Received LIDAR data: {points}")

            # Clear the previous plot
            ax.cla()

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

            # Set limits and labels again after clearing the axes
            ax.set_xlim(-20, 20)
            ax.set_ylim(-20, 20)
            ax.set_zlim(-5, 5)
            ax.set_xlabel("X (meters)")
            ax.set_ylabel("Y (meters)")
            ax.set_zlabel("Z (meters)")

            plt.draw()  # Redraw the plot
            plt.pause(0.01)  # Pause briefly to allow the plot to update

if __name__ == "__main__":
    visualize_lidar_3d_real_time()
