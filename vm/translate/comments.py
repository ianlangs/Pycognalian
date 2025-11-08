import re

def onword(code):
    return re.sub("//[^\s]*", "", code)
def online(code):
    return re.sub(r"#.*", "", code)
def multiline(code):
    return re.sub(r"<<<.*>>>", "", code, flags=re.DOTALL)
def all(code):
    code = onword(code)
    code = online(code)
    code = multiline(code)
    return code

