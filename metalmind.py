"""
Programmer: Zachary Champion
Project:    lord_ruler
Project Description:
    A rule-based system which can add, subtract, and modify facts from a knowledge base using a set of rules.
    WISH: It can add, subtract, and modify rules as well as facts.
File:       metalmind.py
File Description:
    Describes the metalmind class, which details how the knowledge and rule bases are stored as well as the operations
    that can be performed on them.
    Rules are stored in tuple form in the format (trigger action).
    Facts are stored in simple single string format.
"""


class Metalmind:
    def __init__(self):
        self.rulebase = []   # List of rules.
        self.knowledge = []  # List of facts.

    def add_fact(self, fact):
        self.knowledge.append(fact)

    def rem_fact(self, fact):
        del self.knowledge[self.knowledge.index(fact)]

    def mod_fact(self, fact, tofact):
        self.rem_fact(fact)
        self.add_fact(tofact)

    def create_rule(self, trigger, action):
        self.rulebase.append((trigger, action))

    def rem_rule(self, rule):
        pass

    def mod_rule(self, rule, torule):
        pass


def bullshit():
    print("bullshit")


if __name__ == "__main__":
    bullshit()
