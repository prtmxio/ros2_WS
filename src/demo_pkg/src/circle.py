#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class CircleMover(Node):
    def __init__(self):
        super().__init__("circle_mover")
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.radius = 2.0  
        self.linear_speed = 3.5  
        self.angular_speed = self.linear_speed / self.radius
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.move_callback)

    def move_callback(self):
        msg = Twist()        
        msg.linear.x = self.linear_speed
        msg.angular.z = self.angular_speed
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    circle_mover_node = CircleMover()
    rclpy.spin(circle_mover_node)
    
    circle_mover_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()