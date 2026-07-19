from pathlib import Path
from PIL import Image, ImageDraw

base = Path(__file__).resolve().parent.parent

sizes = [
    ("images/hero-nairobi-small.webp", (700, 525)),
    ("images/hero-nairobi-large.webp", (1200, 900)),
]

for name, size in sizes:
    img = Image.new("RGB", size, (247, 241, 230))
    draw = ImageDraw.Draw(img)

    draw.rectangle((0, size[1] // 2, size[0], size[1]), fill=(31, 75, 75))
    draw.rectangle((0, size[1] // 2 - 80, size[0], size[1] // 2 + 20), fill=(191, 122, 46))
    draw.ellipse((size[0] // 2 - 90, 80, size[0] // 2 + 90, 260), fill=(242, 184, 75))
    draw.rectangle((80, size[1] // 2 + 40, size[0] - 80, size[1] - 60), fill=(255, 252, 244))
    draw.rectangle((110, size[1] // 2 + 70, size[0] - 110, size[1] - 90), fill=(223, 236, 231))

    img.save(base / name, "WEBP", quality=90)
