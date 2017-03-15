from ast import literal_eval
from urllib.parse import urlencode
import requests
from DELETE.SGdelete import BaseDeleteTest
from POST.SGpost import post
from tests.application_identity_controller.DELETEv1_applicationIdentityMappings.data import bodies_list
from tests.application_identity_controller.DELETEv1_applicationIdentityMappings.data import header
from tests.application_identity_controller.DELETEv1_applicationIdentityMappings.data import metadata
from tests.application_identity_controller.DELETEv1_applicationIdentityMappings.data import auth_data
from tests.sign_up_controller.properties import url
from tests.application_identity_controller import properties


# from POST.SGpost import post

#HI-246
def delete_application_identity_mappings_test():
    post(url, bodies_list, header)
    header['Authorization'] = literal_eval(
        requests.post(url=properties.auth_url, data=urlencode(auth_data['body']), headers=auth_data['header'],
                      verify=False).content.decode())['access_token']
    requests.delete(url=properties.url + '/' + header['Authorization'], headers=header, verify=False)
    BaseDeleteTest(properties.url, {'header': header, 'body': {'id': bodies_list['identity']['email']}},
                   metadata).launch()
