# TODO: add parameter to only print positive results
import os
import datetime
import threading
import requests
from argparse import ArgumentParser

from accessories import dynamic_test_print, Notify
from sites import sites


class Sagemode(Notify):
    def __init__(self):
        super().__init__()
        self.positive_count = 0

    # check for the username exists in the site
    def check_site(self, username, site, url, result_file):
        url = url.format(username)
        response = requests.get(url)
        if response.status_code == 200 and username in response.text:
            # to prevent multiple threads from accessing/modifying the positive
            # counts simultaneously and prevent race conditions.
            with threading.Lock():
                self.positive_count += 1
            self.notify_found(site, url)
            with open(result_file, "a") as f:
                f.write(f"{url}\n")
        else:
            self.notify_not_found(site)

    def sagemode(self, username):
        self.notify_start(username, sites)
        result_file = os.path.join("data", f"{username}.txt")

        current_datetime = datetime.datetime.now()
        date = current_datetime.strftime("%m/%d/%Y")
        time = current_datetime.strftime("%I:%M %p")

        with open(result_file, "a") as file:
            file.write(f"\n\n{29*'#'} {date}, {time} {29*'#'}\n\n")

        threads = []

        try:
            with self.console.status(f"[*] Searching for target: {username}"):
                for site, url in sites.items():
                    thread = threading.Thread(
                        target=self.check_site, args=(username, site, url,
                                                      result_file)
                    )
                    threads.append(thread)
                    thread.start()

                for thread in threads:
                    thread.join()

            # notify how many sites the username has been found
            self.notify_positive_res(username, self.positive_count)

            # notify where the result is stored
            self.notify_stored_result(result_file)

        except (requests.exceptions.ConnectionError, KeyboardInterrupt):
            self.console.print_exception()


def main():
    parser = ArgumentParser(description="Sagemode Jutsu: Unleash Your Inner Ninja")
    parser.add_argument("username", help="username to search for", action="store")
    args = parser.parse_args()

    Sagemode().sagemode(args.username)


if __name__ == "__main__":
    main()
