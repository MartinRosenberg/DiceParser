#!/usr/bin/env python3

from collections import namedtuple
import operator as op
import random
import re
import sys

def d(a, b):
    return sum(random.randrange(b) + 1 for _ in range(a))

Op = namedtuple("Op", "prec func")
ops = {
    "d": Op(4, d),
    "^": Op(3, op.pow),
    "*": Op(2, op.mul),
    "/": Op(2, op.truediv),
    "%": Op(2, op.mod), # Conflicts with "d%"
    "+": Op(1, op.add),
    "-": Op(1, op.sub),
    ">": Op(0, op.gt),
    ">=": Op(0, op.ge),
    "<": Op(0, op.lt),
    "<=": Op(0, op.le),
    "=": Op(0, op.eq),
    # Keep/drop requires more advanced behavior for `d` and figuring out precedence
    # "kh": Op(4, kh),
    # "kl": Op(4, kl),
    # "dh": Op(4, dh),
    # "dl": Op(4, dl),
}

if __name__ == "__main__":
    expr = re.sub(r"\s+", "", sys.argv[1])
    expr = re.findall(r"[()]+|[^\d()]+|\d+", expr)

    op_stack = []
    num_stack = []
