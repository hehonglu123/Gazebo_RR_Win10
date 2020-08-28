import RobotRaconteur as RR
RRN=RR.RobotRaconteurNode.s

import numpy as np
import time
import traceback
import sys


Rd=np.array([[ -1, 0., 0 ],
 [ 0., 1,  0.],
 [0,  0., -1]])



with RR.ClientNodeSetup(argv=sys.argv):


	####################Start Service and robot setup
	robot = RRN.ConnectService('rr+tcp://localhost:58654?service=robot')	 

	##########Initialize velocity control parameters
	cmd_w = robot.position_command.Connect()
	state_w = robot.robot_state.Connect()
	RobotJointCommand = RRN.GetStructureType("com.robotraconteur.robotics.robot.RobotJointCommand",robot)

	robot_const = RRN.GetConstants("com.robotraconteur.robotics.robot", robot)
	halt_mode = robot_const["RobotCommandMode"]["halt"]
	jog_mode = robot_const["RobotCommandMode"]["jog"]
	position_mode = robot_const["RobotCommandMode"]["position_command"]
	robot.command_mode = halt_mode
	time.sleep(0.1)

	robot.command_mode = jog_mode
	robot.jog_joint(np.zeros(7), np.ones((7,)), False, True)

	# robot.command_mode = position_mode 
	# q_temp=inv(Rd,[0.5,0,0.1])
	# q_temp=[np.pi/2,np.pi/2,np.pi/2,0,0,0]
	# # robot.jog_joint(q_temp, np.ones((6,)), False, True)
	# now=time.time()
	# jog_joint(robot,vel_ctrl,q_temp,1)
	# print(time.time()-now)

	# joints=robot.robot_state.PeekInValue()[0].joint_position
	# pose=robot.robot_state.PeekInValue()[0].kin_chain_tcp[0]
	# print(joints)


	# # print(staubli_fwd(joints))
	# R = q2R(np.array(pose['orientation'].tolist()))
	# print(R)
