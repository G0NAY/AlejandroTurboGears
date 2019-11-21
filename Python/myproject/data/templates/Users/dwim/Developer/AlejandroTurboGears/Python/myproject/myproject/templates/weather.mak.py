# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1574208770.767524
_enable_loop = True
_template_filename = '/Users/dwim/Developer/AlejandroTurboGears/Python/myproject/myproject/templates/weather.mak'
_template_uri = '/Users/dwim/Developer/AlejandroTurboGears/Python/myproject/myproject/templates/weather.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'local:templates.master', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        pressure = context.get('pressure', UNDEFINED)
        temperature = context.get('temperature', UNDEFINED)
        humidity = context.get('humidity', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<HTML>\n    <HEAD>\n    <TITLE>Weather</TITLE>\n    </HEAD>\n    <BODY BGCOLOR="FFFFFF">\n        <CENTER><IMG SRC="https://goldentroutwilderness.files.wordpress.com/2012/01/various-weather.jpg" height="220" width="220" ALIGN="BOTTOM"> </CENTER>\n        <HR>\n        <H1>State of Mexico\'s Weather</H1>\n        <p>Temperature: ')
        __M_writer(escape(temperature))
        __M_writer(' Celcius</p>\n        <p>Pressure: ')
        __M_writer(escape(pressure))
        __M_writer(' Mb </p>\n        <p>Humidity: ')
        __M_writer(escape(humidity))
        __M_writer(' %</p>\n    </BODY>\n</HTML>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/dwim/Developer/AlejandroTurboGears/Python/myproject/myproject/templates/weather.mak", "uri": "/Users/dwim/Developer/AlejandroTurboGears/Python/myproject/myproject/templates/weather.mak", "source_encoding": "utf-8", "line_map": {"28": 0, "36": 1, "37": 11, "38": 11, "39": 12, "40": 12, "41": 13, "42": 13, "48": 42}}
__M_END_METADATA
"""
