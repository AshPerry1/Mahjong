(function initLookoutMountainAnalytics() {
    const GA_ID = 'G-8C0BWCXBF0';

    window.dataLayer = window.dataLayer || [];
    function gtag() {
        window.dataLayer.push(arguments);
    }
    window.gtag = gtag;

    gtag('js', new Date());
    gtag('config', GA_ID, {
        send_page_view: true,
        allow_google_signals: true,
        allow_ad_personalization_signals: true,
        cookie_flags: 'SameSite=None;Secure'
    });

    function trackEvent(category, action, label, value, isConversion) {
        const eventParams = {
            event_category: category,
            event_label: label,
            engagement_time_msec: 100,
            non_interaction: false
        };

        if (value !== undefined && value !== null) {
            eventParams.value = value;
        }

        if (isConversion) {
            eventParams.conversion_label = label;
            eventParams.send_to = GA_ID;
        }

        gtag('event', action, eventParams);
    }

    window.trackEvent = trackEvent;

    function getPageType() {
        if (document.body.classList.contains('shop-page')) return 'shop';
        if (document.body.classList.contains('faq-page')) return 'faq';
        if (document.querySelector('.hero')) return 'home';
        return 'other';
    }

    function debounce(fn, delay) {
        let timer;
        return function debounced() {
            const args = arguments;
            const context = this;
            clearTimeout(timer);
            timer = setTimeout(function run() {
                fn.apply(context, args);
            }, delay);
        };
    }

    function initEngagementTracking() {
        let engagementStartTime = Date.now();
        let totalEngagementTime = 0;

        function trackEngagement() {
            const now = Date.now();
            const timeSpent = now - engagementStartTime;
            totalEngagementTime += timeSpent;

            if (totalEngagementTime >= 30000) {
                gtag('event', 'user_engagement', {
                    engagement_time_msec: totalEngagementTime,
                    event_category: 'Engagement',
                    event_label: 'Time on Site',
                    page_type: getPageType()
                });
                totalEngagementTime = 0;
            }
            engagementStartTime = now;
        }

        document.addEventListener('mousemove', trackEngagement);
        document.addEventListener('keypress', trackEngagement);
        document.addEventListener('scroll', trackEngagement);
        document.addEventListener('click', trackEngagement);
    }

    function initSiteTracking() {
        gtag('event', 'site_page_context', {
            event_category: 'Traffic',
            event_label: getPageType(),
            page_type: getPageType(),
            page_path: window.location.pathname,
            page_title: document.title
        });

        document.querySelectorAll('nav a[href]').forEach(function(link) {
            link.addEventListener('click', function() {
                const href = this.getAttribute('href') || '';
                const label = href.indexOf('#') === 0 ? href.substring(1) : href;
                trackEvent('Navigation', 'click_nav_link', label);
            });
        });

        document.querySelectorAll('a.logo-link').forEach(function(link) {
            link.addEventListener('click', function() {
                trackEvent('Navigation', 'click_logo', 'Logo');
            });
        });

        document.querySelectorAll('button.cta-button, a.cta-button').forEach(function(button) {
            button.addEventListener('click', function() {
                const buttonText = (this.textContent || '').trim()
                    || (this.querySelector('.button-text') && this.querySelector('.button-text').textContent.trim())
                    || 'Unknown';
                trackEvent('CTA Button', 'click_cta', buttonText, null, true);
                gtag('event', 'high_intent_action', {
                    event_category: 'Conversion',
                    event_label: 'CTA Click - ' + buttonText,
                    engagement_type: 'button_click',
                    user_intent: 'high',
                    page_type: getPageType()
                });
            });
        });

        document.querySelectorAll('button.service-button').forEach(function(button) {
            button.addEventListener('click', function() {
                const buttonText = (this.textContent || '').trim();
                trackEvent('Service Button', 'click_service', buttonText, null, true);
                gtag('event', 'service_interest', {
                    event_category: 'Conversion',
                    event_label: buttonText,
                    service_type: buttonText.toLowerCase().replace('book ', '').replace(' course', ''),
                    user_intent: 'service_inquiry'
                });
            });
        });

        document.querySelectorAll('a[href^="mailto:"]').forEach(function(link) {
            link.addEventListener('click', function() {
                const email = (this.getAttribute('href') || '').replace('mailto:', '').split('?')[0];
                trackEvent('Contact', 'click_email', email, null, true);
                gtag('event', 'contact_intent', {
                    event_category: 'Conversion',
                    event_label: 'Email Click',
                    contact_method: 'email',
                    user_intent: 'contact'
                });
            });
        });

        document.querySelectorAll('a[href^="tel:"]').forEach(function(link) {
            link.addEventListener('click', function() {
                const phone = (this.getAttribute('href') || '').replace('tel:', '');
                trackEvent('Contact', 'click_phone', phone, null, true);
                gtag('event', 'contact_intent', {
                    event_category: 'Conversion',
                    event_label: 'Phone Click',
                    contact_method: 'phone',
                    user_intent: 'contact'
                });
            });
        });

        document.querySelectorAll('a[href^="http"]:not(.tml-button):not(.shop-collection-card):not(.shop-product-card)').forEach(function(link) {
            link.addEventListener('click', function() {
                const url = this.getAttribute('href') || '';
                const linkText = (this.textContent || '').trim();
                trackEvent('External Link', 'click_external', linkText + ' - ' + url);
            });
        });

        document.querySelectorAll('a.footer-social-link, a[href*="instagram"], a[href*="bit.ly"], a[href*="tiktok"], a.site-promo-banner-cta').forEach(function(link) {
            link.addEventListener('click', function() {
                trackEvent('Social Media', 'click_social', this.getAttribute('href') || '');
            });
        });

        const hamburger = document.querySelector('.hamburger');
        if (hamburger) {
            hamburger.addEventListener('click', function() {
                const isOpen = this.classList.contains('active');
                trackEvent('Mobile Menu', isOpen ? 'close_menu' : 'open_menu', getPageType());
            });
        }

        document.querySelectorAll('a.tml-button, a[href*="themahjongline.com"]').forEach(function(link) {
            link.addEventListener('click', function() {
                trackEvent('TML Link', 'click_tml_link', 'Shop TML Products', null, true);
                gtag('event', 'product_interest', {
                    event_category: 'TML Link',
                    event_label: 'Shop TML Products',
                    product_type: 'mahjong_products',
                    affiliate_partner: 'TML',
                    partner_channel: 'ShopMy',
                    user_intent: 'product_purchase'
                });
            });
        });

        document.querySelectorAll('a.scroll-arrow').forEach(function(link) {
            link.addEventListener('click', function() {
                trackEvent('Navigation', 'click_scroll_arrow', this.getAttribute('href') || 'unknown');
            });
        });

        document.querySelectorAll('button.tournament-modal-close').forEach(function(button) {
            button.addEventListener('click', function() {
                const modal = this.closest('.tournament-modal, .share-modal');
                const modalType = modal
                    ? (modal.classList.contains('share-modal') ? 'Share Modal' : 'Registration Form')
                    : 'Unknown';
                trackEvent('Modal', 'click_close_button', modalType);
            });
        });

        document.querySelectorAll('button.register-btn').forEach(function(button) {
            button.addEventListener('click', function() {
                trackEvent('Tournament', 'click_register_button', 'Register Here', null, true);
                gtag('event', 'tournament_interest', {
                    event_category: 'Conversion',
                    event_label: 'Tournament Registration Click',
                    product_type: 'tournament',
                    user_intent: 'tournament_registration'
                });
            });
        });

        document.querySelectorAll('button.share-event-btn').forEach(function(button) {
            button.addEventListener('click', function() {
                trackEvent('Tournament', 'click_share_button', 'Share Event');
            });
        });

        document.querySelectorAll('input, textarea, select').forEach(function(field) {
            field.addEventListener('focus', function() {
                const fieldName = this.name || this.id || 'unknown';
                const formType = this.closest('#tournament-form')
                    ? 'Tournament Form'
                    : (this.closest('form') ? 'Other Form' : 'Standalone');
                trackEvent('Form Interaction', 'field_focus', formType + ' - ' + fieldName);
            });
        });

        document.querySelectorAll('#share-modal input[type="checkbox"], #share-modal input[type="radio"]').forEach(function(input) {
            input.addEventListener('change', function() {
                trackEvent('Share Modal', 'select_option', this.name + ' - ' + this.value);
            });
        });

        document.querySelectorAll('#tournament-form input[type="checkbox"]').forEach(function(input) {
            input.addEventListener('change', function() {
                trackEvent('Tournament Form', this.checked ? 'check_tournament' : 'uncheck_tournament', this.value);
            });
        });

        document.querySelectorAll('#tournament-form input[type="radio"]').forEach(function(input) {
            input.addEventListener('change', function() {
                trackEvent('Tournament Form', 'select_radio', this.name + ' - ' + this.value);
            });
        });

        document.querySelectorAll('select').forEach(function(select) {
            select.addEventListener('change', function() {
                const selectName = this.name || this.id || 'unknown';
                const formType = this.closest('#tournament-form') ? 'Tournament Form' : 'Other Form';
                trackEvent('Form Interaction', 'select_change', formType + ' - ' + selectName + ' - ' + this.value);
            });
        });

        const promoDismiss = document.querySelector('.site-promo-banner-dismiss');
        if (promoDismiss) {
            promoDismiss.addEventListener('click', function() {
                trackEvent('Promo Banner', 'dismiss', 'TikTok Banner');
            });
        }
    }

    function initHomeTracking() {
        const sections = ['hero', 'services', 'pricing', 'testimonials', 'about', 'tml-partnership', 'contact', 'past-events', 'community-impact', 'upcoming-event'];
        const viewedSections = new Set();

        const sectionObserver = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting && !viewedSections.has(entry.target.id)) {
                    viewedSections.add(entry.target.id);
                    trackEvent('Section View', 'view_section', entry.target.id);
                    gtag('event', 'content_engagement', {
                        event_category: 'Engagement',
                        event_label: 'Section Viewed - ' + entry.target.id,
                        content_type: entry.target.id,
                        engagement_type: 'section_view'
                    });
                }
            });
        }, { threshold: 0.5 });

        sections.forEach(function(sectionId) {
            const section = document.getElementById(sectionId);
            if (section) {
                sectionObserver.observe(section);
            }
        });
    }

    function initShopTracking() {
        const shopSections = ['thread-and-ink-shop', 'shop-collections', 'shop-products'];
        const viewedShopSections = new Set();
        const shopObserver = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                const sectionId = entry.target.id || entry.target.className;
                if (entry.isIntersecting && !viewedShopSections.has(sectionId)) {
                    viewedShopSections.add(sectionId);
                    trackEvent('Shop', 'view_section', sectionId);
                }
            });
        }, { threshold: 0.35 });

        shopSections.forEach(function(sectionId) {
            const section = document.getElementById(sectionId);
            if (section) {
                shopObserver.observe(section);
            }
        });
    }

    function initFaqTracking() {
        document.querySelectorAll('.category-btn').forEach(function(button) {
            button.addEventListener('click', function() {
                const category = (this.textContent || '').trim();
                trackEvent('FAQ', 'filter_category', category);
            });
        });

        document.querySelectorAll('.faq-question').forEach(function(question) {
            question.addEventListener('click', function() {
                const heading = question.querySelector('h3');
                const label = heading ? heading.textContent.trim() : 'Unknown question';
                trackEvent('FAQ', 'open_question', label);
            });
        });

        const faqSearch = document.getElementById('faqSearch');
        if (faqSearch) {
            faqSearch.addEventListener('input', debounce(function() {
                const term = faqSearch.value.trim();
                if (!term) return;
                trackEvent('FAQ', 'search', term);
            }, 600));
        }

        document.querySelectorAll('.back-to-home').forEach(function(link) {
            link.addEventListener('click', function() {
                trackEvent('FAQ', 'click_cta', (this.textContent || '').trim(), null, true);
            });
        });
    }

    document.addEventListener('DOMContentLoaded', function() {
        initEngagementTracking();
        initSiteTracking();

        const pageType = getPageType();
        if (pageType === 'home') initHomeTracking();
        if (pageType === 'shop') initShopTracking();
        if (pageType === 'faq') initFaqTracking();
    });
})();
