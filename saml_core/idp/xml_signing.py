"""
Signing code goes here.
"""
# python:
import hashlib
import logging
import string
# other libraries:
from OpenSSL.crypto import  load_certificate, load_privatekey
from OpenSSL.crypto import FILETYPE_PEM
import pem

from OpenSSL.crypto import rsa, sign
# this app:
import saml_core.idp.config_server as  saml2idp_metadata
from saml_core.idp.codex import nice64
from saml_core.idp.xml_templates import SIGNED_INFO, SIGNATURE
import base64

def load_cert_data(certificate_file):
    """
    Returns the certificate data out of the certificate_file.
    """
    certificate = pem.parse_file(certificate_file)
    cert_data = ''.join(certificate[0].pem_str.split('\n')[1:-2])
    return cert_data
    

def get_signature_xml(subject, reference_uri):
    """
    Returns XML Signature for subject.
    """
    config = saml2idp_metadata.SAML2IDP_CONFIG
    private_key_file = config['private_key_file']
    certificate_file = config['certificate_file']
    logging.debug('get_signature_xml - Begin.')
    logging.debug('Using private key file: ' + private_key_file)
    logging.debug('Using certificate file: ' + certificate_file)
    logging.debug('Subject: ' + subject)

    # Hash the subject.
    subject_hash = hashlib.sha1()
    subject_hash.update(subject.encode('utf-8'))
    subject_digest = nice64(subject_hash.digest())
    logging.debug('Subject digest: ' + subject_digest)

    # Create signed_info.
    signed_info = string.Template(SIGNED_INFO).substitute({
        'REFERENCE_URI': reference_uri,
        'SUBJECT_DIGEST': subject_digest,
        })
    logging.debug('SignedInfo XML: ' + signed_info)

    # RSA-sign the signed_info.
    # Load Private key de thuc hien tao chu ky bao mat
    private_key = load_privatekey(FILETYPE_PEM, open(private_key_file, 'rb').read())
    # Tao chu ky
    sign_data = sign(private_key, signed_info, 'sha1')
    # Chuyen chu ky bao mat thanh base 64
    data_base64 = base64.b64encode(sign_data)
    # chuyen base 64 sang dang string binh thuong de tra ve response
    rsa_signature = data_base64.decode("utf-8") 

    # Load the certificate.
    cert_data = load_cert_data(certificate_file)

    # Put the signed_info and rsa_signature into the XML signature.
    signed_info_short = signed_info.replace(' xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', '')
    signature_xml = string.Template(SIGNATURE).substitute({
        'RSA_SIGNATURE': rsa_signature,
        'SIGNED_INFO': signed_info_short,
        'CERTIFICATE': cert_data,
        })
    logging.debug('Signature XML: ' + signature_xml)
    return signature_xml

