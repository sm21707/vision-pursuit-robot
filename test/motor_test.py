import pigpio
import time

pi = pigpio.pi()

if not pi.connected:
    print("ERROR: pigpiod not running!")
    exit()

# L298N pins (from your reference doc)
IN1 = 5  # Left motor direction
IN2 = 6
IN3 = 16  # Right motor direction
IN4 = 20
ENA = 13  # Left motor speed (PWM)
ENB = 12  # Right motor speed (PWM)

# Setup all pins as output
for pin in [IN1, IN2, IN3, IN4, ENA, ENB]:
    pi.set_mode(pin, pigpio.OUTPUT)

SPEED = 128  # 0-255

def backward():
    pi.write(IN1, 1); pi.write(IN2, 0)
    pi.write(IN3, 0); pi.write(IN4, 1)
    pi.set_PWM_dutycycle(ENA, SPEED)
    pi.set_PWM_dutycycle(ENB, SPEED)
    print("Moving BACKWARD")

def forward():
    pi.write(IN1, 0); pi.write(IN2, 1)
    pi.write(IN3, 1); pi.write(IN4, 0)
    pi.set_PWM_dutycycle(ENA, SPEED)
    pi.set_PWM_dutycycle(ENB, SPEED)
    print("Moving FORWARD")

def right():
    pi.write(IN1, 1); pi.write(IN2, 0)
    pi.write(IN3, 1); pi.write(IN4, 0)
    pi.set_PWM_dutycycle(ENA, SPEED)
    pi.set_PWM_dutycycle(ENB, SPEED)
    print("Turning RIGHT")

def left():
    pi.write(IN1, 0); pi.write(IN2, 1)
    pi.write(IN3, 0); pi.write(IN4, 1)
    pi.set_PWM_dutycycle(ENA, SPEED)
    pi.set_PWM_dutycycle(ENB, SPEED)
    print("Turning LEFT")

def stop():
    pi.set_PWM_dutycycle(ENA, 0)
    pi.set_PWM_dutycycle(ENB, 0)
    print("STOPPED")

print("Motor Control Ready!")
print("Commands: w=forward, s=backward, a=left, d=right, x=stop, q=quit")

while True:
    cmd = input("Enter command: ").strip().lower()
    if cmd == 'w':
        forward()
    elif cmd == 's':
        backward()
    elif cmd == 'a':
        left()
    elif cmd == 'd':
        right()
    elif cmd == 'x':
        stop()
    elif cmd == 'q':
        stop()
        pi.stop()
        print("Bye!")
        break
    else:
        print("Unknown command. Use w/a/s/d/x/q")

