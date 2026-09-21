import sys
import os
from PIL import Image, ImageDraw

def process_image(input_path, output_dir):
    image = Image.open(input_path).convert("RGB")
    width, height = image.size
    fmt = image.format or "JPEG"
    filename = os.path.basename(input_path)

    print(f"Metadata -> Name: {filename}, Size: {width}x{height}, Format: {fmt}")

    draw = ImageDraw.Draw(image)
    draw.text((20, height - 40), "CONFIDENTIAL - DEMO", fill=(255, 0, 0))

    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"processed_{filename}")
    image.save(output_path, format="JPEG")
    print(f"Saved processed image to {output_path}")

if __name__ == "__main__":
    input_file = sys.argv[1]
    process_image(input_file, "processed")
