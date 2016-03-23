def last(wires, col):
    try:
        index = len(wires) - wires[::-1].index(col)
        if index == 1:
            return "1st"
        elif index == 2:
            return "2nd"
        elif index == 3:
            return "3rd"
        else:
            return str(index) + "th"
    except ValueError:
        return "error"


def solve(r, bomb):
    r.say("defusing wires")
    colours = r.listen("grammars/wires.gram")
    r.say("colours: " + colours)

    colnum = {"red": 0, "blue": 0, "white": 0, "black": 0, "yellow": 0}

    wires = colours.split()
    for wire in wires:
        if wire in colnum:
            colnum[wire] += 1

    num = len(wires)
    if num == 3:
        if colnum["red"] == 0:
            r.say("cut the second wire")
        elif colours[-1] == "white":
            r.say("cut the last wire")
        elif colnum["blue"] > 1:
            r.say("cut the " + last(wires, "blue") + " wire")
        else:
            r.say("cut the last wire")
    elif num == 4:
        if colnum["red"] > 1 and bomb.get_digit(r) == "odd":
            r.say("cut the " + last(wires, "red") + " wire")
        elif wires[-1] == "yellow" and colnum["red"] == 0:
            r.say("cut the first wire")
        elif colnum["blue"] == 1:
            r.say("cut the first wire")
        elif colnum["yellow"] > 1:
            r.say("cut the last wire")
        else:
            r.say("cut the second wire")
    elif num == 5:
        if wires[-1] == "black" and bomb.get_digit(r) == "odd":
            r.say("cut the fourth wire")
        elif colnum["red"] == 1 and colnum["yellow"] > 1:
            r.say("cut the first wire")
        elif colnum["black"] == 0:
            r.say("cut the second wire")
        else:
            r.say("cut the first wire")
    elif num == 6:
        if colnum["yellow"] == 0 and bomb.get_digit(r) == "odd":
            r.say("cut the third wire")
        elif colnum["yellow"] == 1 and colnum["white"] > 1:
            r.say("cut the fourth wire")
        elif colnum["red"] == 0:
            r.say("cut the last wire")
        else:
            r.say("cut the fourth wire")
    elif num > 6:
        r.say("error too many wires")
    elif num < 3:
        r.say("error not enough wires")