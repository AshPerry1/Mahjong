// Enhanced email functionality with better UX
function sendEmail(type) {
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
        
        // Show success message
        showNotification('Email client opened! Please send your message.', 'success');
        
        // Reset button
        button.innerHTML = originalText;
        button.disabled = false;
    }, 800);
}

// Enhanced smooth scrolling with offset for fixed navbar
function smoothScrollTo(targetId) {
    const target = document.querySelector(targetId);
    if (target) {
        const offset = 80; // Account for fixed navbar
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

hamburger.addEventListener('click', () => {
    isMenuOpen = !isMenuOpen;
    hamburger.classList.toggle('active');
    navMenu.classList.toggle('active');
    
    // Prevent body scroll when menu is open
    document.body.style.overflow = isMenuOpen ? 'hidden' : '';
    
    // Add ARIA attributes for accessibility
    hamburger.setAttribute('aria-expanded', isMenuOpen);
    hamburger.setAttribute('aria-label', isMenuOpen ? 'Close menu' : 'Open menu');
});

// Close mobile menu when clicking on a link
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

// Close mobile menu when clicking outside
document.addEventListener('click', (e) => {
    if (isMenuOpen && !hamburger.contains(e.target) && !navMenu.contains(e.target)) {
        hamburger.classList.remove('active');
        navMenu.classList.remove('active');
        document.body.style.overflow = '';
        isMenuOpen = false;
        hamburger.setAttribute('aria-expanded', 'false');
    }
});

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

// Enhanced navbar background change on scroll
let lastScrollY = window.scrollY;
const navbar = document.querySelector('.navbar');

function updateNavbar() {
    const currentScrollY = window.scrollY;
    
    if (currentScrollY > 100) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
    
    // Hide/show navbar on scroll (optional)
    if (currentScrollY > lastScrollY && currentScrollY > 200) {
        navbar.classList.add('navbar-hidden');
    } else {
        navbar.classList.remove('navbar-hidden');
    }
    
    lastScrollY = currentScrollY;
}

// Throttled scroll event
let ticking = false;
function requestTick() {
    if (!ticking) {
        requestAnimationFrame(updateNavbar);
        ticking = true;
    }
}

window.addEventListener('scroll', () => {
    ticking = false;
    requestTick();
});

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
    
    .navbar.scrolled {
        background: rgba(255, 255, 255, 0.98);
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    }
    
    .navbar.navbar-hidden {
        transform: translateY(-100%);
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
            top: 80px;
            flex-direction: column;
            background-color: rgba(255, 255, 255, 0.98);
            width: 100%;
            text-align: center;
            transition: 0.3s ease;
            box-shadow: 0 10px 27px rgba(0, 0, 0, 0.1);
            padding: 2rem 0;
            backdrop-filter: blur(20px);
        }
        
        .nav-menu.active {
            left: 0;
        }
        
        .nav-menu li {
            margin: 1rem 0;
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
    // Escape key closes mobile menu
    if (e.key === 'Escape' && isMenuOpen) {
        hamburger.classList.remove('active');
        navMenu.classList.remove('active');
        document.body.style.overflow = '';
        isMenuOpen = false;
        hamburger.setAttribute('aria-expanded', 'false');
    }
});

// Testimonials rotation functionality
let currentTestimonial = 0;
const testimonials = document.querySelectorAll('.testimonial-card');
const indicators = document.querySelectorAll('.indicator');
const totalTestimonials = testimonials.length;

function showTestimonial(index) {
    // Remove active class from all testimonials and indicators
    testimonials.forEach(testimonial => testimonial.classList.remove('active', 'prev'));
    indicators.forEach(indicator => indicator.classList.remove('active'));
    
    // Add prev class to current testimonial before hiding
    if (testimonials[currentTestimonial]) {
        testimonials[currentTestimonial].classList.add('prev');
    }
    
    // Update current index
    currentTestimonial = index;
    
    // Show new testimonial
    if (testimonials[currentTestimonial]) {
        testimonials[currentTestimonial].classList.add('active');
    }
    
    // Update indicator
    if (indicators[currentTestimonial]) {
        indicators[currentTestimonial].classList.add('active');
    }
}

function nextTestimonial() {
    const nextIndex = (currentTestimonial + 1) % totalTestimonials;
    showTestimonial(nextIndex);
}

// Auto-rotate testimonials every 5 seconds
let testimonialInterval = setInterval(nextTestimonial, 5000);

// Add click handlers to indicators
indicators.forEach((indicator, index) => {
    indicator.addEventListener('click', () => {
        clearInterval(testimonialInterval);
        showTestimonial(index);
        // Restart auto-rotation after manual selection
        testimonialInterval = setInterval(nextTestimonial, 5000);
    });
});

// Pause auto-rotation on hover
const testimonialsContainer = document.querySelector('.testimonials-container');
if (testimonialsContainer) {
    testimonialsContainer.addEventListener('mouseenter', () => {
        clearInterval(testimonialInterval);
    });
    
    testimonialsContainer.addEventListener('mouseleave', () => {
        testimonialInterval = setInterval(nextTestimonial, 5000);
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
