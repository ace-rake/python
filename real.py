from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
import funcs

# Your application credentials
client_id = 'u-s4t2ud-d5fa7a00cb5f8d5608f3d50cb56e9f10ba2d66f562d5b80fe5abcf83255516dd'
client_secret = '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'

# Create a client
client = BackendApplicationClient(client_id=client_id)
oauth = OAuth2Session(client=client)

# Get an access token
token_url = 'https://api.intra.42.fr/oauth/token'
token = oauth.fetch_token(token_url=token_url,
                          client_id=client_id,
                          client_secret=client_secret)

# print(token)


# params = {'page[size]': 100,
          # 'page[number]': 2,
          # 'range[pool_year]': '2023, 2023',
          # 'range[pool_month]': 'march,march',
          # 'sort': 'first_name',
          # 'filter[first_name]': 'victor',
          # 'filter[last_name]': 'denissen'
          # }

# funcs.print_campusses(oauth)
# funcs.print_users_campus(oauth)
funcs.get_user_piscine_pals(oauth, 'victor', 'denissen')
# print('\n')
# funcs.print_users_cursus(oauth)
# funcs.print_user(oauth, 145793)
# funcs.print_cursusses(oauth)
