#!/usr/bin/env python

import rospy
import actionlib
from std_msgs.msg import String
from planner_msgs.msg import GraspGoal, GraspAction
from geometry_msgs.msg import PoseStamped


def callback(server):
	server.get_logger().info('Executing goal...')
	return server.GraspAction.result


if __name__ == '__main__':
	try:
		#start up sequence
		rospy.init_node('manipulation_client_py', anonymous=True)	
		print("Initialising action server")
		client = actionlib.SimpleActionServer('manipulation',GraspAction, callback, auto_start = False)
		print("Waiting for manipulation server...")
		print("Server ready")

		named_pose(0.5, -0.2, 0.3, client)
		print("Done")
		

    	except rospy.ROSInterruptException:
		pass


