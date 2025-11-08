from functools import partial
def allways(func, **init):
    return partial(func, **init)