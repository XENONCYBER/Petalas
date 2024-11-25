import extractor
import fetcher
import parser

def test_parse_html():
    html_content = '''
    <div style="color: #FF5733;"></div>
    <style>body { background-color: #C70039; }</style>
    '''
    colors = parse_html(html_content)
    assert '#FF5733' in colors
    assert '#C70039' in colors
