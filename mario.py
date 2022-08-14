import argparse

start_data = {
    "points": 0,
    "lives": 3,
    "level": 1.1,
    "improvement": "small mario"
}


def change_points(event, points):
    if event == "hit block":
        new_amount_of_points = points + 100
    elif event == "kill goomba":
        new_amount_of_points = points + 150
    elif event == "kill turtle":
        new_amount_of_points = points + 200
    elif event == "get coin":
        new_amount_of_points = points + 500
    elif event == "get upgrade":
        new_amount_of_points = points + 1000
    else:
        new_amount_of_points = points
    return new_amount_of_points


def change_lives(event, lives, mario):
    if event == "get life":
        new_amount_of_lives = lives + 1
    elif event == "get damaged" and mario == "small mario":
        new_amount_of_lives = lives - 1
    else:
        new_amount_of_lives = lives
    return new_amount_of_lives


def change_level(event, level):
    if event == "finish level" and (level + 0.6).is_integer() is True:
        new_level = round(level + 0.6, 1)
    elif event == "finish level" and (level + 0.6).is_integer() is False:
        new_level = round(level + 0.1, 1)
    else:
        new_level = level
    return new_level


def change_improvement(event, mario):
    if event == "get upgrade" and mario == "small mario":
        new_mario = "big mario"
    elif event == "get upgrade" and mario == "big mario":
        new_mario = "shooting mario"
    elif event == "get damaged" and mario == "shooting mario":
        new_mario = "small mario"
    elif event == "get damaged" and mario == "big mario":
        new_mario = "small mario"
    else:
        new_mario = mario
    return new_mario


def read_file(file_name):
    with open(file_name, 'r') as file_handler:
        file_contents = file_handler.readlines()

    current_points = start_data["points"]
    current_lives = start_data["lives"]
    current_level = start_data["level"]
    current_mario = start_data["improvement"]
    print(
        f"You have {current_points} points, {current_lives} lives, you are on level {current_level} and your Mario is {current_mario}.")
    for read_line in file_contents:
        answer = input(
            "Press 'f' if you want to load next event.\nPress 'n' if you want to load the next game.\nPress 'q' "
            "if you want to quit.\nYour answer: ").strip().lower()
        if answer == "f":
            event = read_line.strip()
            current_points = change_points(event, current_points)
            current_lives = change_lives(event, current_lives, current_mario)
            current_level = change_level(event, current_level)
            current_mario = change_improvement(event, current_mario)
            print(
                f"You have {current_points} points, {current_lives} lives, you are on level {current_level} and "
                f"your Mario is {current_mario}.")
        elif answer == "q":
            print("THE END")
            break
        elif answer == "n":
            new_file = input("Load the file: ")
            read_file(new_file)
            break
        else:
            print("Wrong input! Choose again.")
            continue


def parse_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parsed_args = parser.parse_args()
    return parsed_args


args = parse_cli()

read_file(args.file)


def new_game():
    while True:
        answer = input(
            "Game over.\nPress 'n' if you want to load the next game.\nPress 'q' if you want to quit.\nYour answer: ").strip().lower()
        if answer == "n":
            new_file = input("Load the file: ")
            read_file(new_file)
        elif answer == "q":
            print("THE END")
            break
        else:
            print("Wrong input! Choose again.")
            continue


new_game()
