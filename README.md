## Coder upgrade

This repo intends to automate the upgrade cycle of my Coder deployment.

The Python script calls the GitHub API to retrieve the release tags from `coder/coder`. It parses the JSON response to retrieve the `latest_sha` of the most recent tag, and compares it to the `current_sha` set in the `sha.txt` file.

If the two don't equal, then a new version is available, and a series of commands to upgrade Coder are kicked off using the `os` package. Once Coder is upgraded, the `sha.txt` file is overwritten with the new `sha`. A cron job is present on the Coder host to execute the script once every 12 hours.
