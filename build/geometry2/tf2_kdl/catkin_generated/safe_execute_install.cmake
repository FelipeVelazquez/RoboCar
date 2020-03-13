execute_process(COMMAND "/home/ironlion/RoboCar/build/geometry2/tf2_kdl/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/ironlion/RoboCar/build/geometry2/tf2_kdl/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
