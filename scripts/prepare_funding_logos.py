"""Trim near-white outer margins without resizing or changing retained pixels.

Run from any directory with Python and Pillow installed:
    python3 scripts/prepare_funding_logos.py
Original files are never overwritten. An 8-pixel safety margin is retained.
"""
from pathlib import Path
from PIL import Image, ImageChops

IMAGE_DIR = Path(__file__).resolve().parents[1] / 'assets' / 'images'
WHITE_THRESHOLD = 245
PADDING = 8


def prepare(source_name, output_name):
    with Image.open(IMAGE_DIR / source_name) as source:
        rgba = source.convert('RGBA')
        # Transparency is treated as white only for detecting empty margins.
        visible = Image.alpha_composite(Image.new('RGBA', rgba.size, 'white'), rgba).convert('RGB')
        red, green, blue = visible.split()
        darkest = ImageChops.darker(ImageChops.darker(red, green), blue)
        artwork = darkest.point(lambda value: 255 if value < WHITE_THRESHOLD else 0)
        bounds = artwork.getbbox()
        if bounds is None:
            raise ValueError(f'No artwork detected in {source_name}')
        left, top, right, bottom = bounds
        crop = (max(0, left-PADDING), max(0, top-PADDING),
                min(source.width, right+PADDING), min(source.height, bottom+PADDING))
        result = rgba.crop(crop)
        result.save(IMAGE_DIR / output_name, optimize=True)
        print(f'{source_name}: {source.size} -> {result.size}; crop={crop}; artwork={bounds}')
        return crop


if __name__ == '__main__':
    prepare('dfg.jpg', 'dfg-display.png')
    prepare('jsps.png', 'jsps-display.png')
