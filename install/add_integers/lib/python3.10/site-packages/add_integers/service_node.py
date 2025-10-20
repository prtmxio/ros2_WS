import rclpy
from rclpy.node import Node
from custom_interfaces.srv import AddTwoInts

class Service_node(Node):
    def __init__(self):
        super().__init__("add_int_service")
        self.srv_ = self.create_service(AddTwoInts, "add_two_ints", self.add_callback)

    
    def add_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(f"Icoming request \n a : {request.a} b : {request.b}")
        return response


def main(args = None):
    rclpy.init(args = args)
    # create
    add_srv = Service_node()
    # use
    rclpy.spin(add_srv)
    # destroy
    add_srv.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()