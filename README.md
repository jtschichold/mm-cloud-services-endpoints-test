# Cloud Services Endpoints (Test)

*THIS IS STILL AN EXPERIMENT!! DO NOT USE THIS REPO IN PRODUCTION!!!*

This repo is using Github Actions to automatically mine Cloud Services IP Ranges/Endpoints and translate the results in a format consumable by network security devices.
See [https://github.com/alex/nyt-2020-election-scraper](https://github.com/alex/nyt-2020-election-scraper) for more details about this technique.

The idea is pretty simple:
- every 12 hours the Mine Github Action workflow is triggered
- the workflow grabs the latest versions of the Cloud Services endpoints and filters/translates/aggregates the results in multiple plaintext feeds
- change detection is performed:
  + if there a small change is detected, the new feeds are automatically pushed into the repo
  + if there instead a big change is detected, the workflow creates a PR to ask humans to validate the changes before merge

## GitHub Actions

This repo makes use of the following GitHub Actions:
- [actions/checkout](https://github.com/actions/checkout)
- [jtschichold/mm-cloud-services-miners](https://github.com/jtschichold/mm-cloud-services-miners)
- [jtschichold/mm-process-ip-list](https://github.com/jtschichold/mm-process-ip-list)
- [jtschichold/mm-process-url-list](https://github.com/jtschichold/mm-process-url-list)
- [jtschichold/mm-check-changes](https://github.com/jtschichold/mm-check-changes)
- [peter-evans/create-pull-request](https://github.com/peter-evans/create-pull-request)
