import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Listener_node(Node):
    def __init__(self):
        super().__init__("listener_node")
        self.subscriber_ = self.create_subscription(String, "topic", self.listener_callback, 10)
    
    def listener_callback(self, msg):
        self.get_logger().info(f'Received {msg.data}')


        

def main(args = None):
    rclpy.init(args = args)
    # create
    listner_node = Listener_node()
    # use
    rclpy.spin(listner_node)
    # destroy
    listner_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
