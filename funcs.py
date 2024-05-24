import json


def get_all(oauth, url, params):
    users = []
    page = 1
    print('Working on getting data')
    while True:
        print('Page %s' % page)
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


def print_pretty_json(data):
    try:
        pretty_json = json.dumps(data, indent=4, sort_keys=True)
        print(pretty_json)
    except TypeError as e:
        print("Error: Provided data is not valid JSON. %s" % e)
    except Exception as e:
        print("An unexpected error occurred: %s" % e)


def filter(json, field, value):
    try:
        filtered_data = [item for item in json if item.get(field) == value]
        return filtered_data
    except KeyError:
        print('KeyError')
        return []
    except TypeError:
        print('TypeError')
        return []


def filter_v2(json, field, field2, value):
    try:
        filtered_data = [item for item in json if item.get(field).get(field2) == value]
        return filtered_data
    except KeyError:
        print('KeyError')
        return []
    except TypeError:
        print('TypeError')
        return []


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

    params = {
              'page[size]': 100,
              'filter[first_name]': 'victor',
              'filter[last_name]': 'denissen',
              'range[pool_year]': '2023, 2024',
              'range[pool_month]': 'july,march',
              'cursus_id': 65,
              }
    users = get_all(oauth, url, params)
    # users = oauth.get(url, params=params).json()
    for user in users:
        if user['active?'] is True:
            # print('Login : %s,\tPool year %s,\tPool month %s,\tId %s' % (user['login'], user['pool_year'], user['pool_month'], user['id']))
            # print(user)
            print_pretty_json(user)


def print_users_cursus(oauth):
    url = 'https://api.intra.42.fr/v2/cursus/21/cursus_users'

    params = {
            'page[size]': 100,
            # 'filter[user_id]': 145793,
            'cursus_id': 65,
            'sort': 'level',
            'filter[campus_id]': 12,
            }
    users = get_all(oauth, url, params)
    filtered_data = filter_v2(users, 'user', 'pool_month', 'march')
    filtered_data = filter_v2(filtered_data, 'user', 'pool_year', '2023')
    for user in filtered_data:
        print('Name %s,\tlvl %s,\t Active ? %s' % (user['user']['login'], user['level'], user['user']['active?']))


def print_user(oauth, id):
    url = 'https://api.intra.42.fr/v2/cursus/21/cursus_users'

    params = {
            'page[size]': 100,
            'filter[user_id]': id,
            # 'range[pool_year]': '2023, 2024',
            'cursus_id': 65,
            'filter[campus_id]': 12,
            }
    user = oauth.get(url, params=params).json()
    print_pretty_json(user)
    return user


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


def get_user_piscine_pals(oauth, first_name, last_name):
    url = 'https://api.intra.42.fr/v2/campus/12/users'

    params = {
              'page[size]': 1,
              'filter[first_name]': first_name,
              'filter[last_name]': last_name,
              'cursus_id': 65,
              }
    response = oauth.get(url, params=params)
    if response.status_code != 200:
        print('failed to retrieve person')
        return []
    user = response.json()
    user_id = user[0]['id']
    user = print_user(oauth, user_id)
    pool_month = user[0]['user']['pool_month']
    pool_year = user[0]['user']['pool_year']
    print(pool_year)
    print(pool_month)
    url = 'https://api.intra.42.fr/v2/campus/12/users'

    params = {
              'page[size]': 100,
              'range[pool_year]': '2023, 2024',
              'range[pool_month]': 'july,march',
              'cursus_id': 65,
              }
    users = get_all(oauth, url, params)
    for user in users:
        if user['active?'] is True:
            print('Login : %s,\tPool year %s,\tPool month %s,\tId %s' % (user['login'], user['pool_year'], user['pool_month'], user['id']))
            # print(user)
            # print_pretty_json(user)
