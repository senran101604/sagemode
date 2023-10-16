"""
Accesories used to design and color the
output text in terminals
"""


# script that is used to give colors to output text
def color(text, fg: str, bg="") -> str:
    """
    'function to apply colors to printed text.'
    Parameters:
    text        -- string that is going to be the output

    fg          -- foreground color for the text
                -- { white, black, blue, red, green,yellow, lightgreen,
                    magenta, cyan, lightred, lightblue etc.. }

    bg          -- background color for the text

    return:
        a colored text
    """
    # used to color the output and results
    from colorama import Fore, Back, init

    # initialize colorama
    init()
    # first create a dictionary of foreground colors
    fg_colors = {
        "white": Fore.WHITE,
        "black": Fore.BLACK,
        "blue": Fore.BLUE,
        "red": Fore.RED,
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "cyan": Fore.CYAN,
        "magenta": Fore.MAGENTA,
        "lightwhite": Fore.LIGHTWHITE_EX,
        "gray": Fore.LIGHTBLACK_EX,
        "lightgreen": Fore.LIGHTGREEN_EX,
        "lightred": Fore.LIGHTRED_EX,
        "lightblue": Fore.LIGHTBLUE_EX,
        "lightyellow": Fore.LIGHTYELLOW_EX,
        "lightmagenta": Fore.LIGHTMAGENTA_EX,
    }
    # also create a dictionary of background colors
    bg_colors = {
        "white": Back.WHITE,
        "black": Back.BLACK,
        "blue": Back.BLUE,
        "red": Back.RED,
        "green": Back.GREEN,
        "yellow": Back.YELLOW,
        "cyan": Back.CYAN,
        "magenta": Back.MAGENTA,
        "lightwhite": Back.LIGHTWHITE_EX,
        "gray": Back.LIGHTBLACK_EX,
        "lightgreen": Back.LIGHTGREEN_EX,
        "lightred": Back.LIGHTRED_EX,
        "lightblue": Back.LIGHTBLUE_EX,
        "lightyellow": Back.LIGHTYELLOW_EX,
        "lightcyan": Back.LIGHTCYAN_EX,
        "lightmagenta": Back.LIGHTMAGENTA_EX,
    }

    # transform to lowercase letters
    fg = fg.lower()
    if text == "" and fg == "":
        output = ""
    else:
        # first check if fg exist in the dictionary of fg colors
        if fg in fg_colors.keys():
            # finally return the output with colors
            output = fg_colors.get(fg) + str(text)
            # check if bg is given
            if len(bg) > 0:
                # and check if it exist
                if bg in bg_colors.keys():
                    bg = bg.lower()
                    # finally add the bg colors and return it
                    output = bg_colors.get(bg) + fg_colors.get(fg) + str(text)
                else:
                    # print a good warning and solution
                    print(color(f"Invalid: {bg !r} is not included", "lightred"))
                    for bgs in bg_colors:
                        print(color(bgs, "black", bg=bgs))

        else:
            output = ""
            # print a good warning and solution
            print(
                color(
                    f"\n{fg !r} ",
                    "green",
                )
                + color("is not included in the code", "red")
            )
            print(color("maybe some trailing chraracters\n", "blue"))
            # print all the default colors
            print(color("COLORS:", "yellow"))
            for fgs in fg_colors.keys():
                # print the color names with their colors
                print(color(fgs, fgs))
    return output


def dynamic_test_print(
    sign: str,
    text: str,
    sign_color: str,
    text_color: str,
    brackets_color: str,
    another_text="",
    another_text_color="",
) -> None:
    """
    Parameters
        sign               -- sign of the output (common +, -, *)
        text               -- text to print
        sign_color          -- color of the sign
        text_color          -- color of the text
        brackets_color      -- the color of the brackets surrounding the sign

    Optional Parameters:
        another_text        -- text to show after the first text
        another_text_color  -- color of the another_text parameter
    """
    result = (
        color("[", brackets_color)
        + color(sign, sign_color)
        + color("] ", brackets_color)
        + color(text, text_color)
        + color(another_text, another_text_color)
    )
    print(result)


def status(username, site, url, sign):
    """
    Helper function for sagemode

    Positional Arguments:
        username
        site
        url

    Keyword Argument:
        sign        -- sign status: + or -

    return:
        Nothing
    """
    from rich.console import Console

    console = Console()
    with console.status(f"[*] Searching for target: {username}") as status:
        if sign == "+":
            console.log(f"[red][[green]+[red]] [green]{site}: [blue]{url}")
        elif sign == "-":
            console.log(f"[black][[red]-[black]] [blue]{site}: " + "[yellow]Not Found!")
    return


def start(banner, delay=0.001):
    """
    Parameters:
        banner
        delay=0.2
    """
    # import random
    from time import sleep

    for line in banner.split("\n"):
        for character in line:
            if character in ["#", "@", "%", "&"]:
                print(color(character, "yellow"), end="", flush=True)
                # print(character, end='', flush=True)
            else:
                print(color(character, "lightred"), end="", flush=True)
        print()


ascii_art = """
       ____                __  ___        __
      / __/__ ____ ____   /  |/  /__  ___/ /__
     _\ \/ _ `/ _ `/ -_) / /|_/ / _ \/ _  / -_)
    /___/\_,_/\_, /\__/ /_/  /_/\___/\_,_/\__/
             /___/

                  @@@%%%%%@@@
              @%##`````@`````##&@
            @##````````@````````##@
          @%#`````````@@@`````````#%@
          &#``````````@@@``````````#&
         @#````@@@@@@@@@@@@@@@@@````#@
         @%@``@@@@@@@@@@@@@@@@@@@``@%@
         @%@```@@@@@@@@@@@@@@@@@```#%@
         @@# `````````@@@``````````#@@
          &#``````````@@@``````````#&
           @##`````````@`````````##@
             @##```````@``````###@
                @@#````@````#@@
                  @@@%%%%%@@@
"""


if __name__ == "__main__":
    start(ascii_art)
