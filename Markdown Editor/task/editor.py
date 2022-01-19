def plain():
    temp_text = input("Text: ")
    return f"{temp_text}"


def bold():
    temp_text = input("Text: ")
    return f"**{temp_text}**"


def italic():
    temp_text = input("Text: ")
    return f"*{temp_text}*"


def header():
    while True:
        level = int(input("Level: "))
        if 0 < level < 7:
            temp_text = input("Text: ")
            return f'{"#" * level} {temp_text}\n'
        else:
            print("The level should be within the range of 1 to 6")


def link():
    label = input("Label: ")
    url = input("URL: ")
    return f"[{label}]({url})"


def in_line_code():
    temp_text = input("Text: ")
    return f"`{temp_text}`"


def ordered_list():
    ordered_string = ""
    while True:
        number_of_rows = int(input("Number of rows: "))
        if number_of_rows > 0:
            for number in range(number_of_rows):
                temp_text = input(f"Row #{number + 1}: ")
                ordered_string += f"{number + 1}. {temp_text}\n"
            return f'{ordered_string}'
        else:
            print("The number of rows should be greater than zero")


def unordered_list():
    unordered_string = ""
    while True:
        number_of_rows = int(input("Number of rows: "))
        if number_of_rows > 0:
            for number in range(number_of_rows):
                temp_text = input(f"Row #{number + 1}: ")
                unordered_string += f"* {temp_text}\n"
            return f'{unordered_string}'
        else:
            print("The number of rows should be greater than zero")


def new_line():
    return "\n"


def help_(text):
    print('''Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line
    Special commands: !help !done''')


def done(text):
    with open("output.md", 'w') as output_file:
        output_file.write(text)


available_formatters = {"plain": plain,
                        "bold": bold,
                        "italic": italic,
                        "header": header,
                        "link": link,
                        "inline-code": in_line_code,
                        "ordered-list": ordered_list,
                        "unordered-list": unordered_list,
                        "new-line": new_line}
special_commands = {"!help": help_,
                    "!done": done}

user_input = ''
text = ''
while user_input != "!done":
    user_input = input("Choose a formatter: ")
    if user_input in [key for key in special_commands]:
        special_commands[user_input](text)
    elif user_input in [key for key in available_formatters]:
        new_text = available_formatters[user_input]()
        text += new_text
    else:
        print("Unknown formatting type or command")
    print(text)
