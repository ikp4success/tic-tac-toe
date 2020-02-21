import fileinput
import random


print("WELCOME TO TIC-TAC-TOE - PYTHON 3")

board_template = """
0|1|2
3|4|5
6|7|8
"""


tc_inputs = {
}

wining_range = [
    "048",
    "258",
    "147",
    "036",
    "012",
    "345",
    "678",
    "246",
]


user_token_dict = {
    "USER_1": "X",
    "USER_2": "O"
}


def validate_board():
    for user_p, user_token in user_token_dict.items():
        user_token_range = []
        for k, v in tc_inputs.items():
            if v == user_token:
                user_token_range.append(k)

        for win_range in wining_range:
            win_range_lst = list(win_range)
            count = 0
            for wr in win_range_lst:
                if wr in user_token_range:
                    count += 1
                if count == 3:
                    return user_p

    if len(allowed_range) == 0:
        return "NOBODY"

    return False


def get_board():
    display_board = board_template
    for k, v in tc_inputs.items():
        display_board = display_board.replace(k, v)

    for num in range(0, 9):
        display_board = display_board.replace(str(num), "")

    return display_board


allowed_range = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def allowed_range_validation(num):
    num = int(num)
    if num in allowed_range:
        allowed_range.remove(num)
        return True
    return False


user = 0
is_computer = False
is_computer_input = input("PLAY AGAINST COMPUTER?(Y OR N) : ")
cmp_text_1 = "USER_1"
cmp_text_2 = "USER_2"
if is_computer_input.upper() == "Y":
    is_computer = True
    cmp_text_1 = "YOUR"
    cmp_text_2 = "COMPUTER"
    print(f"PLAYING AGAINT COMPUTER: {is_computer}")
else:
    print(f"PLAYING AGAINT COMPUTER: {is_computer}")

print("\n\n---INSTRUCTIONS---")
print("\nUSE INDEX TO PLACE PIECE")
print("\n---BOARD TEMPLATE---")
print(board_template)

print(f"\n{cmp_text_1} PIECE: {user_token_dict['USER_1']}")
print(f"{cmp_text_2} PIECE: {user_token_dict['USER_2']}\n")

print(f"\nBEGIN GAME NOW\n")

for line in fileinput.input():
    line = str(line).strip()

    if user == 0:
        print("***USER 1 TURN***")
        if not line:
            print(f"***Type an index***")
            user = 0
            continue

        if allowed_range_validation(line):
            tc_inputs[line] = user_token_dict["USER_1"]
        else:
            print(get_board())
            if int(line) > 8:
                print(f"***Index {line} Is Invalid***")
            else:
                print(f"***Index {line} Used***")
            user = 0
            continue
    elif not is_computer:
        print("***USER 2 TURN***")
        if not line:
            print(f"***Type an index***")
            user = 1
            continue
        if allowed_range_validation(line):
            tc_inputs[line] = user_token_dict["USER_2"]
        else:
            print(get_board())
            if int(line) > 8:
                print(f"***Index {line} Is Invalid***")
            else:
                print(f"***Index {line} Used***")
            user = 1
            continue
    if not validate_board():
        print(get_board())
        if is_computer:
            print("***COMPUTER TURN***")
            c_line = random.choice(allowed_range)
            if allowed_range_validation(c_line):
                tc_inputs[str(c_line)] = user_token_dict["USER_2"]
        if not is_computer:
            user += 1
            if user > 1:
                user = 0
        else:
            user = 0
        print(get_board())
    else:
        print(get_board())
        user_p = validate_board()
        if is_computer and user_p == "USER_2":
            user_p = "COMPUTER"

        print(f"***{user_p} is the winner.***")
        break
