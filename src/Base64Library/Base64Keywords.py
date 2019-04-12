import base64

class Base64Keywords(object):
    def __init__(self):
        self.log = None

    def base64_encoding(self, msg = 'hello'):
        #print("[log En]:",msg)
        try:
            msg.encode('utf-8')
            return base64.b64encode(msg.encode('utf-8')).decode('utf-8')
        except:
            return base64.b64encode(msg).decode('utf-8')

    def base64_decoding(self, msg = 'aGVsbG8='):
        try:
            msg.decode('utf-8')
            return base64.b64decode(msg.decode('utf-8'))
        except:
            return base64.b64decode(msg)

if __name__ == "__main__":
    test = Base64Keywords()
    print(test.base64_encoding('hello world'))
    print(test.base64_decoding(test.base64_encoding('hello world')))