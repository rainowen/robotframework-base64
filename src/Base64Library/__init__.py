from .Base64Keywords import Base64Keywords
from .version import VERSION
_version_ = VERSION

class Base64Library(Base64Keywords):
    """ Base64Library is a Base64 encoding and decoding keyword library

    https://github.com/rainowen/robotframework-base64

        Examples:
        | ${data} =    | Hello world |
        | ${encoded} =    | Base64_Encoding | ${data} |
        | ${decoded} =    | Base64_Decoding | ${encoded} |
        | Should Be Equal As Strings |  ${data} | ${decoded} |
    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = VERSION
