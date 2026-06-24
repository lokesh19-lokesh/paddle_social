document.addEventListener('DOMContentLoaded', () => {
    // Mobile Menu Toggle
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const mobileNavClose = document.querySelector('.mobile-nav-close');
    const mobileNav = document.getElementById('mobileNav');

    if (mobileMenuBtn && mobileNavClose && mobileNav) {
        mobileMenuBtn.addEventListener('click', () => {
            mobileNav.classList.add('open');
            document.body.style.overflow = 'hidden'; // Prevent scrolling
        });

        mobileNavClose.addEventListener('click', () => {
            mobileNav.classList.remove('open');
            document.body.style.overflow = '';
        });

        // Close when clicking a link
        const mobileLinks = mobileNav.querySelectorAll('a');
        mobileLinks.forEach(link => {
            link.addEventListener('click', () => {
                mobileNav.classList.remove('open');
                document.body.style.overflow = '';
            });
        });
    }

    // Set Active Link Based on URL
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.header-nav a, .mobile-nav a');
    
    navLinks.forEach(link => {
        const linkPath = link.getAttribute('href');
        // Handle root vs index.html
        if (
            currentPath.endsWith(linkPath) || 
            (currentPath.endsWith('/') && linkPath === 'index.html') ||
            (currentPath.includes(linkPath.replace('.html', '')))
        ) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });

    // Accordion Logic for FAQs
    const accordionHeaders = document.querySelectorAll('.accordion-header');
    accordionHeaders.forEach(header => {
        header.addEventListener('click', () => {
            const content = header.nextElementSibling;
            const icon = header.querySelector('i');
            
            // Close all others
            document.querySelectorAll('.accordion-content').forEach(item => {
                if(item !== content) {
                    item.style.maxHeight = null;
                    item.previousElementSibling.querySelector('i').className = 'fa-solid fa-chevron-down';
                }
            });

            if (content.style.maxHeight) {
                content.style.maxHeight = null;
                icon.className = 'fa-solid fa-chevron-down';
            } else {
                content.style.maxHeight = content.scrollHeight + "px";
                icon.className = 'fa-solid fa-chevron-up';
            }
        });
    });
});
