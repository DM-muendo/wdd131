from PIL import Image
from pathlib import Path

TARGET_DIR = Path(__file__).resolve().parents[1] / 'images'
TARGET_SIZE = 125 * 1024  # 125 KB

files = ['denis.jpg', 'kenya-flag.jpg']

for fname in files:
    path = TARGET_DIR / fname
    if not path.exists():
        print(f"Skipping missing: {path}")
        continue

    img = Image.open(path)
    img = img.convert('RGB')

    # Resize if width > 1200
    max_w = 1200
    if img.width > max_w:
        ratio = max_w / img.width
        new_size = (int(img.width * ratio), int(img.height * ratio))
        img = img.resize(new_size, Image.LANCZOS)
        print(f"Resized {fname} to {new_size}")

    # Try progressive quality until under target size
    quality = 85
    out_path = path
    while quality >= 30:
        img.save(out_path, format='JPEG', quality=quality, optimize=True)
        size = out_path.stat().st_size
        print(f"Saved {fname} with quality={quality}, size={size}")
        if size <= TARGET_SIZE:
            break
        quality -= 5

    if out_path.stat().st_size > TARGET_SIZE:
        # also try saving as WebP as fallback (create same-name .webp)
        webp_path = path.with_suffix('.webp')
        img.save(webp_path, format='WEBP', quality=80)
        print(f"Could not reach target for {fname}; created {webp_path.name} size={webp_path.stat().st_size}")

print('Done')
