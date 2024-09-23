class Solution:
    def entityParser(self, text: str) -> str:
        html_entities = {
            '&quot;': '"',
            '&apos;': "'",
            '&gt;': '>',
            '&lt;': '<',
            '&frasl;': '/',
            '&amp;': '&',
        }
        for html, char in html_entities.items():
            text = text.replace(html, char)

        return text
