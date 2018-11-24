result = [
    [  # no vowel
        [  # 0 strikes
            # red, blue, green, yellow
            "blue", "yellow", "green", "red"
        ],
        [  # 1 strike
            "red", "blue", "yellow", "green"
        ],
        [  # 2 strikes
            "yellow", "green", "blue", "red"
        ]
    ],
    [  # yes vowel
        [  # 0 strikes
            "blue", "red", "yellow", "green"
        ],
        [  # 1 strike
            "yellow", "green", "blue", "red"
        ],
        [  # 2 strikes
            "green", "red", "yellow", "blue"
        ]
    ]
]


def solve(r, bomb):
    r.say("defusing simon says")
    input = r.listen("grammars/simon.gram")
    r.say(input)
    colours = input.split()[1:]
    answer = "press"
    for _, colour in enumerate(colours):
        if colour == "red":
            i = 0
        elif colour == "blue":
            i = 1
        elif colour == "green":
            i = 2
        elif colour == "yellow":
            i = 3

        vowel = bomb.get_vowel(r)
        answer += " " + str(result[vowel][bomb.strikes][i])

    r.say(answer)
