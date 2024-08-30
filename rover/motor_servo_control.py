import RPi.GPIO as GPIO
import time

# GPIO pin setup
MOTOR_PWM_PIN = 18  # PWM pin for motor control
MOTOR_IN1_PIN = 23  # IN1 pin for motor direction control
MOTOR_IN2_PIN = 24  # IN2 pin for motor direction control
SERVO_PIN = 25      # PWM pin for servo control

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR_PWM_PIN, GPIO.OUT)
GPIO.setup(MOTOR_IN1_PIN, GPIO.OUT)
GPIO.setup(MOTOR_IN2_PIN, GPIO.OUT)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Set up PWM for motor and servo
motor_pwm = GPIO.PWM(MOTOR_PWM_PIN, 100)  # 100Hz frequency
servo_pwm = GPIO.PWM(SERVO_PIN, 50)       # 50Hz frequency for servo

motor_pwm.start(0)  # Initialize motor with 0% duty cycle (stopped)
servo_pwm.start(7.5)  # Neutral position for servo (assuming 7.5% duty cycle is neutral)

def set_motor(speed, direction):
    # Control the motor direction
    GPIO.output(MOTOR_IN1_PIN, GPIO.HIGH if direction == 'forward' else GPIO.LOW)
    GPIO.output(MOTOR_IN2_PIN, GPIO.LOW if direction == 'forward' else GPIO.HIGH)
    
    # Control the motor speed
    motor_pwm.ChangeDutyCycle(speed)  # Speed is a percentage (0 to 100)

def set_servo(angle):
    # Convert angle (0 to 180) to duty cycle (2.5 to 12.5)
    duty = 2.5 + (angle / 18.0) * 10.0
    servo_pwm.ChangeDutyCycle(duty)

try:
    while True:
        # Example usage:
        set_motor(50, 'forward')  # Run motor at 50% speed forward
        time.sleep(2)
        set_motor(0, 'forward')  # Stop the motor
        time.sleep(2)

        set_servo(90)  # Turn servo to 90 degrees (center)
        time.sleep(2)
        set_servo(0)   # Turn servo to 0 degrees (left)
        time.sleep(2)
        set_servo(180) # Turn servo to 180 degrees (right)
        time.sleep(2)

except KeyboardInterrupt:
    pass

finally:
    motor_pwm.stop()
    servo_pwm.stop()
    GPIO.cleanup()
