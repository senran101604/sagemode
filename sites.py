sites = {
    # Social Media Platforms
    "Facebook": "https://www.facebook.com/{}",
    "Twitter": "https://twitter.com/{}",
    "Instagram": "https://www.instagram.com/{}",
    "LinkedIn": "https://www.linkedin.com/in/{}",
    "YouTube": "https://www.youtube.com/{}",
    "Snapchat": "https://www.snapchat.com/add/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "Discord": "https://discord.com/users/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    # E-commerce & Marketplace
    "eBay": "https://www.ebay.com/usr/{}",
    "Etsy": "https://www.etsy.com/shop/{}",
    "Fiverr": "https://www.fiverr.com/{}",
    "Amazon": "https://www.amazon.com/gp/profile/amzn1.account.{}",
    # Educational Platforms
    "Khan Academy": "https://www.khanacademy.org/profile/{}",
    "Coursera": "https://www.coursera.org/user/{}",
    "edX": "https://www.edx.org/user/{}",
    "Udemy": "https://www.udemy.com/user/{}",
    # Professional & Business Networks
    "Crunchbase": "https://www.crunchbase.com/person/{}",
    "GitHub Gist": "https://gist.github.com/{}",
    "GitHub": "https://www.github.com/{}",
    "GitLab": "https://gitlab.com/{}",
    "Bitbucket": "https://bitbucket.org/{}",
    "Behance": "https://www.behance.net/{}",
    "Dribbble": "https://dribbble.com/{}",
    "Stack Overflow": "https://stackoverflow.com/users/{}",
    # Creative & Multimedia Platforms
    "DeviantArt": "https://{}.deviantart.com",
    "Patreon": "https://www.patreon.com/{}",
    "Flickr": "https://www.flickr.com/people/{}",
    "Vimeo": "https://vimeo.com/{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "500px": "https://500px.com/{}",
    # Blogging & Writing Platforms
    "Blogger": "https://www.blogger.com/profile/{}",
    "Tumblr": "https://{}.tumblr.com/",
    "Medium": "https://medium.com/@{}",
    "Ghost": "https://{}.ghost.io",
    "Wix": "https://{}.wixsite.com/website",
    "Weebly": "https://{}.weebly.com",
    "WordPress": "https://{}.wordpress.com",
    "LiveJournal": "https://{}.livejournal.com",
    "BuzzFeed": "https://buzzfeed.com/{}",
    # Other Platforms
    "Gravatar": "https://en.gravatar.com/{}",
    "SlideShare": "https://www.slideshare.net/{}",
    "HubPages": "https://hubpages.com/@{}",
    "Wikipedia": "https://en.wikipedia.org/wiki/User:{}",
    "DailyMotion": "https://www.dailymotion.com/{}",
    "Vine": "https://vine.co/{}",
    "Mixcloud": "https://www.mixcloud.com/{}/",
    "Patreon": "https://www.patreon.com/{}",
    "Quora": "https://www.quora.com/profile/{}",
    "Wattpad": "https://www.wattpad.com/user/{}",
    # Programming & Coding Platforms
    "CodePen": "https://codepen.io/{}",
    "LeetCode": "https://leetcode.com/{}",
    "Exercism": "https://exercism.io/profiles/{}",
    "Coderbyte": "https://www.coderbyte.com/profile/{}",
    "Codecademy": "https://www.codecademy.com/profiles/{}",
    # Gaming & Streaming Platforms
    "Steam": "https://steamcommunity.com/id/{}",
    "Twitch": "https://www.twitch.tv/{}",
    "PlayStation": "https://my.playstation.com/profile/{}",
    "Nintendo": "https://en-americas-support.nintendo.com/app/social-profile",
    "Origin": "https://www.origin.com/usa/en-us/profile/{}/",
    "Epic Games": "https://www.epicgames.com/account/personal?productName=&lang=en_US",
    "GOG": "https://www.gog.com/u/{}",
    "Ubisoft": "https://club.ubisoft.com/en-US/profile/{}",
    "Spotify": "https://open.spotify.com/user/{}",
    # Additional Platforms
    "Wellfound": "https://wellfound.com/u/{}",
    "SlideShare": "https://www.slideshare.net/{}",
    "F6S": "https://www.f6s.com/{}",
    "Dribbble": "https://dribbble.com/{}",
    "Angel.co": "https://angel.co/{}",
    "Gravatar": "https://en.gravatar.com/{}",
    "SpeakerDeck": "https://speakerdeck.com/{}",
    "Behance": "https://www.behance.net/{}",
    "Academia.edu": "https://{}.academia.edu",
    "ResearchGate": "https://www.researchgate.net/profile/{}",
    "Vimeo": "https://vimeo.com/{}",
    "Keybase": "https://keybase.io/{}",
    "Bitbucket": "https://bitbucket.org/{}",
    "GitLab": "https://gitlab.com/{}",
    "Goodreads": "https://www.goodreads.com/{}",
    "Last.fm": "https://www.last.fm/user/{}",
    "ReverbNation": "https://www.reverbnation.com/{}",
    "Letterboxd": "https://letterboxd.com/{}",
    "Bandcamp": "https://bandcamp.com/{}",
    "Dailymotion": "https://www.dailymotion.com/{}",
    "Vine": "https://vine.co/{}",
    "Quora": "https://www.quora.com/profile/{}",
    "Medium": "https://medium.com/@{}",
    "Mixcloud": "https://www.mixcloud.com/{}",
    "ProductHunt": "https://www.producthunt.com/@{}",
    "Steam": "https://steamcommunity.com/id/{}",
    "Wikipedia": "https://en.wikipedia.org/wiki/User:{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Slack": "https://{}.slack.com",
    "MySpace": "https://www.myspace.com/{}",
    "MyAnimeList": "https://myanimelist.net/profile/{}",
    "BuyMeACoffee": "https://www.buymeacoffee.com/{}",
}

# indicators for false positive 200 responses
soft404_indicators = [
    "This profile could not be found",
    "Sorry, this user was not found.",
    "Page not available",
    "Page Not Found",
    "the profile was either removed ",
    "The specified profile could not be found",
    # for wordpress
    "doesn&apos;t&nbsp;exist",
    "This page doesn't exist",
    "404 Not Found",
]


if __name__ == "__main__":
    from rich import print as rprint

    for site, url in sites.items():
        rprint(f"[bright_green]{site}: [blue]{url}")

    rprint(f"\n[magenta]{len(sites)} Sites")
