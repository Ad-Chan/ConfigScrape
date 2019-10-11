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

    def findSimilar(self, text):
        for j in text:
            if j.lower() in self.name.lower() or j.lower() in self.role.lower() or j.lower() in self.team.lower():
                return True 
            for i in self.config:
                if j.lower() in i.lower():
                    return True
        return False

    def printConfig(self):
        output = "["
        output += self.team
        output += "] ["
        output += self.name
        output += "] ["
        output += self.role
        output += "] "
        for i in self.config:
            output += "["
            output += i
            output += "] "
        print(output)
    
    def setInfo(self):
        #print(self.config)
        self.team = self.config[0]
        self.name = self.config[1]
        self.role = self.config[2]
        self.config.remove(self.team)
        self.config.remove(self.name)
        self.config.remove(self.role)
        #print(self.team + self.name + self.role)

    def returnConfig(self):
        output = ""
        output += self.team
        output += "|"
        output += self.name
        output += "|"
        output += self.role
        output += "|"
        for i in self.config:
            output += i
            output += "|"
        return output

    def checkPlayer(self):
        #print(self.config)
        if len(self.config) <= 0:
            return False
        else:
            return True
