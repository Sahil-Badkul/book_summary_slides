from PIL import Image
import os

TARGET_SIZE = 1.9 * 1024 * 1024  # 1.9 MB in bytes

def compress_png(input_path, output_path):
    img = Image.open(input_path)

    # Start with high-quality palette conversion (best balance)
    colors = 256  

    while colors >= 32:
        temp_output = output_path

        # Convert to palette-based PNG (reduces size without much visual loss)
        compressed = img.convert("P", palette=Image.ADAPTIVE, colors=colors)

        compressed.save(
            temp_output,
            optimize=True,
            compress_level=9  # max compression
        )

        size = os.path.getsize(temp_output)

        if size <= TARGET_SIZE:
            print(f"Success! Final size: {round(size/1024/1024, 2)} MB")
            return

        # Reduce colors gradually if still too large
        colors -= 32

    print("Could not reach target size without noticeable quality drop.")

# Usage
png_name = "Happiness is a skill"
input_path = f"/Users/mayankjain/Documents/Sahil Jain/Thumbnail/{png_name}.png"
output_path = f"/Users/mayankjain/Documents/Sahil Jain/Thumbnail/{png_name}_compressed.png"
# input_path = "/Users/mayankjain/Documents/Mayank Badkul/Thumbnail/How to earn 1cr in 365 days.png"
# output_path = "/Users/mayankjain/Documents/Mayank Badkul/Thumbnail/How to earn 1cr in 365 days_compressed.png"
compress_png(input_path, output_path)
