
#!/usr/bin/env python
import urllib.parse
from zapv2 import ZAPv2

context_id = 1
apiKey = 'zap-api-1337'
context_name = 'Default Context'
target_url = 'http://localhost:3000'

# By default ZAP API client will connect to port 8080
zap = ZAPv2(apikey=apiKey)

# Use the line below if ZAP is not listening on port 8080, for example, if listening on port 8090
# zap = ZAPv2(apikey=apiKey, proxies={'http': 'http://127.0.0.1:8090', 'https': 'http://127.0.0.1:8090'})


def set_include_in_context():
    include_url = 'http://localhost:3000.*'
    zap.context.include_in_context(context_name, include_url)
    print('Configured include and exclude regex(s) in context')


def set_logged_in_indicator():
    logged_in_regex = '\Q<a href="logout.php">Logout</a>\E'
    logged_out_regex = '(?:Location: [./]*login\.php)|(?:\Q<form action="login.php" method="post">\E)'

    zap.authentication.set_logged_in_indicator(context_id, logged_in_regex)
    zap.authentication.set_logged_out_indicator(context_id, logged_out_regex)
    print('Configured logged in indicator regex: ')


def set_json_based_auth():
    login_url = "http://localhost:3000/rest/user/login"
    login_request_data = 'email={%username%}&password={%password%}'

    json_based_config = 'loginUrl=' + urllib.parse.quote(login_url) + '&loginRequestData=' + urllib.parse.quote(login_request_data)
    zap.authentication.set_authentication_method(context_id, 'jsonBasedAuthentication', json_based_config)
    print('Configured form based authentication')


def set_user_auth_config():
    user = 'Test User'
    username = 'test@example.com'
    password = 'testtest'

    user_id = zap.users.new_user(context_id, user)
    user_auth_config = 'username=' + urllib.parse.quote(username) + '&password=' + urllib.parse.quote(password)
    zap.users.set_authentication_credentials(context_id, user_id, user_auth_config)


def add_script():
    script_name = 'jwtScript.js'
    script_type = 'httpsender'
    script_engine = 'Oracle Nashorn'
    file_name = '/tmp/jwtScript.js'
    zap.script.load(script_name, script_type, script_engine, file_name)


set_include_in_context()
add_script()
set_json_based_auth()
set_logged_in_indicator()
set_user_auth_config()