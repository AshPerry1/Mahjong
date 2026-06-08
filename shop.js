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
            const response = await fetch(CATALOG_URL);
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
