__author__ = 'John Underwood'

def split(line, types=None, delimiter=None):
    """
    :param line: string of text
    :param types:
    :param delimiter: default is ' ' (space)
    :return: list
    """
    fields = line.split(delimiter)
    # clean out leading spaces for delimiter ['a, b, c'] -> ['a', ' b', ' c']
    fields = [field.lstrip() for field in fields]  # becomes ['a', 'b', 'c']
    if types:
        fields = [t(val) for t, val in zip(types, fields)]
    return fields

if __name__ is '__main__':
    print('Hello, there.')
    s = split('GOOG, 100, 490.90', delimiter=',')
    print(s)
