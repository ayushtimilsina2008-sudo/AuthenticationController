import time

class JointController:
    def __init__(self):
        # standard motor limits for a basic robotic arm servo
        self.min_angle = 0
        self.max_angle = 180
        self.current_pos = 90  # start right in the middle position

    def move_to_angle(self, target_angle):
        print(f"\n[SYSTEM] Received command to rotate to: {target_angle} degrees")
        time.sleep(0.2) # small pause to mimic hardware startup delay
        
        # safety check: check that the user input doesn't grind the gears
        if target_angle < self.min_angle or target_angle > self.max_angle:
            print(">>> ERROR: Angle instruction is out of bounds! Movement blocked.")
            return False, f"Limit Override Active. Stay between {self.min_angle} and {self.max_angle}."
        
        # move the joint step by step to the target angle position
        print("Moving motor shaft...")
        if target_angle > self.current_pos:
            while self.current_pos < target_angle:
                self.current_pos += 1
        elif target_angle < self.current_pos:
            while self.current_pos > target_angle:
                self.current_pos -= 1
                
        return True, f"Success! Arm joint moved cleanly to {self.current_pos} degrees."

# ==========================================
# INTERACTIVE TERMINAL APP TEST FOR APPLICANT
# ==========================================
if __name__ == "__main__":
    robot_arm = JointController()
    
    print("--------------------------------------------------")
    print("      ROBOTIC ARM SERVO MOTOR CONTROL INTERFACE   ")
    print("--------------------------------------------------")
    print(f"Current setup status: Robot joint is currently sitting at {robot_arm.current_pos}°")
    
    try:
        user_input = int(input("Where would you like to move the arm? (Enter 0-180): "))
        
        # execute the motor instruction block
        success, final_log = robot_arm.move_to_angle(user_input)
        
        print("\n--------------------------------------------------")
        print("            HARDWARE DIAGNOSTIC LOGS              ")
        print("--------------------------------------------------")
        print(f" Target Position Input : {user_input}°")
        print(f" Motor Running Status  : {'FINISHED' if success else 'OVERRIDE_STOP'}")
        print(f" Output System Message : {final_log}")
        print("--------------------------------------------------")
        
    except ValueError:
        print("\n[INPUT ERROR] Please enter a valid whole number angle.")
