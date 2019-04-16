# fu-clips

[![Build Status](https://travis-ci.com/toku345/fu-clips.svg?branch=master)](https://travis-ci.com/toku345/fu-clips)
[![Maintainability](https://api.codeclimate.com/v1/badges/d08ec756057b41e32ee6/maintainability)](https://codeclimate.com/github/toku345/fu-clips/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/d08ec756057b41e32ee6/test_coverage)](https://codeclimate.com/github/toku345/fu-clips/test_coverage)

# Requirement

- [Vision Kit](https://aiyprojects.withgoogle.com/vision/)
- gpac
- [Slack Bot Token](https://slack.com/apps/A0F7YS25R-bots)
- Slack channel ID

``` console
# in Vision Kit(RaspberryPi)
$ sudo apt-get install -y gpac
```

# Installation

# Usage

https://slack.com/apps/A0F7YS25R-bots


``` console
$ cd /path/to/myclips
$ env SLACK_TOKEN=xxxxx SLACK_CHANNEL_ID=xxxxx python3 main.py
```

# Development

## Requirement

- Python 3.5.3
- gpac

``` console
# in macOS
$ brew install gpac
```

## Run test

``` console
$ cd /path/to/myclips
$ pipenv install --dev
$ pipenv run pytest
```
