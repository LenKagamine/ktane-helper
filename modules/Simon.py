strikes = 0

result = [
    [ #no vowel
        [ #0 strikes
            # red, blue, green, yellow
            "blue", "yellow", "green", "red"
        ],
        [ #1 strike
            "red", "blue", "yellow", "green"
        ],
        [ # 2 strikes
            "yellow", "green", "blue", "red"
        ]
    ],
    [ #yes vowel
        [ #0 strikes
            "blue", "red", "yellow", "green"
        ],
        [ #1 strike
            "yellow", "green", "blue", "red"
        ],
        [ # 2 strikes
            "green", "red", "yellow", "blue"
        ]
    ]
]
def solve(r, bomb):
    r.say("defusing simon says")
    colours = r.listen("grammars/simon.gram")
    r.say(colours)
    colours = colours.split()[1:]
    answer = "press"
    for i, val in enumerate(colours):
        if colours[i] == "red":
            colours[i] = 0
        elif colours[i] == "blue":
            colours[i] = 1
        elif colours[i] == "green":
            colours[i] = 2
        elif colours[i] == "yellow":
            colours[i] = 3

        answer += " " + str(result[bomb.get_vowel(r)][strikes][colours[i]])

    r.say(answer)


def add_strike():
    global strikes
    strikes += 1