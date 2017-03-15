from utilities.random import generate_random_str

static_mail = generate_random_str(10) + '@cisco.com'
static_literal = generate_random_str(10)

auth_data = {'header': {'Authorization': 'Basic dGVzdENsaWVudDpwYXNzd29yZA==',
                        'Content-Type': 'application/x-www-form-urlencoded'},
             'body': {'grant_type': 'password',
                      'username': static_mail, 'password': 'V3RYS0RRY', 'scope': 'profile'}}

header = {
          }

bodies_list = {'identity': {'email': static_mail,
                            'firstname': 'test'.join(generate_random_str(10)) + 'First',
                            'lastname': 'test'.join(generate_random_str(10)) + 'Last',
                            'status': 'active', 'username': generate_random_str(10) + '@cisco.com'},
               'domain': {'name': static_literal, 'description': generate_random_str(255), 'status': 'active'}}

metadata = 200
