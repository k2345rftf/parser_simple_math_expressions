from Models.ExpParsers.KindsOfToken import KindOfToken


class Token:

    def __init__(self, kind_of_token: KindOfToken):
        self.kind_of_token = kind_of_token
        self.__string = None
        self.__value = None

    string = property()
    value = property()

    @string.setter
    def string(self, value: str):
        self.__string = value

    @string.getter
    def string(self) -> str:
        return self.__string

    @value.setter
    def value(self, x: float):
        self.__value = x

    @value.getter
    def value(self) -> float:
        return self.__value


class TokenParser:
    __string: str

    def __init__(self, string):
        self.__string = self.__prepare_string(string) + chr(0)
        self.pointer = 0
        self.max_pointer = len(self.__string) - 1

    def __prepare_string(self, string):
        for x in KindOfToken.SPECCHARS.value:
            string = string.replace(x, '')
        return string

    def __skip_chars(self, kind_of_token, skip_first_char_if_it_is_not_kind_of_token=False):
        if skip_first_char_if_it_is_not_kind_of_token:
            self.pointer = self.pointer + 1
        while self.__token_in(kind_of_token):
            self.pointer = self.pointer + 1

    def __token_is(self, kind_of_token):
        return self.__string[self.pointer] == kind_of_token.value

    def __token_in(self, kind_of_token) -> bool:
        return self.__string[self.pointer] in kind_of_token.value

    def get_next_token(self):
        sp = self.pointer

        self.__skip_chars(KindOfToken.SPECCHARS)
        if self.__token_is(KindOfToken.EOL):
            return self.__create_token(KindOfToken.EOL)
        if self.__token_in(KindOfToken.NUMBER):
            return self.__get_num_token(sp)

        elif self.__token_in(KindOfToken.CHARS):
            return self.__get_chars_token(sp)
        else:
            self.pointer = self.pointer + 1
        return self.__create_token(KindOfToken(self.__string[self.pointer-1]))

    def __get_num_token(self, sp):
        self.__skip_chars(KindOfToken.NUMBER)
        if self.__token_is(KindOfToken.DOT):
            self.__skip_chars(KindOfToken.NUMBER, True)
        if self.__string[self.pointer] in ['e', 'E']:
            self.pointer = self.pointer + 1
            if self.__string[self.pointer] in ['+', '-']:
                self.__skip_chars(KindOfToken.NUMBER, True)
        return self.__create_token(KindOfToken.NUMBER, self.__string[sp:self.pointer], float(self.__string[sp:self.pointer]))

    def __get_chars_token(self, sp):
        self.__skip_chars(KindOfToken.CHARS)
        if self.__token_is(KindOfToken.LBRACE):
            try:
                return self.__create_token(KindOfToken(self.__string[sp:self.pointer]))
            except ValueError:
                print(f'This \'{self.__string[sp:self.pointer-1]}\' not found!!!')
                raise ValueError
        return self.__create_token(KindOfToken.CHARS, self.__string[sp:self.pointer])

    def __create_token(self, kind: KindOfToken, string=None, value=None):
        token = Token(kind)
        if string is not None:
            token.string = string
        if value is not None:
            token.value = value
        return token

    def get_pointer(self):
        return self.pointer
