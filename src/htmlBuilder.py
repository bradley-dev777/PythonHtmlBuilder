class HTMLBuilder:
    def __init__(self):
        self.html_text = ""

    def append(self, html_snippet):
        self.html_text += html_snippet

    def get_html(self):
        return self.html_text

    def doctype(self):
        snippet = '<!DOCTYPE html>'
        self.append(snippet)
        return snippet

    def html(self, content):
        snippet = '<html>' + str(content) + '</html>'
        self.append(snippet)
        return snippet

    def body(self, content):
        snippet = '<body>' + str(content) + '</body>'
        
        return snippet

    def p(self, content):
        snippet = '<p>' + str(content) + '</p>'
        
        return snippet

    def h1(self, content):
        snippet = '<h1>' + str(content) + '</h1>'
        
        return snippet

    def h2(self, content):
        snippet = '<h2>' + str(content) + '</h2>'
        
        return snippet

    def h3(self, content):
        snippet = '<h3>' + str(content) + '</h3>'
        
        return snippet

    def h4(self, content):
        snippet = '<h4>' + str(content) + '</h4>'
        
        return snippet

    def h5(self, content):
        snippet = '<h5>' + str(content) + '</h5>'
        
        return snippet

    def h6(self, content):
        snippet = '<h6>' + str(content) + '</h6>'
    @staticmethod
    def ol(content):
        return '<ol>' + str(content) + '</ol>'

    @staticmethod
    def li(content):
        return '<li>' + str(content) + '</li>'

    @staticmethod
    def table(content):
        return '<table>' + str(content) + '</table>'

    @staticmethod
    def tr(content):
        return '<tr>' + str(content) + '</tr>'

    @staticmethod
    def td(content):
        return '<td>' + str(content) + '</td>'

    @staticmethod
    def th(content):
        return '<th>' + str(content) + '</th>'

    @staticmethod
    def header(content):
        return '<header>' + str(content) + '</header>'

    @staticmethod
    def footer(content):
        return '<footer>' + str(content) + '</footer>'

    @staticmethod
    def section(content):
        return '<section>' + str(content) + '</section>'

    @staticmethod
    def article(content):
        return '<article>' + str(content) + '</article>'

    @staticmethod
    def aside(content):
        return '<aside>' + str(content) + '</aside>'

    @staticmethod
    def form(content):
        return '<form>' + str(content) + '</form>'

    @staticmethod
    def input(type_attr, name_attr, value_attr=""):
        return f'<input type="{type_attr}" name="{name_attr}" value="{value_attr}">'

    @staticmethod
    def button(content):
        return '<button>' + str(content) + '</button>'

    @staticmethod
    def label(for_attr, content):
        return f'<label for="{for_attr}">' + str(content) + '</label>'

    @staticmethod
    def select(name_attr, content):
        return f'<select name="{name_attr}">' + str(content) + '</select>'

    @staticmethod
    def option(value_attr, content):
        return f'<option value="{value_attr}">' + str(content) + '</option>'

    @staticmethod
    def img(src, alt=""):
        return f'<img src="{src}" alt="{alt}">'

    @staticmethod
    def blockquote(content):
        return '<blockquote>' + str(content) + '</blockquote>'

    @staticmethod
    def hr():
        return '<hr />'

    @staticmethod
    def br():
        return '<br />'

    @staticmethod
    def head(content):
        return '<head>' + str(content) + '</head>'

    @staticmethod
    def title(content):
        return '<title>' + str(content) + '</title>'

    @staticmethod
    def meta(charset=None, name=None, content=None):
        if charset:
            return f'<meta charset="{charset}">'
        elif name and content:
            return f'<meta name="{name}" content="{content}">'

    @staticmethod
    def link(rel, href, type_attr=None):
        type_string = f' type="{type_attr}"' if type_attr else ''
        return f'<link rel="{rel}" href="{href}"{type_string}>'

    @staticmethod
    def style(content):
        return '<style>' + str(content) + '</style>'

    @staticmethod
    def script(src, content):
        if src != "noImport":
            return f'<script src="{src}"></script>'
        else:
            return '<script>' + str(content) + '</script>'
