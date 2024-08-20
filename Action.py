from constants import ACTIONS, N_ARGUMENTS, USER_MSG

# Only the actions and number of arguments are permitted.
VALID_ACTIONS = ACTIONS
VALID_ARGUMENTS = N_ARGUMENTS


class Action:
    def __init__(self, arguments):
        self.name = arguments[0] if len(arguments) > 0 else ""
        self.arguments = arguments[0:]
        self.n_args = len(arguments) - 1
        self.error_message = ""

    def is_valid(self) -> bool:
        return self.is_valid_action() and not self.is_empty()

    def is_empty(self) -> bool:
        self.error_message = USER_MSG["NO_ACTION"]
        return True if self.name == "" else False

    def get_name(self) -> str:
        return self.name

    def get_n_args(self) -> int:
        return self.n_args

    def has_valid_arguments(self) -> bool:
        pos = VALID_ACTIONS.index(self.name)
        if N_ARGUMENTS[pos] != self.n_args:
            self.error_message = USER_MSG["N_ARGS_NO_VALID"]
        return N_ARGUMENTS[pos] == self.n_args

    def is_valid_action(self) -> bool:
        if self.name not in VALID_ACTIONS:
            self.error_message = USER_MSG["NO_VALID_ACTION"]
        return self.name in VALID_ACTIONS

    def get_error_message(self) -> str:
        return self.error_message

    def get_args(self):
        return self.arguments
