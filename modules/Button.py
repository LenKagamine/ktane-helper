def hold(r):
    r.say("hold the button")
    r.say("what is the strip colour?")
    strip = r.listen("grammars/buttonstrip.gram")
    r.say("button strip " + strip)
    if strip == "blue":
        r.say("release at a 4")
    elif strip == "yellow":
        r.say("release at a 5")
    else:
        r.say("release at a 1")


def press(r):
    r.say("press and release the button")


def solve(r, bomb):
    r.say("defusing button")
    button = r.listen("grammars/button.gram")
    r.say("button " + button)

    colour, text = button.split()
    if colour == "blue" and text == "abort":
        hold(r)
    elif bomb.get_bat(r) > 1 and text == "detonate":
        press(r)
    elif colour == "white" and bomb.get_car(r):
        hold(r)
    elif bomb.get_bat(r) > 2 and bomb.get_frk(r):
        press(r)
    elif colour == "red" and text == "hold":
        press(r)
    else:
        hold(r)
