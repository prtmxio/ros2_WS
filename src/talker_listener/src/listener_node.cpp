#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
using std::placeholders::_1;

class Listener_node : public rclcpp::Node{
  public:
    Listener_node() : Node("My_listener") {
      subscription_ = this->create_subscription<std_msgs::msg::String>("PUB", 10, std::bind(&Listener_node::topic_callback, this, _1));
    }

  private:
    void topic_callback(const std_msgs::msg::String & msg) const {
      RCLCPP_INFO(this->get_logger(), "I heard: '%s'", msg.data.c_str());
    }
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
};

int main(int argc, char * argv[]){
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<Listener_node>());
  rclcpp::shutdown();
  return 0;
}