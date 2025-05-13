import importlib.util

# Load the HTMLBuilder module dynamically
spec = importlib.util.spec_from_file_location("HTMLBuilder", "./src/Html_Builder_Bradley_Hu/htmlBuilder.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
HTMLBuilder = module.HTMLBuilder

# Test 1: Basic HTML structure
def test_1():
    obj = HTMLBuilder()
    obj.doctype(obj)
    obj.html(obj, obj.head("") + obj.body(obj, obj.h1(obj, "Title test") + obj.p(obj, "Paragraph")))
    print(obj.get_html())

# Test 2: Nested HTML elements
def test_2():
    obj = HTMLBuilder()
    obj.doctype(obj)
    nested_div = obj.div(obj, obj.p(obj, "Nested paragraph inside div") + obj.span(obj, "Span inside div"))
    obj.html(obj, obj.body(obj, obj.h1(obj, "Nested Elements Test") + nested_div))
    print(obj.get_html())

# Test 3: HTML with attributes
def test_3():
    obj = HTMLBuilder()
    obj.doctype(obj)
    obj.html(obj, obj.body(obj, obj.h1(obj, "Attributes Test", {"class": "header"}) + obj.p(obj, "Paragraph with id", {"id": "para1"})))
    print(obj.get_html())

# Test 4: Complex structure with multiple elements
def test_4():
    obj = HTMLBuilder()
    obj.doctype(obj)
    obj.html(obj, obj.body(obj, 
        obj.h1(obj, "Complex Structure Test") +
        obj.div(obj, 
            obj.ul(obj, 
                obj.li(obj, "Item 1") +
                obj.li(obj, "Item 2") +
                obj.li(obj, "Item 3")
            ) +
            obj.p(obj, "Paragraph inside div")
        ) +
        obj.footer(obj, "Footer content")
    ))
    print(obj.get_html())

# Test 5: Empty tags and self-closing tags
def test_5():
    obj = HTMLBuilder()
    obj.doctype(obj)
    obj.html(obj, obj.body(obj, 
        obj.h1(obj, "Empty and Self-Closing Tags Test") +
        obj.img(obj, {"src": "image.jpg", "alt": "Sample Image"}) +
        obj.br(obj) +
        obj.hr(obj)
    ))
    print(obj.get_html())

# Test 6: Invalid inputs and error handling
def test_6():
    obj = HTMLBuilder()
    try:
        obj.doctype(obj)
        obj.html(obj, obj.body(obj, obj.h1(obj, None)))  # Passing None as content
        print(obj.get_html())
    except Exception as e:
        print(f"Error caught: {e}")

# Test 7: Multiple nested levels
def test_7():
    obj = HTMLBuilder()
    obj.doctype(obj)
    deeply_nested = obj.div(obj, 
        obj.div(obj, 
            obj.div(obj, 
                obj.p(obj, "Deeply nested paragraph")
            )
        )
    )
    obj.html(obj, obj.body(obj, deeply_nested))
    print(obj.get_html())

# Run all tests
if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    test_6()
    test_7()
