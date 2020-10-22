from time import time
from random import randint, shuffle
from math import sqrt as root

message = "Somebody once told me the world is gonna roll me I ain't the sharpest tool" \
          " in the shed She was looking kind of dumb with her finger and her thumb"


class Self_Editing_String:
    def __init__(self, value):
        self.value = value

    def add(self, new_value):
        self.value += new_value
        return self

    def get_len(self):
        return len(self.value)

    def add_spaces_between_letters(self, spaces=2):
        self.value = "".join(letter + " " * spaces for letter in self.value)
        return self

    def make_self_len(self, length):
        self.value = self.value + " " * (length - len(self.value))
        return self


# TESTS:________________________________________________
def make_array_v2(message, width=10, height=12, spaces=2):
    try:
        if len(message) <= 0 or width < 0 or height < 0:
            print("something went wrong")
            return ""
    except TypeError:
        print("something went wrong")
        return ""
    global total
    empty_string_array = [Self_Editing_String("") for x in range(height)]

    filled_array = [empty_string_array[x % height].add(letter)
                    for x, letter in enumerate(message)
                    if empty_string_array[-1].get_len() < width]

    filled_array = filled_array[:int(root(len(filled_array)))]
    # filled_array = [filled_array[x] for x in range(int(sqrt(len(filled_array))))]

    spaced_array = [line.add_spaces_between_letters(spaces=spaces) for line in filled_array]

    consistant_array = [line.make_self_len(width) for line in spaced_array]

    printed_string = "".join(line.value + "\n" for line in consistant_array)

    return printed_string


# def left_right_horizontal(message, width=10, height=12, spaces=2, start="top"):
#    width *= (1 + spaces)
#
#    message = "".join(letter + " " * spaces for letter in message)
#
#    arranged_array = [message[start:start + width]
#                      for start, x in zip(range(0, len(message), width), range(height))]
#
#    consistant_array = [line + " " * (width - len(line)) + "\n"
#                        for line in arranged_array]
#
#    printed_string = "".join(consistant_array)
#
#    return printed_string


def speed_test():
    height = 1_000
    width = 1_000

    all_char = 'abcdefghijklmnopqrstuvwxyz'

    start_time = time()
    randomized_string = "".join(all_char[randint(0, 25)] for x in range(1_000_000))
    string_time = time() - start_time

    start_time = time()
    og = left_right_horizontal(randomized_string, height=height, width=width, spaces=spaces)
    # print(classless)
    og_time = time() - start_time

    start_time = time()
    v2 = left_right_hor_v2(randomized_string, height=height, width=width, spaces=spaces)
    # print(with_class)
    v2_time = time() - start_time

    print(

        f"Same result for both: {og == v2}\n"
        f"Time it took using og: {round(og_time, 5)} sec(s)\n" \
        f"Time it took using v2 : {round(v2_time, 5)} sec(s)\n" \
        F"Time it took to make the string: {round(string_time, 5)} sec(s)"

    )


# def south_west_diagonal(message, width=12, height=19, spaces=2, start="top-left"):
#    def len_filler(line):
#        return (width * (spaces + 1) - len(line))
#
#    if not (isinstance(message, str) and isinstance(width, int) \
#            and isinstance(width, int) and isinstance(width, int)) \
#            or width < 0 or height < 0 or spaces < 0 or len(message) <= 0:
#        print("something went wrong")
#        return ""
#
#    empty_array = ["" for x in range(height)]
#
#    message_increment = 0
#
#    for x in range(1, len(message) + 1):
#        for y in range(x):
#            if len(empty_array[y % height]) < width * (1 + spaces):
#                if start.lower() == "top-left":
#                    empty_array[y] += message[message_increment] + " " * spaces
#                else:
#                    empty_array[y] += " " * spaces + message[message_increment]
#                message_increment += 1
#
#    if not start.lower() == "top-left":
#        empty_array = [line[::-1] for line in empty_array]
#
#    consistant_array = [line + " " * len_filler(line) + "\n" for line in empty_array]
#
#    printed_array = "".join(consistant_array)
#
#    return printed_array
#
#
# def new_north_east(message, width=12, height=19, spaces=2, start="top-left"):
#    def len_filler(line):
#        return (width * (spaces + 1) - len(line))
#
#    empty_array = ["" for x in range(height + 1)]
#
#    message_increment = 0
#
#    for x in range(len(message[:width * height])):
#        for y in range(x + 1, 0, -1):
#            if len(empty_array[y % (height + 1)]) < width * (1 + spaces) and y % (height + 1) != 0:
#                empty_array[y] += message[message_increment] + " " * spaces
#                message_increment += 1
#
#    consistant_array = [line + " " * len_filler(line) + "\n" for line in empty_array]
#
#    printed_array = "".join(consistant_array[1::])
#    return printed_array


# OFICIAL_________________________
def flip_vertically(double_array):
    return [line[::-1] for line in double_array]


def flip_horizontally(double_array):
    return double_array[::-1]


def make_consistant(double_array, width, spaces):
    return [line + " " * (width * (spaces + 1) - len(line)) + "\n"
            for line in double_array if len(line) > 0]


def remove_spaces_and_make_double_array(message, spaces):
    message = message.split("\n")

    message_array = [[mini_array[x] for x in range(0, len(mini_array), spaces + 1)]
                     for mini_array in message if len(mini_array) != 0]
    return message_array


# ______________VERTICAL____________________
def TL_top_down_vertical(message, width=10, height=12, spaces=2):
    if not (isinstance(message, str) and isinstance(width, int) \
            and isinstance(width, int) and isinstance(width, int)) \
            or width < 0 or height < 0 or spaces < 0 or len(message) <= 0:
        print("something went wrong")
        return ""

    empty_string_array = ["" for x in range(height)]

    for x, letter in zip(range(width * height), message):
        empty_string_array[x % height] += letter + " " * spaces

    consistant_array = make_consistant(empty_string_array, width, spaces)

    printed_string = "".join(consistant_array)

    return printed_string


def TL_top_down_vertical_revert(message, spaces=2):
    if not isinstance(message, str) or not isinstance(spaces, int) \
            or len(message) <= 0 or spaces < 0:
        print("something went wrong")
        return ""

    message_array = remove_spaces_and_make_double_array(message, spaces)

    arranged_array = [
        message_array[x][y]
        for y in range(len(message_array[0]))
        for x in range(len(message_array))
    ]

    printed_string = "".join(arranged_array)  # .strip()
    return printed_string


def TR_top_down_vertical(message, width=10, height=12, spaces=2):
    if not (isinstance(message, str) and isinstance(width, int) \
            and isinstance(width, int) and isinstance(width, int)) \
            or width < 0 or height < 0 or spaces < 0 or len(message) <= 0:
        print("something went wrong")
        return ""

    empty_string_array = ["" for x in range(height)]

    for x, letter in zip(range(width * height), message):
        empty_string_array[x % height] += " " * spaces + letter

    consistant_array = make_consistant(empty_string_array, width, spaces)

    printed_string = "".join(flip_vertically(consistant_array))

    return printed_string


def TR_top_down_vertical_revert(message, spaces=2):
    if not isinstance(message, str) or not isinstance(spaces, int) \
            or len(message) <= 0 or spaces < 0:
        print("something went wrong")
        return ""

    message_array = remove_spaces_and_make_double_array(message, spaces)

    arranged_array = [
        message_array[y][x]
        for x in range(len(message_array[0]) - 1, -1, -1)
        for y in range(len(message_array))
    ]

    printed_string = "".join(arranged_array)  # .strip()

    return printed_string


def BL_top_up_vertical(message, width=10, height=12, spaces=2):
    if not (isinstance(message, str) and isinstance(width, int) \
            and isinstance(width, int) and isinstance(width, int)) \
            or width < 0 or height < 0 or spaces < 0 or len(message) <= 0:
        print("something went wrong")
        return ""

    empty_string_array = TL_top_down_vertical(message, width=width, spaces=spaces, height=height)

    empty_string_array = empty_string_array.split("\n")[::-1]

    printed_string = "".join(line + "\n" for line in empty_string_array)

    return printed_string


def BL_top_up_vertical_revert(message, spaces=2):
    if not isinstance(message, str) or not isinstance(spaces, int) \
            or len(message) <= 0 or spaces < 0:
        print("something went wrong")
        return ""

    message_array = remove_spaces_and_make_double_array(message, spaces)
    message_array = flip_horizontally(message_array)

    arranged_array = [
        message_array[x][y]
        for y in range(len(message_array[0]))
        for x in range(len(message_array))
    ]

    printed_string = "".join(arranged_array)  # .strip()
    return printed_string


def BR_top_up_vertical(message, width=10, height=12, spaces=2):
    if not (isinstance(message, str) and isinstance(width, int) \
            and isinstance(width, int) and isinstance(width, int)) \
            or width < 0 or height < 0 or spaces < 0 or len(message) <= 0:
        print("something went wrong")
        return ""

    empty_string_array = TR_top_down_vertical(message, width=width, spaces=spaces, height=height)

    empty_string_array = empty_string_array.split("\n")[::-1]

    printed_string = "".join(line + "\n" for line in empty_string_array[:-1])

    return printed_string


def BR_top_up_vertical_revert(message, spaces=2):
    if not isinstance(message, str) or not isinstance(spaces, int) \
            or len(message) <= 0 or spaces < 0:
        print("something went wrong")
        return ""

    message_array = remove_spaces_and_make_double_array(message, spaces=spaces)

    message_array = flip_horizontally(message_array)

    arranged_array = [
        message_array[y][x]
        for x in range(len(message_array[0]) - 1, -1, -1)
        for y in range(len(message_array))
    ]

    printed_string = "".join(arranged_array)  # .strip()

    return printed_string


# ______________LEFT_RIGHT____________________
def TL_left_right_horizontal_v2(message, width=10, height=12, spaces=2):
    arranged_array = [message[start:start + width]
                      for start, x in zip(range(0, len(message), width), range(height))]

    added_spaces = ["".join(letter + " " * spaces for letter in mini_array)
                    for mini_array in arranged_array]

    consistant_array = make_consistant(added_spaces, width, spaces)

    printed_string = "".join(consistant_array)

    return printed_string


def TL_left_right_horizontal_revert(message, spaces=2):
    message_array = remove_spaces_and_make_double_array(message, spaces)
    # try:
    printed_string = "".join("".join(line) for line in message_array)  # .strip()
    # except:
    #    print(f"message: {message_array}")

    return printed_string


def BL_left_right_horizontal(message, width=10, height=12, spaces=2):
    arranged_array = [message[start:start + width]
                      for start, x in zip(range(0, len(message), width), range(height))]

    added_spaces = ["".join(letter + " " * spaces for letter in mini_array)
                    for mini_array in arranged_array]

    added_spaces = flip_horizontally(added_spaces)

    consistant_array = make_consistant(added_spaces, width, spaces)

    printed_string = "".join(consistant_array)

    return printed_string


def BL_left_right_horizontal_revert(message, spaces=2):
    message_array = remove_spaces_and_make_double_array(message, spaces)

    message_array = flip_horizontally(message_array)

    printed_string = "".join("".join(line) for line in message_array)  # .strip()

    return printed_string


def TR_right_left_horizontal(message, width=10, height=12, spaces=2):
    arranged_array = [message[start:start + width]
                      for start, x in zip(range(0, len(message), width), range(height))]

    added_spaces = ["".join(" " * spaces + letter for letter in mini_array)
                    for mini_array in arranged_array]

    consistant_array = make_consistant(added_spaces, width, spaces)

    consistant_array = flip_vertically(consistant_array)

    printed_string = "".join(consistant_array)

    return printed_string


def TR_right_left_horizontal_revert(message, spaces=2):
    message_array = remove_spaces_and_make_double_array(message, spaces)

    message_array = flip_vertically(message_array)

    printed_string = "".join("".join(line) for line in message_array)  # .strip()

    return printed_string


def BR_right_left_horizontal(message, width=10, height=12, spaces=2):
    arranged_array = [message[start:start + width]
                      for start, x in zip(range(0, len(message), width), range(height))]

    added_spaces = ["".join(" " * spaces + letter for letter in mini_array)
                    for mini_array in arranged_array]

    consistant_array = make_consistant(added_spaces, width, spaces)

    fliped_array = flip_vertically(consistant_array)

    printed_string = "".join(fliped_array)

    return printed_string


def BR_right_left_horizontal_revert(message, spaces=2):
    message_array = remove_spaces_and_make_double_array(message, spaces)

    message_array = flip_vertically(message_array)

    printed_string = "".join("".join(line) for line in message_array)  # .strip()

    return printed_string


# ______________NORTH_EAST____________________
def TL_north_east_diagonal(message, width=12, height=19, spaces=2):
    empty_string = ["" for x in range(height + 1)]
    message_increment = 0
    repeat = height + width
    not_bigger_than_height = 0

    for x in range(repeat):
        if (x - width) > 0:
            bottom = x - width
        else:
            bottom = 0

        for y in range(x - not_bigger_than_height, bottom, -1):
            # print(f"inc {message_increment}")
            coord = y % (height + 1)

            if message_increment > len(message) or message_increment > len(message) - 1:
                break
            elif coord > bottom:
                empty_string[coord] += message[message_increment] + spaces * " "

                message_increment += 1

        not_bigger_than_height += x > height
    # for thing in empty_string:
    #   print(thing)
    consistant_array = make_consistant(empty_string, width, spaces)

    printed_string = "".join(consistant_array)

    return printed_string


def TL_north_east_diagonal_revert(message, spaces=2):
    if not (isinstance(message, str) and isinstance(spaces, int)) \
            or spaces < 0 or len(message) <= 0:
        print("something went wrong")
        return ""

    final_message = []
    message_array = remove_spaces_and_make_double_array(message, spaces)

    # for line in message_array:
    #    print(line)
    for x in range(len(message), 0, -1):
        thing = x
        while True:
            try:
                final_message += [message_array[thing][-1]]
                message_array[thing].pop(-1)
                thing += 1
            except IndexError:
                break
    # for line in message_array:
    #    print(line)
    mini_array, increment = 0, 0

    while len(message_array[0]) > 0:
        if len(message_array[mini_array]) > 0:
            final_message += [message_array[mini_array][-1]]
            message_array[mini_array].pop(-1)
            mini_array += 1
            mini_array %= (len(message_array))
        else:
            mini_array = 0

    final_message = "".join(final_message[::-1])  # .strip()

    return final_message


def TR_north_west_diagonal(message, width=12, height=19, spaces=2):
    empty_string = ["" for x in range(height + 1)]
    message_increment = 0
    repeat = height + width
    not_bigger_than_height = 0

    for x in range(repeat):
        if (x - width) > 0:
            bottom = x - width
        else:
            bottom = 0

        for y in range(x - not_bigger_than_height, bottom, -1):
            # print(f"inc {message_increment}")
            coord = y % (height + 1)

            if message_increment > len(message) or message_increment > len(message) - 1:
                break
            elif coord > bottom:
                empty_string[coord] += spaces * " " + message[message_increment]
                message_increment += 1

        not_bigger_than_height += x > height
    # for thing in empty_string:
    #   print(thing)
    consistant_array = make_consistant(empty_string, width, spaces)

    consistant_array = flip_vertically(consistant_array)

    printed_string = "".join(consistant_array)

    return printed_string


def TR_north_west_diagonal_revert(message, spaces=2):
    if not (isinstance(message, str) and isinstance(spaces, int)) \
            or spaces < 0 or len(message) <= 0:
        print("something went wrong")
        return ""

    final_message = []
    message_array = remove_spaces_and_make_double_array(message, spaces)

    message_array = flip_vertically(message_array)
    # for line in message_array:
    #    print(line)
    for x in range(len(message), 0, -1):
        thing = x
        while True:
            try:
                final_message += [message_array[thing][-1]]
                message_array[thing].pop(-1)
                thing += 1
            except IndexError:
                break
    # for line in message_array:
    #    print(line)
    mini_array, increment = 0, 0

    while len(message_array[0]) > 0:
        if len(message_array[mini_array]) > 0:
            final_message += [message_array[mini_array][-1]]
            message_array[mini_array].pop(-1)
            mini_array += 1
            mini_array %= (len(message_array))
        else:
            mini_array = 0

    final_message = "".join(final_message[::-1])  # .strip()

    return final_message


def BL_south_east_diagonal(message, width=12, height=19, spaces=2):
    empty_string = ["" for x in range(height + 1)]
    message_increment = 0
    repeat = height + width
    not_bigger_than_height = 0

    for x in range(repeat):
        if (x - width) > 0:
            bottom = x - width
        else:
            bottom = 0

        for y in range(x - not_bigger_than_height, bottom, -1):

            coord = y % (height + 1)

            if message_increment > len(message) or message_increment > len(message) - 1:
                break
            elif coord > bottom:
                empty_string[coord] += message[message_increment] + spaces * " "

                message_increment += 1

        not_bigger_than_height += x > height

    consistant_array = make_consistant(empty_string, width, spaces)

    flipped_array = flip_horizontally(consistant_array)

    printed_string = "".join(flipped_array)

    return printed_string


def BL_south_east_diagonal_revert(message, spaces=2):
    if not (isinstance(message, str) and isinstance(spaces, int)) \
            or spaces < 0 or len(message) <= 0:
        print("something went wrong")
        return ""

    final_message = []
    message_array = remove_spaces_and_make_double_array(message, spaces)
    message_array = flip_horizontally(message_array)

    for x in range(len(message), 0, -1):
        thing = x
        while True:
            try:
                final_message += [message_array[thing][-1]]
                message_array[thing].pop(-1)
                thing += 1
            except IndexError:
                break

    mini_array, increment = 0, 0

    while len(message_array[0]) > 0:
        if len(message_array[mini_array]) > 0:
            final_message += [message_array[mini_array][-1]]
            message_array[mini_array].pop(-1)
            mini_array += 1
            mini_array %= (len(message_array))
        else:
            mini_array = 0

    final_message = "".join(final_message[::-1])  # .strip()

    return final_message


def BR_south_west_diagonal(message, width=12, height=19, spaces=2):
    empty_string = ["" for x in range(height + 1)]
    message_increment = 0
    repeat = height + width
    not_bigger_than_height = 0

    for x in range(repeat):
        if (x - width) > 0:
            bottom = x - width
        else:
            bottom = 0

        for y in range(x - not_bigger_than_height, bottom, -1):

            coord = y % (height + 1)

            if message_increment > len(message) or message_increment > len(message) - 1:
                break
            elif coord > bottom:
                empty_string[coord] += spaces * " " + message[message_increment]
                message_increment += 1

        not_bigger_than_height += x > height

    consistant_array = make_consistant(empty_string, width, spaces)

    consistant_array = flip_vertically(consistant_array)

    flipped_array = flip_horizontally(consistant_array)

    printed_string = "".join(flipped_array)

    return printed_string


def BR_south_west_diagonal_revert(message, spaces=2):
    if not (isinstance(message, str) and isinstance(spaces, int)) \
            or spaces < 0 or len(message) <= 0:
        print("something went wrong")
        return ""

    final_message = []
    message_array = remove_spaces_and_make_double_array(message, spaces)

    message_array = flip_horizontally(message_array)
    message_array = flip_vertically(message_array)


    for x in range(len(message), 0, -1):
        thing = x
        while True:
            try:
                final_message += [message_array[thing][-1]]
                message_array[thing].pop(-1)
                thing += 1
            except IndexError:
                break

    mini_array, increment = 0, 0

    while len(message_array[0]) > 0:
        if len(message_array[mini_array]) > 0:
            final_message += [message_array[mini_array][-1]]
            message_array[mini_array].pop(-1)
            mini_array += 1
            mini_array %= (len(message_array))
        else:
            mini_array = 0

    final_message = "".join(final_message[::-1])  # .strip()

    return final_message


# ______________SOUTH_WEST____________________
def TL_south_west_diagonal(message, width=12, height=19, spaces=2):
    if not (isinstance(message, str) and isinstance(width, int) \
            and isinstance(width, int) and isinstance(width, int)) \
            or width < 0 or height < 0 or spaces < 0 or len(message) <= 0:
        print("something went wrong")
        return ""

    empty_array = ["" for x in range(height)]

    message_increment, begin = 0, 0

    if height * width > len(message):
        repeat = len(message)
    else:
        repeat = height + width

    for x in range(repeat):
        if x > width:
            begin += 1
        for y in range(begin, x):
            if y == height or message_increment > len(message) - 1:
                break
            else:
                empty_array[y] += message[message_increment] + " " * spaces
                message_increment += 1

    consistant_array = make_consistant(empty_array, width, spaces)

    printed_array = "".join(consistant_array)

    return printed_array


def TL_south_west_diagonal_revert(message, spaces=2):
    if not (isinstance(message, str) and isinstance(spaces, int)) \
            or spaces < 0 or len(message) <= 0:
        print("something went wrong")
        return ""

    message_array = remove_spaces_and_make_double_array(message, spaces)

    final_message = []
    height = len(message_array)
    width = len(message_array[0])

    for x in range(width - 1):
        increment = height - 1
        while True:

            next_array = message_array[increment - 1]
            current_array = message_array[increment]

            final_message += current_array[-1]
            current_array.pop(-1)

            if len(next_array) == len(current_array) + 1 or increment == 0:
                break
            else:
                increment -= 1


    for x in range(len(message_array) - 1, -1, -1):
        for y in range(x, x - width, -1):

            try:

                final_message += message_array[y][-1]
                message_array[y].pop(-1)

            except:
                break

    printed_string = "".join(final_message[::-1])  # .strip()
    return printed_string


def TR_south_east_diagonal(message, width=12, height=19, spaces=2):
    def len_filler(line):
        return (width * (spaces + 1) - len(line))

    if not (isinstance(message, str) and isinstance(width, int) \
            and isinstance(width, int) and isinstance(width, int)) \
            or width < 0 or height < 0 or spaces < 0 or len(message) <= 0:
        print("something went wrong")
        return ""

    empty_array = ["" for x in range(height)]

    message_increment, begin = 0, 0

    if height * width > len(message):
        repeat = len(message)
    else:
        repeat = height + width

    for x in range(repeat):
        if x > width:
            begin += 1
        for y in range(begin, x):
            if y == height or message_increment > len(message) - 1:
                break
            else:
                empty_array[y] += " " * spaces + message[message_increment]

                message_increment += 1

    consistant_array = make_consistant(empty_array, width, spaces)

    consistant_array = flip_vertically(consistant_array)

    printed_array = "".join(consistant_array)

    return printed_array


def TR_south_east_diagonal_revert(message, spaces=2):
    if not (isinstance(message, str) and isinstance(spaces, int)) \
            or spaces < 0 or len(message) <= 0:
        print("something went wrong")
        return ""

    message_array = remove_spaces_and_make_double_array(message, spaces)

    message_array = flip_vertically(message_array)

    final_message = []
    height = len(message_array)
    width = len(message_array[0])

    for x in range(width - 1):
        increment = height - 1
        while True:

            next_array = message_array[increment - 1]
            current_array = message_array[increment]

            final_message += current_array[-1]
            current_array.pop(-1)

            if len(next_array) == len(current_array) + 1 or increment == 0:
                break
            else:
                increment -= 1

    for x in range(len(message_array) - 1, -1, -1):
        for y in range(x, x - width, -1):

            try:

                final_message += message_array[y][-1]
                message_array[y].pop(-1)

            except:
                break



    printed_string = "".join(final_message[::-1])  # .strip()
    return printed_string


def BL_south_west_diagonal(message, width=12, height=19, spaces=2):
    if not (isinstance(message, str) and isinstance(width, int) \
            and isinstance(width, int) and isinstance(width, int)) \
            or width < 0 or height < 0 or spaces < 0 or len(message) <= 0:
        print("something went wrong")
        return ""

    empty_array = ["" for x in range(height)]

    message_increment, begin = 0, 0

    if height * width > len(message):
        repeat = len(message)
    else:
        repeat = height + width

    for x in range(repeat):
        if x > width:
            begin += 1
        for y in range(begin, x):
            if y == height or message_increment > len(message) - 1:
                break
            else:
                empty_array[y] += message[message_increment] + " " * spaces
                message_increment += 1

    consistant_array = make_consistant(empty_array, width, spaces)

    flipped_array = flip_horizontally(consistant_array)
    printed_array = "".join(flipped_array)

    return printed_array


def BL_south_west_diagonal_revert(message, spaces=2):
    if not (isinstance(message, str) and isinstance(spaces, int)) \
            or spaces < 0 or len(message) <= 0:
        print("something went wrong")
        return ""

    message_array = remove_spaces_and_make_double_array(message, spaces)
    message_array = flip_horizontally(message_array)
    final_message = []
    height = len(message_array)
    width = len(message_array[0])

    for x in range(width - 1):
        increment = height - 1
        while True:

            next_array = message_array[increment - 1]
            current_array = message_array[increment]

            final_message += current_array[-1]
            current_array.pop(-1)

            if len(next_array) == len(current_array) + 1 or increment == 0:
                break
            else:
                increment -= 1

    for x in range(len(message_array) - 1, -1, -1):
        for y in range(x, x - width, -1):

            try:

                final_message += message_array[y][-1]
                message_array[y].pop(-1)

            except:
                break

    printed_string = "".join(final_message[::-1])  # .strip()
    return printed_string


def BR_south_east_diagonal(message, width=12, height=19, spaces=2):
    if not (isinstance(message, str) and isinstance(width, int) \
            and isinstance(width, int) and isinstance(width, int)) \
            or width < 0 or height < 0 or spaces < 0 or len(message) <= 0:
        print("something went wrong")
        return ""

    empty_array = ["" for x in range(height)]

    message_increment, begin = 0, 0

    if height * width > len(message):
        repeat = len(message)
    else:
        repeat = height + width

    for x in range(repeat):
        if x > width:
            begin += 1
        for y in range(begin, x):
            if y == height or message_increment > len(message) - 1:
                break
            else:
                empty_array[y] += " " * spaces + message[message_increment]

                message_increment += 1

    consistant_array = make_consistant(empty_array, width, spaces)

    consistant_array = flip_vertically(consistant_array)
    flipped_array = flip_horizontally(consistant_array)

    printed_array = "".join(flipped_array)

    return printed_array


def BR_south_east_diagonal_revert(message, spaces=2):
    if not (isinstance(message, str) and isinstance(spaces, int)) \
            or spaces < 0 or len(message) <= 0:
        print("something went wrong")
        return ""

    message_array = remove_spaces_and_make_double_array(message, spaces)

    message_array = flip_vertically(message_array)
    message_array = flip_horizontally(message_array)
    final_message = []
    height = len(message_array)
    width = len(message_array[0])

    for x in range(width - 1):
        increment = height - 1
        while True:

            next_array = message_array[increment - 1]
            current_array = message_array[increment]

            final_message += current_array[-1]
            current_array.pop(-1)

            if len(next_array) == len(current_array) + 1 or increment == 0:
                break
            else:
                increment -= 1

    for x in range(len(message_array) - 1, -1, -1):
        for y in range(x, x - width, -1):

            try:

                final_message += message_array[y][-1]
                message_array[y].pop(-1)

            except:
                break

    printed_string = "".join(final_message[::-1])  # .strip()
    return printed_string


# _____________________________________________________
def make_random_string(length):
    all_char = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV' \
                    'WXYZ 1234567890"\'^[]<>{}\\/|;:.,~!?@#$%=&*()°€¥£-_+')
    shuffle(all_char)
    return all_char[:length]


def the_most_insane_encoder(message, switches, height=10, width=10,
                            type_of_encoding_key="random", encoding_key=""):
    TL_TD = TL_top_down_vertical
    TL_TD_R = TL_top_down_vertical_revert
    TR_TD = TR_top_down_vertical
    TR_TD_R = TR_top_down_vertical_revert
    BL_TU = BL_top_up_vertical
    BL_TU_R = BL_top_up_vertical_revert
    BR_TU = BR_top_up_vertical
    BR_TU_R = BR_top_up_vertical_revert
    TL_LR = TL_left_right_horizontal_v2
    TL_LR_R = TL_left_right_horizontal_revert
    BL_LR = BL_left_right_horizontal
    BL_LR_R = BL_left_right_horizontal_revert
    TR_LR = TR_right_left_horizontal
    TR_LR_R = TR_right_left_horizontal_revert
    BR_RL = BR_right_left_horizontal
    BR_RL_R = BR_right_left_horizontal_revert
    TL_NE = TL_north_east_diagonal
    TL_NE_R = TL_north_east_diagonal_revert
    TR_NW = TR_north_west_diagonal
    TR_NW_R = TR_north_west_diagonal_revert
    BL_SE = BL_south_east_diagonal
    BL_SE_R = BL_south_east_diagonal_revert
    BR_SW = BR_south_west_diagonal
    BR_SW_R = BR_south_west_diagonal_revert
    TL_SW = TL_south_west_diagonal
    TL_SW_R = TL_south_west_diagonal_revert
    TR_SE = TR_south_east_diagonal
    TR_SE_R = TR_south_east_diagonal_revert
    BL_SW = BL_south_west_diagonal
    BL_SW_R = BL_south_west_diagonal_revert
    BR_SE = BR_south_east_diagonal
    BR_SE_R = BR_south_east_diagonal_revert

    opposite_dict = \
        {TL_TD: TL_TD_R,
         TR_TD: TR_TD_R,
         BL_TU: BL_TU_R,
         BR_TU: BR_TU_R,
         TL_LR: TL_LR_R,
         BL_LR: BL_LR_R,
         TR_LR: TR_LR_R,
         BR_RL: BR_RL_R,
         TL_NE: TL_NE_R,
         TR_NW: TR_NW_R,
         BL_SE: BL_SE_R,
         BR_SW: BR_SW_R,
         TL_SW: TL_SW_R,
         TR_SE: TR_SE_R,
         BL_SW: BL_SW_R,
         BR_SE: BR_SE_R,
         TL_TD_R: TL_TD,
         TR_TD_R: TR_TD,
         BL_TU_R: BL_TU,
         BR_TU_R: BR_TU,
         TL_LR_R: TL_LR,
         BL_LR_R: BL_LR,
         TR_LR_R: TR_LR,
         BR_RL_R: BR_RL,
         TL_NE_R: TL_NE,
         TR_NW_R: TR_NW,
         BL_SE_R: BL_SE,
         BR_SW_R: BR_SW,
         TL_SW_R: TL_SW,
         TR_SE_R: TR_SE,
         BL_SW_R: BL_SW,
         BR_SE_R: BR_SE}

    new_encoders = [
        BL_LR,
        BL_SE,
        BL_SW,
        BL_TU,
        BR_RL,
        BR_SE,
        BR_SW,
        BR_TU,
        TL_LR,
        TL_NE,
        TL_SW,
        TL_TD,
        TR_LR,
        TR_NW,
        TR_SE,
        TR_TD
    ]
    new_decoders = [
        BL_LR_R,
        BL_SE_R,
        BL_SW_R,
        BL_TU_R,
        BR_RL_R,
        BR_SE_R,
        BR_SW_R,
        BR_TU_R,
        TL_LR_R,
        TL_NE_R,
        TL_SW_R,
        TL_TD_R,
        TR_LR_R,
        TR_NW_R,
        TR_SE_R,
        TR_TD_R
    ]

    dict_chars = make_random_string(32)
    first_sixteen = dict_chars[:16]
    last_sixteen = dict_chars[16:]

    encoding_dict = {char: func for char, func in zip(first_sixteen, new_encoders)}
    decoding_dict = {char: func for char, func in zip(last_sixteen, new_decoders)}

    order_of_encoding = "".join(first_sixteen[randint(0, 15)] if x % 2 == 0
                                else last_sixteen[randint(0, 15)]
                                for x in range(switches))
    global success
    message = message + " " * (height * width - len(message))
    og_message = message

    for x, letter in enumerate(order_of_encoding):
        if x % 2 == 0:
            message = encoding_dict[letter](message, height=height, width=width, spaces=0)
            # print(f"{encoding_dict[option].__name__}")
        else:
            message = decoding_dict[letter](message, spaces=0)
            # print(f"{decoding_dict[option].__name__}")

    return message, order_of_encoding, dict_chars


def the_most_insane_decoder(message, dict_chars, order_of_encoding, height=10, width=10):
    TL_TD = TL_top_down_vertical
    TL_TD_R = TL_top_down_vertical_revert
    TR_TD = TR_top_down_vertical
    TR_TD_R = TR_top_down_vertical_revert
    BL_TU = BL_top_up_vertical
    BL_TU_R = BL_top_up_vertical_revert
    BR_TU = BR_top_up_vertical
    BR_TU_R = BR_top_up_vertical_revert
    TL_LR = TL_left_right_horizontal_v2
    TL_LR_R = TL_left_right_horizontal_revert
    BL_LR = BL_left_right_horizontal
    BL_LR_R = BL_left_right_horizontal_revert
    TR_LR = TR_right_left_horizontal
    TR_LR_R = TR_right_left_horizontal_revert
    BR_RL = BR_right_left_horizontal
    BR_RL_R = BR_right_left_horizontal_revert
    TL_NE = TL_north_east_diagonal
    TL_NE_R = TL_north_east_diagonal_revert
    TR_NW = TR_north_west_diagonal
    TR_NW_R = TR_north_west_diagonal_revert
    BL_SE = BL_south_east_diagonal
    BL_SE_R = BL_south_east_diagonal_revert
    BR_SW = BR_south_west_diagonal
    BR_SW_R = BR_south_west_diagonal_revert
    TL_SW = TL_south_west_diagonal
    TL_SW_R = TL_south_west_diagonal_revert
    TR_SE = TR_south_east_diagonal
    TR_SE_R = TR_south_east_diagonal_revert
    BL_SW = BL_south_west_diagonal
    BL_SW_R = BL_south_west_diagonal_revert
    BR_SE = BR_south_east_diagonal
    BR_SE_R = BR_south_east_diagonal_revert
    opposite_dict = \
        {TL_TD: TL_TD_R,
         TR_TD: TR_TD_R,
         BL_TU: BL_TU_R,
         BR_TU: BR_TU_R,
         TL_LR: TL_LR_R,
         BL_LR: BL_LR_R,
         TR_LR: TR_LR_R,
         BR_RL: BR_RL_R,
         TL_NE: TL_NE_R,
         TR_NW: TR_NW_R,
         BL_SE: BL_SE_R,
         BR_SW: BR_SW_R,
         TL_SW: TL_SW_R,
         TR_SE: TR_SE_R,
         BL_SW: BL_SW_R,
         BR_SE: BR_SE_R,
         TL_TD_R: TL_TD,
         TR_TD_R: TR_TD,
         BL_TU_R: BL_TU,
         BR_TU_R: BR_TU,
         TL_LR_R: TL_LR,
         BL_LR_R: BL_LR,
         TR_LR_R: TR_LR,
         BR_RL_R: BR_RL,
         TL_NE_R: TL_NE,
         TR_NW_R: TR_NW,
         BL_SE_R: BL_SE,
         BR_SW_R: BR_SW,
         TL_SW_R: TL_SW,
         TR_SE_R: TR_SE,
         BL_SW_R: BL_SW,
         BR_SE_R: BR_SE}
    new_encoders = [
        BL_LR,
        BL_SE,
        BL_SW,
        BL_TU,
        BR_RL,
        BR_SE,
        BR_SW,
        BR_TU,
        TL_LR,
        TL_NE,
        TL_SW,
        TL_TD,
        TR_LR,
        TR_NW,
        TR_SE,
        TR_TD
    ]
    new_decoders = [
        BL_LR_R,
        BL_SE_R,
        BL_SW_R,
        BL_TU_R,
        BR_RL_R,
        BR_SE_R,
        BR_SW_R,
        BR_TU_R,
        TL_LR_R,
        TL_NE_R,
        TL_SW_R,
        TL_TD_R,
        TR_LR_R,
        TR_NW_R,
        TR_SE_R,
        TR_TD_R
    ]
    first_sixteen = dict_chars[:16]
    last_sixteen = dict_chars[16:]

    encoding_dict = {char: func for char, func in zip(first_sixteen, new_encoders)}
    decoding_dict = {char: func for char, func in zip(last_sixteen, new_decoders)}

    if order_of_encoding[0] in encoding_dict:
        result = 1
    else:
        result = 0

    for x, letter in enumerate(order_of_encoding[::-1]):
        if x % 2 == result:
            message = opposite_dict[encoding_dict[letter]](message, spaces=0)
        else:
            message = opposite_dict[decoding_dict[letter]] \
                (message, height=height, width=width, spaces=0)

    return message


def descramble_readable_message(message):
    replace_pairs = ["<",">","\"|","|\""]

    for look_for in replace_pairs:
        print(f"replacing {look_for} with {'(())'}")
        message = message.replace(look_for,"(())")
    message = [line for line in message.split("(())") if len(line) > 0]
    for x, value in enumerate(message):
        if x % 2 == 0:
            message[x] = int(value)
    message = "".join(value * " " if isinstance(value, int) else value for value in message)

    return message


def make_scrambled_message_readable(message):
    def make_num_x_long(number, length):
        return (length - len(str(number))) * "0" + str(number)

    largest = float("-inf")
    count = 0
    print(f"there are {message.count(' ')} spaces in the message")
    for letter in message:
        if letter == " ":
            count += 1
        else:
            if count > largest:
                largest = count
            count = 0
    longest_digit = len(str(largest))

    count = 0
    readable_message = []
    for letter in message:
        if letter == " ":
            count += 1
        else:
            readable_message += [f"<{str(make_num_x_long(count, longest_digit))}>|\"{letter}\"|"]
            count = 0

    readable_message += [f"<{str(make_num_x_long(count, longest_digit))}>"]

    readable_message = ''.join(readable_message)

    return readable_message



# OPTIONS:_______________________________________________________________________
message = "Somebody once told me the world was gonna roll me I ain't the sharpest tool" \
          " in the shed She was looking kind of dumb with her finger and her thumb"
success = 0
height = 1_00
width = 1_00

spaces = 2
switch_amount = 1_000
#encoded_messages = []
#average = []
# _______________________________________________________________________________
encoded_message, encoding_list, thirty_two_chars = the_most_insane_encoder \
    (message, switch_amount, height=height, width=width)
encoded_message = make_scrambled_message_readable(encoded_message)

print(f"scrambled message : \n{encoded_message}"
      f"\norder of encoding : {encoding_list}"
      f"\ndict chars : {thirty_two_chars}")

encoded_message = descramble_readable_message(encoded_message)
decoded_message = the_most_insane_decoder \
    (encoded_message, thirty_two_chars, encoding_list, height=height, width=width)

print(f"decoded message : {decoded_message.strip()}")


