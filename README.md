# Office365 MineMeld Actions

*THIS IS STILL AN EXPERIMENT!! DO NOT USE THIS REPO IN PRODUCTION!!!*

This repo is using Github Actions to automatically mine O365 Endpoint API and translate the results in a format consumable by network security devices.
See [https://github.com/alex/nyt-2020-election-scraper](https://github.com/alex/nyt-2020-election-scraper) for more details about this technique.

The idea is pretty simple:
- every 12 hours the Mine Github Action workflow is triggered
- the workflow grabs the latest versions of the O365 endpoints and translates them in multiple plaintext feeds
- if there was a small change, the new feeds are automatically pushed into the repo
- if there was a large change, the workflow creates a PR to ask humans to validate the changes

## Feeds

| URL |
| --- |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/worldwide/exchange-ips.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/worldwide/exchange-urls.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/worldwide/ips.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/worldwide/sharepoint-ips.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/worldwide/sharepoint-urls.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/worldwide/skype-ips.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/worldwide/skype-urls.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/worldwide/urls.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/germany/exchange-ips.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/germany/exchange-urls.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/germany/ips.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/germany/sharepoint-ips.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/germany/sharepoint-urls.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/germany/skype-ips.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/germany/skype-urls.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/germany/urls.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/china/exchange-ips.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/china/exchange-urls.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/china/ips.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/china/sharepoint-ips.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/china/sharepoint-urls.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/china/skype-ips.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/china/skype-urls.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/china/urls.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/usgovdod/exchange-ips.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/usgovdod/exchange-urls.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/usgovdod/ips.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/usgovdod/sharepoint-ips.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/usgovdod/sharepoint-urls.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/usgovdod/skype-ips.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/usgovdod/skype-urls.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/usgovdod/urls.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/usgovgcchigh/exchange-ips.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/usgovgcchigh/exchange-urls.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/usgovgcchigh/ips.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/usgovgcchigh/sharepoint-ips.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/usgovgcchigh/sharepoint-urls.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/usgovgcchigh/skype-ips.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/usgovgcchigh/skype-urls.txt |
| https://raw.githubusercontent.com/jtschichold/office365-minemeld-actions/main/feeds/usgovgcchigh/urls.txt |
