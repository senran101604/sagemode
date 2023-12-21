#! /usr/bin/env python3
"""
Sagemode: Track and Unveil Online identities across social media platforms.
"""
import os
import re
import datetime
import subprocess
import threading
import random
import requests
from argparse import ArgumentParser
from rich.console import Console
from bs4 import BeautifulSoup

from accessories import Notify
from sites import sites, soft404_indicators, user_agents


__version__ = "1.1.3"


class Sagemode:
    def __init__(self, username: str, found_only=False):
        self.console = Console()
        self.notify = Notify
        self.positive_count = 0
        self.username = username
        self.result_file = os.path.join("data", f"{self.username}.txt")
        self.found_only = found_only

    # this function checks if the url not a false positive result, return false
    def is_soft404(self, html_response: str) -> bool:
        # this is for checking the title bar of the page
        soup = BeautifulSoup(html_response, "html.parser")
        page_title = soup.title.string.strip() if soup.title else ""

        # I know this is kinda messy solution but it currently solve.. reduce the problem
        # in soft404 responses (false positives)
        for error_indicator in soft404_indicators:
            if (
                # check if the error indicator is in the html string response
                error_indicator.lower() in html_response.lower()
                # check for the title bar of the page if there are anyi error_indicator
                or error_indicator.lower() in page_title.lower()
                # Specific check sites, since positive result will have the username in the title bar.
                or page_title.lower() == "instagram"
                # patreon's removed user
                or page_title.lower() == "patreon logo"
                or "sign in" in page_title.lower()
            ):
                return True
        return False

    def check_site(self, site: str, url: str, headers):
        url = url.format(self.username)
        # we need headers to avoid being blocked by requesting the website 403 error
        try:
            with requests.Session() as session:
                response = session.get(url, headers=headers)
                # Raises an HTTPError for bad responses
            # further check to reduce false positive results
            if (
                response.status_code == 200
                and self.username.lower() in response.text.lower()
                and not self.is_soft404(response.text)
            ):
                # to prevent multiple threads from accessing/modifying the positive
                # counts simultaneously and prevent race conditions.
                with threading.Lock():
                    self.positive_count += 1
                self.console.print(self.notify.found(site, url))
                with open(self.result_file, "a") as f:
                    f.write(f"{url}\n")
            # the site reurned 404 (user not found)
            else:
                if not self.found_only:
                    self.console.print(self.notify.not_found(site))
        except Exception as  e:
            self.notify.exception(site, e)

    def start(self):
        """
        Start the search.
        """
        self.console.print(self.notify.start(self.username, len(sites)))

        current_datetime = datetime.datetime.now()
        date = current_datetime.strftime("%m/%d/%Y")
        time = current_datetime.strftime("%I:%M %p")
        headers = {"User-Agent": random.choice(user_agents)}

        with open(self.result_file, "a") as file:
            file.write(f"\n\n{29*'#'} {date}, {time} {29*'#'}\n\n")

        # keep track of thread objects.
        threads = []

        try:
            with self.console.status(
                f"[*] Searching for target: {self.username}", spinner="bouncingBall"
            ):
                for site, url in sites.items():
                    # creates a new thread object
                    thread = threading.Thread(target=self.check_site, args=(site, url, headers))
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

    sage = Sagemode(args.username, found_only=args.found)

    # check if the username arguemnt is given then start searching, this will ensure
    # that we can use the --version flag without supplying the username.
    if args.username is not None:
        sage.start()
    else:
        sage.console.print("[?] [bright_green]Please specify a [yellow]username[/yellow] to search for, see [yellow]--help[/yellow] for available parameters.")
    if args.show_version:
        sage.console.rule(sage.notify.version(__version__))
    if args.do_update:
        sage.do_update()

    # always check for update in every run
    sage.check_for_update()


if __name__ == "__main__":
    main()
