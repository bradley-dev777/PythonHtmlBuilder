from htmlBuilder import HTMLBuilder
obj = HTMLBuilder()
obj.doctype()
obj.html(obj.head("")+obj.body(obj.h1("Title test")+obj.p("Paragraph")))
print(obj.get_html())