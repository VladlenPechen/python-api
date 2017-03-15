from utilities.random import generate_random_str

static_mail = generate_random_str(10) + '@cisco.com'
static_literal = generate_random_str(10)

header = {'Accept': '*/*'
          }

bodies_list = [{
    'identity': {'email': static_mail,
                 'firstname': 'test'.join(generate_random_str(10)) + 'First',
                 'lastname': 'test'.join(generate_random_str(10)) + 'Last',
                 'status': 'active', 'username': generate_random_str(10) + '@cisco.com'},
    'domain': {'name': static_literal, 'description': generate_random_str(255), 'status': 'active'}},
    {'identity': {'email': generate_random_str(10) + '@cisco.com',
                  'firstname': 'test'.join(generate_random_str(10)) + 'First',
                  'lastname': 'test'.join(generate_random_str(10)) + 'Last',
                  'status': 'active', 'username': generate_random_str(10) + '@cisco.com'},
     'domain': {'name': generate_random_str(10), 'description': generate_random_str(349), 'status': 'active'}},
    {'identity': {'email': generate_random_str(10) + '@cisco.com',
                  'firstname': 'test'.join(generate_random_str(10)) + 'First',
                  'lastname': 'test'.join(generate_random_str(10)) + 'Last',
                  'status': 'active', 'username': generate_random_str(10) + '@cisco.com'},
     'domain': {'name': generate_random_str(10), 'description': generate_random_str(351), 'status': 'active'}},

    # HI-187
    {'identity': {'email': static_mail,
                  'firstname': static_literal,
                  'lastname': static_literal,
                  'status': 'active', 'username': static_mail},
     'domain': {'name': static_literal, 'description': static_literal, 'status': 'active'}
     },
    {'identity': {'email': static_mail,
                  'firstname': static_literal,
                  'lastname': static_literal,
                  'status': 'active', 'username': static_mail},
     'domain': {'name': generate_random_str(10), 'description': static_literal, 'status': 'active'}
     }
]

metadata = [201, 201, 500, 500, 500]
