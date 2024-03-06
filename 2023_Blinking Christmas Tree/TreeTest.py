import os
import sys
import random
import time
import threading
import math

mutex = threading.Lock()
stop_signal = False

def base_tree(max_width):
    if max_width == 2:
        text = "This is the hand-made tree by young-dumb-broke myself, tree made by recycled material \n\n"
    if max_width == 3:
        text = "This is the tree from the new hire!\n\n"
    if max_width == 4:
        text = "What a year! Salute from 2 years of work experience myself!\n\n"
    if max_width == 5:
        text = "Becoming a senior member of the team!\n\n"
    if max_width >= 6:
        text = "Future is bright! You got this! \n\n"
    text += max_width * " " + "*\n"
    text += (max_width - 1) * " " + "***\n"
    for i in range(1, max_width):
        text += (max_width - i) * " "
        for j in range(i):
            text += "/" + "_"
        text += "\\\n"
        text += (max_width - i) * " "
        text += "/"
        for m in range(i):
            text += "_" + "\\"
        text += "\n"
    if max_width == 2:
        text += (max_width - 1) * " "  + "[_]\n"
    else:
        if max_width % 2 == 0:
            for i in range(math.ceil(max_width / 3)):
                text += (max_width - 1) * " "  + "[_]\n"
        else:
            for i in range(math.ceil(max_width / 3)):
                text += (max_width - 1) * " "  + "[_]\n"
    return text

def rand_change(tree, colors):
    tree_list = list(tree)

    for i, char in enumerate(tree_list):
        if char == "_" and i % 5 == random.choice((0, 1, 4)):
            tree_list[i] = random.choice(colors)
        if char == "[":
            break

    return ''.join(tree_list)

def colored_dot(color):
    if color == "red":
        return f'\033[91m●\033[0m'

    if color == "green":
        return f'\033[92m●\033[0m'

    if color == "yellow":
        return f'\033[93m●\033[0m'

    if color == "blue":
        return f'\033[94m●\033[0m'

def lights(color, indexes, tree):
    global stop_signal
    off = True
    while not stop_signal:
        with mutex:
            for idx in indexes:
                tree[idx] = colored_dot(color) if off else "●"
            os.system('cls' if os.name == "nt" else "clear")
            print(''.join(tree))
        off = not off
        time.sleep(random.uniform(0.1, 0.8))

    #with mutex:
        #for idx in indexes:
            #tree[idx] = '●'
        #print(''.join(tree))


def create_tree(input_size):
    global stop_signal
    stop_signal = False

    if input_size <= 1:
        print("NO TREE THIS SMALL!")
        return

    #stop_signal.clear()
    tree = base_tree(input_size)
    tree = rand_change(tree, ("*", "+", "@", "$"))
    tree = list(tree)

    yellow, red, green, blue = [], [], [], []

    for i, c in enumerate(tree):
        if c == "*":
            yellow.append(i)
            tree[i] = '●'

        if c == "+":
            red.append(i)
            tree[i] = '●'

        if c == "@":
            green.append(i)
            tree[i] = '●'

        if c == "$":
            blue.append(i)
            tree[i] = '●'

    threads = []

    for color, indexes in (('yellow', yellow), ('red', red), ('green', green), ('blue', blue)):
        t = threading.Thread(target=lights, args=(color, indexes, tree))
        threads.append(t)

    for t in threads:
        t.daemon = True
        t.start()

    time.sleep(5)

    #input("\nPress Enter to continue the journey!")

    stop_signal = True

    for t in threads:
        t.join()

while True:
    user_input = input("Please enter an integer or 'exit' to quit: ")
    if user_input.lower() == 'exit':
        break
    try:
        input_size = int(user_input)
        create_tree(input_size)
        stop_signal = False
    except ValueError:
        print("\nPlease enter a valid int or 'exit' to quit")



