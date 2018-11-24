from Speech import Speech
from Bomb import Bomb
import modules.Wires as Wires
import modules.Button as Button
import modules.Simon as Simon
import modules.Memory as Memory

r = Speech()
r.calibrate(duration=5)

b = Bomb()

while True:
    print("1. On the Subject of Wires (defuse wires)")
    print("2. On the Subject of The Button (defuse button)")
    print("4. On the Subject of Simon Says (defuse simon says)")
    print("6. On the Subject of Memory (defuse memory)")
    print("12. Update Strikes (strikes #)")
    print("13. Run Setup (bomb setup)")
    print("14. Undo Memory (undo memory)")
    print("15. Reset Memory (reset memory)")
    r.say("Select a module")
    choice = r.listen("grammars/menu.gram")
    # select module
    if choice == "defuse wires":
        Wires.solve(r, b)
    elif choice == "defuse button":
        Button.solve(r, b)
    elif choice == "defuse simon says":
        Simon.solve(r, b)
    elif choice == "defuse memory":
        Memory.solve(r, b)

    # strikes
    elif choice[0] == "s":
        r.say(choice)
        number = choice.split()[1]
        if number == "zero":
            b.strikes = 0
        elif number == "one":
            b.strikes = 1
        else:
            b.strikes = 2
    # setup
    elif choice == "bomb setup":
        b.setup(r)
    # undo stages
    elif choice == "undo memory":
        Memory.undo(r)
    # reset stages
    elif choice == "reset memory":
        Memory.reset(r)
    # exit
    elif choice == "terminate" or choice == "exit":
        print("---Exit---")
        r.say("goodbye")
        break
