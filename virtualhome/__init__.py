#import glob
#import sys
#from sys import platform
#
## Needs to be fixed!
#original_path = sys.path[5]
#new_path = original_path + '/virtualhome/simulation'
#sys.path.append(new_path)
#
#from unity_simulator.comm_unity import UnityCommunication
#from unity_simulator import utils_viz
#

##################################################################
##################################################################
##################################################################
#import os
#import sys
#
## Get the current script's directory
#current_dir = os.path.dirname(os.path.abspath(__file__))
#
## Construct the new path
#new_path = os.path.join(current_dir, 'virtualhome', 'simulation')
#
## Add the new path to sys.path if it's not already there
#if new_path not in sys.path:
#    sys.path.append(new_path)
#
## Import necessary modules
##try:
##    from unity_simulator.comm_unity import UnityCommunication
##    from unity_simulator import utils_viz
##except ImportError as e:
##    raise ImportError(f"Could not import necessary modules: {e}")
##