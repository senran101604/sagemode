"""
accessory module used to design and color the output text for pretty terminal
output.
"""

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


def start(banner: str, delay=0.001):
    """
    Parameters:
        banner
        delay=0.2
    """
    # import random
    from time import sleep
    from rich import print as rprint

    for line in banner.split("\n"):
        for character in line:
            if character in ["#", "@", "%", "&"]:
                rprint(f"[yellow]{character}", end="", flush=True)
            else:
                rprint(f"[bright_red]{character}", end="", flush=True)
        print()


class Notify:
    "A helper class for notifications of Sagemode process"

    @staticmethod
    def start(username: str, number_of_sites) -> str:
        start(ascii_art, delay=0.1)
        if username or sites is not None:
            return f"[yellow][[bright_red]*[yellow][yellow]] [bright_blue]Searching {number_of_sites} sites for target: [bright_yellow]{username}"

    # notify the user how many sites the username has been found
    @staticmethod
    def positive_res(username: str, count) -> str:
        return f"\n[yellow][[bright_red]+[yellow]][bright_green] Found [bright_red]{username} [bright_green]in [bright_magenta]{count}[bright_green] sites"

    # notify the user where the result is stored
    @staticmethod
    def stored_result(result_file: str) -> str:
        return f"[bright_green][[yellow]@[bright_green]] [orange3]Results stored in: [bright_green]{result_file}\n"

    @staticmethod
    def not_found(site: str, status_code="") -> str:
        if status_code:
            return f"[black][[red]-[black]] [blue]{site}: [yellow]Not Found! {status_code}"
        return f"[black][[red]-[black]] [blue]{site}: [yellow]Not Found!"

    @staticmethod
    def found(site: str, url: str) -> str:
        return f"[red][[green]+[red]] [green]{site}: [blue]{url}"

    @staticmethod
    def update(local_version: str, remote_version: str) -> str:
        return (
            "[red][[bright_red]![red]] [yellow]Update Available!\n[/yellow]"
            + f"[red][[yellow]![red]] [bright_yellow]You are running Version: [bright_green]{local_version}\n"
            + f"[red][[/red][yellow]![red]][bright_yellow] New Version Available: [bright_green]{remote_version}"
        )

    @staticmethod
    def update_error(error: str) -> str:
        return f"[bright_red][[bright_red]![bright_red]] [bright_yellow]A problem occured while checking for an update: [bright_red]{error}"

    @staticmethod
    def version(version: str) -> str:
        return f"[bright_yellow]Sagemode [bright_red]{version}"


if __name__ == "__main__":
    start(ascii_art)
