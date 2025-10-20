#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class Node_A(Node):
    def __init__(self):
        super().__init__('node_A')

        # PUB over t1
        self.pub_t1 = self.create_publisher(Int32, 't1', 10)
        
        # SUB over t2
        self.sub_t2 = self.create_subscription(Int32, 't2', self.callback_t2, 10)
        self.val = 0
        self.waiting_for_response = False
        time = 1.0  
        self.get_logger().info(f'#### --- Node_A --- ####')
        self.timer = self.create_timer(time, self.timer_callback)
        
    def timer_callback(self):
        if self.val > 5:
            self.get_logger().info('Transfer Abort!!')
            self.timer.cancel() 
            return
        
        if not self.waiting_for_response:
            msg = Int32()
            msg.data = self.val
            self.pub_t1.publish(msg)
            self.get_logger().info(f'Tx Value : {self.val}')
            self.get_logger().info("\t")
            self.waiting_for_response = True

    
    def callback_t2(self, msg):
        self.get_logger().info(f'#### --- Node_A --- ####')
        self.val = msg.data
        self.get_logger().info(f'Rx Value : {self.val}')
        self.waiting_for_response = False

def main():
    rclpy.init()
    node = Node_A()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ =='__main__':
    main()