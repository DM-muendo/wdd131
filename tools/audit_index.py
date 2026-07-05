from pathlib import Path
import re
p=Path('index.html')
if not p.exists():
    print('index.html not found')
    raise SystemExit(1)
s=p.read_text(encoding='utf-8')
checks=[]
# doctype
doctype_ok = bool(re.search(r'<!DOCTYPE\s+html>', s, re.I))
checks.append(('Doctype present',doctype_ok))
# html lang
html_lang_ok = bool(re.search(r'<html[^>]*\slang=["\']?\w+', s, re.I))
checks.append(('HTML tag with lang', html_lang_ok))
# meta charset
meta_charset_ok = bool(re.search(r'<meta\s+charset=["\']?utf-8["\']?', s, re.I))
checks.append(('Meta charset', meta_charset_ok))
# title
title_m = re.search(r'<title>(.*?)</title>', s, re.I|re.S)
title_ok = False
if title_m:
    t = title_m.group(1)
    title_ok = ('WDD' in t or 'WDD 131' in t) and 'Dynamic Web Fundamentals' in t and ('Denis' in t or 'Muendo' in t)
checks.append(('Title includes required text', title_ok))
# meta description
md_m = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', s, re.I|re.S)
md_ok = False
if md_m:
    content = md_m.group(1).strip()
    md_ok = 50 <= len(content) <= 160 and 'WDD 131' in content and 'Denis' in content
checks.append(('Meta description', md_ok))
# meta author
ma_ok = bool(re.search(r'<meta\s+name=["\']author["\']\s+content=["\'](.*?)["\']', s, re.I|re.S))
checks.append(('Meta author present', ma_ok))
# header and course-title
header_ok = bool(re.search(r'<header[\s\S]*?>', s, re.I))
course_title_ok = bool(re.search(r'<span[^>]*id=["\']course-title["\']', s, re.I))
checks.append(('Header element', header_ok))
checks.append(('Span #course-title present', course_title_ok))
# nav links
nav_m = re.search(r'<nav[\s\S]*?</nav>', s, re.I)
nav_links_ok = False
if nav_m:
    a_tags = re.findall(r'<a\s+[^>]*>', nav_m.group(0), re.I)
    nav_links_ok = len(a_tags) >= 4
checks.append(('Nav with >=4 links', nav_links_ok))
# main and h1
main_ok = bool(re.search(r'<main[\s\S]*?>', s, re.I))
h1_ok = bool(re.search(r'<main[\s\S]*?<h1[^>]*>.*?</h1>', s, re.I))
checks.append(('Main element', main_ok))
checks.append(('Main contains single h1', h1_ok))
# two section.cards
cards = re.findall(r'<section[^>]+class=["\']?[^>]*card[^>]*>', s, re.I)
checks.append(('At least two sections.card', len(cards) >= 2))
# footer p checks
footer_m = re.search(r'<footer[\s\S]*?</footer>', s, re.I)
footer_ok = False
if footer_m:
    p_tags = re.findall(r'<p[^>]*>.*?</p>', footer_m.group(0), re.I)
    span_inside = bool(re.search(r'<span[^>]*id=["\']currentyear["\']', footer_m.group(0), re.I))
    footer_ok = len(p_tags) == 2 and span_inside
checks.append(('Footer has 2 <p> and <span id="currentyear">', footer_ok))
# stylesheet link
css_ok = bool(re.search(r'<link\s+[^>]*href=["\']styles/base.css["\']', s, re.I))
checks.append(('Linked styles/base.css', css_ok))
# google fonts links
gf_ok = bool(re.search(r'fonts.googleapis.com', s, re.I)) and bool(re.search(r'rel=["\']preconnect["\']\s+href=["\']https://fonts.googleapis.com', s, re.I))
checks.append(('Google Fonts preconnect and link', gf_ok))
# script
script_ok = bool(re.search(r'<script\s+[^>]*src=["\']scripts/getdates.js["\'][^>]*defer', s, re.I))
checks.append(('Script getdates.js with defer', script_ok))
# images local
imgs = re.findall(r'<img\s+[^>]*src=["\']([^"\']+)["\'][^>]*alt=["\']([^"\']*)["\']', s, re.I)
imgs_ok = len(imgs) >= 2 and all(not src.startswith('http') for src,alt in imgs) and all(alt.strip() for src,alt in imgs)
checks.append(('Local images with alt text (>=2)', imgs_ok))

print('Local audit checklist for index.html')
for name,ok in checks:
    print(f"- {'PASS' if ok else 'FAIL'}: {name}")

print('\nSuggestions:')
if not doctype_ok: print('- Add <!DOCTYPE html> as the very first line of the document.')
if not md_ok: print('- Update meta description to 50-160 characters and include "WDD 131" and your full name.')
if not ma_ok: print('- Add <meta name="author" content="Your Full Name">')
if not nav_links_ok: print('- Ensure the <nav> contains at least 4 <a> links.')
if not cards or len(cards) < 2: print('- Add two <section class="card"> elements inside <main>.')
if not footer_ok: print('- Ensure <footer> contains exactly two <p> elements and the first contains <span id="currentyear"></span>.')
print('\nEnd of audit')
