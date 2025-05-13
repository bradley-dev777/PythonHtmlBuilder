import importlib.util
spec = importlib.util.spec_from_file_location("HTMLBuilder", "/workspaces/PythonHtmlBuilder/src/Html_Builder_Bradley_Hu/htmlBuilder.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
HTMLBuilder = module.HTMLBuilder
obj = HTMLBuilder()
obj.doctype(obj)
obj.html(obj,obj.head("")+obj.body(obj,obj.h1(obj,"Title test")+obj.p(obj,"Paragraph")))
print(obj.get_html())