---
name: mn-feed-fwd-podcast
description: Produce and package FEED//FWD podcast episodes in the approved Music Nerd pilot style. Use for video editing, collage graphics, audio, QC, episode thumbnails/titles/descriptions/tags/chapters/credits, recap coordination, publishing review and handoff. For a standalone written recap, use mn-feed-fwd-recap.
---

# FEED//FWD episode workflow

Match the approved pilot's visual language and editorial restraint, not its guest, timestamps, duration or accidental technical limitations. New instructions override the baseline. A local edit request does not authorize uploads, publication, third-party outreach, or permanent deletion.

## Start from the right material

- Canonical series root for the current project: the existing series root recorded in the episode manifest. Finder may show slashes; do not create another hierarchy.
- Locate the actual episode record, source manifest, current accepted movie and edit dependencies. Confirm the file, not only an alias or open app window. Work locally unless another destination is requested.
- Read `references/pilot-reference.md` when matching the pilot. Its timing and gains are examples, not automatic settings for another episode.
- Read `references/visual-system.md` for layout/animation; `references/audio-editorial.md` before any timing or sound change; `references/delivery-qc.md` before render, handoff or cleanup.
- Use `assets/episode-settings.example.json` as a per-episode manifest template; replace placeholders and leave unknown facts explicitly unresolved. Inspect actual assets and streams. Preserve originals and an accepted baseline; avoid building a new episode by repeatedly recompressing an old review. Reuse the source timeline/compositor with episode parameters.

The episode process includes both the finished video and its supporting written package. This skill coordinates the full workflow; `mn-feed-fwd-recap` supplies specialized article-writing guidance, rather than a separate unrelated process. Honor a narrow edit-only request without creating unrequested long-form work.

## Episode workflow

1. **Ingest and map:** hash original files; identify speakers; record media start offsets, frame rates/time bases, audio rates, screen-share offset and transcript timing basis. Align cameras and screen-share by evidence. Maintain a source-to-output edit map.
2. **Editorial pass:** read the whole transcript and inspect requested moments in the recording. Build a narrative cut without changing meaning. Keep natural breath and pacing. Do not automatically remove every filler. Get a short preview of risky dialogue cuts listened to before full rendering.
3. **Style and motion:** use the shared torn-paper/pink-tape system and real simultaneous sources. Show a small representative preview when a new design choice affects the whole episode. Apply accepted choices consistently across cold open, single/two-person, screen-share, graphics and ending.
4. **Music:** locate the supplied stinger and its real duration/fade. Anchor music and ducking to the actual words in the edited timeline. Keep dialogue independently recoverable. Size the ending to fit the music, not the other way around.
5. **Render and verify:** render versioned output, test full decode/stream durations, inspect changed boundaries and representative layouts, compare untouched streams where possible. Perform actual audiovisual audition; if unavailable, explicitly mark it pending and ask Pete to listen to a focused preview. Never equate ASR/waveform/peak checks with hearing the result.
6. **Deliver and record:** put the real accepted file in the original episode folder, update version/state manifest, reveal it in Finder or open QuickTime if requested, and verify the displayed document. A process exit alone is not proof the right file is open.
7. **Package and recap:** prepare or update title, description, tags, verified links, final-cut chapters/timestamps, captions and credits. Read `references/episode-packaging.md`, including `references/thumbnail-production.md` and its verified Recoup renderer reference. For a requested or established recap deliverable, load the installed `mn-feed-fwd-recap` skill and apply its source-backed writing/review workflow to this episode, reusing existing evidence. Track an unrequested long-form recap as not requested, rather than silently treating it as complete or creating one automatically.
8. **Publishing review:** present the accepted video and writing together, identify outstanding checks, verify destination and exact upload/send authorization. Draft preparation is not publication approval. Recheck final timing and credits if picture changes.
9. **Cleanup only when requested:** retain a rebuildable project; dependency-check before moving disposable files to recoverable Trash. Do not call a folder disposable merely because it is old, temporary, or under Codex.

## Pilot-derived defaults

- Correct brand pink **#FF75D8**, near-black background, warm white paper, actual Music Nerd/FEED//FWD artwork.
- Imperfect collage, torn edges, tape, drawings and stop-motion feeling. Prefer procedural/drawn motion and sourced photographs over AI-generated imagery for this show.
- Stable top-left show mark with consistent safe gutters; no tiny persistent subtitle. Larger identity on title/end cards. No extra glasses icon floating above the cold-open description.
- One shared nameplate design for host and guests. Keep it inside its camera composition with breathing room, not colliding with the ripped border.
- Animate to explain a person, connection, tool or idea. Avoid decorative repetition and quote overload. Return smoothly to a full speaker frame immediately when the insert is finished.
- End with verified show/guest/host social handles and site, then logo/site hold through the full music fade and a short visual tail. Attribution belongs in a legible appropriate place and in actual public publication credits where required.

## Before saying finished

Record what was watched/listened to, technical checks, remaining limitations, accepted version, exact file path and approval scope. For a complete-episode request, also report packaging and recap state (ready, awaiting review, not requested, or blocked), not just whether the movie rendered. `APPROVED-REVIEW` means accepted for now, not published or a broadcast master. The pilot approval did not establish a continuous end-to-end perceptual QC pass or final 1080p master.
