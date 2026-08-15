import math
import time

class Ros2SensorFusionNode:
    def __init__(self):
        # Setting camera calibration properties (Field of View focal points)
        self.camera_focal_length = 500  # pixels
        self.target_real_width = 0.5    # meters (e.g., width of a tracking box)

    def process_camera_bounding_box(self, box_width_pixels):
        # Uses geometric optics logic to estimate distance based on pixel width
        if box_width_pixels <= 0:
            return 0.0
        calculated_depth = (self.target_real_width * self.camera_focal_length) / box_width_pixels
        return round(calculated_depth, 3)

    def execute_sensor_fusion(self, camera_pixel_width, lidar_range_meters):
        print("[ROS2 NODE] Processing incoming high-frequency data streams...")
        time.sleep(0.3)
        
        # Calculate distance calculated by camera logic
        camera_depth_estimate = self.process_camera_bounding_box(camera_pixel_width)
        
        print(f"  > Camera Tracking Node Estimate : {camera_depth_estimate}m")
        print(f"  > LiDAR Range Finder Reading    : {lidar_range_meters}m")
        
        # Mathematical Data Fusion: Weighted averaging to filter reading noise
        fused_distance = (camera_depth_estimate * 0.4) + (lidar_range_meters * 0.6)
        
        # Tracking check layer
        if fused_distance < 1.0:
            return round(fused_distance, 3), "CRITICAL_PROXIMITY_WARN: Object inside navigation clear boundary."
        return round(fused_distance, 3), "TARGET_TRACKING_STABLE: Safe tracking margin maintained."

# =====================================================================
# OPERATION RUNTIME ENGINE (INTERACTIVE USER INPUT INITIALIZATION)
# =====================================================================
if __name__ == "__main__":
    fusion_node = Ros2SensorFusionNode()
    
    print("=" * 68)
    print("      ROS2 AUTONOMOUS ROBOT MULTI-SENSOR DATA FUSION CONTROLLER      ")
    print("=" * 68)
    
    # 1. Gather dynamic hardware input metrics
    print("\n[STREAM INPUT 01: COMPUTER VISION OBJECT RECOGNITION]")
    pixels = int(input("Enter detected target width on camera canvas (in pixels, e.g., 125): "))
    
    print("\n[STREAM INPUT 02: LASER RANGE FINDER telemetry]")
    lidar_dist = float(input("Enter raw distance feedback from LiDAR sensor (in meters, e.g., 1.95): "))
    
    # Run data processing algorithms
    print("\nSynthesizing coordinate arrays across active nodes...")
    time.sleep(0.3)
    final_distance, system_flag = fusion_node.execute_sensor_fusion(pixels, lidar_dist)

    print("\n" + "=" * 68)
    print(" AUTONOMOUS NAVIGATION NODE DIAGNOSTIC ARCHIVE")
    print("=" * 68)
    print(f" [VISION NODE FEED] Camera Target Canvas Frame: {pixels} px")
    print(f" [LIDAR TELEMETRY] Laser Sensor Distance File : {lidar_dist}m")
    print(f" [ALGORITHM RESULT] Fused Spatial Localization : {final_distance}m")
    print(f" [TRACKING TRACK]   System Operational Status : {system_flag}")
    print("=" * 68)
