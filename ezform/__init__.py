#!/usr/bin/env python
# -*- coding: utf-8 -*-

class NotSupportedError(Exception):
    pass


def multiline_variations(line):
    """
                elif line.__contains__("*/"):
                line_sec1 = line.split("*/")
    """


def concatenate(lines):

    needs_newline_after = [
        "oneline",
        "normal with comment",
        "multiline start",
        "multiline continue",
        "multiline end",
        "multiline wholeline"
    ]

    length = len(lines)

    index = 0
    line = lines[index][0]
    line_type = lines[index][1]

    content = line
    index += 1
    while index < length:
        new_content = ""
        if line_type in needs_newline_after:
            new_content += "\n"

        line = lines[index][0]
        line_type = lines[index][1]

        if line_type == "normal":
            new_content += " "
        new_content += line

        content += new_content
        index += 1
    return content


def labelize(lines):
    out = []
    length = len(lines)
    index = 0
    while index < length:
        line = lines[index]

        if line.startswith("//"):
            out.append((line, "oneline"))

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
            out.append((line, "normal with comment"))
        else:
            out.append((line, "normal"))

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
