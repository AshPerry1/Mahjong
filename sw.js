// Service Worker for Lookout Mountain Mahjong
const CACHE_NAME = 'mahjong-cache-v13';
const urlsToCache = [
  '/',
  '/index.html',
  '/shop.html',
  '/faq.html',
  '/styles.css',
  '/script.js',
  '/shop.js',
  '/analytics.js',
  '/logo.png'
];

const CACHEABLE_IMAGE_SUFFIXES = [
  '/logo.png',
  '/Attachment-1.png',
  '/FES.png',
  '/LMS.png'
];

function isSameOrigin(url) {
  return url.origin === self.location.origin;
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

  return true;
}

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(urlsToCache))
  );
});

self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') {
    return;
  }

  event.respondWith(
    fetch(event.request)
      .then((response) => {
        if (shouldCacheRequest(event.request, response)) {
          const responseClone = response.clone();
          caches.open(CACHE_NAME).then((cache) => {
            cache.put(event.request, responseClone);
          });
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
    ))
  );
});

self.addEventListener('sync', (event) => {
  if (event.tag === 'background-sync') {
    event.waitUntil(Promise.resolve());
  }
});
