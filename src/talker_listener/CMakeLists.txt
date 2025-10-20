cmake_minimum_required(VERSION 3.8)
project(talker_listener)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)
add_executable(my_talker src/talker_node.cpp)
ament_target_dependencies(my_talker rclcpp std_msgs)
add_executable(my_listener src/listener_node.cpp)
ament_target_dependencies(my_listener rclcpp std_msgs)


install(TARGETS
  my_talker
  my_listener
  DESTINATION lib/${PROJECT_NAME})

ament_package()
