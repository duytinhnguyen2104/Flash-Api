import os

PATH_ROOT = os.getcwd()

PATH = os.path.join(os.path.join(PATH_ROOT, 'saml_core') , 'cerifycate')

SAML2IDP_CONFIG = {
    'autosubmit': True,
    'issuer': 'https://allexceed2019.cybozu.com',
    'signing': True,
    'certificate_file':  os.path.join(PATH, 'certificate.pem'),
    'private_key_file':  os.path.join(PATH,'private-key.pem'),
    'signing    ': True
}

SAML2IDP_REMOTES = {
    'cybozu': {
            'acs_url': 'https://allexceed2019.cybozu.com/saml/acs',
            'processor': 'saml_core.idp.cybozu.Processor',
        },
}