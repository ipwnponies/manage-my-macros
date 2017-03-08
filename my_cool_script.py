#!/usr/bin/env python
import sys
from pprint import pprint

import arrow
import yaml
from fitbit.api import Fitbit

from gather_keys_oauth2 import OAuth2Server


def main():
    try:
        with open('config.yaml', 'r') as config_file:
            config = yaml.load(config_file)
    except:
        config = None

    if config:
        client = Fitbit(
            config['client_id'],
            config['client_secret'],
            access_token=config['access_token'],
            refresh_token=config['refresh_token']
        )
    else:
        if not len(sys.argv) == 3:
            print("Arguments: client_id and client_secret")
            sys.exit(1)

        server = OAuth2Server(*sys.argv[1:])
        server.browser_authorize()
        client = server.fitbit
        config = {
            'client_id': sys.argv[1],
            'client_secret': sys.argv[2],
            'access_token': client.client.session.token['access_token'],
            'refresh_token': client.client.session.token['refresh_token'],
        }
        with open('config.yaml', 'w+') as config_file:
            yaml.dump(config, config_file, default_flow_style=False)

    profile = client.user_profile_get()
    print('You are authorized to access data for the user: {}'.format(
        profile['user']['fullName']))

    print('TOKEN\n=====\n')
    for key, value in client.client.session.token.items():
        print('{} = {}'.format(key, value))

    print('Devices:\n')
    pprint(client.get_devices())

    last_week = arrow.now().replace(weeks=-1)
    print('Weight:\n')
    pprint(client.get_bodyweight(last_week.date(), period='30d'))


if __name__ == '__main__':
    exit(main())
