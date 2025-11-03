from classes.agent import Agent, print_reports
from classes.mission import Mission
from classes.cyber_agent import CyberAgent
from classes.field_agent import FieldAgent


if __name__ == "__main__":
    f1 = FieldAgent("sad",4,"israel")
    f2 = CyberAgent("sad",4,"hacking")

    print_reports([f1,f2])