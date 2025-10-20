#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class Node_B(Node):
    def __init__(self):
        super().__init__('node_B')

        # SUB over t1
        self.sub_t1 = self.create_subscription(Int32, 't1', self.callback_t1, 10)

        # PUB over t2
        self.pub_t2 = self.create_publisher(Int32, 't2', 10)

        self.response_val = None
        self.response_timer = None
    
    def callback_t1(self, msg):
        received_val = msg.data
        self.get_logger().info(f'#### --- Node_B --- ####')
        self.get_logger().info(f'Rx Value : {received_val}')

        if self.response_timer is not None:
            self.response_timer.cancel()
        
        self.get_logger().info(f'--- Incrementation---')
        self.response_val = received_val + 1
        time = 2.0
        self.response_timer = self.create_timer(time, self.delayed_send)
    
    def delayed_send(self):
        if self.response_val is not None:
            response = Int32()
            response.data = self.response_val
            self.pub_t2.publish(response)
            self.get_logger().info(f'Tx Value : {self.response_val}')
            self.get_logger().info("\t")
            if self.response_timer is not None:
                self.response_timer.cancel()
                self.response_timer = None
            self.response_val = None


def main():
    rclpy.init()
    node = Node_B()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ =='__main__':
    main()