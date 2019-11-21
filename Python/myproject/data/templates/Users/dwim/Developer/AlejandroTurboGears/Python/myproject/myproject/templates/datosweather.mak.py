# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1574284831.777358
_enable_loop = True
_template_filename = '/Users/dwim/Developer/AlejandroTurboGears/Python/myproject/myproject/templates/datosweather.mak'
_template_uri = '/Users/dwim/Developer/AlejandroTurboGears/Python/myproject/myproject/templates/datosweather.mak'
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
        json = context.get('json', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\n<HTML>\n    <HEAD>\n    <TITLE>DatosWeather</TITLE>\n    </HEAD>\n    <BODY BGCOLOR="FFFFFF">\n        <CENTER>\n\n            <ul>\n')
        for key, value in json.items():
            __M_writer('                    <p>')
            __M_writer(escape(key))
            __M_writer(',')
            __M_writer(escape(value))
            __M_writer('</p>\n')
            if key == "sys":
                for key1, value1 in json[key].items():
                    __M_writer('                                <h3>')
                    __M_writer(escape(key1))
                    __M_writer(',')
                    __M_writer(escape(value1))
                    __M_writer('</h3>\n')
            __M_writer('\n')
        __M_writer('\n            </ul>\n\n\n            <h1>')
        __M_writer(escape(json['name']))
        __M_writer("</h1>\n            <p></p>\n\n        <H1>State of Mexico's Weather</H1>\n        </CENTER>\n    </BODY>\n</HTML>")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/dwim/Developer/AlejandroTurboGears/Python/myproject/myproject/templates/datosweather.mak", "uri": "/Users/dwim/Developer/AlejandroTurboGears/Python/myproject/myproject/templates/datosweather.mak", "source_encoding": "utf-8", "line_map": {"28": 0, "34": 1, "35": 12, "36": 13, "37": 13, "38": 13, "39": 13, "40": 13, "41": 14, "42": 15, "43": 16, "44": 16, "45": 16, "46": 16, "47": 16, "48": 19, "49": 21, "50": 25, "51": 25, "57": 51}}
__M_END_METADATA
"""
