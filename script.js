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

I'm excited to invest in premium mahjong tiles from The Mahjong Line and would love your ambassador recommendations.

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
    } else if (!isMenuOpen && window.matchMedia('(min-width: 769px)').matches && currentScrollY > lastScrollY + 2 && currentScrollY > 72) {
        navbar.classList.add('navbar-hidden');
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

    // Fallback: some mobile browsers never fire intersection callbacks reliably
    setTimeout(() => {
        document.querySelectorAll('.animate-on-scroll:not(.animate-in)').forEach((el) => {
            el.classList.add('animate-in');
        });
    }, 2000);
});

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

// Start rotation every 10 seconds (homepage only)
let testimonialInterval = null;
const testimonialsContainer = document.querySelector('.testimonials-container');
if (testimonialsContainer && document.querySelector('[data-testimonial]')) {
    testimonialInterval = setInterval(rotateTestimonials, 10000);

    testimonialsContainer.addEventListener('mouseenter', () => {
        clearInterval(testimonialInterval);
    });

    testimonialsContainer.addEventListener('mouseleave', () => {
        testimonialInterval = setInterval(rotateTestimonials, 10000);
    });
}

// Service Worker registration — deferred so it does not compete with LCP
if ('serviceWorker' in navigator) {
    const registerServiceWorker = () => {
        navigator.serviceWorker.register('/sw.js?v=15').catch(() => {});
    };
    if ('requestIdleCallback' in window) {
        requestIdleCallback(registerServiceWorker, { timeout: 4000 });
    } else {
        window.addEventListener('load', registerServiceWorker, { once: true });
    }
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

(function initFlyerDownloadNotify() {
    const FLYER_NOTIFY_ENDPOINT = 'https://formsubmit.co/ajax/lookoutmountainmahjong@gmail.com';
    const FLYER_SESSION_PREFIX = 'lmm_flyer_notify_';

    function getDeviceSummary() {
        const width = window.innerWidth || 0;
        if (width <= 768) return 'Mobile';
        if (width <= 1024) return 'Tablet';
        return 'Desktop';
    }

    function trackFlyerDownload(flyerId, flyerLabel) {
        if (typeof trackEvent === 'function') {
            trackEvent('Events', 'download_flyer', flyerLabel, null, true);
        }

        if (typeof gtag !== 'undefined') {
            gtag('event', 'download_flyer', {
                event_category: 'Events',
                event_label: flyerLabel,
                flyer_id: flyerId,
                user_intent: 'event_interest'
            });
        }
    }

    async function notifyFlyerDownload(flyerId, flyerLabel) {
        const dedupeKey = `${FLYER_SESSION_PREFIX}${flyerId}`;
        try {
            if (sessionStorage.getItem(dedupeKey) === '1') {
                trackFlyerDownload(flyerId, flyerLabel);
                return;
            }
            sessionStorage.setItem(dedupeKey, '1');
        } catch (e) {
            /* private browsing */
        }

        trackFlyerDownload(flyerId, flyerLabel);

        const payload = {
            _subject: `Flyer downloaded: ${flyerLabel}`,
            _template: 'table',
            _captcha: 'false',
            event: flyerLabel,
            flyer_id: flyerId,
            downloaded_at: new Date().toLocaleString('en-US', { timeZone: 'America/New_York' }),
            page_url: window.location.href,
            referrer: document.referrer || 'Direct visit',
            device: getDeviceSummary()
        };

        try {
            await fetch(FLYER_NOTIFY_ENDPOINT, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    Accept: 'application/json'
                },
                body: JSON.stringify(payload)
            });
        } catch (error) {
            console.warn('Flyer download notification failed', error);
        }
    }

    function wireFlyerLinks() {
        document.querySelectorAll('[data-flyer-download]').forEach((link) => {
            if (link.dataset.flyerWired === 'true') return;
            link.dataset.flyerWired = 'true';

            link.addEventListener('click', () => {
                const flyerId = link.dataset.flyerDownload || 'flyer';
                const flyerLabel = link.dataset.flyerLabel || 'Event Flyer';
                notifyFlyerDownload(flyerId, flyerLabel);
            });
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', wireFlyerLinks);
    } else {
        wireFlyerLinks();
    }
})();
