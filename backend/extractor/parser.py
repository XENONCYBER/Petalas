from bs4 import BeautifulSoup #type: ignore

def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    colors = []

    # Extract inline styles
    for element in soup.find_all(style=True):
        style = element['style']
        if 'color:' in style or 'background-color:' in style:
            colors.append(style)

    # Extract colors from <style> blocks
    for style_tag in soup.find_all('style'):
        colors.extend(style_tag.string.split(';'))

    return colors
