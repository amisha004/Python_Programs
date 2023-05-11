class Robot:
    # Class variable
    count = 0
    def __init__(self, name):
        # Instance variable
        self.name = name
        Robot.count += 1
        
    def say_hello(self):
        print(f"Hello, my name is {self.name}")
        
    @classmethod
    def robot_count(cls):
        print(f"There are currently {cls.count} robots")
# To create an instance of the Robot class.
r1 = Robot("Robo")
r1.say_hello() 
r2 = Robot("Bot")
r2.say_hello()
Robot.robot_count() 


