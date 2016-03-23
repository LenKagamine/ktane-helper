class Bomb:
    def __init__(self):
        self.port = None
        self.frk = None
        self.car = None
        self.digit = None
        self.vowel = None
        self.bat = None

        self.ready = False

        if False:
            self.port = True
            self.frk = True
            self.car = True
            self.vowel = True
            self.digit = "odd"
            self.bat = 3
            self.ready = True

    def stoi(self, word):
        units = [
            "zero", "one", "two", "three", "four", "five",
            "six", "seven", "eight", "nine", "even", "odd"
            ]
        if word in units:
            return units.index(word)
        return -1


    def get_port(self, r):
        if self.port is None:
            r.say("parallel port?")
            choice = r.listen("grammars/checkport.gram").split()
            self.port = choice[2] == "yes"
        return self.port


    def get_frk(self, r):
        if self.frk is None:
            r.say("freak indicator?")
            choice = r.listen("grammars/checkfrk.gram").split()
            self.frk = choice[2] == "yes"
        return self.frk


    def get_car(self, r):
        if self.car is None:
            r.say("car indicator?")
            choice = r.listen("grammars/checkcar.gram").split()
            self.car = choice[2] == "yes"
        return self.car


    def get_digit(self, r):
        if self.digit is None:
            r.say("last digit of serial number?")
            choice = r.listen("grammars/checkdigit.gram").split()
            self.digit = self.stoi(choice[2]) % 2 == 0
        return self.digit


    def get_vowel(self, r):
        if self.vowel is None:
            r.say("is there a vowel in there serial number?")
            choice = r.listen("grammars/checkvowel.gram").split()
            self.vowel = choice[2] == "yes"
        return self.vowel


    def get_bat(self, r):
        if self.bat is None:
            r.say("number of batteries?")
            choice = r.listen("grammars/checkbat.gram").split()
            self.bat = self.stoi(choice[1])
        return self.bat


    def setup(self, r):
        r.say("bomb setup")
        while not self.ready:
            choice = r.listen("grammars/bomb.gram")
            r.say(choice)
            choice = choice.split()
            if choice[0] == "parallel":
                self.port = choice[2] == "yes"
            elif choice[0] == "freak":
                self.frk = choice[2] == "yes"
            elif choice[0] == "car":
                self.car = choice[2] == "yes"
            elif choice[0] == "serial":
                self.vowel = choice[2] == "yes"
            elif choice[0] == "last":
                self.digit = self.stoi(choice[2]) % 2 == 0
            elif choice[0] == "batteries":
                self.bat = self.stoi(choice[1])

            if self.port is not None and self.digit is not None and\
                    self.vowel is not None and self.bat is not None and\
                    self.frk is not None and self.car is not None:
                self.ready = True
            else:
                self.ready = False


    def reset(self):
        self.port = None
        self.digit = None
        self.vowel = None
        self.bat = None
        self.frk = None
        self.car = None
        self.ready = False
