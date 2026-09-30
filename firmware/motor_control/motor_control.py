class MotorController:

    def forward(self):
        print("FORWARD command received")

    def backward(self):
        print("BACKWARD command received")

    def left(self):
        print("LEFT command received")

    def right(self):
        print("RIGHT command received")

    def stop(self):
        print("STOP command received")


def main():
    motor = MotorController()

    print("SmartScan Motor Control")
    print("Commands: FORWARD, BACKWARD, LEFT, RIGHT, STOP")
    print("Type EXIT to quit.")

    while True:
        command = input("> ").strip().upper()

        if command == "FORWARD":
            motor.forward()
        elif command == "BACKWARD":
            motor.backward()
        elif command == "LEFT":
            motor.left()
        elif command == "RIGHT":
            motor.right()
        elif command == "STOP":
            motor.stop()
        elif command == "EXIT":
            break
        else:
            print("Unknown command")


if __name__ == "__main__":
    main()
