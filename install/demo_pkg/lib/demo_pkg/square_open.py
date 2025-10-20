#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
# from math import pi

class Open_mover(Node):
    def __init__(self):
        super().__init__('square_mover_open')
        self.cmd_vel_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        time.sleep(1.0)
        self.move_square()
    
    def move_straight(self, distance, speed = 2.0):
        msg = Twist()
        msg.linear.x = speed
        duration = distance / speed
        self.get_logger().info(f'Move straight for {distance} units')
        start_time = time.time()
        while(time.time() - start_time) < duration:
            self.cmd_vel_pub.publish(msg)
            time.sleep(0.1)
        
        msg.linear.x = 0.0
        self.cmd_vel_pub.publish(msg)

    def turn_90(self, angular_speed = 3.14/2):
        msg = Twist()
        msg.angular.z = angular_speed
        duration = 1.571 / angular_speed
        self.get_logger().info(f'Turn 90')
        start_time = time.time()
        while(time.time() - start_time) < duration:
            self.cmd_vel_pub.publish(msg)
            time.sleep(0.1)
        
        msg.angular.z = 0.0
        self.cmd_vel_pub.publish(msg)

    def move_square(self):
        self.get_logger().info(f'Starting square movement......')

        for i in range(4):
            self.move_straight(2.0)
            time.sleep(0.5)
            self.turn_90()
            time.sleep(0.5)
        
        self.get_logger().info(f'Square Completed!!')
    
def main(args = None):
    rclpy.init(args=args)
    node = Open_mover()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
    



        
