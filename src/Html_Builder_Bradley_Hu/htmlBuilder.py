class HTMLBuilder:
    def __init__(self):
        self.html_text = ""

    def append(self, html_snippet):
        self.html_text += html_snippet

    def get_html(self):
        return self.html_text

    @staticmethod
    def doctype(self):
        snippet = '<!DOCTYPE html>\n'
        self.append(snippet)
        return snippet

    @staticmethod
    def html(self, content):
        snippet = '<html>' + str(content) + '</html>'
        self.append(snippet)
        return snippet

    @staticmethod
    def span(content):
        if content is None:
            raise ValueError("Invalid content provided")
        snippet = '<span>' + str(content) + '</span>'
        return snippet

    @staticmethod
    def img(src, alt=""):
        return f'<img src="{src}" alt="{alt}">'

    @staticmethod
    def br():
        return '<br />'

    @staticmethod
    def hr():
        return '<hr />'

    # Add other methods as needed...
