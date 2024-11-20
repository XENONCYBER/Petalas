# Petalas
## Objective
The project is designed to:
1. **Extract colors** from websites' CSS and HTML.
2. **Organize extracted color data** for analysis and reuse.
3. **Predict and recommend color combinations** for frontend design based on UI/UX principles.
4. **Generate shades and tints** for any given color.
5. **Group similar colors** (e.g., shades of a color) for better organization.

---

## Core Features

### 1. Color Extraction
- **Purpose**: Automatically extracts all colors used on a website, including inline styles, `<style>` blocks, and external CSS files.
- **Method**:
  - Parse HTML for inline styles and `<style>` blocks.
  - Fetch and analyze external CSS files.
  - Extract properties like `color`, `background-color`, and `border-color`.

### 2. Color Storage and Organization
- **Purpose**: Store extracted colors in a database for easy retrieval and analysis.
- **Details**:
  - Store colors along with metadata:
    - **Hex/RGB value**
    - **Source** (e.g., URL, element type, CSS file)
    - **Usage Context** (e.g., primary text, button background)
  - Group similar colors based on their LAB color space proximity using clustering algorithms.

### 3. Shade Generation
- **Purpose**: Generate lighter and darker shades for any given color to provide design flexibility.
- **Details**:
  - Use the HSL (Hue, Saturation, Lightness) model for manipulating lightness values.
  - Output shades in HEX format for easy use in design.

### 4. Predictive Color Matching
- **Purpose**: Recommend complementary and harmonious color palettes for UI/UX design.
- **Details**:
  - Analyze stored color combinations from various websites.
  - Use principles like analogous, complementary, and triadic color harmony to recommend matching palettes.
  - Optionally, incorporate machine learning to enhance predictions.

---

## Implementation Roadmap

### Phase 1: Core Color Extraction
- **Tasks**:
  1. Parse HTML for inline styles and `<style>` blocks using `BeautifulSoup`.
  2. Extract colors from external CSS files using `cssutils` and `requests`.
- **Output**: A Python function to extract and list all colors used on a website.

---

### Phase 2: Color Storage and Grouping
- **Tasks**:
  1. Set up a database (SQLite or MongoDB) to store colors with metadata.
  2. Use LAB color space and clustering algorithms (e.g., K-Means) to group similar colors.
  3. Create an interface for querying stored color data.
- **Output**: A structured database of colors grouped by similarity.

---

### Phase 3: Shade Generation
- **Tasks**:
  1. Use `matplotlib.colors` or `colorsys` to generate lighter and darker shades.
  2. Create a function to output a range of shades for any input color.
- **Output**: A utility to generate a palette of shades for any given color.

---

### Phase 4: Predictive Color Matching
- **Tasks**:
  1. Analyze stored color combinations to identify common patterns.
  2. Build a rule-based recommendation engine based on color harmony principles.
  3. (Optional) Integrate machine learning to predict harmonious palettes based on data trends.
- **Output**: A recommendation system for harmonious color palettes.

---

## Technologies Used
- **Web Scraping**:
  - `BeautifulSoup` for parsing HTML.
  - `cssutils` for analyzing CSS.
  - `requests` for fetching external CSS files.
- **Database**:
  - SQLite or MongoDB for storing extracted color data.
- **Visualization**:
  - `matplotlib` for generating and visualizing color palettes.
- **Color Analysis**:
  - `colormath` for working with LAB color space.
  - `sklearn` for clustering similar colors.
- **Backend**:
  - Python for core functionality.

---

## Project Workflow

1. **Data Input**:
   - Accepts a website URL as input.
2. **Color Extraction**:
   - Parses HTML and CSS to extract all color-related properties.
3. **Storage**:
   - Stores extracted colors with metadata in a database.
   - Groups similar colors using clustering algorithms.
4. **Processing**:
   - Generates lighter and darker shades for individual colors.
   - Analyzes stored data to recommend harmonious color palettes.
5. **Output**:
   - Users can query:
     - All colors used on a website.
     - Recommended palettes for a specific input color.
     - Shades of a given color.

---

## Key Code Modules

### 1. **Extractor**
- Extracts colors from websites' inline styles, `<style>` blocks, and external CSS files.

### 2. **Storage**
- Stores extracted colors in a database and organizes them into groups based on similarity.

### 3. **Shade Generator**
- Generates shades and tints for any given color.

### 4. **Recommender**
- Predicts harmonious color palettes using predefined rules and data analysis.

---
