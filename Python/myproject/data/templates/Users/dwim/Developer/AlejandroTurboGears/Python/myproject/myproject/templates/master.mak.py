# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1574808349.758198
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
        self = context.get('self', UNDEFINED)
        tg = context.get('tg', UNDEFINED)
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
        __M_writer('\n\n</head>\n<body class="')
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
        tg = context.get('tg', UNDEFINED)
        getattr = context.get('getattr', UNDEFINED)
        tmpl_context = context.get('tmpl_context', UNDEFINED)
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
        page = context.get('page', UNDEFINED)
        tmpl_context = context.get('tmpl_context', UNDEFINED)
        request = context.get('request', UNDEFINED)
        tg = context.get('tg', UNDEFINED)
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
{"filename": "/Users/dwim/Developer/AlejandroTurboGears/Python/myproject/myproject/templates/master.mak", "uri": "/Users/dwim/Developer/AlejandroTurboGears/Python/myproject/myproject/templates/master.mak", "source_encoding": "utf-8", "line_map": {"17": 0, "24": 1, "25": 4, "26": 4, "27": 5, "28": 5, "29": 6, "30": 6, "31": 7, "32": 7, "33": 10, "34": 10, "35": 11, "36": 11, "37": 14, "38": 14, "39": 15, "40": 15, "41": 17, "42": 17, "43": 19, "44": 19, "45": 35, "46": 37, "47": 41, "48": 42, "49": 44, "50": 51, "51": 102, "57": 23, "63": 23, "64": 24, "65": 25, "66": 26, "67": 27, "68": 26, "69": 27, "70": 28, "71": 30, "72": 30, "73": 34, "74": 34, "75": 34, "81": 37, "90": 38, "95": 38, "96": 39, "97": 39, "103": 42, "112": 44, "116": 44, "122": 46, "130": 46, "131": 48, "132": 48, "133": 49, "134": 49, "135": 49, "136": 49, "142": 53, "151": 53, "152": 63, "153": 63, "154": 64, "155": 64, "156": 65, "157": 65, "158": 71, "159": 71, "160": 71, "161": 71, "162": 72, "163": 72, "164": 72, "165": 72, "166": 73, "167": 73, "168": 73, "169": 73, "170": 74, "171": 74, "172": 74, "173": 74, "174": 75, "175": 75, "176": 75, "177": 75, "178": 76, "179": 76, "180": 76, "181": 76, "182": 77, "183": 77, "184": 77, "185": 77, "186": 78, "187": 78, "188": 78, "189": 78, "190": 79, "191": 79, "192": 79, "193": 79, "194": 80, "195": 80, "196": 80, "197": 80, "198": 81, "199": 81, "200": 81, "201": 81, "202": 82, "203": 82, "204": 82, "205": 82, "206": 83, "207": 83, "208": 83, "209": 83, "210": 84, "211": 84, "212": 84, "213": 84, "214": 85, "215": 85, "216": 85, "217": 85, "218": 86, "219": 86, "220": 86, "221": 86, "222": 87, "223": 87, "224": 87, "225": 87, "226": 90, "227": 91, "228": 92, "229": 93, "230": 93, "231": 93, "232": 94, "233": 95, "234": 95, "235": 95, "236": 96, "237": 96, "238": 98, "239": 100, "245": 239}}
__M_END_METADATA
"""
