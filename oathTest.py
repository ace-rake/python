import requests
from requests_oauthlib import OAuth2Session

# These are placeholders, you need to get these from the service you are using (GitHub in this case)
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
authorization_base_url = 'https://github.com/login/oauth/authorize'
token_url = 'https://github.com/login/oauth/access_token'
redirect_uri = 'https://your-redirect-url.com/callback'  # This must match the redirect URI you set up in the GitHub app

# Step 1: User Authorization.
github = OAuth2Session(client_id, redirect_uri=redirect_uri)
authorization_url, state = github.authorization_url(authorization_base_url)

# Redirect the user to the GitHub authorization URL
print("Please go to {%s} and authorize access." % authorization_url)

# Step 2: Get the authorization response
redirect_response = input('Paste the full redirect URL here: ')

# Step 3: Fetch the access token
github.fetch_token(token_url, client_secret=client_secret, authorization_response=redirect_response)

# Step 4: Fetch a protected resource, like the user's profile
response = github.get('https://api.github.com/user')
print(response.json())

