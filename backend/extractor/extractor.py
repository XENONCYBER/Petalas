import requests #type: ignore
from bs4 import BeautifulSoup #type: ignore
from color_parser import parse_html #type: ignore
from css_fetcher import fetch_css, parse_css #type: ignore
import re
from colormath.color_objects import sRGBColor #type: ignore

def extract_colors_from_url(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to fetch the webpage.")

    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract inline and <style> colors
    inline_colors = parse_html(html_content)

    # Extract external CSS colors
    external_colors = []
    for link in soup.find_all('link', {'rel': 'stylesheet'}):
        css_url = link['href']
        if not css_url.startswith('http'):
            css_url = url + css_url  # Handle relative URLs
        css_content = fetch_css(css_url)
        if css_content:
            external_colors.extend(parse_css(css_content))

    # Combine and remove duplicates
    all_colors = set(inline_colors + external_colors)
    return all_colors


def normalize_color(color):
    # Handle HEX format directly
    if color.startswith('#'):
        return color

    # Handle RGB(A) format
    match = re.match(r'rgb(a?)\(([\d\s,\.]+)\)', color)
    if match:
        components = [float(c) for c in match.group(2).split(',')[:3]]
        rgb = sRGBColor(*[c / 255.0 for c in components], is_upscaled=False)
        return rgb.get_hex()
    
    return None
