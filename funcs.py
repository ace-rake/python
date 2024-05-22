def get_all(oauth, url, params):
    users = []
    page = 1
    while True:
        params['page[number]'] = page
        response = oauth.get(url, params=params)
        if response.status_code != 200:
            print('Failed to retrieve data')
            break
        data = response.json()
        if not data:
            break  # No more data to fetch
        users.extend(data)
        page += 1
        # print(page)
    return users


def print_campusses(oauth):
    url = 'https://api.intra.42.fr/v2/campus'

    params = {'page[size]': 100,
              }
    response = oauth.get(url, params=params)
    if response.status_code != 200:
        print('Failed: print campusses')
        return
    campusses = response.json()
    for campus in campusses:
        print('Name: %s,\tId: %s' % (campus['name'], campus['id']))


def print_users_campus(oauth):
    url = 'https://api.intra.42.fr/v2/campus/12/users'

    params = {'page[size]': 100,
              'filter[first_name]': 'victor',
              'filter[last_name]': 'denissen',
              'range[pool_year]': '2023, 2024',
              # 'cursus_id': 65,
              }
    users = get_all(oauth, url, params)
    # users = oauth.get(url, params=params).json()
    for user in users:
        if user['active?'] is True:
            print('Login : %s,\tPool year %s,\tPool month %s,\tId %s' % (user['login'], user['pool_year'], user['pool_month'], user['id']))
            print(user)


def print_users_campus_v2(oauth):
    url = 'https://api.intra.42.fr/v2/cursus/21/cursus_users'

    params = {
                    'page[size]': 100,
                    'filter[user_id]': 145793,
                    # 'range[pool_year]': '2023, 2024',
                    'cursus_id': 65,
                    'filter[campus_id]': 12,
              }
    users = get_all(oauth, url, params)
    # users = oauth.get(url, params=params).json()
    for user in users:
        print('Name %s,\tlvl %s' % (user['user']['login'], user['level']))
        # print(user)


def print_cursusses(oauth):
    url = 'https://api.intra.42.fr/v2/cursus'

    params = {'page[size]': 100,
              }
    response = oauth.get(url, params=params)
    if response.status_code != 200:
        print('Failed: print cursusses')
        return
    cursusses = response.json()
    for cursus in cursusses:
        print('Id: %s,\tKind: %s,\tName %s' % (cursus['id'], cursus['kind'], cursus['name']))
        # print(cursus)
