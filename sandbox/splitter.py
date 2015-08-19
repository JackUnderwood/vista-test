__author__ = 'John Underwood'


def split(line, types=None, delimiter=None):
    """
    :param line: string of delimited text
    :param types: list of data types, e.g. [str, int, float]
    :param delimiter: default splits all white space
    :return: list
    This split alters the traditional split by converting a string
    element to its type, e.g. '100' with type int, converts element to 100
    Example - converts 'GOOG 100 490.90' using types [str, int, float] to
    a list ['GOOG', 100, 490.9].
    See unit tests 'testsplitter.py' for more examples.
    """
    fields = line.split(delimiter)
    # Clean out leading spaces for delimiter ['a, b, c'] -> ['a', ' b', ' c']
    fields = [field.lstrip() for field in fields]  # becomes ['a', 'b', 'c']
    if types:
        fields = [t(val) for t, val in zip(types, fields)]
    return fields
