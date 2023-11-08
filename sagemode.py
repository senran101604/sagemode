# TODO add a function to check for updates from my github repository
import os
import re
import datetime
import threading
import requests
from argparse import ArgumentParser

from accessories import Notify
from sites import sites


__version__ = "1.0.1"


class Sagemode(Notify):
    def __init__(self, username, found_only=False):
        super().__init__()
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
            self.notify_found(site, url)
            with open(self.result_file, "a") as f:
                f.write(f"{url}\n")
        if not self.found_only:
            self.notify_not_found(site)

    def start(self):
        """
        Start the search.
        """
        self.notify_start(self.username, sites)

        current_datetime = datetime.datetime.now()
        date = current_datetime.strftime("%m/%d/%Y")
        time = current_datetime.strftime("%I:%M %p")

        with open(self.result_file, "a") as file:
            file.write(f"\n\n{29*'#'} {date}, {time} {29*'#'}\n\n")

        threads = []

        try:
            with self.console.status(f"[*] Searching for target: {self.username}"):
                for site, url in sites.items():
                    thread = threading.Thread(target=self.check_site, args=(site, url))
                    threads.append(thread)
                    thread.start()

                for thread in threads:
                    thread.join()

            # notify how many sites the username has been found
            self.notify_positive_res(self.username, self.positive_count)
            # notify where the result is stored
            self.notify_stored_result(self.result_file)

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
                self.notify_update(local_version, remote_version)

        except Exception as error:
            self.notify_update_error(error)


def main():
    # TODO: add a argument to show version info without giving the required
    # username argument.
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
    args = parser.parse_args()

    sagemode = Sagemode(args.username, found_only=args.found)

    if args.username != None:
        sagemode.start()

    sagemode.check_for_update()


if __name__ == "__main__":
    main()
