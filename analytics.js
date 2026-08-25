(function initMahjongAnalytics() {
    const GA_ID = 'G-8C0BWCXBF0';

    function isMahjongSite() {
        const hostname = window.location.hostname.toLowerCase();
        return hostname === 'lookoutmountainmahjong.com'
            || hostname === 'www.lookoutmountainmahjong.com'
            || hostname === 'localhost'
            || hostname === '127.0.0.1';
    }

    window.gtag = function noopGtag() {};
    window.trackEvent = function noopTrackEvent() {};

    if (!isMahjongSite()) {
        return;
    }

    window.dataLayer = window.dataLayer || [];
    function gtag() {
        window.dataLayer.push(arguments);
    }
    window.gtag = gtag;

    function loadGtagScript() {
        if (window.__lmmGtagLoaded) return;
        window.__lmmGtagLoaded = true;

        const gtagScript = document.createElement('script');
        gtagScript.async = true;
        gtagScript.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(GA_ID);
        document.head.appendChild(gtagScript);

        gtag('js', new Date());
        gtag('config', GA_ID, {
            send_page_view: true,
            allow_google_signals: true,
            allow_ad_personalization_signals: true,
            cookie_flags: 'SameSite=None;Secure',
            page_location: window.location.href,
            page_hostname: window.location.hostname
        });
    }

    function scheduleGtagLoad() {
        if ('requestIdleCallback' in window) {
            requestIdleCallback(loadGtagScript, { timeout: 3500 });
        } else {
            setTimeout(loadGtagScript, 1500);
        }
    }

    if (document.readyState === 'complete') {
        scheduleGtagLoad();
    } else {
        window.addEventListener('load', scheduleGtagLoad, { once: true });
    }

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
        if (document.body.classList.contains('seo-page')) return 'seo';
        if (document.body.classList.contains('shop-page')) return 'shop';
        if (document.body.classList.contains('faq-page')) return 'faq';
        if (document.body.classList.contains('yacht-event-page')) return 'yacht';
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

        document.querySelectorAll('button.cta-button, a.cta-button:not(#upcoming-event a)').forEach(function(button) {
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

        document.querySelectorAll('a[href^="mailto:"]:not(#upcoming-event a)').forEach(function(link) {
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

        document.querySelectorAll('a[href^="http"]:not(.tml-button):not(.shop-collection-card):not(.shop-product-card):not(#upcoming-event a)').forEach(function(link) {
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

                    if (entry.target.id === 'upcoming-event') {
                        trackEvent('Yacht Event', 'view_yacht_event_section', '2027 Ritz Yacht Mahjong Journey');
                        gtag('event', 'yacht_event_impression', {
                            event_category: 'Yacht Event',
                            event_label: '2027 Ritz Yacht Mahjong Journey',
                            event_name: '2027 Ritz Yacht Mahjong Journey',
                            engagement_type: 'section_view',
                            user_intent: 'event_discovery'
                        });
                    }
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

    function initYachtEventTracking() {
        const yachtSection = document.getElementById('upcoming-event');
        if (!yachtSection) return;

        const eventName = '2027 Ritz Yacht Mahjong Journey';

        yachtSection.querySelectorAll('[data-flyer-download]').forEach(function(link) {
            link.addEventListener('click', function() {
                const flyerId = this.dataset.flyerDownload || 'flyer';
                const flyerLabel = this.dataset.flyerLabel || 'Event Flyer';

                trackEvent('Yacht Event', 'download_flyer', flyerLabel, null, true);

                gtag('event', 'download_flyer', {
                    event_category: 'Yacht Event',
                    event_label: flyerLabel,
                    flyer_id: flyerId,
                    event_name: eventName,
                    user_intent: 'event_interest'
                });

                gtag('event', 'yacht_event_interest', {
                    event_category: 'Conversion',
                    event_label: 'Flyer Download - ' + flyerLabel,
                    event_name: eventName,
                    engagement_type: 'flyer_download',
                    user_intent: 'yacht_event_inquiry'
                });
            });
        });

        yachtSection.querySelectorAll('a[href^="http"]').forEach(function(link) {
            if (link.hasAttribute('data-yacht-share') || link.hasAttribute('data-yacht-video') || link.hasAttribute('data-flyer-download')) return;

            link.addEventListener('click', function() {
                const linkText = (this.textContent || '').trim();
                const url = this.getAttribute('href') || '';

                trackEvent('Yacht Event', 'click_partner_link', linkText + ' - ' + url, null, true);

                gtag('event', 'yacht_event_interest', {
                    event_category: 'Conversion',
                    event_label: 'Partner Link - ' + linkText,
                    event_name: eventName,
                    link_url: url,
                    engagement_type: 'partner_click',
                    user_intent: 'yacht_event_inquiry'
                });
            });
        });

        yachtSection.querySelectorAll('[data-yacht-video]').forEach(function(link) {
            link.addEventListener('click', function() {
                const platform = this.dataset.yachtVideo || 'video';
                trackEvent('Yacht Event', 'watch_announcement_video', platform, null, true);
                gtag('event', 'watch_announcement_video', {
                    event_category: 'Yacht Event',
                    event_label: 'Instagram Announcement Video',
                    event_name: eventName,
                    video_platform: platform,
                    video_url: this.getAttribute('href') || '',
                    engagement_type: 'video_watch',
                    user_intent: 'yacht_event_viral'
                });
                gtag('event', 'yacht_event_interest', {
                    event_category: 'Conversion',
                    event_label: 'Watch Announcement Video',
                    event_name: eventName,
                    engagement_type: 'video_watch',
                    user_intent: 'yacht_event_inquiry'
                });
            });
        });

        document.querySelectorAll('[data-yacht-video]').forEach(function(link) {
            if (yachtSection.contains(link)) return;
            if (link.dataset.yachtVideoWired === 'true') return;
            link.dataset.yachtVideoWired = 'true';
            link.addEventListener('click', function() {
                trackEvent('Yacht Event', 'watch_announcement_video', 'instagram_banner', null, true);
                gtag('event', 'watch_announcement_video', {
                    event_category: 'Yacht Event',
                    event_label: 'Instagram Announcement Video - Banner/Hero',
                    event_name: eventName,
                    video_platform: 'instagram',
                    engagement_type: 'video_watch',
                    user_intent: 'yacht_event_viral'
                });
            });
        });

        yachtSection.querySelectorAll('a[href^="mailto:"]:not([data-yacht-share])').forEach(function(link) {
            link.addEventListener('click', function() {
                const email = (this.getAttribute('href') || '').replace('mailto:', '').split('?')[0];

                trackEvent('Yacht Event', 'click_contact_email', email, null, true);

                gtag('event', 'yacht_event_interest', {
                    event_category: 'Conversion',
                    event_label: 'Contact Email - ' + email,
                    event_name: eventName,
                    contact_method: 'email',
                    engagement_type: 'contact_click',
                    user_intent: 'yacht_event_inquiry'
                });
            });
        });

        yachtSection.querySelectorAll('[data-yacht-share]').forEach(function(button) {
            button.addEventListener('click', function() {
                const channel = this.dataset.yachtShare || 'share';
                const labelMap = {
                    text: 'Share via Text',
                    email: 'Share via Email',
                    'copy-video': 'Copy Video Link',
                    'video-text': 'Text the Video'
                };
                const label = labelMap[channel] || ('Share - ' + channel);

                trackEvent('Yacht Event', 'share_yacht_event', label, null, true);

                gtag('event', 'share_yacht_event', {
                    event_category: 'Yacht Event',
                    event_label: label,
                    event_name: eventName,
                    share_channel: channel,
                    engagement_type: 'social_sharing',
                    user_intent: 'yacht_event_sharing'
                });

                gtag('event', 'yacht_event_interest', {
                    event_category: 'Conversion',
                    event_label: 'Share - ' + label,
                    event_name: eventName,
                    share_channel: channel,
                    engagement_type: 'social_sharing',
                    user_intent: 'yacht_event_inquiry'
                });
            });
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

    function initSeoTracking() {
        const slug = document.body.dataset.seoSlug
            || window.location.pathname.replace(/^\//, '').replace(/\.html$/, '');
        const heading = document.querySelector('.seo-page h1');
        const pageTopic = heading ? heading.textContent.trim() : slug;

        gtag('event', 'seo_page_view', {
            event_category: 'SEO',
            event_label: slug,
            page_topic: pageTopic,
            page_type: 'seo',
            page_path: window.location.pathname
        });

        document.querySelectorAll('.seo-page a[href]').forEach(function(link) {
            link.addEventListener('click', function() {
                const href = this.getAttribute('href') || '';
                const linkText = (this.textContent || '').trim() || href;
                const isBook = href.indexOf('book-mahjong-lesson') !== -1;
                const isHome = href === '/' || href === 'https://lookoutmountainmahjong.com/'
                    || href === 'https://lookoutmountainmahjong.com';

                trackEvent(
                    'SEO',
                    isBook ? 'click_book_link' : (isHome ? 'click_home_link' : 'click_internal_link'),
                    slug + ' -> ' + linkText,
                    null,
                    isBook
                );

                if (isBook) {
                    gtag('event', 'high_intent_action', {
                        event_category: 'Conversion',
                        event_label: 'SEO Book Link - ' + slug,
                        page_type: 'seo',
                        user_intent: 'high'
                    });
                }
            });
        });
    }

    document.addEventListener('DOMContentLoaded', function() {
        initEngagementTracking();
        initSiteTracking();

        const pageType = getPageType();
        if (pageType === 'home') {
            initHomeTracking();
            initYachtEventTracking();
        }
        if (pageType === 'yacht') initYachtEventTracking();
        if (pageType === 'shop') initShopTracking();
        if (pageType === 'faq') initFaqTracking();
        if (pageType === 'seo') initSeoTracking();
    });
})();
