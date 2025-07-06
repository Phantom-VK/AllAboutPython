from rembg import remove
from PIL import Image

# Load image
input_path = "AirSageWIthName.png"  # Change this to your image path
output_path = "AirSageWIthNameNoBG.png"

def remove_background(input_path: str, output_path: str):
    image = Image.open(input_path).convert("RGBA")  # Convert to RGBA for transparency
    output = remove(image)  # Remove background
    output.save(output_path, format="PNG")  # Save as PNG to preserve transparency
    print(f"✅ Background removed successfully! Saved at: {output_path}")

# Save the output
# Run background removal
remove_background(input_path, output_path)
