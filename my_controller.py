"""drive_my_drive controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()
print("hello")
    
# get the time step of the current world.
timestep = 64
max_speed=6.28
#create motor instances
left_motor=robot.getMotor("motor 1")
right_motor=robot.getMotor("motor 2")
    
left_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
    
right_motor.setPosition(float('inf'))
right_motor.setVelocity(0.0)
    
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    print("hello")
    left_speed = 0.5 * max_speed
    right_speed= 0.5 * max_speed
        
    left_motor.setVelocity(left_speed)
    right_motor.setVelocity(right_speed)
    
    # Enter here exit cleanup code.
    