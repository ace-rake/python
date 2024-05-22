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
intra_url = 'https://api.intra.42.fr'
# params = {'page[size]': 100, 'filter[first_name]': 'victor'}
params = {'page[size]': 100,
          'page[number]': 2,
          # 'range[pool_year]': '2023, 2023',
          # 'range[pool_month]': 'march,march',
          # 'sort': 'first_name',
          # 'filter[first_name]': 'victor',
          # 'filter[last_name]': 'denissen'
          }

# funcs.print_campusses(oauth)
funcs.print_users_campus_v2(oauth)
# funcs.print_cursusses(oauth)

# users = oauth.get(intra_url + '/v2/campus/12/users', params=params)
# users = oauth.get(intra_url + '/v2/cursus/65/users', params=params)
# users = get_all(oauth, '/v2/')
# users = oauth.get(intra_url + '/v2/me')
# users = get_all(oauth, '/v2/campus/12/users')

# if users.status_code == 200:
#     users = users.json()
#     # for user in users:
#         # if user['active?'] is True:
#         #     print('Login : %s,\tPool year %s,\tPool month %s,\tActive %s' % (user['login'], user['pool_year'], user['pool_month'], user['active?']))
#     print('Name %s,\tid %s,\txp %s' % (users['name'], users['id'], users['cursus_users']['level']))
#         # print(user)
# else:
#     print('2')
# for user in users:
    # print('Login : %s,\tPool year %s,\tPool month %s,\tActive %s,\tlocation %s,\tWallet %s' % (user['login'], user['pool_year'], user['pool_month'], user['active?'], user['location'], user['wallet']))
    # print('name %s,\tcursus %s' % (user['user']['login'], user['cursus']['name']))
    # print('Name %s,\tlvl %s' % (user['user']['login'], user['level']))
    # print(user)

# campusses = oauth.get(intra_url + '/v2/campus/12', params=params)
#
# if campusses.status_code == 200:
#     campusses = campusses.json()
#     for campus in campusses:
#         print("Id :\t%s, Name :\t%s" % (campus['id'], campus['name']))
# else:
#     print('3')
