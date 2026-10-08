// Injected into a staging artist page (agent-browser `eval`) right after it opens, before you capture anything.
// Rewrites every piece of the real artist's data to a fictional artist, blurs every photo (platform icons in Links
// stay sharp), and keeps doing so as the page repaints during the build. See references/staging-build-capture.md.
//
// Set the real artist's strings first, in the same eval or one before it:
//   window.__MN_OBF_REAL = { name: "Real Name", handle: "realhandle", places: [["Real City, State", "the Gulf Coast"]] };
// The fictional artist below is a salsa band; swap NAME/ABOUT/TITLES/RELEASES to fit the real artist's genre.
// The real artist's data must never appear in a kept frame (owner ruling 2026-10-08): run a leak check per capture.
(() => {
  if (window.__mnObf) return;
  const REAL = window.__MN_OBF_REAL || { name: "", handle: "", places: [] };
  const esc = (s) => s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  const NAME = "Orquesta Lumbre";
  const HANDLE = "orquestalumbre";
  const ABOUT = "Orquesta Lumbre is a nine-piece salsa band from the Gulf Coast, formed in 2004, known for long live descargas, a horn line that writes its own arrangements, and a run of self-released records that built a loyal dance-floor following…";
  const TITLES = [
    "Orquesta Lumbre - Encyclopedia entry", "Orquesta Lumbre: the band that kept salsa dura local",
    "Review: Noche Larga by Orquesta Lumbre", "Orquesta Lumbre | Album profile",
    "Inside the horn section of Orquesta Lumbre", "Orquesta Lumbre live at the Harbor Room",
    "Orquesta Lumbre talk twenty years of descargas", "A field guide to Orquesta Lumbre",
    "Orquesta Lumbre - Fuego Lento | Review", "Orquesta Lumbre on making records without a label",
  ];
  const DOMAINS = ["encyclopedia.example", "gulfsound.example", "salsareview.example", "albumguide.example",
    "harborweekly.example", "tropicalbeat.example", "musicjournal.example", "radiolatina.example"];
  const CAPTION = "Friday night descarga at the Harbor Room with the full horn line. Doors at 9, music till late. Free entry. #salsadura #livesalsa";
  const RELEASES = ["Noche Larga", "Fuego Lento", "Puerto Viejo", "Marea", "Lumbre en Vivo"];
  const MAP = [
    ...(REAL.name ? [[new RegExp(esc(REAL.name), "g"), NAME]] : []),
    ...(REAL.handle ? [[new RegExp(esc(REAL.handle) + "\\w*", "gi"), HANDLE]] : []),
    ...(REAL.places || []).map(([from, to]) => [new RegExp(esc(from), "g"), to]),
  ];
  const HANDLES = /@[A-Za-z0-9_.]{2,}/g;
  const UI = /^(Lore|Links|Latest|About|Add to Lore|Read more|Listen|Edit profile|Ask|New|new|Support the artist|Spotify|Deezer|Instagram|YouTube|Facebook|Soundcloud|SoundCloud|Discogs|Bandcamp|TikTok|Twitch|X|Linktree|All \(\d+\)|Article \(\d+\)|Profile \(\d+\)|Review \(\d+\)|Interview \(\d+\)|PROFILE|ARTICLE|REVIEW|INTERVIEW|INSTAGRAM|RELEASES|\d+ new|Read the post|From Instagram|Choose where to listen|Stories, interviews, and other sources curated by the artist\.)$/;
  const seen = new WeakMap();
  let ti = 0, di = 0, ri = 0;
  const pick = (arr, i) => arr[i % arr.length];
  const fix = (node) => {
    const v = node.nodeValue;
    if (!v || !v.trim() || seen.get(node) === v) return;
    let out = v;
    const t = v.trim();
    const el = node.parentElement;
    const inAbout = el && el.closest("#mn-about");
    const inLore = el && el.closest("#mn-lore");
    const inLatest = el && el.closest("#mn-latest");
    if (inAbout && t.length > 40) out = ABOUT;
    else if (!UI.test(t)) {
      if (inLore && /^[\w-]+(\.[\w-]+)+$/.test(t)) out = pick(DOMAINS, di++);
      else if (inLore && t.length > 12) out = pick(TITLES, ti++);
      else if (inLatest && t.length > 40) out = CAPTION;
      else if (inLatest && /^(Single|Ep|EP|Album) by /.test(t)) out = t.replace(/ by .*/, " by " + NAME);
      else if (inLatest && el.closest("button") && t.length > 2 && t.length < 40 && !/^\w{3} \d{1,2}, \d{4}$/.test(t)) out = pick(RELEASES, ri++);
    }
    for (const [re, rep] of MAP) out = out.replace(re, rep);
    if (inLatest || inLore) out = out.replace(HANDLES, "@" + HANDLE);
    if (out !== v) node.nodeValue = out;
    seen.set(node, node.nodeValue);
  };
  // Latest captions are split across text nodes and @-links, so rewrite each caption block whole.
  const latestFix = () => {
    const sec = document.getElementById("mn-latest");
    if (!sec) return;
    for (const art of sec.querySelectorAll("article")) {
      for (const e of art.querySelectorAll("p, div, span")) {
        const len = e.textContent.trim().length;
        if (len < 30 || e.closest("button")) continue;
        const kids = [...e.children].some((k) => k.textContent.trim().length >= 0.8 * len);
        if (!kids && e.textContent !== CAPTION) e.textContent = CAPTION;
      }
    }
  };
  const iconFix = () => { for (const i of document.querySelectorAll("#mn-links img")) i.style.setProperty("filter", "none", "important"); };
  const walk = (root) => {
    latestFix(); iconFix();
    const w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
    let n; while ((n = w.nextNode())) fix(n);
    if (REAL.name && document.title.includes(REAL.name)) document.title = document.title.replace(REAL.name, NAME);
  };
  const css = document.createElement("style");
  css.textContent = `#mn-links img { filter: none !important; }
    main :not(#mn-links *) img:not([src*="logo" i]):not([src$=".svg"]):not([width="16"]):not([width="20"]):not([width="24"]),
    main [style*="background-image"], main video { filter: blur(18px) saturate(.6) !important; }
    main img { transition: none !important; }`;
  document.documentElement.appendChild(css);
  walk(document.body);
  new MutationObserver((ms) => { for (const m of ms) {
    if (m.type === "characterData") fix(m.target);
    for (const a of m.addedNodes) a.nodeType === 3 ? fix(a) : a.nodeType === 1 && walk(a);
  } }).observe(document.body, { subtree: true, childList: true, characterData: true });
  window.__mnObf = true;
})();
