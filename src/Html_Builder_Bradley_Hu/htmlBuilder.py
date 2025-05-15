class HTMLBuilder:
    def __init__(self):
        self.html_text = ""

    def append(self, html_snippet):
        self.html_text += html_snippet

    def get_html(self):
        return self.html_text

    @staticmethod
    def validate_content(content):
        if content is None:
            raise ValueError("Invalid content provided: None is not allowed")
        return str(content)

    @staticmethod
    def doctype(self):
        snippet = '<!DOCTYPE html>\n'
        self.append(snippet)
        return snippet

    @staticmethod
    def html(self, content):
        snippet = '<html>' + self.validate_content(content) + '</html>'
        self.append(snippet)
        return snippet

    @staticmethod
    def head(self,content):
        snippet = '<head>' + HTMLBuilder.validate_content(content) + '</head>'
        return snippet

    @staticmethod
    def body(self, content):
        snippet = '<body>' + self.validate_content(content) + '</body>'
        return snippet

    @staticmethod
    def p(self, content):
        snippet = '<p>' + self.validate_content(content) + '</p>'
        return snippet

    @staticmethod
    def h1(self, content):
        snippet = '<h1>' + self.validate_content(content) + '</h1>'
        return snippet

    @staticmethod
    def div(self, content):
        snippet = '<div>' + self.validate_content(content) + '</div>'
        return snippet

    @staticmethod
    def img(src, alt=""):
        if not src:
            raise ValueError("Invalid src attribute for img tag")
        return f'<img src="{src}" alt="{alt}">'

    @staticmethod
    def br():
        return '<br />'

    @staticmethod
    def hr():
        return '<hr />'

    # Other methods remain unchanged, but you can add validation as needed
