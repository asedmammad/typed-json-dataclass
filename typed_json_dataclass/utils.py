def to_snake(string_to_convert: str) -> str:
    import re
    string_to_convert = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', string_to_convert)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', string_to_convert).lower()


def to_camel(string_to_convert: str):
    converted = ''
    next_is_capital = False
    for i, c in enumerate(string_to_convert):
        if c == '_':
            next_is_capital = i != 0 and converted != ''
            continue

        if c == c.upper():
            next_is_capital = True

        if i == 0:
            converted += c.lower()
            next_is_capital = False
            continue

        if next_is_capital:
            converted += c.upper()
            next_is_capital = False
        else:
            converted += c.lower()

    return converted


def to_fullcase(string_to_convert: str):
    converted = to_camel(string_to_convert)
    return converted[0].upper() + converted[1:]


def recursive_rename(raw_dict, format_method):
    renamed_dict = {}
    for k, v in raw_dict.items():
        if isinstance(v, dict):
            v = recursive_rename(v, format_method)
        renamed_dict[format_method(k)] = v
    return renamed_dict
