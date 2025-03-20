from scripts.print_error import log_constraint_error

class ErrorLogger:
    def __init__(self) -> None:
        return

    def log_constraint_error(self, constraint_type, description):
        return log_constraint_error(constraint_type, description)

    def log_fatal_error(self, error_type, description):
        return log_constraint_error(error_type, description)