"""
Python script of a function to guess the user's number with
a summary display of the search interval in the console.

Group : Davoud, Mattéo, Vincent - NSI

It's the final algorithm for the 'lower, higher' game.
"""

def show_interval(
        first: str | int = '?',
        second: str | int = '?',
        line_char: str = '-',
        point_char: str = '^',
        empty_char: str = ' ',
        spacing_margin: int = 5,
        spacing_point: int = 15
    ) -> str:
    """Function for displaying a horizontal line containing two points
    of an interval.

    Args:
        first (str | int, optional): The character(s) of the first bound of the interval. Defaults to '?'.
        second (str | int, optional): The character(s) of the second bound of the interval. Defaults to '?'.
        line_char (str, optional): The character representing the right. Defaults to '-'.
        point_char (str, optional): The character representing the position of the points on the line. Defaults to '^'.
        empty_char (str, optional): The character representing an empty space. Defaults to ' '.
        spacing_margin (int, optional): Line spacing from -∞ to the first point,
        and from the second point to +∞. Defaults to 5.
        spacing_point (int, optional): Line spacing between the two points. Defaults to 15.

    Returns:
        str: Returns a character string spread over two lines, representing the two limits of the interval.
    """

    first, second = str(first), str(second)
    length: int = max(len(first), len(second)) # we look at the longer length for each of the two terminals

    return spacing_margin * empty_char + first.center(length, empty_char) + \
           spacing_point * empty_char + second.center(length, empty_char) + \
           spacing_margin * empty_char + '\n' + \
           spacing_margin * line_char + point_char.center(length, line_char) + \
           spacing_point * line_char + point_char.center(length, line_char) + \
           spacing_margin * line_char

def guess(increase: int = 2, /) -> int:
    """This function allows you to guess a positive or negative integer as you
    answer the input questions. It uses a single question: "Indicate the position
    of your number in relation to x." It then looks to see whether the number is
    greater (1), less (-1), or equal (0) to x.

    Args:
        increase (int, optional): The number to be used as a starting point
        for increasing the number of the second terminal. The milestone will
        become powers of 2 successive 3, then 9, then 81, ... until the end of
        the search interval is found. Defaults to 2.

    Raises:
        Exception: Causes an exception if the increase parameter is less than 2.

    Returns:
        int: Returns the number obtained after the search algorithm.
    """
    if increase < 2: # because 1^2 will always be worth 1
        raise Exception(f"The 'increase' parameter must be greater than or equal to 2: {increase}")

    def find(nbr: str) -> str:
        print(f"Your number is {nbr}.")
        return nbr

    show = lambda start, second: print('\n' + show_interval(start, second))
    ask = lambda nbr: input(f"Indicate the position of your number in relation to {nbr} : ")

    print("Choose a whole number, whether positive or negative.\n\nq & n: exit\n\n-1: lower\n0: equal\n1: higher")
    show('?', '?')

    borne_1: int = 0
    borne_2: str = '?'
    N: int = increase

    while True:
        match ask(borne_1):
            case '1': break
            case '-1':
                borne_2 = borne_1
                N **= 2
                borne_1 -= N
            case '0':
                return find(borne_1)
            case 'q' | 'n': return
            case _: pass

    show(borne_1, borne_2)

    if borne_2 == '?':
        borne_2: int = increase

        while True:
            match ask(borne_2):
                case '-1': break
                case '1':
                    borne_1 = borne_2
                    borne_2 **= 2
                case '0':
                    return find(borne_2)
                case 'q' | 'n': return
                case _: pass

        show(borne_1, borne_2)

    while True:
        milieu: int = round((borne_1 + borne_2) / 2)

        match ask(milieu):
            case '1':
                borne_1 = milieu
            case '-1':
                borne_2 = milieu
            case '0':
                return find(milieu)
            case 'q' | 'n': return
            case _: pass

        if borne_1 + 1 == borne_2:
            return find(milieu)

        show(borne_1, borne_2)

if __name__ == '__main__':
    guess()
