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
    Rules are stored in tuple form in the format (trigger action). Rules are loaded from a text file in an if, then
    format.
    Facts are stored in simple single string format.
    Wish list idea: put the actions of the rules in python code and exec() it.
"""


class Metalmind:
    def __init__(self, rulefile, factfile):
        self.rulebase = []   # List of rules.
        self.knowledge = []  # List of facts.

        # Load all of the initial rules.
        with open(rulefile) as source:
            for rule in source:
                rule_in = self.read_rule(rule)
                self.create_rule(rule_in[0], rule_in[1])

        # Load all of the initial facts.
        with open(factfile) as source:
            for fact in source:
                self.add_fact(fact)

    def add_fact(self, fact):
        if fact not in self.knowledge:
            self.knowledge.append(fact.strip())

    def rem_fact(self, fact):
        del self.knowledge[self.knowledge.index(fact)]

    def mod_fact(self, fact, tofact):
        self.rem_fact(fact)
        self.add_fact(tofact)

    def create_rule(self, trigger, action):
        self.rulebase.append((trigger, action))

    def read_rule(self, raw):
        """
        Assumes each rule is written in an "If this, then that." format.
        Parses a raw rule into a rule in the rule base.
        :param raw:
        :return:
        """
        return raw[3:raw.index(",")].strip(), raw[raw.index(",") + 7:raw.index(".")].strip()

    def rem_rule(self, rule):
        pass

    def mod_rule(self, rule, torule):
        pass

    def check_rule(self, condition):
        """
        Returns true/false based on if a fact fulfilling the condition is in the knowledge base.
        :param condition:
        :return:
        """
        return condition in self.knowledge


if __name__ == "__main__":
    mind = Metalmind("basic.rules", "basic.facts")

    # Print out the initial fact and rule bases
    print("Rules:")
    for r in range(len(mind.rulebase)):
        print("{:4}. If {}, then {}.".format(r+1, mind.rulebase[r][0], mind.rulebase[r][1]))

    print("Facts:")
    for f in range(len(mind.knowledge)):
        print("{:4}. {}".format(f+1, mind.knowledge[f].strip()))

    # START MAIN BODY

    cont = True     # Set a flag to continue processing facts

    while cont:
        for rule in mind.rulebase:
            cont = False    # Reset the continue flag

            if mind.check_rule(rule[0]):
                mind.add_fact(rule[1])
                print("Fact added: " + rule[1])
                # If there has been a fact added to the knowledge base, then we need to go through again
                # to check if it fires any more rules.
                cont = True

    # END MAIN BODY

    # Print out the initial fact and rule bases
    print("Processed Rules:")
    for r in range(len(mind.rulebase)):
        print("{:4}. If {}, then {}.".format(r+1, mind.rulebase[r][0], mind.rulebase[r][1]))

    print("Processed Facts:")
    for f in range(len(mind.knowledge)):
        print("{:4}. {}".format(f+1, mind.knowledge[f].strip()))
