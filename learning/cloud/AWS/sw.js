// 改版時記得把版本號 +1，activate 會自動清掉舊快取
const CACHE = "aws-saa-v7";

const ASSETS = [
  "index.html",
  "basics.html",
  "quiz.html",
  "flashcards.html",
  "manifest.json",
  "icon.svg",
  "assets/lesson.css",
  "01-account-iam.html",
  "02-vpc-build.html",
  "03-ec2-storage.html",
  "04-s3-deep.html",
  "05-database.html",
  "06-elb-asg.html",
  "07-serverless.html",
  "08-monitor-cost.html",
  "09-architecture.html",
  "10-iac.html",
  "11-ecs-containers.html",
  "12-identity-api.html",
  "13-analytics.html",
  "14-ai-ml.html",
  "15-migration.html",
  "16-eks.html",
  "17-cicd.html",
  "18-security-services.html",
  "19-hybrid-network.html",
  "20-file-backup.html",
  "exam-strategy.html",
  "notes/01-服務對照速查表.md",
  "notes/02-四大領域重點筆記.md",
  "notes/03-八週讀書計畫.md"
];

self.addEventListener("install", e => {
  e.waitUntil(
    caches.open(CACHE)
      // 個別加入，單一檔案 404 不會讓整個安裝失敗
      .then(c => Promise.allSettled(ASSETS.map(a => c.add(a))))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", e => {
  e.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

// HTML 用「網路優先」：有網路時一定拿到最新內容，離線才回退快取。
// 舊版是純快取優先，會導致內容更新後使用者永遠看到舊頁面。
self.addEventListener("fetch", e => {
  const req = e.request;
  if (req.method !== "GET") return;

  const isHTML =
    req.mode === "navigate" ||
    (req.headers.get("accept") || "").includes("text/html");

  if (isHTML) {
    e.respondWith(
      fetch(req)
        .then(res => {
          const copy = res.clone();
          caches.open(CACHE).then(c => c.put(req, copy));
          return res;
        })
        .catch(() => caches.match(req).then(r => r || caches.match("index.html")))
    );
    return;
  }

  // 靜態資源用「快取優先」，但背景更新
  e.respondWith(
    caches.match(req).then(cached => {
      const network = fetch(req)
        .then(res => {
          const copy = res.clone();
          caches.open(CACHE).then(c => c.put(req, copy));
          return res;
        })
        .catch(() => cached);
      return cached || network;
    })
  );
});
