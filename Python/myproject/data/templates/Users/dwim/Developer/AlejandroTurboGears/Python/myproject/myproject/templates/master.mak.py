# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1574356839.220772
_enable_loop = True
_template_filename = '/Users/dwim/Developer/AlejandroTurboGears/Python/myproject/myproject/templates/master.mak'
_template_uri = '/Users/dwim/Developer/AlejandroTurboGears/Python/myproject/myproject/templates/master.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = ['content_wrapper', 'body_class', 'meta', 'head_content', 'title', 'footer', 'main_menu']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        tg = context.get('tg', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n<head>\n    ')
        __M_writer(escape(self.meta()))
        __M_writer('\n    <title>')
        __M_writer(escape(self.title()))
        __M_writer('</title>\n    <link rel="stylesheet" type="text/css" media="screen" href="')
        __M_writer(escape(tg.url('/css/bootstrap.min.css')))
        __M_writer('" />\n    <link rel="stylesheet" type="text/css" media="screen" href="')
        __M_writer(escape(tg.url('/css/style.css')))
        __M_writer('" />\n\n     <script src="http://code.jquery.com/jquery.js"></script>\n  <script src="')
        __M_writer(escape(tg.url('/javascript/bootstrap.min.js')))
        __M_writer('"></script>\n    ')
        __M_writer(escape(self.head_content()))
        __M_writer('\n</head>\n<body class="')
        __M_writer(escape(self.body_class()))
        __M_writer('">\n    ')
        __M_writer(escape(self.main_menu()))
        __M_writer('\n  <div class="container">\n    ')
        __M_writer(escape(self.content_wrapper()))
        __M_writer('\n  </div>\n    ')
        __M_writer(escape(self.footer()))
        __M_writer('\n\n</body>\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_wrapper(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        tg = context.get('tg', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  ')

        flash=tg.flash_obj.render('flash', use_js=False)
          
        
        __M_writer('\n')
        if flash:
            __M_writer('      <div class="row">\n        <div class="col-md-8 col-md-offset-2">\n              ')
            __M_writer(flash )
            __M_writer('\n        </div>\n      </div>\n')
        __M_writer('  ')
        __M_writer(escape(self.body()))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_class(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_meta(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        response = context.get('response', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <meta charset="')
        __M_writer(escape(response.charset))
        __M_writer('" />\n  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_content(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        tmpl_context = context.get('tmpl_context', UNDEFINED)
        getattr = context.get('getattr', UNDEFINED)
        tg = context.get('tg', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <footer class="footer hidden-xs hidden-sm">\n    <a class="pull-right" href="http://www.turbogears.org"><img style="vertical-align:middle;" src="')
        __M_writer(escape(tg.url('/img/under_the_hood_blue.png')))
        __M_writer('" alt="TurboGears 2" /></a>\n    <p>Copyright &copy; ')
        __M_writer(escape(getattr(tmpl_context, 'project_name', 'TurboGears2')))
        __M_writer(' ')
        __M_writer(escape(h.current_year()))
        __M_writer('</p>\n  </footer>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_menu(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        tg = context.get('tg', UNDEFINED)
        tmpl_context = context.get('tmpl_context', UNDEFINED)
        page = context.get('page', UNDEFINED)
        getattr = context.get('getattr', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <!-- Navbar -->\n  <nav class="navbar navbar-default">\n    <div class="navbar-header">\n      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar-content">\n        <span class="sr-only">Toggle navigation</span>\n        <span class="icon-bar"></span>\n        <span class="icon-bar"></span>\n        <span class="icon-bar"></span>\n      </button>\n      <a class="navbar-brand" href="')
        __M_writer(escape(tg.url('/')))
        __M_writer('">\n        <img src="')
        __M_writer(escape(tg.url('/img/turbogears_logo.png')))
        __M_writer('" height="20" alt="TurboGears 2"/>\n        ')
        __M_writer(escape(getattr(tmpl_context, 'project_name', 'turbogears2')))
        __M_writer('\n      </a>\n    </div>\n\n    <div class="collapse navbar-collapse" id="navbar-content">\n      <ul class="nav navbar-nav">\n        <li class="')
        __M_writer(escape(('', 'active')[page=='index']))
        __M_writer('"><a href="')
        __M_writer(escape(tg.url('/')))
        __M_writer('">Welcome</a></li>\n        <li class="')
        __M_writer(escape(('', 'active')[page=='libreria']))
        __M_writer('"><a href="')
        __M_writer(escape(tg.url('/libreria/libreria')))
        __M_writer('">Libreria</a></li>\n        <li class="')
        __M_writer(escape(('', 'active')[page=='testbasededatos']))
        __M_writer('"><a href="')
        __M_writer(escape(tg.url('/libreria/tablaBase2')))
        __M_writer('">Tabla de prestamos</a></li>\n        <li class="')
        __M_writer(escape(('', 'active')[page=='weather']))
        __M_writer('"><a href="')
        __M_writer(escape(tg.url('/weather')))
        __M_writer('">Clima</a></li>\n        <li class="')
        __M_writer(escape(('', 'active')[page=='reload']))
        __M_writer('"><a href="')
        __M_writer(escape(tg.url('/reload/JsonReload')))
        __M_writer('">Recarga</a></li>\n        <li class="')
        __M_writer(escape(('', 'active')[page=='courses']))
        __M_writer('"><a href="')
        __M_writer(escape(tg.url('/courses/CoursesLoad')))
        __M_writer('">Cursos</a></li>\n        <li class="')
        __M_writer(escape(('', 'active')[page=='datosweather']))
        __M_writer('"><a href="')
        __M_writer(escape(tg.url('/datosweather')))
        __M_writer('">Datos Json</a></li>\n        <li class="')
        __M_writer(escape(('', 'active')[page=='connection']))
        __M_writer('"><a href="')
        __M_writer(escape(tg.url('/connection')))
        __M_writer('">Base Datos</a></li>\n        <li class="')
        __M_writer(escape(('', 'active')[page=='telefonica']))
        __M_writer('"><a href="')
        __M_writer(escape(tg.url('/telefonica')))
        __M_writer('">Telefonica</a></li>\n        <li class="')
        __M_writer(escape(('', 'active')[page=='test']))
        __M_writer('"><a href="')
        __M_writer(escape(tg.url('/test')))
        __M_writer('">Test</a></li>\n        <li class="')
        __M_writer(escape(('', 'active')[page=='vistasj']))
        __M_writer('"><a href="')
        __M_writer(escape(tg.url('/vistasj')))
        __M_writer('">Tabla Json</a></li>\n        <li class="')
        __M_writer(escape(('', 'active')[page=='vistasj2']))
        __M_writer('"><a href="')
        __M_writer(escape(tg.url('/vistasj2')))
        __M_writer('">Tablas Json</a></li>\n        <li class="')
        __M_writer(escape(('', 'active')[page=='jqgrid']))
        __M_writer('"><a href="')
        __M_writer(escape(tg.url('/jqgrid')))
        __M_writer('">Tablas jqGrid CRUD</a></li>\n        <li class="')
        __M_writer(escape(('', 'active')[page=='phonebook']))
        __M_writer('"><a href="')
        __M_writer(escape(tg.url('/phonebook')))
        __M_writer('">Tablas CRUD Phonebook</a></li>\n        <li class="')
        __M_writer(escape(('', 'active')[page=='about']))
        __M_writer('"><a href="')
        __M_writer(escape(tg.url('/about')))
        __M_writer('">About</a></li>\n        <li class="')
        __M_writer(escape(('', 'active')[page=='data']))
        __M_writer('"><a href="')
        __M_writer(escape(tg.url('/data')))
        __M_writer('">Serving Data</a></li>\n        <li class="')
        __M_writer(escape(('', 'active')[page=='environ']))
        __M_writer('"><a href="')
        __M_writer(escape(tg.url('/environ')))
        __M_writer('">WSGI Environment</a></li>\n      </ul>\n\n')
        if tg.auth_stack_enabled:
            __M_writer('      <ul class="nav navbar-nav navbar-right">\n')
            if not request.identity:
                __M_writer('        <li><a href="')
                __M_writer(escape(tg.url('/login')))
                __M_writer('">Login</a></li>\n')
            else:
                __M_writer('        <li><a href="')
                __M_writer(escape(tg.url('/logout_handler')))
                __M_writer('">Logout</a></li>\n        <li><a href="')
                __M_writer(escape(tg.url('/admin')))
                __M_writer('">Admin</a></li>\n')
            __M_writer('      </ul>\n')
        __M_writer('    </div>\n  </nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/dwim/Developer/AlejandroTurboGears/Python/myproject/myproject/templates/master.mak", "uri": "/Users/dwim/Developer/AlejandroTurboGears/Python/myproject/myproject/templates/master.mak", "source_encoding": "utf-8", "line_map": {"17": 0, "24": 1, "25": 4, "26": 4, "27": 5, "28": 5, "29": 6, "30": 6, "31": 7, "32": 7, "33": 10, "34": 10, "35": 11, "36": 11, "37": 13, "38": 13, "39": 14, "40": 14, "41": 16, "42": 16, "43": 18, "44": 18, "45": 34, "46": 36, "47": 40, "48": 41, "49": 43, "50": 50, "51": 101, "57": 22, "63": 22, "64": 23, "65": 24, "66": 25, "67": 26, "68": 25, "69": 26, "70": 27, "71": 29, "72": 29, "73": 33, "74": 33, "75": 33, "81": 36, "90": 37, "95": 37, "96": 38, "97": 38, "103": 41, "112": 43, "116": 43, "122": 45, "130": 45, "131": 47, "132": 47, "133": 48, "134": 48, "135": 48, "136": 48, "142": 52, "151": 52, "152": 62, "153": 62, "154": 63, "155": 63, "156": 64, "157": 64, "158": 70, "159": 70, "160": 70, "161": 70, "162": 71, "163": 71, "164": 71, "165": 71, "166": 72, "167": 72, "168": 72, "169": 72, "170": 73, "171": 73, "172": 73, "173": 73, "174": 74, "175": 74, "176": 74, "177": 74, "178": 75, "179": 75, "180": 75, "181": 75, "182": 76, "183": 76, "184": 76, "185": 76, "186": 77, "187": 77, "188": 77, "189": 77, "190": 78, "191": 78, "192": 78, "193": 78, "194": 79, "195": 79, "196": 79, "197": 79, "198": 80, "199": 80, "200": 80, "201": 80, "202": 81, "203": 81, "204": 81, "205": 81, "206": 82, "207": 82, "208": 82, "209": 82, "210": 83, "211": 83, "212": 83, "213": 83, "214": 84, "215": 84, "216": 84, "217": 84, "218": 85, "219": 85, "220": 85, "221": 85, "222": 86, "223": 86, "224": 86, "225": 86, "226": 89, "227": 90, "228": 91, "229": 92, "230": 92, "231": 92, "232": 93, "233": 94, "234": 94, "235": 94, "236": 95, "237": 95, "238": 97, "239": 99, "245": 239}}
__M_END_METADATA
"""
