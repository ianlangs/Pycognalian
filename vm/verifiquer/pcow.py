from syntax.classtypes import String
from utils.decorators import allways
pcow = ("def",
        "print",
        "input",
        "lambda",
        "import"
        ";")

def analize(code:str|String, prohibited:list[str]|tuple[str]=()):
    for p in prohibited:
        if p in code:
            raise SyntaxError(f"prohibited word / char {p} in code")
    return code
analize = allways(analize, prohibited=pcow)

