import pytest
import importlib.util

# Dynamically load the HTMLBuilder module
spec = importlib.util.spec_from_file_location("HTMLBuilder", "./src/Html_Builder_Bradley_Hu/htmlBuilder.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
HTMLBuilder = module.HTMLBuilder


@pytest.fixture
def html_builder():
    """Fixture to create an instance of HTMLBuilder for each test."""
    return HTMLBuilder()


def test_basic_html_structure(html_builder):
    html_builder.doctype(html_builder)
    html_builder.html(html_builder.head("") + html_builder.body(html_builder.h1("Title test") + html_builder.p("Paragraph")))
    expected_html = "<!DOCTYPE html>\n<html><head></head><body><h1>Title test</h1><p>Paragraph</p></body></html>"
    assert html_builder.get_html() == expected_html


def test_nested_html_elements(html_builder):
    html_builder.doctype(html_builder)
    nested_div = html_builder.div(html_builder.p("Nested paragraph inside div") + html_builder.div("Span inside div"))
    html_builder.html(html_builder.body(html_builder.h1("Nested Elements Test") + nested_div))
    expected_html = (
        "<!DOCTYPE html>\n<html><body>"
        "<h1>Nested Elements Test</h1>"
        "<div><p>Nested paragraph inside div</p><div>Span inside div</div></div>"
        "</body></html>"
    )
    assert html_builder.get_html() == expected_html


def test_html_with_attributes(html_builder):
    html_builder.doctype(html_builder)
    html_builder.html(html_builder.body(html_builder.h1("Attributes Test") + html_builder.p("Paragraph with id")))
    expected_html = (
        '<!DOCTYPE html>\n<html><body>'
        '<h1>Attributes Test</h1>'
        '<p>Paragraph with id</p>'
        '</body></html>'
    )
    assert html_builder.get_html() == expected_html


def test_complex_structure(html_builder):
    html_builder.doctype(html_builder)
    html_builder.html(html_builder.body(
        html_builder.h1("Complex Structure Test") +
        html_builder.div(
            html_builder.ol(
                html_builder.li("Item 1") +
                html_builder.li("Item 2") +
                html_builder.li("Item 3")
            ) +
            html_builder.p("Paragraph inside div")
        ) +
        html_builder.footer("Footer content")
    ))
    expected_html = (
        "<!DOCTYPE html>\n<html><body>"
        "<h1>Complex Structure Test</h1>"
        "<div><ol><li>Item 1</li><li>Item 2</li><li>Item 3</li></ol>"
        "<p>Paragraph inside div</p></div>"
        "<footer>Footer content</footer>"
        "</body></html>"
    )
    assert html_builder.get_html() == expected_html


def test_empty_and_self_closing_tags(html_builder):
    html_builder.doctype(html_builder)
    html_builder.html(html_builder.body(
        html_builder.h1("Empty and Self-Closing Tags Test") +
        html_builder.img("image.jpg", "Sample Image") +
        html_builder.br() +
        html_builder.hr()
    ))
    expected_html = (
        '<!DOCTYPE html>\n<html><body>'
        '<h1>Empty and Self-Closing Tags Test</h1>'
        '<img src="image.jpg" alt="Sample Image">'
        '<br /><hr />'
        '</body></html>'
    )
    assert html_builder.get_html() == expected_html


def test_invalid_inputs(html_builder):
    with pytest.raises(ValueError, match="Invalid content provided: None is not allowed"):
        html_builder.doctype(html_builder)
        html_builder.html(html_builder.body(html_builder.h1(None)))  # Passing None as content


def test_multiple_nested_levels(html_builder):
    html_builder.doctype(html_builder)
    deeply_nested = html_builder.div(
        html_builder.div(
            html_builder.div(
                html_builder.p("Deeply nested paragraph")
            )
        )
    )
    html_builder.html(html_builder.body(deeply_nested))
    expected_html = (
        "<!DOCTYPE html>\n<html><body>"
        "<div><div><div><p>Deeply nested paragraph</p></div></div></div>"
        "</body></html>"
    )
    assert html_builder.get_html() == expected_html


if __name__ == "__main__":
    pytest.main()
