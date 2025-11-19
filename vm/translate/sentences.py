import re

def rw(code):
    return re.sub(r"write: (.*)", lambda m: f"print({m.group(1)})", code)
def use(code):
    code = re.sub(r"from: (.*) use: (.*)", lambda m: f"from {m.group(1)} import {m.group(2)})", code)
    code = re.sub(r"use: (.*)", lambda m: f"import {m.group(1)}", code)
    return code
def fn(code):
    return re.sub(r"fn", lambda m: f"def", code)
def loop(code):
    return re.sub(r"loop:", "while True:", code)