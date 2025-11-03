from classes.agent import Agent

class Mission:
    def __init__(self, mission_name, target_location, assigned_agent:Agent):
        self.mission_name = mission_name
        self.target_location = target_location
        self.assigned_agent = assigned_agent

    def brief(self):
        print(f"mission: {self.mission_name}, target {self.target_location}, agent: {self.assigned_agent.code_name}")
