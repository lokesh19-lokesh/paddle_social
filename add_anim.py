import glob

anim_html = """
        <div class="pickleball-animation">
            <div class="paddle left-paddle"></div>
            <div class="net"></div>
            <div class="paddle right-paddle"></div>
            <div class="ball"><div class="ball-inner"></div></div>
        </div>"""

for file in glob.glob("*.html"):
    with open(file, 'r') as f:
        content = f.read()
    
    target = '<footer class="footer">'
    if target in content and 'class="pickleball-animation"' not in content:
        content = content.replace(target, target + anim_html)
        with open(file, 'w') as f:
            f.write(content)
        print(f"Added animation to {file}")
