
from random import randint, shuffle


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


def the_most_insane_encoder(message, **kwargs):

    switches = kwargs.get("switches", 10)
    dict_chars = kwargs.get("encoding_dict", None)
    order_of_encoding = kwargs.get("order_of_encoding", None)
    mode = kwargs.get("mode", " ")

    height = kwargs.get("height", 10)
    width = kwargs.get("width", 10)

    encoders = [BL_left_right_horizontal,
                    BL_south_east_diagonal,
                    BL_south_west_diagonal,
                    BL_top_up_vertical,
                    BR_right_left_horizontal,
                    BR_south_east_diagonal,
                    BR_south_west_diagonal,
                    BR_top_up_vertical,
                    TL_left_right_horizontal_v2,
                    TL_north_east_diagonal,
                    TL_south_west_diagonal,
                    TL_top_down_vertical,
                    TR_right_left_horizontal,
                    TR_north_west_diagonal,
                    TR_south_east_diagonal,
                    TR_top_down_vertical]
    decoders = [BL_left_right_horizontal_revert,
                    BL_south_east_diagonal_revert,
                    BL_south_west_diagonal_revert,
                    BL_top_up_vertical_revert,
                    BR_right_left_horizontal_revert,
                    BR_south_east_diagonal_revert,
                    BR_south_west_diagonal_revert,
                    BR_top_up_vertical_revert,
                    TL_left_right_horizontal_revert,
                    TL_north_east_diagonal_revert,
                    TL_south_west_diagonal_revert,
                    TL_top_down_vertical_revert,
                    TR_right_left_horizontal_revert,
                    TR_north_west_diagonal_revert,
                    TR_south_east_diagonal_revert,
                    TR_top_down_vertical_revert]

    if dict_chars is None:
        dict_chars = make_random_string(32)
        first_sixteen = dict_chars[:16]
        last_sixteen = dict_chars[16:]
    elif len(dict_chars) != 32:
        print("You need exactly 32 characters to make your own dictionary!")
        return
    else:
        first_sixteen = dict_chars[:16]
        last_sixteen = dict_chars[16:]

    encoding_dict = dict(zip(first_sixteen, encoders))
    decoding_dict = dict(zip(last_sixteen, decoders))

    if order_of_encoding is None:
        if switches % 2 == 1:
            order_of_encoding = "".join(choice(first_sixteen) if not x % 2 else choice(last_sixteen)
                                        for x in range(switches))
        else:
            reverts_needed = int(switches / 2)
            order_of_encoding = "".join(map(lambda x: "".join(x), zip(choices(first_sixteen, k=reverts_needed),
                                                                      choices(last_sixteen, k=reverts_needed))))
    else:
        encodes = [order_of_encoding[x] for x in range(0, len(order_of_encoding),2)]
        decodes = [order_of_encoding[x] for x in range(1, len(order_of_encoding),2)]
        if any(encode not in encoding_dict for encode in encodes) or \
                any(decode not in decoding_dict for decode in decodes):
            print("Something's wrong with your order of encoding")
            return

    len_message = len(message)
    print(f"len message {len_message}")
    if mode == "numbers":
        message = ",".join(str(ord(letter)) for letter in message) + ","

        space_left = (height * width) - len(message)
        commas_needed = int(space_left / 5)
        numbers_needed = int(space_left * (4 / 5))

        numbers_needed += (height * width) - (numbers_needed + commas_needed + len(message))

        min_x_num_digits = int("1" + "0" * (numbers_needed - 1))
        max_x_num_digits = int("9" * numbers_needed)

        thing = list(str(randrange(min_x_num_digits, max_x_num_digits))) + list("," * commas_needed)
        shuffle(thing)
        message += "".join(thing)

    else:
        characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV' \
                     'WXYZ 1234567890"\'^[]<>{}\\/|;:.,~!?@#$%=&*()°€¥£-_+'
        message += "".join(choices(characters, k=(height * width)))

    for x, letter in enumerate(order_of_encoding):
        if x % 2 == 0:
            message = encoding_dict[letter](message, height=height, width=width, spaces=0)
        else:
            message = decoding_dict[letter](message, spaces=0)

    return message, order_of_encoding, dict_chars, len_message


def the_most_insane_decoder(message, dict_chars, order_of_encoding, len_message, **kwargs):

    height = kwargs.get("height", 10)
    width = kwargs.get("width", 10)
    mode = kwargs.get("mode", "")

    encoders = [ BL_left_right_horizontal,
                     BL_south_east_diagonal,
                     BL_south_west_diagonal,
                     BL_top_up_vertical,
                     BR_right_left_horizontal,
                     BR_south_east_diagonal,
                     BR_south_west_diagonal,
                     BR_top_up_vertical,
                     TL_left_right_horizontal_v2,
                     TL_north_east_diagonal,
                     TL_south_west_diagonal,
                     TL_top_down_vertical,
                     TR_right_left_horizontal,
                     TR_north_west_diagonal,
                     TR_south_east_diagonal,
                     TR_top_down_vertical ]
    decoders = [ BL_left_right_horizontal_revert,
                     BL_south_east_diagonal_revert,
                     BL_south_west_diagonal_revert,
                     BL_top_up_vertical_revert,
                     BR_right_left_horizontal_revert,
                     BR_south_east_diagonal_revert,
                     BR_south_west_diagonal_revert,
                     BR_top_up_vertical_revert,
                     TL_left_right_horizontal_revert,
                     TL_north_east_diagonal_revert,
                     TL_south_west_diagonal_revert,
                     TL_top_down_vertical_revert,
                     TR_right_left_horizontal_revert,
                     TR_north_west_diagonal_revert,
                     TR_south_east_diagonal_revert,
                     TR_top_down_vertical_revert ]

    opposite_dict = dict(zip(decoders + encoders, encoders + decoders))

    first_sixteen = dict_chars[:16]
    last_sixteen = dict_chars[16:]

    encoding_dict = dict(zip(first_sixteen, encoders))
    decoding_dict = dict(zip(last_sixteen, decoders))

    result = int(order_of_encoding[0] in encoding_dict)

    for x, letter in enumerate(order_of_encoding[::-1]):
        if x % 2 == result:
            message = opposite_dict[encoding_dict[letter]](message, spaces=0)
        else:
            message = opposite_dict[decoding_dict[letter]](message, height=height, width=width, spaces=0)

    if mode == 'numbers':
        message = "".join(chr(int(number)) for number in message.split(',')[:len_message])
        # message = "".join(map(lambda x: chr(int(x)), message.split(',')[:len_message]))
    else:
        message = message[:len_message]

    return message


# OPTIONS:_______________________________________________________________________
message = "Somebody once told me the world was gonna roll me I ain't the sharpest tool" \
          " in the shed She was looking kind of dumb with her finger and her thumb"
success = 0
height = 30
width = 30
mode = "numbers"

spaces = 2
switch_amount = 10

# _______________________________________________________________________________
encoded_message, encoding_list, thirty_two_chars, len_message = the_most_insane_encoder \
    (message, switches=switch_amount, height=height, width=width, mode=mode)

print(f"scrambled message : \n{encoded_message}"
      f"\norder of encoding : {encoding_list}"
      f"\ndict chars : {thirty_two_chars}")

decoded_message = the_most_insane_decoder \
    (encoded_message, thirty_two_chars, encoding_list, len_message, height=height, width=width, mode=mode)

print(f"decoded message : {decoded_message.strip()}")


