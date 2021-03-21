[![Python package](https://github.com/momcilo78/vaccination_news_feed_parser/actions/workflows/python.yml/badge.svg)](https://github.com/momcilo78/vaccination_news_feed_parser/actions/workflows/python.yml)
[![CodeQL](https://github.com/momcilo78/vaccination_news_feed_parser/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/momcilo78/vaccination_news_feed_parser/actions/workflows/codeql-analysis.yml)

# vaccination_news_feed_parser
Repository for a small tool to easier parse and generate the feedback for covid-19 vaccination progress.
## Install from git repository
```
# checkout this repository
git clone git@github.com:momcilo78/vaccination_news_feed_parser.git
# install requirements
pip3 install -r requirements.txt --user
# install localy from source
python3 setup.py install
```
## How to use?
```
usage: cov19extract processDirectURL [-h] [--dry-run] [-v] --url URL [--template {human}]

optional arguments:
  -h, --help          show this help message and exit
  --dry-run           designates if dry run is to be executed. The tool should not change anything. Warning: this feaature is still not fully implemented!
  -v, --verbose       set verbosity level [default: None]
  --url URL           url to be processed, tool will determine if it is able to parse it.
  --template {human}  template generator (default is human) to be used for output
```
