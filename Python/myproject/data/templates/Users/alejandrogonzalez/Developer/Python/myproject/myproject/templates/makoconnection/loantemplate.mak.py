# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1573169940.3957949
_enable_loop = True
_template_filename = '/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/makoconnection/loantemplate.mak'
_template_uri = '/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/makoconnection/loantemplate.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('<script type="text/javascript">\n    $(\'.datepicker\').datepicker({\n        dateFormat: \'yy-mm-dd\',\n    startDate: \'-3d\'\n    });\n</script>\n<form id="loanForm">\n  <div class="form-group">\n    <label for="amount">Cantidad</label>\n    <input type="number" class="form-control" id="amount" name="amount">\n  </div>\n  <div class="form-group">\n    <label for="due_date">Fecha de vencimiento</label>\n      <br>\n      <input class="datepicker" id="due_date" name="due_date" data-date-format="yyyy-mm-dd">\n  </div>\n</form>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/makoconnection/loantemplate.mak", "uri": "/Users/alejandrogonzalez/Developer/Python/myproject/myproject/templates/makoconnection/loantemplate.mak", "source_encoding": "utf-8", "line_map": {"17": 0, "22": 1, "28": 22}}
__M_END_METADATA
"""
