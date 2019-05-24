import saml_core.idp.base as base
import saml_core.idp.exceptions as exceptions
import saml_core.idp.xml_render as xml_render

class Processor(base.Processor):
    """
    cybozu.com-specific SAML 2.0 AuthnRequest to Response Handler Processor.
    """
    def _validate_request(self):
        """
        Validates the _saml_request. Sub-classes should override this and
        throw an Exception if the validation does not succeed.
        """
        super(Processor, self)._validate_request()
        if not 'https://allexceed2019.cybozu.com/saml/acs' in self._request_params['ACS_URL']:
            raise exceptions.CannotHandleAssertion('AssertionConsumerService is not a cybozu URL.')

    def _determine_audience(self):
        self._audience = 'https://allexceed2019.cybozu.com'

    def _format_assertion(self):
        self._assertion_xml = xml_render.get_assertion_xml(self._assertion_params, signed=True)
