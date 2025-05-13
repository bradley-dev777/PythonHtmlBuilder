import sys
import os
sys.path.append(os.path.abspath("/workspaces/Html_Builder_Bradley_Hu/src"))
from htmlBuilder import HTMLBuilder
obj = HTMLBuilder()
obj.doctype()
obj.html(obj.head("")+obj.body(obj.h1("Title test")+obj.p("Paragraph")))
print(obj.get_html())