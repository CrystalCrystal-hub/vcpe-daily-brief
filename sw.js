const CACHE = 'vcpe-v3';
const SHELL = [
  './',
  './index.html',
  './app.webmanifest',
  './data.json',
  './icons/icon-192.png',
  './icons/icon-512.png'
];

self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE).then((c) => c.addAll(SHELL)).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys()
      .then((ks) => Promise.all(ks.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (e) => {
  const req = e.request;
  const url = new URL(req.url);

  // 导航请求：网络优先，失败才回退缓存首页，保证内容最新
  if (req.mode === 'navigate') {
    e.respondWith(
      fetch(req).catch(() => caches.match('./index.html'))
    );
    return;
  }

  // data.json 与 archive 下的简报：网络优先，避免看到旧/空内容
  if (url.pathname.endsWith('data.json') || url.pathname.startsWith('/archive/')) {
    e.respondWith(
      fetch(req)
        .then((resp) => {
          if (!resp || resp.status !== 200) throw new Error('bad');
          const cp = resp.clone();
          caches.open(CACHE).then((c) => c.put(req, cp));
          return resp;
        })
        .catch(() => caches.match(req))
    );
    return;
  }

  // 其余静态资源：缓存优先，缺则网络并回填
  e.respondWith(
    caches.match(req).then((r) =>
      r || fetch(req).then((resp) => {
        const cp = resp.clone();
        caches.open(CACHE).then((c) => c.put(req, cp));
        return resp;
      }).catch(() => r)
    )
  );
});
