#!/usr/bin/env python
# -*- coding: utf-8 -*-

class NotSupportedError(Exception):
    pass


line_types = {
    "code": {
        "before": " ",
        "after": ""
    },
    "preprocessor": {
        "before": "",
        "after": "\n"
    },
    "code with comment": {
        "before": " ",
        "after": "\n"
    },
    "oneline comment": {
        "before": "\n",
        "after": "\n"
    },
    "multiline wholeline": {
        "before": "\n",
        "after": "\n"
    },
    "multiline start": {
        "before": "\n",
        "after": "\n"
    },
    "multiline continue": {
        "before": '',
        "after": "\n"
    },
    "multiline end": {
        "before": '',
        "after": "\n"
    }
}


def concatenate(lines):

    length = len(lines)

    content = ""
    index = 0
    while index < length:
        line = lines[index][0]
        line_type = lines[index][1]
        needs = line_types[line_type]
        content += needs["before"] + line + needs["after"]
        index += 1
    return content


def labelize(lines):
    out = []
    length = len(lines)
    index = 0
    while index < length:
        line = lines[index]

        if line.startswith("//"):
            out.append((line, "oneline comment"))

        elif line.startswith("/*"):
            if line.endswith("*/"):
                out.append((line, "multiline wholeline"))
            elif line.__contains__("*/"):
                raise NotSupportedError
            else:
                out.append((line, "multiline start"))
                index += 1
                line = lines[index]
                while not line.endswith("*/"):
                    if line.__contains__("*/"):
                        raise NotSupportedError
                    out.append((line, "multiline continue"))
                    index += 1
                    line = lines[index]
                out.append((line, "multiline end"))
        elif line.startswith("#"):
            out.append((line, "preprocessor"))

        elif line.__contains__("/*") or line.__contains__("//"):
            out.append((line, "code with comment"))
        else:
            out.append((line, "code"))

        index += 1

    return out


def ezform(content, options={}):
    """
        in: content -> c source code
        in: optins  -> a dictionary of options to modify the result
    """
    lines = str(content).split("\n")
    lines = [line.strip() for line in lines]
    lines = labelize(lines)
    content = concatenate(lines)
    return content
