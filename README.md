# Cloud Services Endpoints (Test)

*THIS IS STILL AN EXPERIMENT!! DO NOT USE THIS REPO IN PRODUCTION!!!*

This repo is using Github Actions to automatically mine Cloud Services IP Ranges/Endpoints and translate the results in a format consumable by network security devices.
See [https://github.com/alex/nyt-2020-election-scraper](https://github.com/alex/nyt-2020-election-scraper) for more details about this technique.

The idea is pretty simple:
- every 12 hours the Mine Github Action workflow is triggered
- the workflow grabs the latest versions of the O365 endpoints and translates them in multiple plaintext feeds
- if there was a small change, the new feeds are automatically pushed into the repo
- if there was a large change, the workflow creates a PR to ask humans to validate the changes

## Feeds
