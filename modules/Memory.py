stage = 1
pos = [0, 0, 0, 0, 0]  # position of pressed button
num = [0, 0, 0, 0, 0]  # label of pressed button


def solve(r, bomb):
    global stage, pos, num
    r.say("defusing memory, stage " + str(stage))
    memory = r.listen("grammars/memory.gram")
    r.say(memory)
    memory = memory.split()[1:]
    for i, val in enumerate(memory):
        memory[i] = bomb.stoi(val)

    if stage == 1:
        if memory[0] == 1 or memory[0] == 2:
            r.say("press %d" % memory[2])
            pos[0] = 2
            num[0] = memory[2]
        elif memory[0] == 3:
            r.say("press %d" % memory[3])
            pos[0] = 3
            num[0] = memory[3]
        elif memory[0] == 4:
            r.say("press %d" % memory[4])
            pos[0] = 4
            num[0] = memory[4]

    elif stage == 2:
        if memory[0] == 1:
            r.say("press four")
            pos[1] = memory.index(4)
            num[1] = 4
        elif memory[0] == 2 or memory[0] == 4:
            r.say("press %d" % memory[pos[0]])
            pos[1] = pos[0]
            num[1] = memory[pos[0]]
        elif memory[0] == 3:
            r.say("press %d" % memory[1])
            pos[1] = 1
            num[1] = memory[1]

    elif stage == 3:
        if memory[0] == 1:
            r.say("press %d" % num[1])
            pos[2] = memory.index(num[1])
            num[2] = num[1]
        elif memory[0] == 2:
            r.say("press %d" % num[0])
            pos[2] = memory.index(num[0])
            num[2] = num[0]
        elif memory[0] == 3:
            r.say("press %d" % memory[3])
            pos[2] = 3
            num[2] = memory[3]
        elif memory[0] == 4:
            r.say("press four")
            pos[2] = memory.index(4)
            num[2] = 4

    elif stage == 4:
        if memory[0] == 1:
            r.say("press %d" % memory[pos[0]])
            pos[3] = pos[0]
            num[3] = memory[pos[0]]
        elif memory[0] == 2:
            r.say("press %d" % memory[1])
            pos[3] = 1
            num[3] = memory[1]
        elif memory[0] == 3 or memory[0] == 4:
            r.say("press %d" % memory[pos[1]])
            pos[3] = pos[1]
            num[3] = memory[pos[1]]

    elif stage == 5:
        if memory[0] == 1:
            r.say("press %d" % num[0])
        elif memory[0] == 2:
            r.say("press %d" % num[1])
        elif memory[0] == 3:
            r.say("press %d" % num[3])
        elif memory[0] == 4:
            r.say("press %d" % num[2])

    stage += 1


def reset(r):
    global stage
    stage = 1
    r.say("memory reset")


def undo(r):
    global stage
    if stage > 1:
        stage -= 1
    r.say("memory at stage " + str(stage))
