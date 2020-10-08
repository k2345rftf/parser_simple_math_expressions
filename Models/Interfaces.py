

class ContextInterface:
    vars: dict

    def reg_var(self, name: str, value):
        raise NotImplementedError

    def get_var(self, name):
        raise NotImplementedError


class ExpressionInterface:

    def bind(self, context: ContextInterface):
        raise NotImplementedError

    def eval(self) -> float:
        raise NotImplementedError

    def print(self, need_br: bool) -> str:
        raise NotImplementedError


class ParserInterface:

    def parse_to_expression(self, item) -> ExpressionInterface:
        raise NotImplementedError

    def parse_to_string(self, expresion: ExpressionInterface):
        return expresion.print()



