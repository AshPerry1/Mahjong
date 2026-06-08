// Service Worker for Lookout Mountain Mahjong
const CACHE_NAME = 'mahjong-cache-v15';
const PRECACHE_URLS = [
  '/',
  '/index.html',
  '/shop.html',
  '/faq.html',
  '/critical.css',
  '/fonts/fonts.css',
  '/styles.css',
  '/script.js',
  '/shop.js',
  '/analytics.js',
  '/logo-100.png',
  '/logo.png',
  '/fonts/playfair-400.woff2',
  '/fonts/inter-400.woff2',
  '/fonts/inter-500.woff2',
  '/fonts/inter-700.woff2'
];

const CACHEABLE_IMAGE_SUFFIXES = [
  '/logo.png',
  '/logo-100.png',
  '/Attachment-1.png',
  '/FES.png',
  '/LMS.png'
];

function isSameOrigin(url) {
  return url.origin === self.location.origin;
}

function isStaticAsset(pathname) {
  return /\.(css|js|woff2|png|jpe?g|webp|gif|json)$/i.test(pathname);
}

function isDocumentRequest(request, pathname) {
  return request.mode === 'navigate' || pathname === '/' || pathname.endsWith('.html');
}

function shouldCacheRequest(request, response) {
  if (!response || response.status !== 200 || request.method !== 'GET') {
    return false;
  }

  const url = new URL(request.url);
  if (!isSameOrigin(url)) {
    return false;
  }

  const path = url.pathname;
  if (/\.(png|jpe?g|webp|gif)$/i.test(path)) {
    if (path.startsWith('/images/opt/')) {
      return true;
    }
    return CACHEABLE_IMAGE_SUFFIXES.some((suffix) => path.endsWith(suffix));
  }

  return isStaticAsset(path) || path === '/' || path.endsWith('.html');
}

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => (
      Promise.allSettled(PRECACHE_URLS.map((url) => cache.add(url)))
    ))
  );
  self.skipWaiting();
});

self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') {
    return;
  }

  const url = new URL(event.request.url);
  if (!isSameOrigin(url)) {
    return;
  }

  if (isDocumentRequest(event.request, url.pathname)) {
    event.respondWith(
      fetch(event.request)
        .then((response) => {
          if (shouldCacheRequest(event.request, response)) {
            const clone = response.clone();
            caches.open(CACHE_NAME).then((cache) => cache.put(event.request, clone));
          }
          return response;
        })
        .catch(() => caches.match(event.request).then((cached) => cached || caches.match('/index.html')))
    );
    return;
  }

  const useCacheFirst = isStaticAsset(url.pathname) || url.pathname.startsWith('/images/opt/');

  if (useCacheFirst) {
    event.respondWith(
      caches.match(event.request).then((cached) => {
        if (cached) {
          return cached;
        }
        return fetch(event.request).then((response) => {
          if (shouldCacheRequest(event.request, response)) {
            const clone = response.clone();
            caches.open(CACHE_NAME).then((cache) => cache.put(event.request, clone));
          }
          return response;
        });
      })
    );
    return;
  }

  event.respondWith(
    fetch(event.request)
      .then((response) => {
        if (shouldCacheRequest(event.request, response)) {
          const clone = response.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(event.request, clone));
        }
        return response;
      })
      .catch(() => caches.match(event.request))
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => Promise.all(
      cacheNames.map((cacheName) => {
        if (cacheName !== CACHE_NAME) {
          return caches.delete(cacheName);
        }
        return undefined;
      })
    )).then(() => self.clients.claim())
  );
});
