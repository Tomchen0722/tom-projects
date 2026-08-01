const CACHE = "aws-saa-v2";
const ASSETS = [
  "index.html",
  "basics.html",
  "quiz.html",
  "flashcards.html",
  "manifest.json",
  "icon.svg",
  "notes/01-服務對照速查表.md",
  "notes/02-四大領域重點筆記.md",
  "notes/03-八週讀書計畫.md"
];
self.addEventListener("install", e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)).then(() => self.skipWaiting()));
});
self.addEventListener("activate", e => {
  e.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener("fetch", e => {
  e.respondWith(caches.match(e.request).then(r => r || fetch(e.request)));
});
