from random import SystemRandom
import string


def generate_random_str(cnt):
    return ''.join(SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in
                   range(cnt))
