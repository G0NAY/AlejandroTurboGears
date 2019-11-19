# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1572996423.127681
_enable_loop = True
_template_filename = '/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/makoconnection/connection.mak'
_template_uri = '/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/makoconnection/connection.mak'
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
        kw = context.get('kw', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<HTML>\n    <HEAD>\n    <TITLE>Datos</TITLE>\n    </HEAD>\n    <BODY BGCOLOR="FFFFFF">\n        <CENTER>\n')
        for it in kw['tracker']:
            __M_writer('                        <p> No de registro: ')
            __M_writer(escape(it['id']))
            __M_writer(' IMEI: ')
            __M_writer(escape(it['imei']))
            __M_writer(' No.Ticket: ')
            __M_writer(escape(it['ticket']))
            __M_writer(' Nombre: ')
            __M_writer(escape(it['name']))
            __M_writer(' </p>\n')
        __M_writer('        </CENTER>\n        <HR>\n    </BODY>\n</HTML>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/makoconnection/connection.mak", "uri": "/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/makoconnection/connection.mak", "source_encoding": "utf-8", "line_map": {"28": 0, "34": 1, "35": 9, "36": 10, "37": 10, "38": 10, "39": 10, "40": 10, "41": 10, "42": 10, "43": 10, "44": 10, "45": 12, "51": 45}}
__M_END_METADATA
"""
