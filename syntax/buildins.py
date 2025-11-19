from syntax.classtypes import Number
readInput = input
write = print
def scientific(n:Number, te:Number):
    return Number(float(n) * 10 ** float(te))