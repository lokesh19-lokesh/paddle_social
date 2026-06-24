import os
import glob

new_footer = """    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col">
                    <img src="asset/logo.png" alt="Paddle Social by Smaar" style="height: 40px; margin-bottom: 20px;">
                    <p>A new place to play, connect & belong. An initiative by Shehzan Mohammed, Founder, Smaar.</p>
                    <div style="margin-top: 15px; color: var(--neon-lime);">
                        <p><i class="fa-solid fa-location-dot" style="margin-right: 10px;"></i> Vijayapuri Colony, Tarnaka</p>
                        <p><i class="fa-solid fa-phone" style="margin-right: 10px;"></i> <a href="tel:8885072259" style="color: var(--neon-lime);">8885072259</a></p>
                    </div>
                    <div class="social-links">
                        <a href="#"><i class="fa-brands fa-instagram"></i></a>
                        <a href="#"><i class="fa-brands fa-twitter"></i></a>
                        <a href="#"><i class="fa-brands fa-facebook-f"></i></a>
                    </div>
                </div>
                <div class="footer-col">
                    <h4>Quick Links</h4>
                    <ul class="footer-links">
                        <li><a href="index.html">Home</a></li>
                        <li><a href="programs.html">Programs</a></li>
                        <li><a href="coaches.html">Coaches</a></li>
                        <li><a href="faqs.html">FAQs</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Community</h4>
                    <ul class="footer-links">
                        <li><a href="rtm.html">Tournaments (RTM)</a></li>
                        <li><a href="private-events.html">Private Events</a></li>
                        <li><a href="sponsor.html">Sponsorships</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                &copy; 2026 Paddle Social. All Rights Reserved. Designed by <a href="https://thepatternscompany.com/" style="color: var(--text-gray); text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='var(--neon-lime)'" onmouseout="this.style.color='var(--text-gray)'">The Patterns Company.</a>
            </div>
        </div>
    </footer>"""

for file in glob.glob("*.html"):
    with open(file, 'r') as f:
        content = f.read()
    
    start_idx = content.find('<footer')
    end_idx = content.find('</footer>') + len('</footer>')
    
    if start_idx != -1 and end_idx != -1:
        new_content = content[:start_idx] + new_footer + content[end_idx:]
        with open(file, 'w') as f:
            f.write(new_content)
        print(f"Updated {file}")
