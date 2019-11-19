# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1573258259.84184
_enable_loop = True
_template_filename = '/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/libreria/hello.mak'
_template_uri = '/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/libreria/hello.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        book = context.get('book', UNDEFINED)
        usuario = context.get('usuario', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<HTML>\n    <HEAD>\n    <TITLE>Datos</TITLE>\n    </HEAD>\n    <BODY BGCOLOR="FFFFFF">\n        <CENTER>\n        <table>\n\t\t<caption>Datos de usuario</caption>\n\t\t<tr>\n\t\t\t<td>Id de Usuario:</td>\n\t\t\t<td>')
        __M_writer(escape(usuario.usuario_id))
        __M_writer('</td>\n\t\t</tr>\n\t\t<tr>\n\t\t\t<td>Nombre de usuario:</td>\n\t\t\t<td>')
        __M_writer(escape(usuario.name))
        __M_writer('</td>\n\t\t</tr>\n        <tr>\n            <td>Libros de usuario:</td>\n')
        for it in book:
            __M_writer('                         <tr><td>')
            __M_writer(escape(it['book_name']))
            __M_writer(' </td></tr>\n')
        __M_writer('        </tr>\n\t\t</table>\n\n        </CENTER>\n        <HR>\n    </BODY>\n</HTML>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/libreria/hello.mak", "uri": "/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/libreria/hello.mak", "source_encoding": "utf-8", "line_map": {"17": 0, "24": 1, "25": 11, "26": 11, "27": 15, "28": 15, "29": 19, "30": 20, "31": 20, "32": 20, "33": 22, "39": 33}}
__M_END_METADATA
"""
