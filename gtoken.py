# -*- coding: utf-8 -*-
import ast
import math
import re
import time

import requests


class TokenAcquirer(object):
    RE_TKK = re.compile(r'TKK=eval\(\'\(\(function\(\)\{(.+?)\}\)\(\)\)\'\);',
                        re.DOTALL)

    def __init__(self, tkk='0', session=None, host='translate.google.com'):
        self.session = session or requests.Session()
        self.tkk = tkk
        self.host = host if 'http' in host else 'https://' + host

    def _update(self):
        """update tkk
        """
        # we don't need to update the base TKK value when it is still valid
        now = math.floor(int(time.time() * 1000) / 3600000.0)
        if self.tkk and int(self.tkk.split('.')[0]) == now:
            return

        r = self.session.get(self.host)
        # this will be the same as python code after stripping out a reserved word 'var'
        code = str(self.RE_TKK.search(r.text).group(1)).replace('var ', '')
        code = code.encode().decode('unicode-escape')

        if code:
            tree = ast.parse(code)
            visit_return = False
            operator = '+'
            n, keys = 0, dict(a=0, b=0)
            for node in ast.walk(tree):
                if isinstance(node, ast.Assign):
                    name = node.targets[0].id
                    if name in keys:
                        if isinstance(node.value, ast.Num):
                            keys[name] = node.value.n
                        # the value can sometimes be negative
                        elif isinstance(node.value, ast.UnaryOp) and \
                                isinstance(node.value.op, ast.USub):  # pragma: nocover
                            keys[name] = -node.value.operand.n
                elif isinstance(node, ast.Return):
                    # parameters should be set after this point
                    visit_return = True
                elif visit_return and isinstance(node, ast.Num):
                    n = node.n
                elif visit_return and n > 0:
                    # the default operator is '+' but implement some more for
                    # all possible scenarios
                    if isinstance(node, ast.Add):  # pragma: nocover
                        pass
                    elif isinstance(node, ast.Sub):  # pragma: nocover
                        operator = '-'
                    elif isinstance(node, ast.Mult):  # pragma: nocover
                        operator = '*'
                    elif isinstance(node, ast.Pow):  # pragma: nocover
                        operator = '**'
                    elif isinstance(node, ast.BitXor):  # pragma: nocover
                        operator = '^'
            # a safety way to avoid Exceptions
            clause = compile('{1}{0}{2}'.format(
                operator, keys['a'], keys['b']), '', 'eval')
            value = eval(clause, dict(__builtin__={}))
            result = '{}.{}'.format(n, value)

            self.tkk = result

    def _xr(self, a, b):
        size_b = len(b)
        c = 0
        while c < size_b - 2:
            d = b[c + 2]
            d = ord(d[0]) - 87 if 'a' <= d else int(d)
            d = rshift(a, d) if '+' == b[c + 1] else a << d
            a = a + d & 4294967295 if '+' == b[c] else a ^ d

            c += 3
        return a

    def acquire(self, text):
        b = self.tkk if self.tkk != '0' else ''
        d = b.split('.')
        b = int(d[0]) if len(d) > 1 else 0

        # assume e means char code array
        e = []
        g = 0
        size = len(text)
        for i, char in enumerate(text):
            l = ord(char)
            # just append if l is less than 128(ascii: DEL)
            if l < 128:
                e.append(l)
            # append calculated value if l is less than 2048
            else:
                if l < 2048:
                    e.append(l >> 6 | 192)
                else:
                    # append calculated value if l matches special condition
                    if (l & 64512) == 55296 and g + 1 < size and \
                            ord(text[g + 1]) & 64512 == 56320:
                        g += 1
                        l = 65536 + ((l & 1023) << 10) + ord(text[g]) & 1023
                        e.append(l >> 18 | 240)
                        e.append(l >> 12 & 63 | 128)
                    else:
                        e.append(l >> 12 | 224)
                        e.append(l >> 6 & 63 | 128)
                e.append(l & 63 | 128)
        a = b
        for i, value in enumerate(e):
            a += value
            a = self._xr(a, '+-a^+6')
        a = self._xr(a, '+-3^+b+-f')
        a ^= int(d[1]) if len(d) > 1 else 0
        if a < 0:  # pragma: nocover
            a = (a & 2147483647) + 2147483648
        a %= 1000000  # int(1E6)

        return '{}.{}'.format(a, a ^ b)

    def do(self, text):
        self._update()
        tk = self.acquire(text)
        return tk


def rshift(val, n):
    """python port for '>>>'(right shift with padding)
    """
    return (val % 0x100000000) >> n