# TODO: make a an option to save or not save the result of the search
import os
import random
import threading

from argparse import ArgumentParser

import requests

from accessories import ascii_art
from accessories import dynamic_test_print
from accessories import color
from accessories import status
from accessories import start
from requests import exceptions
from rich.console import Console
from sites import sites

console = Console()
# count the number of sites where the user is located
positive_count = 0
# ensure that only one thread can access at a time to avoid unexpected result
# to prevent race conditions: threads accessing shared resource at the same time
count_lock = threading.Lock()


def check_site(username: str, site: str, url: str, dont_write, result_file):
    global positive_count
    # get request to site
    url = url.format(username)
    r = requests.get(url)
    # check the if the status code is okay
    if r.status_code == 200 and username in r.text:
        # acquire the lock
        with count_lock:
            positive_count += 1
        console.log(f"[red][[green]+[red]] [green]{site}: " + f"[blue]{url}")
        # check if the folder for storing results does not exist
        if not os.path.exists("data"):
            os.mkdir("data")
        # write to a file named as the username being searched
        with open(result_file, "a") as f:
            f.write(f"{url}\n")
    else:
        console.log(f"[black][[red]-[black]] [blue]{site}: " + "[yellow]Not Found!")


def sagemode(username: str, specific_site=None, dont_write=False):
    """
    Used to search for usernames using the Sagemode Jutsu
    Parameter:
        username            -- username to search for

    Optional Parameter:
        specific_site       -- specific site to search for username
    """
    start(ascii_art, delay=0.1)
    if specific_site:
        # check to see if the site is a list or a single string if it is a list
        # that means the user gave 2 sites or more to search for in the term
        # then change the status message
        if isinstance(specific_site, list):
            dynamic_test_print(
                "*",
                f"Searching {len(specific_site)} sites for target: ",
                "red",
                "lightblue",
                "yellow",
                another_text=username,
                another_text_color="yellow",
            )
        elif isinstance(specific_site, str):
            dynamic_test_print(
                "*",
                f"Searching 1 site for target: ",
                "red",
                "lightblue",
                "yellow",
                another_text=username,
                another_text_color="yellow",
            )

    else:
        # check the default list of sites for the suername message
        dynamic_test_print(
            "*",
            f"Searching {len(sites)} sites for target: ",
            "red",
            "lightblue",
            "yellow",
            another_text=username,
            another_text_color="yellow",
        )

    print(color("...\n", "lightgreen"))

    result_file = os.path.join("data", f"{username}.txt")
    # console = Console()
    threads = []
    try:
        with console.status(f"[*] Searching for target: {username}"):
            for site, url in sites.items():
                thread = threading.Thread(
                    target=check_site,
                    args=(username, site, url, dont_write, result_file),
                )
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()

        dynamic_test_print(
            "+",
            f"Found {color(username, 'red')} {color('in', 'lightgreen')} {color(positive_count, 'magenta')} sites",
            "lightred",
            "lightgreen",
            "yellow",
        )
        dynamic_test_print(
            "@",
            f"Results stored in: {color(result_file, 'lightgreen')}",
            "yellow",
            "lightred",
            "lightblue",
        )

    except (exceptions.ConnectionError, requests.exceptions.ConnectionError):
        dynamic_test_print(
            "!!", "Please Check Internet Connection\n", "red", "lightred", "gray"
        )
    except KeyboardInterrupt:
        dynamic_test_print("!!", f"Keyboard Interrupt\n", "red", "lightred", "gray")
    return None


def main():
    # TODO: add --no-write or -nw argument
    parser = ArgumentParser(description="Sagemode Jutsu: Unleash Your Inner Ninja")
    parser.add_argument("username", help="username to search for", action="store")
    parser.add_argument(
        "--site",
        "-s",
        help="specify a site(s) to search for",
        action="store",
        dest="site",
        metavar="",
    )
    args = parser.parse_args()

    if args.site:
        if args.site.find(",") != -1:
            sites = args.site.split(",")
            sagemode(args.username, sites)
        else:
            sagemode(args.username, args.site)

    else:
        sagemode(args.username)


if __name__ == "__main__":
    main()
