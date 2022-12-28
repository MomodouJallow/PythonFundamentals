"""A useful way to remember how Python resolves scope is with the
LEGB rule. This rule is an acronym for Local, Enclosing, Global, Built-in."""


x = 5  # Global scope


def outer_func():
    y = 3  # Enclosing scope


    def inner_func():

        z = x + y  # Local scope
        return z


    return inner_func()
