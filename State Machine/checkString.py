from enum import Enum, auto
import time

class States(Enum):
    STATE_0= auto()
    STATE_1 = auto()
    STATE_2 = auto()
    STATE_3 = auto()

class SETUP:
    def __init__(self):
        self.__state = States.STATE_0

    def set_state(self, state):
        self.__state = state

    def get_state(self):
        return self.__state


class Check:


    def match(self,s):

        state = SETUP()

        for c in s:
            print("character : ", c, " type: ", type(c))
            print("state: ", state.get_state())
            if state.get_state() == States.STATE_0:
                if c == '@':
                    state.set_state(States.STATE_1)
            elif state.get_state() == States.STATE_1:
                print("c: ", c)
                if c in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    state.set_state(States.STATE_2)
                elif c == '@':
                    state.set_state(States.STATE_1)

            elif state.get_state() == States.STATE_2:
                if c == '#' :
                    state.set_state(States.STATE_3)
                elif c in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    state.set_state(States.STATE_2)
                elif c == '@' :
                    state.set_state(States.STATE_1)

            elif state.get_state() == States.STATE_3:
                if c == '@':
                    state.set_state(States.STATE_1)
                elif c in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    state.set_state(States.STATE_2)

        if state.get_state() == States.STATE_3:
            print("matches")
        else:
            print("Not matches")



string = input("Enter string: ")
check = Check()
check.match(string)


