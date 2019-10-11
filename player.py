class Player:

    def __init__(self):
        self.name = ""
        self.team = ""
        self.role = ""
        self.config = []

    def getName(self):
        return self.name

    def getTeam(self):
        return self.team

    def getRole(self):
        return self.role

    def getConfig(self):
        return self.config

    def addToConfig(self, text):
        self.config.append(text)

    def removeFromConfig(self, text):
        for i in self.config:
            if i == text:
                self.config.remove(i)

    def printConfig(self):
        output = ""
        output += self.team
        output += " "
        output += self.name
        output += " "
        output += self.role
        output += " "
        for i in self.config:
            output += i
            output += " "
        print(output)
    
    def setInfo(self):
        self.team = self.config[0]
        if self.config[1] == "(B)":
            self.name = self.config[2]
            self.role = self.config[3]
            self.config.remove("(B)")
        else:
            self.name = self.config[1]
            self.role = self.config[2]
        self.config.remove(self.team)
        self.config.remove(self.name)
        self.config.remove(self.role)
        #print(self.team + self.name + self.role)

    def returnConfig(self):
        output = ""
        output += self.team
        output += " "
        output += self.name
        output += " "
        output += self.role
        output += " "
        for i in self.config:
            output += i
            output += " "
        return output
