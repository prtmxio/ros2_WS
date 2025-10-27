import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Listener_node(Node):
    def __init__(self):
        super().__init__("listener_node")
        self.declare_parameter('topic', value='talker_topic')
        topic_name = self.get_parameter('topic').get_parameter_value().string_value
        self.subscriber_ = self.create_subscription(String, topic_name, self.listener_callback, 10)
    
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
