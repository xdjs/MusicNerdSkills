# Filming a screen only a claimant sees (the research build)

Some of Music Nerd's best moments only exist for a signed-in claimant during a build: the status card stepping
through "finding your profiles…", skeletons resolving into content, "N new" marks, the tour opening on the drafted
About. A signed-out capture cannot show them. Film a **real build on staging**, with the artist's data replaced by
a fictional artist before anything is captured (owner ruling, 2026-10-08). First used for the
"watch your profile build itself" short (account workspace `content/mn-research-in-place/`).

## Before you start

- **An owner go-ahead to reset that artist on staging.** The reset deletes rows; it is staging only, and the
  artist is restored afterwards.
- **A claimed staging artist whose claimant can sign in.** The fixture used so far is Bio Ritmo on staging, whose
  claimant is a team member's account. Ask whose account it is; never create or approve a claim to get one.
- **The staging database connection** (the web app's Vercel `staging` environment). Never the production one: check
  the project ref before any write, as `scripts/onboarding-scenario.sh` in MusicNerdWeb does.
- A browser you can drive with emulation: `agent-browser --session <name> --headed`, then
  `set device "iPhone 16 Pro"` (402×874 at 3×) and **`set media dark`**. The theme follows `prefers-color-scheme`;
  a run without it came out light.

## Sign in

Open `https://staging.musicnerd.net/` (the home page, **not** the artist page: opening the artist page as the
claimant starts the build), open the menu, Log In, enter the claimant's email, and ask the claimant for the six-digit
Privy code. Stay on the home page.

## Reset (back up first)

1. Back up, to a private scratch location, never this repo: the artist's link columns, its `artist_onboarding_steps`
   rows, and the `artist_vault_sources` rows the last build created (by `created_at`).
2. In one transaction: null every link column except `deezer`; delete the artist's `artist_onboarding_steps`;
   delete the vault sources the last build created. Older sources stay (re-discovery skips URLs it already has).
3. After the last capture, restore from the backup (`json_populate_recordset`) and check the counts match.

A build takes about 30 seconds. Each one leaves idle `mnweb` sessions behind, and staging's session pool (35) filled
after about four builds; the fifth failed with "try again". Space the runs, check
`select state, count(*) from pg_stat_activity where usename='mnweb' group by 1` before each, and wait for it to drain.

## Capture

1. Open the artist page, then immediately inject `scripts/obfuscate.js` with the real
   artist's strings set first:
   `window.__MN_OBF_REAL = { name, handle, places: [[realPlace, fictionalPlace]] };`. It renames the artist, writes a
   fictional About, source titles and domains, rewrites Latest captions whole (they are split across text nodes and
   @-links), blurs every photo, keeps the platform icons in Links sharp, and keeps doing so as the page repaints.
2. Each tick (about every 1.5s) until "Your page is ready", screenshot the viewport three times: scrolled to the
   top, to `#mn-links`, and to `#mn-lore`. `screenshot --full` does not work here: it misses the sections.
   **Use absolute paths**; relative ones silently save nowhere.
3. **Leak check every tick:** pull the real artist's source titles from the database, add the name, handles, places
   and release names, and test the page's `innerText` against them. Any hit, discard the run.
4. The "new" marks clear 5 seconds after a section has been on screen, so the arrival frames are the first one or
   two after each step completes. Name files by elapsed seconds (`links-013.6.png`) to find them.
5. Look at every frame you keep. Real handles and captions hide in places a text check can miss.

## Choosing frames

Status card states from the top shots; skeleton then arrival from the Links and Lore shots; the tour's first card
over the About for the finish. Before the final render, check open PRs that change what is shown: on 2026-10-08 the
"Your page is ready" card was being removed (#1465), so the last beat used the tour card, true before and after.
