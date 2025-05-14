import importlib.util

# Load the HTMLBuilder module dynamically
spec = importlib.util.spec_from_file_location("HTMLBuilder", "./src/Html_Builder_Bradley_Hu/htmlBuilder.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
HTMLBuilder = module.HTMLBuilder

# Test 1: Basic HTML structure
def test_basic_html_structure():
    obj = HTMLBuilder()
    obj.doctype(obj)
    obj.html(obj, obj.head("") + obj.body(obj.h1("Title test") + obj.p("Paragraph")))
    expected_html = "<!DOCTYPE html><html><head></head><body><h1>Title test</h1><p>Paragraph</p></body></html>"
    assert obj.get_html() == expected_html

# Test 2: Nested HTML elements
def test_nested_html_elements():
    obj = HTMLBuilder()
    obj.doctype(obj)
    nested_div = obj.div(obj.p("Nested paragraph inside div") + obj.span("Span inside div"))
    obj.html(obj, obj.body(obj.h1("Nested Elements Test") + nested_div))
    expected_html = (
        "<!DOCTYPE html><html><body>"
        "<h1>Nested Elements Test</h1>"
        "<div><p>Nested paragraph inside div</p><span>Span inside div</span></div>"
        "</body></html>"
    )
    assert obj.get_html() == expected_html

# Test 3: HTML with attributes
def test_html_with_attributes():
    obj = HTMLBuilder()
    obj.doctype(obj)
    obj.html(obj, obj.body(obj.h1("Attributes Test", {"class": "header"}) + obj.p("Paragraph with id", {"id": "para1"})))
    expected_html = (
        '<!DOCTYPE html><html><body>'
        '<h1 class="header">Attributes Test</h1>'
        '<p id="para1">Paragraph with id</p>'
        '</body></html>'
    )
    assert obj.get_html() == expected_html

# Test 4: Complex structure with multiple elements
def test_complex_structure():
    obj = HTMLBuilder()
    obj.doctype(obj)
    obj.html(obj, obj.body(
        obj.h1("Complex Structure Test") +
        obj.div(
            obj.ul(
                obj.li("Item 1") +
                obj.li("Item 2") +
                obj.li("Item 3")
            ) +
            obj.p("Paragraph inside div")
        ) +
        obj.footer("Footer content")
    ))
    expected_html = (
        "<!DOCTYPE html><html><body>"
        "<h1>Complex Structure Test</h1>"
        "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul>"
        "<p>Paragraph inside div</p></div>"
        "<footer>Footer content</footer>"
        "</body></html>"
    )
    assert obj.get_html() == expected_html

# Test 5: Empty tags and self-closing tags
def test_empty_and_self_closing_tags():
    obj = HTMLBuilder()
    obj.doctype(obj)
    obj.html(obj, obj.body(
        obj.h1("Empty and Self-Closing Tags Test") +
        obj.img({"src": "image.jpg", "alt": "Sample Image"}) +
        obj.br() +
        obj.hr()
    ))
    expected_html = (
        '<!DOCTYPE html><html><body>'
        '<h1>Empty and Self-Closing Tags Test</h1>'
        '<img src="image.jpg" alt="Sample Image"/>'
        '<br/><hr/>'
        '</body></html>'
    )
    assert obj.get_html() == expected_html

# Test 6: Invalid inputs and error handling
def test_invalid_inputs():
    obj = HTMLBuilder()
    try:
        obj.doctype(obj)
        obj.html(obj, obj.body(obj.h1(None)))  # Passing None as content
        assert False, "Expected an exception when passing None as content"
    except Exception as e:
        assert str(e) == "Invalid content provided", f"Unexpected error: {e}"

# Test 7: Multiple nested levels
def test_multiple_nested_levels():
    obj = HTMLBuilder()
    obj.doctype(obj)
    deeply_nested = obj.div(
        obj.div(
            obj.div(
                obj.p("Deeply nested paragraph")
            )
        )
    )
    obj.html(obj, obj.body(deeply_nested))
    expected_html = (
        "<!DOCTYPE html><html><body>"
        "<div><div><div><p>Deeply nested paragraph</p></div></div></div>"
        "</body></html>"
    )
    assert obj.get_html() == expected_html
