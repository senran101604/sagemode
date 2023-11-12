#! /usr/bin/env python3
"""
Sagemode: Track and Unveil Online identities across social media platforms.
"""
import os
import re
import datetime
import subprocess
import threading
import requests
from argparse import ArgumentParser
from rich.console import Console

from accessories import Notify
from sites import sites


__version__ = "1.0.2"


class Sagemode:
    def __init__(self, username, found_only=False):
        self.console = Console()
        self.notify = Notify
        self.positive_count = 0
        self.username = username
        self.result_file = os.path.join("data", f"{self.username}.txt")
        self.found_only = found_only

    def check_site(self, site, url):
        url = url.format(self.username)
        response = requests.get(url)
        if response.status_code == 200 and self.username in response.text:
            # to prevent multiple threads from accessing/modifying the positive
            # counts simultaneously and prevent race conditions.
            with threading.Lock():
                self.positive_count += 1
            self.console.print(self.notify.found(site, url))
            with open(self.result_file, "a") as f:
                f.write(f"{url}\n")
        if not self.found_only:
            self.console.print(self.notify.not_found(site))

    def start(self):
        """
        Start the search.
        """
        self.console.print(self.notify.start(self.username, sites))

        current_datetime = datetime.datetime.now()
        date = current_datetime.strftime("%m/%d/%Y")
        time = current_datetime.strftime("%I:%M %p")

        with open(self.result_file, "a") as file:
            file.write(f"\n\n{29*'#'} {date}, {time} {29*'#'}\n\n")

        # storage of thread objects
        # will create 76 threads
        threads = []

        try:
            with self.console.status(
                f"[*] Searching for target: {self.username}", spinner="bouncingBall"
            ):
                for site, url in sites.items():
                    # creates a new thread object
                    thread = threading.Thread(target=self.check_site, args=(site, url))
                    # track the thread objects by storing it in the assigned threads list.
                    threads.append(thread)
                    # initiate the execution of the thread
                    thread.start()
                for thread in threads:
                    # waits for each thread to finish before proceeding.
                    # to avoid output problems and maintain desired order of executions
                    thread.join()

            # notify how many sites the username has been found
            self.console.print(
                self.notify.positive_res(self.username, self.positive_count)
            )
            # notify where the result is stored
            self.console.print(self.notify.stored_result(self.result_file))

        except Exception:
            self.console.print_exception()

    def check_for_update(self):
        try:
            r = requests.get(
                "https://raw.githubusercontent.com/senran101604/sagemode/master/sagemode.py"
            )

            remote_version = str(re.findall('__version__ = "(.*)"', r.text)[0])
            local_version = __version__

            if remote_version != local_version:
                self.console.print(self.notify.update(local_version, remote_version))

        except Exception as error:
            self.console.print(self.notify.update_error(error))

    def do_update(self):
        repo_dir = os.path.dirname(os.path.realpath(__file__))
        # ensure we're performing git command in the local git repo directory
        os.chdir(repo_dir)
        subprocess.run(["git", "pull"])


def main():
    # create data folder if it doesn't exist
    if not os.path.exists("data"):
        os.mkdir("data")

    parser = ArgumentParser(description="Sagemode Jutsu: Unleash Your Inner Ninja")
    parser.add_argument(
        "username", help="username to search for", action="store", nargs="?"
    )
    parser.add_argument(
        "-f",
        "--found",
        dest="found",
        help="output only found sites",
        action="store_true",
    )
    parser.add_argument(
        "-v",
        "--version",
        dest="show_version",
        help="Print Sagemode Version",
        action="store_true",
    )
    parser.add_argument(
        "-U", "--update", dest="do_update", help="update Sagemode", action="store_true"
    )
    args = parser.parse_args()

    sagemode = Sagemode(args.username, found_only=args.found)

    # avoid empty username when sagemode run
    if args.username is not None:
        sagemode.start()
    if args.show_version:
        sagemode.console.rule(sagemode.notify.version(__version__))
    if args.do_update:
        sagemode.do_update()

    # always check for update in every run
    sagemode.check_for_update()


if __name__ == "__main__":
    main()
