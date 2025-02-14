def read_int(msg):
    """Reads an integer from user input, ensuring valid input."""
    while True:
        try:
            num = int(input(msg).strip())
        except (ValueError, TypeError):
            print('\033[1;31mPlease enter a valid integer!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;32mUser chose not to enter a number.\033[m')
            return 0
        else:
            return num


def line(length=42):
    """Returns a horizontal line of the specified length."""
    return '-' * length


def text(msg, length=42):
    """Prints a formatted text message within horizontal lines."""
    print(line(length))
    print(msg.center(length))
    print(line(length))


def menu(options):
    """Displays a menu with numbered options and returns the user's choice."""
    text('MAIN MENU')
    for index, item in enumerate(options, start=1):
        print(f'\033[1;33m{index}\033[m - \033[1;34m{item}\033[m')
    print(line())
    choice = read_int('\033[33mYour Option:\033[m ')
    return choice

