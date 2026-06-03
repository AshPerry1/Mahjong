// Enhanced email functionality with better UX
function sendEmail(type) {
    // Track email button click (conversion event for retargeting)
    if (typeof gtag !== 'undefined') {
        gtag('event', 'click_email_button', {
            'event_category': 'Conversion',
            'event_label': type,
            'service_type': type,
            'user_intent': 'service_inquiry',
            'engagement_type': 'email_action'
        });
        
        // Add service-specific audience parameter
        const serviceMap = {
            'lesson': 'General Lesson Inquiry',
            '101': 'Mahjong 101 Course',
            '102': 'Mahjong 102 Course',
            'events': 'Private Event',
            'contact': 'General Contact',
            'travel': 'Travel Event',
            'tml': 'TML Products'
        };
        
        gtag('event', 'service_inquiry', {
            'event_category': 'Conversion',
            'event_label': serviceMap[type] || type,
            'service_interest': type
        });
    }
    
    const email = 'lookoutmountainmahjong@gmail.com';
    let subject = '';
    let body = '';
    
    // Add loading state to button
    const button = event.target;
    const originalText = button.innerHTML;
    button.innerHTML = '<span class="loading-spinner"></span> Sending...';
    button.disabled = true;
    
    switch(type) {
        case 'lesson':
            subject = 'Book Mahjong Lesson - Lookout Mountain Mahjong';
            body = `Dear Mahj Jen and Mahj Hen,

I'm excited to begin my mahjong journey with Lookout Mountain Mahjong and would love to book a lesson.

Could you please share:
- Available lesson dates and times
- Location and venue details
- What to expect during the session
- Investment for the lesson
- Whether you offer 101, 102, or other specialized courses

I'm eager to master American mahjong under your expert guidance and would appreciate any recommendations for the best starting point based on my experience level.

Best regards,
[Your Name]`;
            break;
            
        case '101':
            subject = 'Book Mahjong 101 Lessons';
            body = `Dear Mahj Jen and Mahj Hen,

I'm excited to begin my mahjong journey with Lookout Mountain Mahjong and would love to book your Mahjong 101 course.

Could you please share:
- Available session dates and times
- Location and venue details
- What to expect during the 2-3 hour session
- Investment for the course

I'm eager to master the fundamentals of American mahjong under your expert guidance.

Best regards,
[Your Name]`;
            break;
            
        case '102':
            subject = 'Book Mahjong 102 Lessons';
            body = `Dear Mahj Jen and Mahj Hen,

I'm ready to elevate my mahjong skills and would love to enroll in your Mahjong 102 advanced course.

Could you please provide:
- Available session dates and times
- Location and venue details
- Advanced strategies and techniques we'll explore
- Investment for the course

I'm excited to perfect my technique and master advanced strategies like Siamese and Patio play.

Best regards,
[Your Name]`;
            break;
            
        case 'events':
            subject = 'Book Private Mahjong Event - Lookout Mountain Mahjong';
            body = `Dear Mahj Jen and Mahj Hen,

I'm interested in booking a private mahjong event with Lookout Mountain Mahjong for my group.

Event Details:
- Group size: [Number of participants]
- Preferred date(s): [Date(s)]
- Event type: [Corporate team building/Social gathering/Special occasion]
- Location: [Your venue/Our location]
- Duration: [Preferred length]

Could you please provide:
- Custom pricing based on our needs
- Available dates and times
- What's included in the experience
- Setup requirements and materials
- Travel arrangements (if applicable)

We're excited to experience mahjong instruction tailored to our group's needs and skill levels.

Best regards,
[Your Name]`;
            break;
            
        case 'contact':
            subject = 'Inquiry - Lookout Mountain Mahjong';
            body = `Dear Mahj Jen and Mahj Hen,

I'd love to connect with you about Lookout Mountain Mahjong and explore how we might work together.

I'm interested in learning more about:
- Your mahjong instruction services
- Available lesson types and scheduling
- Private event options
- Pricing and packages
- Any upcoming tournaments or special events

Please share any additional information that would help me understand how Lookout Mountain Mahjong can best serve my mahjong needs.

I look forward to hearing from you and discovering how we can create an exceptional mahjong experience together.

Best regards,
[Your Name]`;
            break;
            
        case 'events':
            subject = 'Book Private Mahjong Event';
            body = `Dear Mahj Jen and Mahj Hen,

I'm excited to create a memorable mahjong experience and would love to book a private event with Lookout Mountain Mahjong.

Event Details:
- Preferred Date: [Date]
- Preferred Time: [Time]
- Venue/Location: [Location]
- Number of Participants: [Number]
- Event Type: [Corporate Team Building/Private Party/Sorority/Fraternity/Social Gathering/etc.]
- Special Requests: [Any specific requirements or preferences]

Could you please share:
- Your availability for our preferred date
- Investment and package options
- What's included in your premium service
- Any additional details to ensure our event is exceptional

I'm thrilled to bring the joy of mahjong to our group and create lasting memories together.

Best regards,
[Your Name]`;
            break;
            
        case 'travel':
            subject = 'Book Travel Mahjong Event';
            body = `Dear Mahj Jen and Mahj Hen,

I'm thrilled to bring Lookout Mountain Mahjong's expertise to our location and would love to book a travel event.

Event Details:
- Destination: [City/State]
- Preferred Date: [Date]
- Preferred Time: [Time]
- Event Type: [Corporate Team Building/Private Party/Sorority/Fraternity/Social Gathering/etc.]
- Number of Participants: [Number]
- Venue: [Hotel/Office/Home/etc.]

Could you please provide:
- Your travel availability and schedule
- Investment including travel accommodations
- Premium service inclusions
- Any additional details to ensure a seamless experience

I'm excited to create an unforgettable mahjong experience for our group in our own space.

Best regards,
[Your Name]`;
            break;
            
        case 'tml':
            subject = 'TML Referral Code Inquiry';
            body = `Dear Mahj Jen and Mahj Hen,

I'm excited to invest in premium mahjong tiles from The Mahjong Line and would love to use your exclusive referral code LOOKOUTMOUNTAIN.

Could you please share:
- Exclusive offers and special discounts available through your partnership
- Recommended tile collections for beginners and experienced players
- Additional insights about TML's exceptional craftsmanship and quality

I'm eager to enhance my mahjong experience with these beautifully crafted tiles.

Best regards,
[Your Name]`;
            break;
    }
    
    // Simulate email opening with success feedback
    setTimeout(() => {
        const mailtoLink = `mailto:${email}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
        window.open(mailtoLink);
        
        // Track email client opened
        if (typeof gtag !== 'undefined') {
            gtag('event', 'email_client_opened', {
                'event_category': 'Email Action',
                'event_label': type + ' - Email Client Opened'
            });
        }
        
        // Show success message
        showNotification('Email client opened! Please send your message.', 'success');
        
        // Reset button
        button.innerHTML = originalText;
        button.disabled = false;
    }, 800);
}

// Enhanced smooth scrolling with offset for fixed navbar + optional promo banner
function getFixedHeaderScrollOffset() {
    const bannerH = parseFloat(getComputedStyle(document.body).getPropertyValue('--site-promo-banner-height')) || 0;
    return bannerH + 96;
}

function smoothScrollTo(targetId) {
    const target = document.querySelector(targetId);
    if (target) {
        const offset = getFixedHeaderScrollOffset();
        const targetPosition = target.offsetTop - offset;
        
        window.scrollTo({
            top: targetPosition,
            behavior: 'smooth'
        });
    }
}

// Initialize smooth scrolling
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            smoothScrollTo(targetId);
        });
    });
});

// Enhanced mobile menu with better animations
const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');
let isMenuOpen = false;

if (hamburger && navMenu) {
    hamburger.addEventListener('click', () => {
        isMenuOpen = !isMenuOpen;
        hamburger.classList.toggle('active');
        navMenu.classList.toggle('active');

        document.body.style.overflow = isMenuOpen ? 'hidden' : '';

        hamburger.setAttribute('aria-expanded', isMenuOpen);
        hamburger.setAttribute('aria-label', isMenuOpen ? 'Close menu' : 'Open menu');
    });

    document.querySelectorAll('.nav-menu a').forEach(link => {
        link.addEventListener('click', () => {
            if (isMenuOpen) {
                hamburger.classList.remove('active');
                navMenu.classList.remove('active');
                document.body.style.overflow = '';
                isMenuOpen = false;
                hamburger.setAttribute('aria-expanded', 'false');
            }
        });
    });

    document.addEventListener('click', (e) => {
        if (isMenuOpen && !hamburger.contains(e.target) && !navMenu.contains(e.target)) {
            hamburger.classList.remove('active');
            navMenu.classList.remove('active');
            document.body.style.overflow = '';
            isMenuOpen = false;
            hamburger.setAttribute('aria-expanded', 'false');
        }
    });
}

// Enhanced intersection observer for animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate-in');
        }
    });
}, observerOptions);

// Enhanced navbar: solid background + hide on scroll down / show on scroll up
let lastScrollY = window.scrollY || 0;
const navbar = document.getElementById('site-navbar') || document.querySelector('.navbar');

function updateNavbar() {
    if (!navbar) return;

    const currentScrollY = window.scrollY || document.documentElement.scrollTop || 0;
    const isLightHeaderPage = document.body.classList.contains('shop-page')
        || document.body.classList.contains('faq-page')
        || !document.querySelector('.hero');

    if (isLightHeaderPage || currentScrollY > 80) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }

    if (currentScrollY <= 40) {
        navbar.classList.remove('navbar-hidden');
    } else if (currentScrollY > lastScrollY + 2 && currentScrollY > 72) {
        navbar.classList.add('navbar-hidden');
        if (isMenuOpen && hamburger && navMenu) {
            hamburger.classList.remove('active');
            navMenu.classList.remove('active');
            document.body.style.overflow = '';
            isMenuOpen = false;
            hamburger.setAttribute('aria-expanded', 'false');
        }
    } else if (currentScrollY + 2 < lastScrollY) {
        navbar.classList.remove('navbar-hidden');
    }

    lastScrollY = currentScrollY;
}

let navScrollRaf = null;
function scheduleNavbarUpdate() {
    if (!navbar || navScrollRaf !== null) return;
    navScrollRaf = requestAnimationFrame(() => {
        navScrollRaf = null;
        updateNavbar();
    });
}

if (navbar) {
    window.addEventListener('scroll', scheduleNavbarUpdate, { passive: true });
    window.addEventListener('resize', scheduleNavbarUpdate, { passive: true });
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => {
            lastScrollY = window.scrollY || 0;
            updateNavbar();
        });
    } else {
        lastScrollY = window.scrollY || 0;
        updateNavbar();
    }
}

// Enhanced tile animations
const tiles = document.querySelectorAll('.tile');
tiles.forEach((tile, index) => {
    // Add staggered animation delay
    tile.style.animationDelay = `${index * 0.1}s`;
    
    tile.addEventListener('mouseenter', () => {
        tile.style.transform = 'rotateY(0deg) rotateX(0deg) scale(1.1)';
        tile.style.zIndex = '10';
    });
    
    tile.addEventListener('mouseleave', () => {
        tile.style.transform = 'rotateY(20deg) rotateX(10deg) scale(1)';
        tile.style.zIndex = '1';
    });
    
    // Add click interaction
    tile.addEventListener('click', () => {
        tile.style.transform = 'rotateY(0deg) rotateX(0deg) scale(1.2)';
        setTimeout(() => {
            tile.style.transform = 'rotateY(20deg) rotateX(10deg) scale(1)';
        }, 300);
    });
});

// Enhanced image placeholder interactions
const imagePlaceholders = document.querySelectorAll('.image-placeholder');
imagePlaceholders.forEach(placeholder => {
    placeholder.addEventListener('click', () => {
        // Create file input for image upload
        const input = document.createElement('input');
        input.type = 'file';
        input.accept = 'image/*';
        input.style.display = 'none';
        
        input.addEventListener('change', (e) => {
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = (e) => {
                    placeholder.style.backgroundImage = `url(${e.target.result})`;
                    placeholder.style.backgroundSize = 'cover';
                    placeholder.style.backgroundPosition = 'center';
                    placeholder.querySelector('.placeholder-text').style.display = 'none';
                };
                reader.readAsDataURL(file);
            }
        });
        
        document.body.appendChild(input);
        input.click();
        document.body.removeChild(input);
    });
});

// Notification system
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.innerHTML = `
        <div class="notification-content">
            <span class="notification-message">${message}</span>
            <button class="notification-close">&times;</button>
        </div>
    `;
    
    // Add styles
    notification.style.cssText = `
        position: fixed;
        top: 100px;
        right: 20px;
        background: ${type === 'success' ? '#4CAF50' : '#2196F3'};
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.15);
        z-index: 10000;
        transform: translateX(100%);
        transition: transform 0.3s ease;
        max-width: 400px;
    `;
    
    document.body.appendChild(notification);
    
    // Animate in
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    // Close button
    const closeBtn = notification.querySelector('.notification-close');
    closeBtn.addEventListener('click', () => {
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    });
    
    // Auto remove after 5 seconds
    setTimeout(() => {
        if (document.body.contains(notification)) {
            notification.style.transform = 'translateX(100%)';
            setTimeout(() => {
                if (document.body.contains(notification)) {
                    document.body.removeChild(notification);
                }
            }, 300);
        }
    }, 5000);
}

// Enhanced form handling with validation
const contactForm = document.querySelector('.contact-form');
if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Get form data
        const formData = new FormData(this);
        const name = this.querySelector('input[name="name"]')?.value || '';
        const email = this.querySelector('input[name="email"]')?.value || '';
        const message = this.querySelector('textarea[name="message"]')?.value || '';
        
        // Enhanced validation
        const errors = [];
        if (!name.trim()) errors.push('Name is required');
        if (!email.trim()) errors.push('Email is required');
        else if (!isValidEmail(email)) errors.push('Please enter a valid email');
        if (!message.trim()) errors.push('Message is required');
        
        if (errors.length > 0) {
            showNotification(errors.join(', '), 'error');
            return;
        }
        
        // Show loading state
        const submitButton = this.querySelector('.submit-button');
        const originalText = submitButton.textContent;
        submitButton.textContent = 'Sending...';
        submitButton.disabled = true;
        
        // Simulate form submission
        setTimeout(() => {
            showNotification('Thank you for your message! We\'ll get back to you soon.', 'success');
            this.reset();
            submitButton.textContent = originalText;
            submitButton.disabled = false;
        }, 2000);
    });
}

// Email validation helper
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Enhanced accessibility features
document.addEventListener('DOMContentLoaded', () => {
    // Add skip link for accessibility
    const skipLink = document.createElement('a');
    skipLink.href = '#main';
    skipLink.textContent = 'Skip to main content';
    skipLink.className = 'skip-link';
    skipLink.style.cssText = `
        position: absolute;
        top: -40px;
        left: 6px;
        background: #000;
        color: white;
        padding: 8px;
        text-decoration: none;
        z-index: 10001;
        transition: top 0.3s;
    `;
    
    skipLink.addEventListener('focus', () => {
        skipLink.style.top = '6px';
    });
    
    skipLink.addEventListener('blur', () => {
        skipLink.style.top = '-40px';
    });
    
    document.body.insertBefore(skipLink, document.body.firstChild);
    
    // Add main landmark
    const main = document.querySelector('main');
    if (main) {
        main.id = 'main';
    }
    
    // Observe elements for animation
    const animatedElements = document.querySelectorAll('.feature, .instructor-card, .tile, .referral-code');
    
    animatedElements.forEach(el => {
        el.classList.add('animate-on-scroll');
        observer.observe(el);
    });
});

// Enhanced CSS for animations and interactions
const enhancedStyles = `
    .animate-on-scroll {
        opacity: 0;
        transform: translateY(30px);
        transition: opacity 0.6s ease, transform 0.6s ease;
    }
    
    .animate-on-scroll.animate-in {
        opacity: 1;
        transform: translateY(0);
    }
    
    .loading-spinner {
        display: inline-block;
        width: 16px;
        height: 16px;
        border: 2px solid rgba(255, 255, 255, 0.3);
        border-radius: 50%;
        border-top-color: white;
        animation: spin 1s ease-in-out infinite;
        margin-right: 8px;
    }
    
    @keyframes spin {
        to { transform: rotate(360deg); }
    }
    
    .notification-content {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1rem;
    }
    
    .notification-close {
        background: none;
        border: none;
        color: white;
        font-size: 1.5rem;
        cursor: pointer;
        padding: 0;
        line-height: 1;
    }
    
    .notification-close:hover {
        opacity: 0.8;
    }
    
    @media (prefers-reduced-motion: reduce) {
        .animate-on-scroll,
        .navbar,
        .tile,
        .cta-button {
            transition: none !important;
            animation: none !important;
        }
    }
    
    @media (max-width: 768px) {
        .nav-menu {
            position: fixed;
            left: -100%;
            top: calc(var(--site-promo-banner-height, 0px) + 80px);
            flex-direction: column;
            background: linear-gradient(180deg, rgba(245, 239, 252, 0.98) 0%, rgba(255, 255, 255, 0.99) 100%);
            width: 100%;
            text-align: center;
            transition: 0.3s ease;
            box-shadow: 0 12px 30px rgba(126, 34, 206, 0.18);
            padding: 1.25rem 1rem 1.5rem;
            border-top: 1px solid rgba(168, 85, 184, 0.25);
            backdrop-filter: blur(12px);
            z-index: 1004;
        }
        
        .nav-menu.active {
            left: 0;
            display: flex !important;
        }
        
        .nav-menu li {
            margin: 0.4rem 0;
            width: 100%;
        }

        .nav-menu a {
            display: block;
            width: 100%;
            max-width: 340px;
            margin: 0 auto;
            padding: 0.9rem 1.1rem;
            color: #5b2a86;
            text-shadow: none;
            background: rgba(255, 255, 255, 0.78);
            border: 1px solid rgba(168, 85, 184, 0.25);
            border-radius: 14px;
            font-weight: 600;
        }

        .nav-menu a:hover,
        .nav-menu a:focus-visible {
            color: #fff;
            background: linear-gradient(135deg, #c26add 0%, #9d48c0 100%);
            border-color: rgba(157, 72, 192, 0.65);
            text-shadow: none;
            outline: none;
        }

        .nav-menu a.active {
            color: #fff;
            background: linear-gradient(135deg, #b55cd0 0%, #9443b8 100%);
            border-color: rgba(148, 67, 184, 0.72);
            box-shadow: 0 6px 18px rgba(148, 67, 184, 0.28);
        }
        
        .hamburger.active span:nth-child(2) {
            opacity: 0;
        }
        
        .hamburger.active span:nth-child(1) {
            transform: translateY(8px) rotate(45deg);
        }
        
        .hamburger.active span:nth-child(3) {
            transform: translateY(-8px) rotate(-45deg);
        }
    }
`;

// Inject enhanced styles
const styleSheet = document.createElement('style');
styleSheet.textContent = enhancedStyles;
document.head.appendChild(styleSheet);

// Performance optimization: Lazy load images
if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });
    
    document.querySelectorAll('img[data-src]').forEach(img => {
        imageObserver.observe(img);
    });
}

// Keyboard navigation enhancement
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && isMenuOpen && hamburger && navMenu) {
        hamburger.classList.remove('active');
        navMenu.classList.remove('active');
        document.body.style.overflow = '';
        isMenuOpen = false;
        hamburger.setAttribute('aria-expanded', 'false');
    }
});

// Testimonials rotation functionality
let currentPosition = 0; // Which position to rotate next (0, 1, or 2)
const positions = [
    [0, 3, 6], // Position 1: Sarah, Emma, James
    [1, 4, 7], // Position 2: Michael, David, Amanda  
    [2, 5]     // Position 3: Lisa, Rachel
];
let currentIndexes = [0, 0, 0]; // Current index in each position array

function rotateTestimonials() {
    // Hide current testimonial in the rotating position
    const currentTestimonialIndex = positions[currentPosition][currentIndexes[currentPosition]];
    const currentCard = document.querySelector(`[data-testimonial="${currentTestimonialIndex}"]`);
    if (currentCard) {
        currentCard.classList.remove('active');
    }
    
    // Move to next testimonial in this position
    currentIndexes[currentPosition] = (currentIndexes[currentPosition] + 1) % positions[currentPosition].length;
    
    // Show new testimonial in the same position
    const newTestimonialIndex = positions[currentPosition][currentIndexes[currentPosition]];
    const newCard = document.querySelector(`[data-testimonial="${newTestimonialIndex}"]`);
    if (newCard) {
        newCard.classList.add('active');
    }
    
    // Move to next position for next rotation
    currentPosition = (currentPosition + 1) % 3;
}

// Start rotation every 10 seconds
let testimonialInterval = setInterval(rotateTestimonials, 10000);

// Pause rotation on hover
const testimonialsContainer = document.querySelector('.testimonials-container');
if (testimonialsContainer) {
    testimonialsContainer.addEventListener('mouseenter', () => {
        clearInterval(testimonialInterval);
    });
    
    testimonialsContainer.addEventListener('mouseleave', () => {
        testimonialInterval = setInterval(rotateTestimonials, 10000);
    });
}

// Service Worker registration for PWA capabilities
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js')
            .then(registration => {
                console.log('SW registered: ', registration);
            })
            .catch(registrationError => {
                console.log('SW registration failed: ', registrationError);
            });
    });
}

(function initImpactStatCounters() {
    function parseTargetValue(text) {
        const trimmed = (text || '').trim();
        const match = trimmed.match(/^(\d+)(.*)$/);
        if (!match) return null;
        return {
            value: parseInt(match[1], 10),
            suffix: match[2] || ''
        };
    }

    function animateCounter(el) {
        if (!el || el.dataset.countAnimated === '1') return;
        const parsed = parseTargetValue(el.textContent);
        if (!parsed) return;

        const durationMs = 1400;
        const startTime = performance.now();
        el.dataset.countAnimated = '1';

        function tick(now) {
            const progress = Math.min((now - startTime) / durationMs, 1);
            const eased = 1 - Math.pow(1 - progress, 3);
            const current = Math.round(parsed.value * eased);
            el.textContent = `${current}${parsed.suffix}`;

            if (progress < 1) {
                requestAnimationFrame(tick);
            } else {
                el.textContent = `${parsed.value}${parsed.suffix}`;
            }
        }

        requestAnimationFrame(tick);
    }

    function wireImpactStats() {
        const statNumbers = Array.from(document.querySelectorAll('.impact-stats .stat-number'));
        if (!statNumbers.length) return;

        const statsSection = document.querySelector('.impact-stats');
        if (!statsSection) return;

        if (!('IntersectionObserver' in window)) {
            statNumbers.forEach(animateCounter);
            return;
        }

        const counterObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach((entry) => {
                if (!entry.isIntersecting) return;
                statNumbers.forEach(animateCounter);
                observer.unobserve(entry.target);
            });
        }, { threshold: 0.35 });

        counterObserver.observe(statsSection);
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', wireImpactStats);
    } else {
        wireImpactStats();
    }
})();

(function initServiceFitQuiz() {
    function getSelectedValue(name) {
        const selected = document.querySelector(`input[name="${name}"]:checked`);
        return selected ? selected.value : '';
    }

    function buildResult(scores) {
        const total = scores.s101 + scores.s102 + scores.custom;
        let pick = '101';

        if (scores.custom >= 2) {
            pick = 'custom';
        } else if (scores.s102 > scores.s101) {
            pick = '102';
        } else if (scores.s102 === scores.s101) {
            const q1 = getSelectedValue('q1');
            pick = q1 === '102' ? '102' : '101';
        }

        if (total === 0) {
            pick = '101';
        }

        if (pick === 'custom') {
            return {
                title: 'Recommended: Custom / Private Package',
                body: 'Based on your answers, a tailored experience (private event, larger group, venue logistics, or travel) is usually the best fit. We’ll coordinate details, materials, and flow for your group.',
                primaryText: 'Plan a private / custom experience',
                secondaryText: 'Prefer lessons instead? Book 101',
                primaryType: 'events',
                secondaryType: '101'
            };
        }

        if (pick === '102') {
            return {
                title: 'Recommended: Mahjong 102',
                body: 'Based on your answers, you’re ready for advanced strategy, coaching-style feedback, and next-level play drills (including topics like Siamese / Patio concepts when appropriate).',
                primaryText: 'Book 102 Course',
                secondaryText: 'Need fundamentals first? Book 101',
                primaryType: '102',
                secondaryType: '101'
            };
        }

        return {
            title: 'Recommended: Mahjong 101',
            body: 'Based on your answers, a fundamentals-first session is the smartest starting point—tile fluency, NMJL rules/scoring confidence, and guided play so you finish feeling ready for real games.',
            primaryText: 'Book 101 Course',
            secondaryText: 'Already experienced? Book 102',
            primaryType: '101',
            secondaryType: '102'
        };
    }

    function renderResult(result) {
        const el = document.getElementById('service-fit-result');
        if (!el) return;

        el.classList.remove('is-hidden');
        el.innerHTML = `
            <h4>${result.title}</h4>
            <p>${result.body}</p>
            <div class="service-fit-result-actions">
                <button type="button" class="service-fit-btn primary" onclick="sendEmail('${result.primaryType}')">${result.primaryText}</button>
                <button type="button" class="service-fit-btn secondary" onclick="sendEmail('${result.secondaryType}')">${result.secondaryText}</button>
            </div>
            <p class="service-fit-mini">Want a second opinion? Email us at <strong>lookoutmountainmahjong@gmail.com</strong> — mention you used the Services quiz.</p>
        `;
    }

    function updateStepUI(state) {
        const steps = Array.from(document.querySelectorAll('.service-fit-step'));
        const prev = document.querySelector('[data-quiz-prev]');
        const next = document.querySelector('[data-quiz-next]');
        const finish = document.querySelector('[data-quiz-finish]');
        const progressText = document.getElementById('service-fit-progress-text');
        const restart = document.querySelector('[data-quiz-restart]');

        steps.forEach((step, idx) => {
            step.classList.toggle('is-active', idx + 1 === state.step);
        });

        if (progressText) {
            progressText.textContent = `Question ${state.step} of 4`;
        }

        if (prev) prev.disabled = state.step === 1;
        if (next) {
            next.classList.toggle('is-hidden', state.step === 4);
            next.disabled = !getSelectedValue(`q${state.step}`);
        }
        if (finish) {
            finish.classList.toggle('is-hidden', state.step !== 4);
            finish.disabled = !getSelectedValue('q4');
        }
        if (restart) restart.classList.toggle('is-hidden', !state.showRestart);
    }

    function wireQuiz() {
        const root = document.getElementById('service-fit-quiz');
        if (!root) return;

        const state = { step: 1, showRestart: false };

        root.addEventListener('change', (e) => {
            const target = e.target;
            if (target && target.matches('input[type="radio"]')) {
                updateStepUI(state);
            }
        });

        const prev = root.querySelector('[data-quiz-prev]');
        const next = root.querySelector('[data-quiz-next]');
        const finish = root.querySelector('[data-quiz-finish]');
        const restart = root.querySelector('[data-quiz-restart]');

        if (prev) {
            prev.addEventListener('click', () => {
                state.step = Math.max(1, state.step - 1);
                updateStepUI(state);
            });
        }

        if (next) {
            next.addEventListener('click', () => {
                if (!getSelectedValue(`q${state.step}`)) return;
                state.step = Math.min(4, state.step + 1);
                updateStepUI(state);
            });
        }

        if (finish) {
            finish.addEventListener('click', () => {
                if (!getSelectedValue('q4')) return;
                const scores = {
                    s101: 0,
                    s102: 0,
                    custom: 0
                };
                ['q1', 'q2', 'q3', 'q4'].forEach((q) => {
                    const v = getSelectedValue(q);
                    if (v === '101') scores.s101 += 1;
                    if (v === '102') scores.s102 += 1;
                    if (v === 'custom') scores.custom += 1;
                });

                renderResult(buildResult(scores));
                state.showRestart = true;
                updateStepUI(state);
                const resultEl = document.getElementById('service-fit-result');
                if (resultEl) {
                    resultEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                }
            });
        }

        if (restart) {
            restart.addEventListener('click', () => {
                root.querySelectorAll('input[type="radio"]').forEach((input) => {
                    input.checked = false;
                });
                state.step = 1;
                state.showRestart = false;
                const resultEl = document.getElementById('service-fit-result');
                if (resultEl) {
                    resultEl.classList.add('is-hidden');
                    resultEl.innerHTML = '';
                }
                updateStepUI(state);
            });
        }

        updateStepUI(state);
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', wireQuiz);
    } else {
        wireQuiz();
    }
})();

(function initPromoBannerDismiss() {
    const STORAGE_KEY = 'lmm_promo_banner_dismissed';

    function wireDismissButtons() {
        document.querySelectorAll('.site-promo-banner-dismiss').forEach((btn) => {
            btn.addEventListener('click', () => {
                try {
                    localStorage.setItem(STORAGE_KEY, '1');
                } catch (e) {
                    /* private mode */
                }
                document.documentElement.classList.add('promo-banner-dismissed');
            });
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', wireDismissButtons);
    } else {
        wireDismissButtons();
    }
})();

(function initTournamentDateTabs() {
    function wireTabs() {
        const tabs = Array.from(document.querySelectorAll('[data-tournament-tab]'));
        const panels = Array.from(document.querySelectorAll('[data-tournament-panel]'));
        if (!tabs.length || !panels.length) {
            return;
        }

        function setActiveTab(target) {
            tabs.forEach((tab) => {
                const isActive = tab.dataset.tournamentTab === target;
                tab.classList.toggle('is-active', isActive);
                tab.setAttribute('aria-selected', isActive ? 'true' : 'false');
            });

            panels.forEach((panel) => {
                const isActive = panel.dataset.tournamentPanel === target;
                panel.classList.toggle('is-active', isActive);
                panel.hidden = !isActive;
            });
        }

        tabs.forEach((tab) => {
            tab.addEventListener('click', () => {
                setActiveTab(tab.dataset.tournamentTab);
            });
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', wireTabs);
    } else {
        wireTabs();
    }
})();

(function initPastEventPortfolioFlips() {
    function toggleCard(card, forceState) {
        const willFlip = typeof forceState === 'boolean'
            ? forceState
            : !card.classList.contains('is-flipped');

        card.classList.toggle('is-flipped', willFlip);
        card.setAttribute('aria-pressed', willFlip ? 'true' : 'false');

        const front = card.querySelector('.event-face-front');
        const back = card.querySelector('.event-face-back');
        if (front) {
            front.setAttribute('aria-hidden', willFlip ? 'true' : 'false');
        }
        if (back) {
            back.setAttribute('aria-hidden', willFlip ? 'false' : 'true');
        }
    }

    function wirePortfolioCards() {
        const cards = Array.from(document.querySelectorAll('[data-portfolio-card]'));
        if (!cards.length) return;

        cards.forEach((card) => {
            card.addEventListener('click', (e) => {
                const interactive = e.target.closest('a, button');
                if (interactive) return;
                toggleCard(card);
            });

            card.addEventListener('keydown', (e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    toggleCard(card);
                }
            });
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', wirePortfolioCards);
    } else {
        wirePortfolioCards();
    }
})();

(function initThreadAndInkShop() {
    const collectionsEl = document.getElementById('shop-collections');
    const productsEl = document.getElementById('shop-products');
    const filtersEl = document.getElementById('shop-filters');
    const productsCountEl = document.getElementById('shop-products-count');
    const featuredWrapEl = document.getElementById('featured-sweater');
    const featuredEl = document.getElementById('shop-featured');
    if (!collectionsEl || !productsEl) return;

    const SHOP_HOME = 'https://threadandinkco.com/';
    const SHOP_PLACEHOLDER_LOGO = 'thread-and-ink-logo.png';
    const CATALOG_URL = 'threadandink-catalog.json?v=featured-sweater-1';
    let catalogData = { collections: [], products: [], categories: [], featured: null };
    let activeCategory = 'all';

    function formatPrice(price) {
        const amount = Number.parseFloat(price);
        if (Number.isNaN(amount)) return price;
        return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(amount);
    }

    function trackShopClick(label, url, action) {
        const eventAction = action || 'click_thread_and_ink';
        if (typeof trackEvent === 'function') {
            trackEvent('Shop', eventAction, label, null, true);
        } else if (typeof gtag !== 'undefined') {
            gtag('event', eventAction, {
                event_category: 'Shop',
                event_label: label,
                link_url: url
            });
        }
    }

    function findProductCard(handle) {
        return document.querySelector(`[data-product-handle="${handle}"]`);
    }

    function wireProductCards(products) {
        products.forEach((product) => {
            const card = findProductCard(product.handle);
            if (!card || card.dataset.shopWired === 'true') return;
            card.dataset.shopWired = 'true';

            card.addEventListener('click', () => {
                trackShopClick(product.title, card.href, 'shop_product_click');

                if (typeof gtag !== 'undefined') {
                    gtag('event', 'shop_product_click', {
                        event_category: 'Shop',
                        event_label: product.title,
                        product_handle: product.handle,
                        link_url: card.href
                    });
                }
            });
        });
    }

    function wireExternalShopLinks() {
        document.querySelectorAll('[data-shop-external], .shop-collection-card').forEach((link) => {
            if (link.dataset.shopWired === 'true') return;
            link.dataset.shopWired = 'true';
            link.addEventListener('click', () => {
                const label = link.getAttribute('data-shop-external')
                    || link.querySelector('h4')?.textContent?.trim()
                    || 'Thread & Ink';
                const action = link.getAttribute('data-shop-external')
                    ? 'click_thread_and_ink_full_shop'
                    : link.classList.contains('shop-collection-card')
                        ? 'shop_collection_click'
                        : 'click_thread_and_ink';
                trackShopClick(label, link.href, action);
            });
        });
    }

    function getFeaturedProduct() {
        const handle = catalogData.featured?.handle;
        if (!handle) return null;
        return catalogData.products.find((product) => product.handle === handle) || null;
    }

    function getFilteredProducts() {
        const featuredHandle = catalogData.featured?.handle;
        const baseProducts = activeCategory === 'all'
            ? catalogData.products
            : catalogData.products.filter((product) => (
                Array.isArray(product.categories) && product.categories.includes(activeCategory)
            ));

        if (!featuredHandle) return baseProducts;
        return baseProducts.filter((product) => product.handle !== featuredHandle);
    }

    function renderFeaturedProduct() {
        const product = getFeaturedProduct();
        if (!featuredWrapEl || !featuredEl || !product) {
            if (featuredWrapEl) featuredWrapEl.hidden = true;
            return;
        }

        const eyebrow = catalogData.featured?.eyebrow || 'Featured';
        const description = catalogData.featured?.description || '';

        featuredWrapEl.hidden = false;
        featuredEl.innerHTML = `
            <a class="shop-featured-card shop-product-card" href="${product.url}" data-product-handle="${product.handle}" target="_blank" rel="noopener noreferrer" title="Buy on Thread &amp; Ink Co">
                <div class="shop-featured-image shop-product-image">
                    ${renderProductImage(product)}
                </div>
                <div class="shop-featured-body">
                    <span class="shop-featured-badge">${eyebrow}</span>
                    <span class="shop-product-collection">${product.collection}</span>
                    <h4>${product.title}</h4>
                    ${description ? `<p class="shop-featured-description">${description}</p>` : ''}
                    <span class="shop-product-price">${formatPrice(product.price)}</span>
                    <span class="shop-product-cta shop-featured-cta">Buy on Thread &amp; Ink Co <span class="shop-product-cta-arrow" aria-hidden="true"></span></span>
                </div>
            </a>
        `;
    }

    function updateProductsCount(count) {
        if (!productsCountEl) return;
        const label = count === 1 ? '1 product' : `${count} products`;
        productsCountEl.textContent = `Showing ${label}. Click any item to buy on Thread & Ink Co.`;
    }

    function renderFilters(categories) {
        if (!filtersEl || !categories.length) return;

        filtersEl.innerHTML = categories.map((category) => `
            <button
                type="button"
                class="shop-filter-btn${category.id === activeCategory ? ' is-active' : ''}"
                data-category="${category.id}"
                role="tab"
                aria-selected="${category.id === activeCategory ? 'true' : 'false'}"
            >${category.label}</button>
        `).join('');

        filtersEl.querySelectorAll('.shop-filter-btn').forEach((button) => {
            button.addEventListener('click', () => {
                activeCategory = button.dataset.category || 'all';
                filtersEl.querySelectorAll('.shop-filter-btn').forEach((btn) => {
                    const isActive = btn.dataset.category === activeCategory;
                    btn.classList.toggle('is-active', isActive);
                    btn.setAttribute('aria-selected', isActive ? 'true' : 'false');
                });
                renderProducts(getFilteredProducts());
                wireProductCards(getFilteredProducts());
                if (typeof trackEvent === 'function') {
                    trackEvent('Shop', 'filter_category', activeCategory);
                }
            });
        });
    }

    function renderCollections(collections) {
        if (!collections.length) {
            collectionsEl.innerHTML = '<p class="shop-empty">No collections match this category.</p>';
            return;
        }

        collectionsEl.innerHTML = collections.map((collection) => `
            <a class="shop-collection-card" href="${collection.url}" target="_blank" rel="noopener noreferrer" title="View full collection on Thread &amp; Ink Co">
                <div class="shop-collection-image">
                    ${collection.image
                        ? `<img src="${collection.image}" alt="${collection.title}" loading="lazy" decoding="async">`
                        : '<span class="shop-product-placeholder">Collection</span>'}
                </div>
                <div class="shop-collection-body">
                    <h4>${collection.title}</h4>
                    <span class="shop-collection-count">${collection.count} items on Thread &amp; Ink Co</span>
                </div>
            </a>
        `).join('');
    }

    function renderProductImage(product) {
        if (product.image) {
            return `<img src="${product.image}" alt="${product.title}" loading="lazy" decoding="async" class="shop-product-photo" onerror="this.onerror=null;this.src='${SHOP_PLACEHOLDER_LOGO}';this.classList.add('is-placeholder-logo');">`;
        }
        return `<img src="${SHOP_PLACEHOLDER_LOGO}" alt="Thread &amp; Ink Co" loading="lazy" decoding="async" class="shop-product-photo is-placeholder-logo">`;
    }

    function renderProducts(products) {
        updateProductsCount(products.length);
        if (!products.length) {
            productsEl.innerHTML = '<p class="shop-empty">No products match this category.</p>';
            return;
        }

        productsEl.innerHTML = products.map((product) => `
            <a class="shop-product-card" href="${product.url}" data-product-handle="${product.handle}" target="_blank" rel="noopener noreferrer" title="Buy on Thread &amp; Ink Co">
                <div class="shop-product-image">
                    ${renderProductImage(product)}
                </div>
                <div class="shop-product-body">
                    <span class="shop-product-collection">${product.collection}</span>
                    <h4>${product.title}</h4>
                    <span class="shop-product-price">${formatPrice(product.price)}</span>
                    <span class="shop-product-cta">Buy on Thread &amp; Ink Co <span class="shop-product-cta-arrow" aria-hidden="true"></span></span>
                </div>
            </a>
        `).join('');
    }

    async function renderCatalog() {
        renderFeaturedProduct();
        renderCollections(catalogData.collections);
        renderFilters(catalogData.categories);
        const visibleProducts = getFilteredProducts();
        renderProducts(visibleProducts);
        wireExternalShopLinks();
        const featuredProduct = getFeaturedProduct();
        const productsToWire = featuredProduct ? [featuredProduct, ...visibleProducts] : visibleProducts;
        wireProductCards(productsToWire);
    }

    function showError() {
        collectionsEl.innerHTML = '<p class="shop-error">Collections are temporarily unavailable.</p>';
        productsEl.innerHTML = `<p class="shop-error">Browse the full mahjong catalog at <a href="${SHOP_HOME}" target="_blank" rel="noopener noreferrer">threadandinkco.com</a>.</p>`;
    }

    async function loadCatalog() {
        try {
            const response = await fetch(CATALOG_URL, { cache: 'no-cache' });
            if (!response.ok) throw new Error('catalog fetch failed');
            const catalog = await response.json();
            catalogData = {
                collections: catalog.collections || [],
                products: catalog.products || [],
                categories: catalog.categories || [{ id: 'all', label: 'All' }],
                featured: catalog.featured || null
            };
            await renderCatalog();
        } catch (error) {
            console.warn('Thread & Ink catalog load failed', error);
            showError();
            wireExternalShopLinks();
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() {
            wireExternalShopLinks();
            loadCatalog();
        });
    } else {
        wireExternalShopLinks();
        loadCatalog();
    }
})();
