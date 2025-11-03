class Agent:
    total_agent = 0

    def __init__(self, code_name:str, clearance_level:int):
        self.code_name = code_name
        self._clearance_level = clearance_level
        Agent.total_agent += 1
    def report(self):
        print(f"agent {self.code_name} reporting. clearance level: {self._clearance_level}")

    def get_clearance_level(self):
        return self._clearance_level

    def set_clearance_level(self,clearance_level):
        if 1 <= clearance_level <= 10:
            self._clearance_level = clearance_level

        else:
            raise f"clearance level cannot be above 10 or below 1"

    @staticmethod
    def get_total_agents(total_agent):
        print(f"sum of agents {total_agent}")



def print_reports(agent_list):
    for agent in agent_list:
         agent.report()