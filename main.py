"""
Show outdated designers from Airtable

Usage:
	designers.py
	designers.py [-w|--write] [-e ENV]
	designers.py -h|--help
	designers.py -v|--version

Options:
	-w --write          Sync outdated designers
	-h --help           Show this screen
	-v --version        Show version
	-e ENV --env=ENV  Use given file for Airtable configuration [default: .env]
"""

# coding: utf-8
from turtle import end_fill
from docopt import docopt


from api.Mattermost import Mattermost
from core.Designers import Designers
from core.Startups import Startups
from utils.Log import Log
from utils.Env import Env
log = Log()
env = Env()


if __name__ == '__main__':

    arguments = docopt(__doc__, version='1.0')
    write = arguments['-w'] or arguments['--write']
    #env = arguments['ENV'] or ".env"

    startups = Startups()
    startups.add_new_startups()
    startups.update_startups()

    designers = Designers()
    designers.add_new_designers()
    designers.update_designers()

    # Poster un message sur Mattermost
    m = Mattermost(
        env.get('MATTERMOST_URL'),
        env.get('MATTERMOST_KEY')
    )

    # print(log.get())
    m.post(log.get())
