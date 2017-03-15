from POST.SGpost import BasePostTest
from tests.sign_up_controller.POSTv1_signup.data import bodies_list
from tests.sign_up_controller.POSTv1_signup.data import header
from tests.sign_up_controller.POSTv1_signup.data import metadata
from tests.sign_up_controller import properties


def post_signup_test():
    for body, status in zip(bodies_list, metadata):
        req = {'header': header, 'body': body}
        BasePostTest(properties.url, req, status).launch()
