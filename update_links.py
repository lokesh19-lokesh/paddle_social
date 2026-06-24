import os
import glob

footer_target = """                        <li><a href="faqs.html">FAQs</a></li>
                    </ul>"""
footer_replacement = """                        <li><a href="faqs.html">FAQs</a></li>
                        <li><a href="contact.html">Contact Us</a></li>
                    </ul>"""

nav_target = """            <a href="sponsor.html">Sponsorship</a>"""
nav_replacement = """            <a href="sponsor.html">Sponsorship</a>
            <a href="contact.html">Contact Us</a>"""

for filepath in glob.glob("*.html"):
    if filepath == "contact.html":
        continue
        
    with open(filepath, 'r') as f:
        content = f.read()
        
    # Replace in footer
    content = content.replace(footer_target, footer_replacement)
    
    # Replace in nav (header and mobile nav both use a similar format or the exact same string)
    content = content.replace(nav_target, nav_replacement)
    
    with open(filepath, 'w') as f:
        f.write(content)
        
    print(f"Updated {filepath}")
