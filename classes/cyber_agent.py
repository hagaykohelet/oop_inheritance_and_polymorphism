from classes.agent import Agent
class CyberAgent(Agent):
    def __init__(self,code_name, clearance_level, specialty  ):
        super().__init__(code_name, clearance_level )
        self.specialty  = specialty


    def report(self):
        print(f"the specialty {self.specialty}")


