#!/usr/bin/env python

import rospy
import actionlib
from std_msgs.msg import String
from planner_msgs.msg import GraspGoal, GraspAction, MoveToNamedPoseAction, MoveToNamedPoseGoal
from geometry_msgs.msg import PoseStamped

#pos_x, pos_y and pos_z from database of poses
#select pose through user interface
def named_pose(pose, client):
	goal = MoveToNamedPoseGoal()
	
	goal.pose_name = pose
	client.send_goal(goal)
	wait = client.wait_for_result()

	if not wait:
		print("Action server not available")
	else:
		print("Finished : {}".format(wait))



#publish object descriptors to publisher packobject
def pack_object(colour, shape, client):
	goal = GraspGoal()
	goal.colour = colour
	goal.shape = shape
	#do not send target position - position to be determined by vision
	
	client.send_goal(goal)

	wait = client.wait_for_result()

	if not wait:
		print("Action server not available")
	else:
		print("Finished : {}".format(wait))



if __name__ == '__main__':
	try:
		#start up sequence
		rospy.init_node('manipulation_client_py', anonymous=True)	
		print("Initialising action client")
		client = actionlib.SimpleActionClient('manipulation',GraspAction)
		print("Waiting for manipulation server...")
		client.wait_for_server()
		print("Server ready")

		#named_pose("home", client)
		pack_object("red", "rectangle", client)
		print("Done")
		

    	except rospy.ROSInterruptException:
		pass

