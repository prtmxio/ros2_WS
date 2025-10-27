import rclpy
from rclpy.node import Node
from custom_interfaces.srv import AddTwoInts
import sys

class Client_node_async(Node):
    def __init__(self):
        super().__init__("add_client_async")
        self.cli_ = self.create_client(AddTwoInts, "add_two_ints")
        while not self.cli_.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Service not available, waiting .........")
        
    
    def send_request(self):
        request = AddTwoInts.Request()
        request.a = int(sys.argv[1])
        request.b = int(sys.argv[2])
        self.future = self.cli_.call_async(request)



def main(args = None):
    rclpy.init(args = args)
    # create node and send_request
    add_cli = Client_node_async()
    add_cli.send_request()
    # use while the context is okay
    while rclpy.ok():
        rclpy.spin_once(add_cli)
        if(add_cli.future.done()):
            try:
                response = add_cli.future.result()
            except Exception as e:
                add_cli.get_logger().info(
                    f'Service call failed {e}'
                )
            else:
                add_cli.get_logger().info(
                    f'Result of addition : {response.sum}'
                )
            break

    # destroy
    add_cli.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()