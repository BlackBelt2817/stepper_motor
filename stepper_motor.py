import RPi.GPIO as GPIO
import time

halfstep_seq_left = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
]

halfstep_seq_right = [
  [0,0,0,1],
  [0,0,1,1],
  [0,0,1,0],
  [0,1,1,0],
  [0,1,0,0],
  [1,1,0,0],
  [1,0,0,0],
  [1,0,0,1]
]



while True:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    control_pins = [7, 11, 13, 15]

    for pin in control_pins:
      GPIO.setup(pin, GPIO.OUT)
      GPIO.output(pin, 0)
    turn = input('Turn (like r50):   ')
    direction = turn[0]
    amount = int(turn[1:])
    
    if direction == 'l':
        for i in range(amount):
          for halfstep in range(8):
            for pin in range(4):
              GPIO.output(control_pins[pin], halfstep_seq_left[halfstep][pin])
            time.sleep(0.001)
        GPIO.cleanup()
    elif direction == 'r':
        for i in range(amount):
          for halfstep in range(8):
            for pin in range(4):
              GPIO.output(control_pins[pin], halfstep_seq_right[halfstep][pin])
            time.sleep(0.001)
        GPIO.cleanup()








