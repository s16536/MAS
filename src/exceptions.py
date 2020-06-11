class MissingRequiredParameterError(Exception):
    def __init__(self, parameter_name: str, class_name: str):
        super().__init__(f"Missing required parameter '{parameter_name}' for class '{class_name}'")