from Models.Interfaces import ContextInterface

class Context(ContextInterface):

    def __init__(self):
        self.vars = {}

    def reg_var(self, name, value):
        self.vars[name] = value

    def get_var(self, name):
        if name in self.vars:
            return self.vars[name]
        raise ValueError(f'Unbound variable {name}!!!')