import pytest
from bs4 import BeautifulSoup
from html2md import remove_tags


@pytest.fixture
def markdown_soup():
    """Returns a BeautifulSoup object representing a sample markdown file."""
    return BeautifulSoup(
        """
        # Heading 1
        Some **bold text** and _italic text_.
        
        A paragraph with a line break  
        and another line.
        
        <div>Some html code to remove.</div>
    """,
        "html.parser",
    )


def test_remove_tags_bold_and_italic(markdown_soup):
    """Test if bold and italic tags are removed properly."""
    assert (
        remove_tags(markdown_soup)
        == """# Heading 1
Some **bold text** and _italic text_.

A paragraph with a line break  
and another line.

Some html code to remove.
"""
    )


def test_remove_tags_linebreak(markdown_soup):
    """Test if line breaks are converted to LaTeX format."""
    assert (
        remove_tags(markdown_soup)
        == """# Heading 1
Some **bold text** and _italic text_.

A paragraph with a line break $\\$  
and another line.

Some html code to remove.
"""
    )


def test_remove_tags_html(markdown_soup):
    """Test if HTML tags are removed properly."""
    assert "<div>" not in remove_tags(markdown_soup)
