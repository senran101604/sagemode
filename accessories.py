"""
Accesories used to design and color the
output text in terminals
"""

from rich.console import Console

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


class Notify:
    def __init__(self):
        self.console = Console(log_time=False, log_path=False)

    # notify the user how many sites it will search
    def notify_start(self, username, sites):
        start(ascii_art, delay=0.1)

        print(
            color("[", "yellow")
            + color("*", "lightred")
            + color("] ", "yellow")
            + color(f"Searching {len(sites)} sites for target: ", "lightblue")
            + color(username + "\n", "lightyellow")
        )

    # notify the user how many sites the username has been found
    def notify_positive_res(self, username, count):
        print(
            color("[", "yellow")
            + color("+", "lightred")
            + color("] ", "yellow")
            + color("Found ", "lightgreen")
            + color(username, "lightred")
            + color(" in ", "lightgreen")
            + color(count, "lightmagenta")
            + color(" sites", "lightgreen")
        )

    # notify the user where the result is stored
    def notify_stored_result(self, result_file):
        print(
            color("[", "lightgreen")
            + color("@", "yellow")
            + color("] ", "lightgreen")
            + color("Results stored in: ", "lightred")
            + color(result_file, "lightgreen")
        )

    def notify_not_found(self, site):
        self.console.print(
            f"[black][[red]-[black]] [blue]{site}: " + "[yellow]Not Found!"
        )

    def notify_found(self, site, url):
        self.console.print(f"[red][[green]+[red]] [green]{site}: " + f"[blue]{url}")

    def notify_update(self, local_version, remote_version):
        print(
            color("[", "lightred")
            + color("!", "lightred")
            + color("] ", "lightred")
            + color("Update Available!\n", "yellow")
            + color("[", "lightred")
            + color("!", "lightred")
            + color("] ", "lightred")
            + color(f"You are running Version: ", "lightyellow")
            + color(local_version, "lightgreen")
            + color("\n[", "lightred")
            + color("!", "lightred")
            + color("] ", "lightred")
            + color("New Version Available: ", "lightyellow")
            + color(remote_version, "lightgreen")
        )

    def notify_update_error(self, error):
        print(
            color("[", "lightred")
            + color("!", "lightred")
            + color("] ", "lightred")
            + color("A problem occured while checking for an update: ", "yellow")
            + color(error, "lightred")
        )

    def notify_version(self, version):
        print(
            color("\nSageMode ", "lightyellow")
            + color(version, "lightred")
        )


if __name__ == "__main__":
    start(ascii_art)
    color("", "show colors")
