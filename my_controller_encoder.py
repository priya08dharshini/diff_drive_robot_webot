"""my_controller_encoder controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot


def run_robot(robot):
    #get the time step of the current world
    timestep = 64
    max_speed= 6.28
    
    #create instance of motor
    left_motor = robot.getMotor('motor_1')
    right_motor= robot.getMotor('motor_2')
    
    left_motor.setPosition(float('int'))
    left_motor.setVelocity(0.0)
    
    right_motor.setPosition(float('int'))
    right_motor.setVelocity(0.0)
    
    #create position sensor instance
    left_ps = robot.getPositionSensor('ps_1')
    left_ps.enable(timestep)
    
    right_ps = robot.getPositionSensor('ps_1')
    right_ps.enable(timestep)
    
    ps_values = [0,0]
    
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the values for position sensors:
    ps_values[0] = left_ps.getValue()
    ps_values[1] = right_ps.detValue()
    
    print("---------------------------")
    print("position sensor values: {} {} ".format(ps_values[0], ps_values[1]))
    
    left_motor.setVelocity(max_speed)
    right_motor.setvelocity(max_speed)
    
if __main__ == "__main__":
   
# Enter here exit cleanup code.
# create the Robot instance.
    my_robot = Robot()
    run_robot(my_robot)
    
    pass