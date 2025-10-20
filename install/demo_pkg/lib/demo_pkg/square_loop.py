#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
from math import pi
from std_srvs.srv import Empty
import time

class Loop_mover(Node):
    def __init__(self):
        super().__init__("square_mover_loop")
        self.cmd_vel_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.pose_sub = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.clear_client = self.create_client(Empty, '/clear')
        while not self.clear_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service /clear not available, waiting...')
        self.current_pos = None
    
    def pose_callback(self, msg):
        self.current_pos = msg
    
    def clear_drawing(self):
        request = Empty.Request()
        self.future = self.clear_client.call_async(request)
        self.get_logger().info("Called /clear service to erase the drawing.")
    
    def move_to_pos(self, tar_x, tar_y):
        self.get_logger().info(f'Moving to: ({tar_x:.2f}, {tar_y:.2f})')
        msg = Twist()
        angle_tolerance = 0.001
        distance_tolerance = 0.01

        while rclpy.ok():
            rclpy.spin_once(self, timeout_sec=0.1)
            
            if self.current_pos is None:
                continue

            dx = tar_x - self.current_pos.x
            dy = tar_y - self.current_pos.y
            distance = math.sqrt(dx**2 + dy**2)

            if distance < distance_tolerance:
                break

            target_angle = math.atan2(dy, dx)
            angle_diff = target_angle - self.current_pos.theta
            
            if angle_diff > pi: angle_diff -= 2 * pi
            elif angle_diff < -pi: angle_diff += 2 * pi

            # --- Control Logic ---
            # Stage 1: If not facing the target, turn first.
            if abs(angle_diff) > angle_tolerance:
                msg.linear.x = 0.0
                msg.angular.z = 1.5 * angle_diff # Proportional control for turning
            # Stage 2: If facing the target, move forward with slight heading correction.
            else:
                msg.linear.x = 0.8 * distance  # Proportional control for linear speed
                msg.angular.z = 0.4 * angle_diff
            
            self.cmd_vel_pub.publish(msg)
        
        # Stop the turtle once it has reached the target
        self.cmd_vel_pub.publish(Twist())
        self.get_logger().info('Arrived at target.')

    def move_square(self):        
        # Wait until we get the first position message
        self.get_logger().info('Waiting for initial pose...')
        while self.current_pos is None and rclpy.ok():
            rclpy.spin_once(self, timeout_sec=0.1)
        self.get_logger().info('Initial pose received.')

        # Define the corners of the square with safe, absolute coordinates
        # These points are well within   the Turtlesim walls (0-11)
        start_X = self.current_pos.x
        start_Y = self.current_pos.y 
        # start_X = 3.0
        # start_Y = 3.0

        distance = 2.0
        square_corners = [
            (0.0, 0.0),
            (distance, 0.0),
            (distance, distance),
            (0.0, distance),
            (0.0, 0.0)
        ]
        
        self.get_logger().info('Starting to move in a square...')
        
        # Sequentially move to each corner of the square
        for corner_x, corner_y in square_corners:
            if not rclpy.ok(): break
            self.move_to_pos(start_X + corner_x, start_Y + corner_y)
            # A small pause can make the movement clearer, but is optional
            # time.sleep(0.5) 

        self.get_logger().info('Square Done!')

def main(args = None):
    rclpy.init(args=args)
    node = Loop_mover()
    node.move_square()
    time.sleep(3.0)
    node.clear_drawing()
    node.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()