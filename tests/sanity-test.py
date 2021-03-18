
 

# from std_msgs import String

import rospy
import math
import time
from std_msgs.msg import UInt16
from sensor_msgs.msg import JointState

head_goal = JointState()
head_goal.position = [math.radians(0), math.radians(0)]
head_goal.name = ["tilt_servo","pan_servo"]

if __name__ == "__main__":

    # head = rospy.Publisher("/head/position_animator", JointState, queue_size=1)
    
    print("Sanity test Started:")
    print("[START] Head node...")
    # head.publish(head_goal)
    pub = rospy.Publisher('/head/position_animator', JointState, queue_size=1)

    rospy.init_node("test_node")
    rate=rospy.Rate(10)

    pub.publish(head_goal)
    time.sleep(5)
    head_goal.position = [math.radians(0), math.radians(45)]
    print("1")

    time.sleep(5)
    pub.publish(head_goal)
    head_goal.position = [math.radians(0), math.radians(0)]
    print("2")
    time.sleep(5)

    # pub.publish(head_goal)
    # head_goal.position = [math.radians(0), math.radians(45)]
    # print("3")
    # time.sleep(5)
    # pub.publish(head_goal)

    # head_goal.position = [math.radians(0), math.radians(0)]  
    # print("3")
  
    # time.sleep(5)
    # pub.publish(head_goal)

    print("[DONE] Head node...")



    while not rospy.is_shutdown():
        rate.sleep()