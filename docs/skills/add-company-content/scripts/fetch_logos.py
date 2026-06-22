import os
import sys
import ssl
import urllib.request
import urllib.error
from urllib.parse import urljoin, urlparse

# Public logo assets; some company sites use self-signed/expired certs.
ssl._create_default_https_context = ssl._create_unverified_context
from html.parser import HTMLParser

class LogoParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.logo_url = None
        self.icons = []

    def handle_starttag(self, tag, attrs):
        if self.logo_url:
            return
        attrs_dict = dict(attrs)
        if tag == 'link':
            rel = attrs_dict.get('rel', '').lower()
            if 'icon' in rel or 'apple-touch-icon' in rel:
                href = attrs_dict.get('href')
                if href:
                    self.icons.append((rel, href))
        elif tag == 'img':
            src = attrs_dict.get('src', '')
            classes = attrs_dict.get('class', '')
            id_val = attrs_dict.get('id', '')
            if 'logo' in id_val.lower() or 'logo' in classes.lower() or 'logo' in src.lower():
                if src:
                    self.logo_url = src

def get_logo_url(html, base_url):
    parser = LogoParser()
    parser.feed(html)
    
    if parser.logo_url:
        return urljoin(base_url, parser.logo_url)
    
    # Priority for apple-touch-icon
    for rel, href in parser.icons:
        if 'apple-touch-icon' in rel:
            return urljoin(base_url, href)
    
    # Fallback to any icon
    if parser.icons:
        return urljoin(base_url, parser.icons[0][1])
        
    return None

companies = [
    ("lymeric", "https://www.lymeric.ai/"),
    ("globaleur", "https://www.globaleur.com/"),
    ("ged", "http://www.gedkorea.com/"),
    ("mk-solar", "http://www.mksolar.co.kr/"),
    ("lazy-yogurt", "https://www.lazyyogurt.com/"),
    ("p2ach-ai", "https://p2ach.ai/"),
    ("nota-ai", "https://www.kr.nota.ai/"),
    ("visionspace", "https://visionspace.co.kr/"),
    ("shmd", "https://shmd.io/"),
    ("ipin-labs", "https://home.ipinlabs.com/"),
    ("miracles", "https://aiblab.kr/"),
    ("tinker", "http://www.tinker.style/"),
    ("sweetndata", "https://sweetndata.co.kr/")
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

for slug, url in companies:
    try:
        print(f"Fetching {slug} from {url}...")
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode('utf-8')
        
        logo_url = get_logo_url(html, url)
        if not logo_url:
            print(f"  [-] Could not find a logo/favicon for {slug}")
            continue
            
        print(f"  [+] Found logo URL: {logo_url}")
        
        img_req = urllib.request.Request(logo_url, headers=headers)
        with urllib.request.urlopen(img_req, timeout=10) as img_response:
            img_data = img_response.read()
            content_type = img_response.getheader('Content-Type', '')
        
        parsed_url = urlparse(logo_url)
        path = parsed_url.path
        ext = os.path.splitext(path)[1].lower()
        if not ext or ext not in ['.png', '.jpg', '.jpeg', '.svg', '.gif', '.ico']:
            if 'image/png' in content_type: ext = '.png'
            elif 'image/jpeg' in content_type: ext = '.jpg'
            elif 'image/svg+xml' in content_type: ext = '.svg'
            elif 'image/x-icon' in content_type: ext = '.ico'
            else: ext = '.png'
            
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
        target_dir = os.path.join(repo_root, "content", "companies", slug)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
            
        filename = f"logo{ext}"
        filepath = os.path.join(target_dir, filename)
        
        with open(filepath, 'wb') as f:
            f.write(img_data)
            
        print(f"  [+] Saved to {filepath}")
        
        for lang in ['index.md', 'index.ko.md']:
            md_path = os.path.join(target_dir, lang)
            if os.path.exists(md_path):
                with open(md_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = content.replace('logo: ""', f'logo: "{filename}"')
                
                with open(md_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"  [+] Updated {lang}")
                
    except Exception as e:
        print(f"  [-] Error processing {slug}: {e}")

print("Done.")
