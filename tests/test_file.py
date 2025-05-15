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
    """Test basic HTML structure generation."""
    html_builder.doctype(html_builder)
    html_builder.html(html_builder,html_builder.head(html_builder,"") + html_builder.body(html_builder,html_builder.h1(html_builder,"Title test") + html_builder.p(html_builder,"Paragraph")))
    expected_html = "<!DOCTYPE html>\n<html><head></head><body><h1>Title test</h1><p>Paragraph</p></body></html>"
    assert html_builder.get_html() == expected_html


def test_nested_html_elements(html_builder):
    """Test HTML with nested elements."""
    html_builder.doctype(html_builder)
    nested_div = html_builder.div(html_builder,html_builder.p(html_builder,"Nested paragraph inside div") + html_builder.div(html_builder,"Span inside div"))
    html_builder.html(html_builder,html_builder.body(html_builder,html_builder.h1(html_builder,"Nested Elements Test") + nested_div))
    expected_html = (
        "<!DOCTYPE html>\n<html><body>"
        "<h1>Nested Elements Test</h1>"
        "<div><p>Nested paragraph inside div</p><div>Span inside div</div></div>"
        "</body></html>"
    )
    assert html_builder.get_html() == expected_html


def test_empty_html_document(html_builder):
    """Test generating an empty HTML document."""
    html_builder.doctype(html_builder)
    html_builder.html(html_builder,"")
    expected_html = "<!DOCTYPE html>\n<html></html>"
    assert html_builder.get_html() == expected_html
