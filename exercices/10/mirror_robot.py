class Robot:

    def __init__(self, n):
        self.__nom = n           # nom du robot
        self.__history = []      # mémoire du robot

    def getnom(self):
        return self.__nom

    def __str__(self):
        return str(self.getnom())

    def getHistory(self):
        return self.__history

    def addHistory(self, action):
        self.__history.append(action)

    def clearHistory(self):
        self.__history = []

    def moveforward(self, distance):
        self.addHistory(("forward", distance))

    def movebackward(self, distance):
        self.addHistory(("backward", distance))

    def turnright(self):
        self.addHistory(("right", 90))

    def turnleft(self):
        self.addHistory(("left", 90))

    def __undoAction(self, action):
        # le paramètre action est un tuple comme ("right",90), etc.
        operation = action[0]
        parameter = action[1]
        if operation == "forward":
            self.movebackward(parameter)
        elif operation == "backward":
            self.moveforward(parameter)
        elif operation == "right":
            self.turnleft()
        elif operation == "left":
            self.turnright()

    def unplay(self):
        history = self.getHistory()
        for i in range(len(history), 0, -1):  # parcours la liste dans l'ordre inverse
            self.__undoAction(history[i-1])
        self.clearHistory()  # vide l'historique après avoir annulé les actions


class MirrorRobot(Robot):

    def __init__(self, robot1, robot2):
        name = robot1.getnom() + " | " + robot2.getnom()
        super().__init__(name)
        self.r1 = robot1
        self.r2 = robot2

    def moveforward(self, distance):
        self.r1.moveforward(distance)
        self.r2.movebackward(distance)

    def movebackward(self, distance):
        self.r2.moveforward(distance)
        self.r1.movebackward(distance)

    def turnright(self):
        self.r1.turnright()
        self.r2.turnleft()

    def turnleft(self):
        self.r2.turnright()
        self.r1.turnleft()

    def unplay(self):
        self.r1.unplay()
        self.r2.unplay()

# Essayer de faire l'exo mais je ne le comprends pas bien