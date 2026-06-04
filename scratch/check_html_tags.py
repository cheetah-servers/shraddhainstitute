from html.parser import HTMLParser

class TagChecker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        # Self-closing tags in HTML5
        self_closing = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 
                        'link', 'meta', 'param', 'source', 'track', 'wbr'}
        if tag not in self_closing:
            self.stack.append((tag, self.getpos()))

    def handle_endtag(self, tag):
        self_closing = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 
                        'link', 'meta', 'param', 'source', 'track', 'wbr'}
        if tag in self_closing:
            return
            
        if not self.stack:
            self.errors.append(f"Unexpected end tag </{tag}> at line {self.getpos()[0]}")
            return
            
        expected_tag, pos = self.stack.pop()
        if expected_tag != tag:
            self.errors.append(f"Mismatched end tag </{tag}> at line {self.getpos()[0]} (expected </{expected_tag}> opened at line {pos[0]})")
            # Push expected back to try to recover
            self.stack.append((expected_tag, pos))

with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

parser = TagChecker()
try:
    parser.feed(html_content)
    if parser.stack:
        for tag, pos in reversed(parser.stack):
            parser.errors.append(f"Unclosed tag <{tag}> opened at line {pos[0]}")
except Exception as e:
    print(f"Parser error: {e}")

if parser.errors:
    print("Found HTML tag mismatch errors:")
    for error in parser.errors[:20]:
        print(" -", error)
else:
    print("HTML tags are balanced and valid!")
