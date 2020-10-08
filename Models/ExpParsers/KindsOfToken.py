import enum


class KindOfToken(enum.Enum):
    NUMBER = [chr(x) for x in range(ord('0'), ord('9') + 1)]
    CHARS = [chr(x) for x in range(ord('a'), ord('z') + 1)] + [chr(x) for x in range(ord('A'), ord('Z') + 1)] + ['_']
    SPECCHARS = [chr(9), chr(10), chr(13), ' ', ' ']
    ADD = '+'
    SUB = '-'
    MUL = '*'
    DIV = '/'
    LBRACE = '('
    RBRACE = ')'
    DOT = '.'
    EOL = chr(0)
    POW = '^'
    LN = 'ln'
    SIN = 'sin'
    COS = 'cos'
    TAN = 'tan'
    ATAN = 'atan'
    ASIN = 'asin'
    ACOS = 'acos'
    SQRT = 'sqrt'
    EXP = 'exp'
    LG = 'lg'
