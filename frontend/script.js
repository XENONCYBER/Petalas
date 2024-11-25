const analyzeBtn = document.getElementById("analyze-btn");
const extractedColorsDiv = document.getElementById("extracted-colors");
const colorPicker = document.getElementById("color-picker");
const generateShadesBtn = document.getElementById("generate-shades");
const shadesOutputDiv = document.getElementById("shades-output");

// Function to simulate color extraction (mock data for demo)
analyzeBtn.addEventListener("click", () => {
  const extractedColors = [
    "#3498db",
    "#e74c3c",
    "#2ecc71",
    "#f1c40f",
    "#9b59b6",
  ];
  extractedColorsDiv.innerHTML = ""; // Clear previous results

  extractedColors.forEach((color) => {
    const colorBox = document.createElement("div");
    colorBox.className = "color-box";
    colorBox.style.backgroundColor = color;
    extractedColorsDiv.appendChild(colorBox);
  });
});

// Function to generate shades
generateShadesBtn.addEventListener("click", () => {
  const baseColor = colorPicker.value;
  shadesOutputDiv.innerHTML = ""; // Clear previous results

  const shades = generateShades(baseColor, 5); // Generate 5 lighter and 5 darker shades
  shades.forEach((shade) => {
    const shadeBox = document.createElement("div");
    shadeBox.className = "color-box";
    shadeBox.style.backgroundColor = shade;
    shadesOutputDiv.appendChild(shadeBox);
  });
});

// Utility: Generate lighter and darker shades of a color
function generateShades(color, count) {
  const shades = [];
  const [r, g, b] = hexToRgb(color);

  for (let i = 1; i <= count; i++) {
    shades.push(rgbToHex(r + i * 10, g + i * 10, b + i * 10)); // Lighter
    shades.push(rgbToHex(r - i * 10, g - i * 10, b - i * 10)); // Darker
  }

  return shades.filter((shade) => isValidColor(shade)); // Ensure valid colors
}

// Utility: Convert HEX to RGB
function hexToRgb(hex) {
  const bigint = parseInt(hex.slice(1), 16);
  return [(bigint >> 16) & 255, (bigint >> 8) & 255, bigint & 255];
}

// Utility: Convert RGB to HEX
function rgbToHex(r, g, b) {
  return `#${((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1)}`;
}

// Utility: Validate if a color is valid
function isValidColor(hex) {
  return /^#[0-9A-F]{6}$/i.test(hex);
}
