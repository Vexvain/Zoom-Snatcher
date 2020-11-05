#  ███████  ██████   ██████  ███    ███     ███████ ███    ██  █████  ████████  ██████ ██   ██ ███████ ██████  #
#     ███  ██    ██ ██    ██ ████  ████     ██      ████   ██ ██   ██    ██    ██      ██   ██ ██      ██   ██ #
#    ███   ██    ██ ██    ██ ██ ████ ██     ███████ ██ ██  ██ ███████    ██    ██      ███████ █████   ██████  #
#   ███    ██    ██ ██    ██ ██  ██  ██          ██ ██  ██ ██ ██   ██    ██    ██      ██   ██ ██      ██   ██ #
#  ███████  ██████   ██████  ██      ██     ███████ ██   ████ ██   ██    ██     ██████ ██   ██ ███████ ██   ██ #
################################################################################################################                                                                                                            
# :) Vexvain :)

import json
import os

import requests

os.system('cls && title [Zoom Snatcher]')

if os.path.exists((config_json := 'Config.json')):
    error = False
    with open(config_json, 'r', encoding='UTF-8', errors='replace') as f:
        try:
            data = json.load(f)
            authorization = data['authorization']
            cookie = data['cookie']
        except (KeyError, json.decoder.JSONDecodeError):
            print('Invalid syntax in Config.json.')
            error = True
        else:
            try:
                x_csrf_token = cookie.split('ct0=')[1].split(';')[0]
                try:
                    x_guest_token = cookie.split('gt=')[1].split(';')[0]
                except IndexError:
                    x_guest_token = cookie.split('gt=')[1]
            except IndexError:
                print('Paste valid headers in Config.json.')
                error = True
else:
    with open(config_json, 'a') as f:
        json.dump({'authorization': 'BEARER TOKEN', 'cookie': 'COOKIE'}, f, indent=4)
    print('Paste your headers in Config.json.')
    error = True

if not error:
    snatched = 0

    def save(text):
        print(text)
        with open('Codes.txt', 'a', encoding='UTF-8', errors='replace') as f:
            f.write(f'{text}\n')

    response = requests.get(
        'https://api.twitter.com/2/search/adaptive.json?include_profile_interstitial_type=1&include'
        '_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mut'
        'e_edge=1&include_can_dm=1&include_can_media_tag=1&skip_status=1&cards_platform=Web-12&incl'
        'ude_cards=1&include_ext_alt_text=true&include_quote_count=true&include_reply_count=1&tweet'
        '_mode=extended&include_entities=true&include_user_entities=true&include_ext_media_color=tr'
        'ue&include_ext_media_availability=true&send_error_codes=true&simple_quoted_tweet=true&q=zo'
        'om%20code&tweet_search_mode=live&count=20&query_source=typed_query&pc=1&spelling_correctio'
        'ns=1&ext=mediaStats%2ChighlightedLabel', headers={
            'accept': '*/*',
            'cookie': cookie,
            'sec-Fetch-Mode': 'cors',
            'sec-Fetch-Dest': 'empty',
            'x-csrf-token': x_csrf_token,
            'sec-Fetch-Site': 'same-site',
            'x-twitter-active-user': 'yes',
            'x-guest-token': x_guest_token,
            'authorization': authorization,
            'x-twitter-client-language': 'sv',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, lik'
                          'e Gecko) Chrome/84.0.4147.125 Safari/537.36'
        }
    )

    try:
        for tweet in response.json()['globalObjects']['tweets'].values():
            content = tweet['full_text']
            if any(i in content for i in ['pass', 'code', 'raid', 'join']) and '@' not in content:
                save(
                    '[POSSIBLE]\n'
                    f'{content}\n'
                    '----------------------------------'
                )
                snatched += 1

            try:
                url = tweet['entities']['urls'][0]['expanded_url']
            except IndexError:
                continue
            if 'us04web.zoom.us' in url and '?pwd=' in url:
                save(
                    '[URL]\n'
                    f'{url}\n'
                    '----------------------------------'
                )
                snatched += 1
            elif 'us04web.zoom.us' in url and '?pwd=' not in url:
                save(
                    '[URL AND TEXT]\n'
                    f'URL: {url}\n'
                    f'TEXT: {content}\n'
                    '----------------------------------'
                )
                snatched += 1
    except KeyError:
        print('Invalid headers.')

    os.system(f'title [Zoom Snatcher] - Snatched: {snatched} && pause >NUL')
else:
    os.system('title [Zoom Snatcher] - Restart required && pause >NUL')
