import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Talker_node(Node):
    def __init__(self):
        super().__init__("talker_node")

        self.declare_parameter('topic', value='talker_topic')
        topic_name = self.get_parameter('topic').get_parameter_value().string_value

        self.publisher_ = self.create_publisher(String, topic_name, 10)
        timer_period = 0.5 # sec
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.counts_ = 0
        
    # timer_callback() will be called every 0.5 secs
    def timer_callback(self):
        msg = String()
        msg.data = f"Hello everyone {self.counts_}"
        self.publisher_.publish(msg)
        self.counts_ += 1
        self.get_logger().info(f"{msg.data} message is being published")
    


def main(args = None):
    rclpy.init(args = args)
    # create node
    talker = Talker_node()
    # use node
    rclpy.spin(talker)
    # destroy node
    talker.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
