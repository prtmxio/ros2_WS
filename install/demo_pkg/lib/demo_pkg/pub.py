#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyPublisher(Node):
    def __init__(self):
        super().__init__('PUB')
        self.publisher_ = self.create_publisher(String, 'xio', 10)
        time = 0.5 # seconds
        self.timer = self.create_timer(time, self.callback_function)
        
    def callback_function(self):
        msg = String()
        msg.data = "Hello ROS2"
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args) 
    pub = MyPublisher()
    rclpy.spin(pub) # keep the code alive to continue publishing
    pub.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()