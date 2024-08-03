import typing

class Schema:
    def __init__(self, **kwargs):
        hints = typing.get_type_hints(self.__class__)
        for key, value in kwargs.items():
            setattr(self, key, value)
        for attribute in hints:
            if not hasattr(self, attribute):
                setattr(self, attribute, None)
        self.validate_types()

    def __repr__(self):
        return str(self.__dict__)
    
    def __str__(self):
        return str(self.__dict__)

    def validate_types(self):
        hints = typing.get_type_hints(self.__class__)
        for attribute, expected_type in hints.items():
            actual_value = getattr(self, attribute)
            if not isinstance(actual_value, expected_type) and actual_value is not None:
                raise TypeError(f"Attribute '{attribute}' should be of type '{expected_type.__name__}', "
                                f"but got '{type(actual_value).__name__}'")