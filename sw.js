// Service Worker for Lookout Mountain Mahjong
const CACHE_NAME = 'mahjong-cache-v20';
const urlsToCache = [
  '/',
  '/index.html',
  '/mahjong.html',
  '/m.html',
  '/find-us.html',
  '/book-mahjong-lesson.html',
  '/invite.html',
  '/mahj-jen-mahj-hen.html',
  '/lookout-mountain-mahjong.html',
  '/mahjong-101.html',
  '/mahjong-102.html',
  '/beginner-mahjong.html',
  '/girls-night-mahjong.html',
  '/country-club-mahjong.html',
  '/west-virginia-mahjong.html',
  '/knoxville-mahjong.html',
  '/charlotte-mahjong.html',
  '/mahjong-lessons-near-me.html',
  '/private-mahjong-lessons.html',
  '/mahjong-tiles.html',
  '/chattanooga-mahjong.html',
  '/atlanta-mahjong.html',
  '/georgia-mahjong.html',
  '/tennessee-mahjong.html',
  '/nashville-mahjong.html',
  '/marthas-vineyard-mahjong.html',
  '/corporate-mahjong-events.html',
  '/sorority-mahjong-parties.html',
  '/mahjong-tips.html',
  '/press.html',
  '/site-map.html',
  '/learn-american-mahjong.html',
  '/greenbrier-mahjong.html',
  '/shop.html',
  '/faq.html',
  '/404.html',
  '/sitemap.xml',
  '/robots.txt',
  '/llms.txt',
  '/humans.txt',
  '/styles.css',
  '/script.js',
  '/analytics.js',
  '/logo.png',
  '/threadandink-catalog.json',
  '/thread-and-ink-logo.png',
  'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap'
];

// Install event - cache resources
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

// Fetch event - always try network first, then cache
self.addEventListener('fetch', event => {
  event.respondWith(
    fetch(event.request)
      .then(response => {
        // If network request succeeds, update cache
        if (response.status === 200) {
          const responseClone = response.clone();
          caches.open(CACHE_NAME)
            .then(cache => {
              cache.put(event.request, responseClone);
            });
        }
        return response;
      })
      .catch(() => {
        // If network fails, try cache
        return caches.match(event.request);
      })
  );
});

// Activate event - clean up old caches
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (cacheName !== CACHE_NAME) {
            console.log('Deleting old cache:', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});

// Background sync for offline form submissions
self.addEventListener('sync', event => {
  if (event.tag === 'background-sync') {
    event.waitUntil(doBackgroundSync());
  }
});

function doBackgroundSync() {
  // Handle offline form submissions
  return new Promise((resolve) => {
    // Implementation for background sync
    resolve();
  });
}

// Push notification handling
self.addEventListener('push', event => {
  const options = {
    body: event.data ? event.data.text() : 'New mahjong event available!',
    icon: '/logo.png',
    badge: '/logo.png',
    vibrate: [100, 50, 100],
    data: {
      dateOfArrival: Date.now(),
      primaryKey: 1
    },
    actions: [
      {
        action: 'explore',
        title: 'Learn More',
        icon: '/logo.png'
      },
      {
        action: 'close',
        title: 'Close',
        icon: '/logo.png'
      }
    ]
  };

  event.waitUntil(
    self.registration.showNotification('Lookout Mountain Mahjong', options)
  );
});

// Notification click handling
self.addEventListener('notificationclick', event => {
  event.notification.close();

  if (event.action === 'explore') {
    event.waitUntil(
      clients.openWindow('/')
    );
  }
});
