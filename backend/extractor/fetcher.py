import requests #type: ignore
import cssutils #type: ignore

def fetch_css(css_url):
    response = requests.get(css_url)
    if response.status_code == 200:
        return response.text
    return None

def parse_css(css_content):
    colors = []
    parser = cssutils.CSSParser()
    stylesheet = parser.parseString(css_content)

    for rule in stylesheet:
        if rule.type == rule.STYLE_RULE:
            for property in rule.style:
                if property.name in ['color', 'background-color', 'border-color']:
                    colors.append(property.value)
    return colors
