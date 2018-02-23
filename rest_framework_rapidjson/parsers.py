import codecs

import six
from django.conf import settings
from rapidjson import DM_ISO8601, NM_DECIMAL, UM_CANONICAL, loads
from rest_framework.exceptions import ParseError
from rest_framework.parsers import BaseParser
from rest_framework_rapidjson.renderers import RapidJSONRenderer


class RapidJSONParser(BaseParser):
    """
    Parses JSON-serialized data.
    """
    media_type = 'application/json'
    renderer_class = RapidJSONRenderer

    def parse(self, stream, media_type=None, parser_context=None):
        """
        Parses the incoming bytestream as JSON and returns the resulting data.
        """
        parser_context = parser_context or {}
        encoding = parser_context.get('encoding', settings.DEFAULT_CHARSET)

        try:
            decoded_stream = codecs.getreader(encoding)(stream)
            return loads(
                decoded_stream.read(), datetime_mode=DM_ISO8601,
                uuid_mode=UM_CANONICAL, number_mode=NM_DECIMAL
            )
        except ValueError as exc:
            raise ParseError('JSON parse error - %s' % six.text_type(exc))
