from robot import Robot
import time
import threading

class AutonomousBehavior:
    def __init__(self, the_robot):
        self.robot = the_robot
        self.angle = 0
        self.forward_dist = 15
        self.right_dist = 15
        self.left_dist = 15
        self.angle_distance = [[90,0],[0,0],[-90,0]]
        self.stopinng_distance_in = 10
    
    def set_pan_start(self):
        self.angle = 0
        self.robot.set_pan(self.angle)
    
    def find_forward_dist(self):
        self.angle = 0
        #self.angle_distance[1][0] = self.angle
        self.angle_distance[1][1] = self.robot.return_distance_at(self.angle)
        #print(self.angle_distance[1][1])
    
    def find_left_dist(self):
        self.angle = 90
        #self.angle_distance[0][0] = self.angle
        self.angle_distance[0][1] = self.robot.return_distance_at(self.angle)
    
    def find_right_dist(self):
        self.angle = -90
        #self.angle_distance[2][0] = self.angle
        self.angle_distance[2][1] = self.robot.return_distance_at(self.angle)
    
    def test_sensor(self):
        test_index = 0
        self.forward_dist()
        while test_index < 20:
            self.find_forward_dist()
            time.sleep(0.5)
            self.find_right_dist()
            time.sleep(0.5)
            self.find_left_dist()
            time.sleep(0.5)
            print(self.angle_distance)
            test_index +=1

    
    def run(self, speed):
        sleepy = 0.25
        while True:
            self.find_forward_dist()
            #time.sleep(sleepy)
            self.find_right_dist()
            time.sleep(sleepy)
            self.find_left_dist()
            #time.sleep(sleepy)
            #self.find_forward_dist()
            print(self.angle_distance)
            print(self.robot.get_speed())
            
            if (self.angle_distance[1][1] > self.stopinng_distance_in):
                self.robot.go_straight(speed)
                print('going forward...')
                check = threading.Thread.start(Robot.check_stopped())

                if (check == True):
                    time.sleep(0.5)
                    check2 = Robot3.check_stopped()

                    if (check2 == True):

                        print("Stopped...\nTurning Around...")
                        start = time.perf_counter()

                        if(self.angle_distance[0][1] > self.stopinng_distance_in):
                            self.robot.go_backwards(speed)
                            time.sleep(0.5)
                            self.robot.turn_left(speed)
                            time.sleep(1.5)

                        elif(self.angle_distance[2][1] > self.stopinng_distance_in):
                            self.robot.go_backwards(speed)
                            time.sleep(0.5)
                            self.robot.turn_right(speed)
                            time.sleep(1.5)

                        else:
                            self.robot.rand_turn_around(speed)
                        
                        end = time.perf_counter()
                        timer = end - start
                        if timer >= 10:
                            self.robot.stop_all()
                            print('stopping...')
                            time.sleep(10) #Wait 10 seconds then start back up?
                            '''code for manual input to confirm robot has been moved/unstuck, 
                            if y then continue running, if n then robot quits'''

                            '''
                            removed = input('Has ButterBot been rescued? (y/n)? ')
                            if removed == 'y':
                                continue
                            else:
                                exit()
                            '''
                            '''Include manual takeover?'''

            elif (self.angle_distance[0][1] > self.stopinng_distance_in):
                self.robot.turn_left(speed)
                print('turning left...')

            elif (self.angle_distance[2][1] > self.stopinng_distance_in):
                self.robot.turn_right(speed)
                print('turn right...')

            else:
                self.robot.stop_all()
                print('stopping...')
            
    
