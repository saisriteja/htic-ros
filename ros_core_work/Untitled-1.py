#!/usr/bin/env python

from TROS import MoveGroupPythonIntefaceTutorial
# from TROS.MoveGroupPythonIntefaceTutorial import go_to_joint_state

tutorial = MoveGroupPythonIntefaceTutorial(speed=0.03, acceleration=0.08)


print("moving to the inital position using joint space")
initial_position = [0, -1.57, 1.57, 0, 1.57, 3.14]
tutorial.go_to_joint_state(initial_position)

print("moving to a particular position using cartesian space")
position = [0.1, 0.56, 0.3]
tutorial.go_to_pose_goal(position)

