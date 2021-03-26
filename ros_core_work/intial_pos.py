#!/usr/bin/env python

import rtde_control
import time

ip = "127.0.0.1"
# ip = "172.16.101.225"

rtde_c = rtde_control.RTDEControlInterface(ip)

dt = 1.0/500  # 2ms
joint_q = [0,-1.57,1.57,0,1.57,3.14] 

# Move to initial joint position with a regular moveJ
rtde_c.moveJ(joint_q,0.2,0.2,False)

rtde_c.stopScript()