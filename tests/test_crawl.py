import unittest
from crawl import (
    normalize_url,
    get_h1_from_html,
    get_first_paragraph_from_html
)

class TestCrawl(unittest.TestCase):
    def test_normalize_url(self):
        input_url = "https://blog.boot.dev/path"
        actual = normalize_url(input_url)
        expected = "blog.boot.dev/path"
        self.assertEqual(actual, expected)

    def test_normalize_url_with_params(self):
        input_url = "https://docs.python.org/3/library/urllib.parse.html"
        expected_url = "docs.python.org/3/library/urllib.parse.html"
        actual_url = normalize_url(input_url)
        self.assertEqual(actual_url, expected_url)

    def test_normalize_multiple_urls(self):
        urls = [
            "https://blog.boot.dev/path/",
            "https://blog.boot.dev/path",
            "http://blog.boot.dev/path/",
            "http://blog.boot.dev/path",
        ]
        expected_url = 'blog.boot.dev/path'
        output_url = [normalize_url(url) for url in urls]
        self.assertListEqual(output_url, [expected_url for _ in range(4)])
        
    def test_normalize_url_with_trailing_slash(self):
        input_url = "https://example.com/path/"
        expected_url = "example.com/path"
        actual_url = normalize_url(input_url)
        self.assertEqual(actual_url, expected_url)

    def test_normalize_url_without_path(self):
        input_url = "https://example.com"
        expected_url = "example.com"
        actual_url = normalize_url(input_url)
        self.assertEqual(actual_url, expected_url)

    def test_normalize_url_with_subdomain(self):
        input_url = "https://sub.example.com/path"
        expected_url = "sub.example.com/path"
        actual_url = normalize_url(input_url)
        self.assertEqual(actual_url, expected_url)

    def test_normalize_url_with_port(self):
        input_url = "https://example.com:8080/path"
        expected_url = "example.com/path"
        actual_url = normalize_url(input_url)
        self.assertEqual(actual_url, expected_url)

    def test_normalize_url_with_query_params(self):
        input_url = "https://example.com/path?query=1"
        expected_url = "example.com/path"
        actual_url = normalize_url(input_url)
        self.assertEqual(actual_url, expected_url)

    def test_normalize_url_with_fragment(self):
        input_url = "https://example.com/path#section"
        expected_url = "example.com/path"
        actual_url = normalize_url(input_url)
        self.assertEqual(actual_url, expected_url)

    def test_normalize_url_with_empty_string(self):
        input_url = ""
        with self.assertRaises(ValueError):
            normalize_url(input_url)

    def test_normalize_url_with_invalid_url(self):
        input_url = "not-a-valid-url"
        with self.assertRaises(ValueError):
            normalize_url(input_url)

    def test_get_h1_from_html_basic(self):
        input_body = '<html><body><h1>Test Title</h1></body></html>'
        actual = get_h1_from_html(input_body)
        expected = "Test Title"
        self.assertEqual(actual, expected)

    def test_get_first_paragraph_from_html_main_priority(self):
        input_body = '''<html><body>
            <p>Outside paragraph.</p>
            <main>
                <p>Main paragraph.</p>
            </main>
        </body></html>'''
        actual = get_first_paragraph_from_html(input_body)
        expected = "Main paragraph."
        self.assertEqual(actual, expected)
        
    def test_get_h1_from_html_no_h1(self):
        input_body = '<html><body><p>No H1 here</p></body></html>'
        expected_body = ''
        output_body = get_h1_from_html(input_body)
        self.assertEqual(output_body, expected_body)

    def test_get_h1_from_html_empty_html(self):
        input_body = ''
        with self.assertRaises(ValueError):
            get_h1_from_html(input_body)

    def test_get_h1_from_html_nested_h1(self):
        input_body = '<html><body><div><h1>Nested H1</h1></div></body></html>'
        actual = get_h1_from_html(input_body)
        expected = "Nested H1"
        self.assertEqual(actual, expected)

    def test_get_first_paragraph_from_html_no_paragraph(self):
        input_body = '<html><body><div>No paragraph here</div></body></html>'
        expected_body = ''
        output_body = get_first_paragraph_from_html(input_body)
        self.assertEqual(output_body, expected_body)

    def test_get_first_paragraph_from_html_empty_html(self):
        input_body = ''
        with self.assertRaises(ValueError):
            get_first_paragraph_from_html(input_body)

    def test_get_first_paragraph_from_html_multiple_paragraphs(self):
        input_body = '''<html><body>
            <p>First paragraph.</p>
            <p>Second paragraph.</p>
        </body></html>'''
        actual = get_first_paragraph_from_html(input_body)
        expected = "First paragraph."
        self.assertEqual(actual, expected)

    def test_get_first_paragraph_from_html_nested_paragraphs(self):
        input_body = '''<html><body>
            <div><p>Nested paragraph.</p></div>
        </body></html>'''
        actual = get_first_paragraph_from_html(input_body)
        expected = "Nested paragraph."
        self.assertEqual(actual, expected)

    def test_get_first_paragraph_from_html_with_whitespace(self):
        input_body = '''<html><body>
            <p>   Paragraph with leading and trailing spaces.   </p>
        </body></html>'''
        actual = get_first_paragraph_from_html(input_body)
        expected = "Paragraph with leading and trailing spaces."
        self.assertEqual(actual, expected)

    def test_get_h1_from_html_with_special_characters(self):
        input_body = '<html><body><h1>Special &amp; Characters</h1></body></html>'
        actual = get_h1_from_html(input_body)
        expected = "Special & Characters"
        self.assertEqual(actual, expected)

    def test_get_first_paragraph_from_html_with_special_characters(self):
        input_body = '<html><body><p>Special &amp; Characters</p></body></html>'
        actual = get_first_paragraph_from_html(input_body)
        expected = "Special & Characters"
        self.assertEqual(actual, expected)
        
    def test_get_first_paragraph_from_html_complex_structure(self):
        input_body = '''<html><body>
            <div>
                <section>
                    <p>First paragraph in section.</p>
                </section>
                <main>
                    <article>
                        <p>Main article paragraph.</p>
                    </article>
                </main>
                <footer>
                    <p>Footer paragraph.</p>
                </footer>
            </div>
        </body></html>'''
        actual = get_first_paragraph_from_html(input_body)
        expected = "Main article paragraph."
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
