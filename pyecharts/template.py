#!/usr/bin/env python
#coding=utf-8
from __future__ import unicode_literals

import os
import re
import sys
import codecs
from jinja2 import Environment, FileSystemLoader
from pyecharts.constants import DEFAULT_JS_LIBRARIES

PY2 = sys.version_info[0] == 2

JS_PATTERN = re.compile(r'<!-- build -->(.*)<!-- endbuild -->',
                        re.IGNORECASE | re.MULTILINE | re.DOTALL)
JS_SRC_PATTERN = re.compile(r'src=\"(.*?)\"')


def freeze_js(html_content):
    """

    :param html_content:
    :return:
    """
    matches = JS_PATTERN.finditer(html_content)

    if not matches:
        return html_content

    for match in reversed(tuple(matches)):
        # JS file block
        src_matches = JS_SRC_PATTERN.findall(match.group(1))

        js_content = ""
        for src in src_matches:
            file_path = os.path.join(
                get_resource_dir('templates'), src.strip())

            with codecs.open(file_path, "r", "utf-8") as f:
                js_content += f.read() + '\n'
        # Replace matched string with inline JS
        fmt = '<script type="text/javascript">{}</script>'
        js_content = fmt.format(js_content)
        html_content = (html_content[:match.start()] + js_content +
                        html_content[match.end():])

    return html_content


def get_resource_dir(folder):
    """

    :param folder:
    :return:
    """
    current_path = os.path.dirname(__file__)
    resource_path = os.path.join(current_path, folder)
    return resource_path


# Single Singleton Instance for jinja2
JINJA2_ENV = Environment(
    loader=FileSystemLoader(get_resource_dir('templates')),
    keep_trailing_newline=True,
    trim_blocks=True,
    lstrip_blocks=True)


def write_utf8_html_file(file_name, html_content):
    """

    :param file_name:
    :param html_content:
    :return:
    """
    if PY2:
        html = html_content.encode('utf-8')
        with open(file_name, "w+") as fout:
            fout.write(html)
    else:
        with open(file_name, "w+", encoding="utf-8") as fout:
            fout.write(html_content)


def produce_require_configuration(dependencies, jshost):
    # if no nick name register, we treat the location as location.js
    require_conf_items = [
        "'%s': '%s/%s'" % (key, jshost, DEFAULT_JS_LIBRARIES.get(key, key))
        for key in dependencies]
    require_libraries = ["'%s'" % key for key in dependencies]
    return dict(
        config_items=require_conf_items,
        libraries=require_libraries
    )
