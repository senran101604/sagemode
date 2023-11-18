## Sagemode Jutsu: Simple and Effective OSINT Username Search Tool

![](https://github.com/senran101604/sagemode/blob/master/gif/example_usage.gif)

## Introduction
Sagemode Jutsu is a straightforward and efficient Open Source Intelligence
(OSINT) tool created with simplicity in mind. It allows users to search for
specific usernames across various online platforms, aiding digital investigators
and cybersecurity enthusiasts in their research.


## Installation
**Clone the Repo**
```console
git clone https://github.com/senran101604/sagemode
```
**change directory to sagemode**
```console
cd sagemode
```
**Install Requirements**

```console
python3 -m pip install -r requirements.txt
```

## Reminder
**Please regularly update SageMode for better user experience:**
```console
❯ python3 sagemode.py -U
```

## Key Features
- **Easy to Use:** A user-friendly tool designed for effortless username
  hunting without unnecessary complications.
- **Real-time Feedback:** Receive instant feedback on positive search results,
  providing insight into the username's online presence.
- **Curated List** of sites for more manageable investigation.
  Users are encouraged to submit pull requests if they fix issues or add useful features.

## How to Use
```console
❯ python3 .\sagemode.py --help
usage: sagemode.py [-h] [-f] [-v] [-U] [username]

Sagemode Jutsu: Unleash Your Inner Ninja

positional arguments:
  username       username to search for

optional arguments:
  -h, --help     show this help message and exit
  -f, --found    output only found sites
  -v, --version  Print Sagemode Version
  -U, --update   update Sagemode

```
#### To search for a <target_username> example
```console
$python sagemode.py <target_username>
```

1. Enter the target username.
2. Sagemode Jutsu will deliver real-time results, highlighting where the
   username has been found online.


## Use Cases
- **For Fun**: Explore the online presence of friends, celebrities, or
  fictional characters for entertainment purposes.
- **Digital Investigations:** Gather information about individuals across online
  platforms for investigative purposes.
- **Cybersecurity:** Identify potential security concerns by detecting
  suspicious usernames linked to malicious activities.
- **Online Reputation Management:** Monitor online presence and address
  potential identity-related issues.
- **Research and Analysis:** Gather data for social media analysis, market
  research, or competitive analysis.


## Disclaimer
* Sagemode Jutsu is intended for ethical and legal use. Users are responsible for
  adhering to applicable laws and regulations while utilizing the tool.
* Please be reminded that Sagemode is still in development and might return
  false results. Sites that are most prone to false positives are Facebook and
  Khan Academy.
* I'm in the process of learning and improving. If you find or fix issues or
  have feature suggestions, your pull requests are welcome.


## TODO
- [X] Reduce soft 404 error responses.
- [ ] Add Tests, Sites, etc...
- [ ] Cleaner Code :)


## Contributions
Contributions and feedback are appreciated! Feel free to submit issues,
suggestions, or enhancements via GitHub.

-------------------------------------------------------------------------------
