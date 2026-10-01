class EncoderReader:
    """
    Software interface for SmartScan wheel encoder data acquisition.

    The current implementation supports simulated encoder pulses.
    Hardware-specific acquisition can be added later.
    """

    def __init__(self):
        self.left_count = 0
        self.right_count = 0

    def add_left_pulses(self, pulses):
        """Add pulses received from the left wheel encoder."""
        if pulses < 0:
            raise ValueError("Pulse count cannot be negative")

        self.left_count += pulses

    def add_right_pulses(self, pulses):
        """Add pulses received from the right wheel encoder."""
        if pulses < 0:
            raise ValueError("Pulse count cannot be negative")

        self.right_count += pulses

    def get_counts(self):
        """Return the current left and right encoder counts."""
        return {
            "left": self.left_count,
            "right": self.right_count
        }

    def reset(self):
        """Reset both encoder counts to zero."""
        self.left_count = 0
        self.right_count = 0


def main():
    encoder = EncoderReader()

    print("SmartScan Encoder Data Acquisition")
    print("Commands: LEFT <pulses>, RIGHT <pulses>, READ, RESET, EXIT")

    while True:
        command = input("> ").strip()

        if not command:
            continue

        parts = command.split()

        if parts[0].upper() == "LEFT" and len(parts) == 2:
            encoder.add_left_pulses(int(parts[1]))
            print("Left encoder pulses added.")

        elif parts[0].upper() == "RIGHT" and len(parts) == 2:
            encoder.add_right_pulses(int(parts[1]))
            print("Right encoder pulses added.")

        elif parts[0].upper() == "READ":
            counts = encoder.get_counts()
            print(
                f"Left: {counts['left']} | "
                f"Right: {counts['right']}"
            )

        elif parts[0].upper() == "RESET":
            encoder.reset()
            print("Encoder counts reset.")

        elif parts[0].upper() == "EXIT":
            break

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
