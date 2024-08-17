from constants import ACTIONS, N_ARGUMENTS

VALID_ACTIONS = ACTIONS
VALID_ARGUMENTS = N_ARGUMENTS


class Action:
    def __init__(self, arguments):
        self.name = arguments[0] if len(arguments) > 0 else ""
        self.arguments = arguments
        self.n_args = len(arguments)
        self.error = "No hay ningun error"

    def is_valid(self) -> bool:

        return (
            self.is_valid_action()
            and not self.is_empty()
            and self.has_valid_arguments()
        )

    def is_empty(self) -> bool:
        self.error = "No ha indicado una acción, por favor escriba una."
        return True if self.name == "" else False

    def get_name(self) -> str:
        return self.name

    def get_n_args(self) -> int:
        return self.n_args

    def has_valid_arguments(self) -> bool:
        pos = VALID_ACTIONS.index(self.name)
        if N_ARGUMENTS[pos] != self.n_args:
            self.error = "Número de argumentos no válido"
        return N_ARGUMENTS[pos] == self.n_args

    def is_valid_action(self):
        if self.name not in VALID_ACTIONS:
            self.error = "Ación no válida"
        return self.name in VALID_ACTIONS

    def show_error(self) -> str:
        return self.error
