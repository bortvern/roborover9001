import time
import zmq
import json
import logging

# Attempt to import RPi.GPIO, and mock it if unavailable
try:
    import RPi.GPIO as GPIO
except ImportError:
    class MockGPIO:
        BCM = 'BCM'
        OUT = 'OUT'
        IN = 'IN'
        HIGH = 'HIGH'
        LOW = 'LOW'
        
        def setmode(self, mode):
            logging.debug(f"Mock GPIO setmode: {mode}")

        def setup(self, pin, mode):
            logging.debug(f"Mock GPIO setup: pin {pin}, mode {mode}")

        def output(self, pin, state):
            logging.debug(f"Mock GPIO output: pin {pin}, state {state}")

        def input(self, pin):
            logging.debug(f"Mock GPIO input called on pin {pin}")
            return self.HIGH  # or self.LOW depending on what you want to simulate

        def cleanup(self):
            logging.debug("Mock GPIO cleanup")

    GPIO = MockGPIO()

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler(),        # Log to console
        logging.FileHandler("roborover9001.log", mode='a')  # Log to file
    ]
)

# ZeroMQ setup
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

# GPIO setup
GPIO.setmode(GPIO.BCM)
TRIG = 23
ECHO = 24
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def measure_distance():
    GPIO.output(TRIG, False)
    time.sleep(2)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    pulse_start = time.time()
    pulse_end = pulse_start  # Initialize pulse_end to avoid unbound error

    if GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    if GPIO.input(ECHO) == 1:
        pulse_end = time.time() + 0.00015  # Simulate a 150us pulse duration

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    logging.debug(f"Measured distance: {distance} cm")
    return round(distance, 2)

try:
    while True:
        dist = measure_distance()
        data = {
            "sensor": "ultrasonic",
            "distance": dist
        }
        socket.send_string(json.dumps(data))
        logging.info(f"Sent: {data}")
        time.sleep(1)

except KeyboardInterrupt:
    logging.info("Measurement stopped by user")
    GPIO.cleanup()
