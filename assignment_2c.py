"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2c(w, x, y, z):
    """
    Argument:
    w -- float
    x -- float
    y -- float
    z -- float

    Returns:
    results {
        "multiply": x times y,
        "divide": x divide by y,
        "add": w plus z,
        "substract" w minus z
    }
    """


    multiplication = x * y
    division = x / y
    addition = w + z
    subtraction = w - z

    results = {"multiply": multiplication,
               "divide": division,
               "add": addition,
               "subtract": subtraction}

    return results
