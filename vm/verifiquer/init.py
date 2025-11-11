from utils.decorators import allways
pinit = ("import",)

def analize(code:str, prohibited:list[str]|tuple[str]|str):
    if isinstance(prohibited, str):
        for No, line in enumerate(code.split("\n")):
            if line.startswith(prohibited):
                raise SyntaxError(f"prohibited init line {No}")
    else:
        for No, line in enumerate(code.split("\n")):
            for init in prohibited:
                if line.startswith(init):
                    raise SyntaxError(f"prohibited init line {No}")
    return code