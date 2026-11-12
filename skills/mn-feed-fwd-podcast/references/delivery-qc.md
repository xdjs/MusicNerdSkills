# Delivery, file organization and verification

## Canonical project and names

Keep the existing series root recorded in the episode manifest, with `00_ADMIN`, `01_BRAND`, `02_EPISODES`, `03_DISTRIBUTION`, `04_AUDIO`, `99_ARCHIVE`. Episode folders use an explicit ID and guest slug. Keep originals, prep, working media, edit projects, review exports, approved release deliverables, distribution records and follow-up separated.

Use `FEED-FWD_<episode>_<guest>_vNN_<YYYY-MM-DD>_<status>.<ext>` for new outputs. Pilot example: `FEED-FWD_PILOT-001_La-Equis_v23_2026-11-11_APPROVED-REVIEW.mp4`. Source filenames remain unchanged. Version every meaningful change; record what changed and which accepted baseline it used. Review acceptance is not publication permission.

The actual user-facing movie belongs inside the ORIGINAL episode folder, normally `05_REVIEW/exports` for a review or `06_APPROVED/masters` for an explicitly approved master. A link there pointing to a scratch/Codex folder is not sufficient. Working files may live elsewhere temporarily, but record them in a dependency manifest and consolidate when safe. Keep a compatibility alias only if needed by existing scripts, and verify it resolves after a move. Never hand off an unverified temporary path.

Keep production code/scripts, reusable artwork and parameters with the episode or a maintained shared template. Do not silently delete prior renders that serve as inputs to a newer version. Before cleanup, trace scripts, symlinks, concat lists and media references. Preserve absolute external dependencies until rewritten and tested. A needed asset from /tmp must be copied into durable storage and references updated.

## Export and color

Probe streams before and after: dimensions, actual FPS, frame count, time base, audio rate/channels, durations, start times, color primaries/transfer/matrix/range. Preserve original files and hash them. Check full decode and boundary playback; inspect black frames, truncated speech/music, audio drift and end duration.

The pilot's correct pink was affected by missing/mismatched color metadata in QuickTime, not merely low resolution. Its approved color-managed 720p stream uses BT.709 primaries, sRGB transfer, SMPTE170M matrix with matching H.264/container signaling. This is a property of that pipeline, NOT a universal mandate to retag other footage. For each pipeline, convert/tag consistently and compare rendered #FF75D8 patches in the actual player. Do not change grade or retag incompatible video blindly. Preserve a known-good reference and avoid repeated unnecessary encoding.

Use `python3 scripts/inspect_export.py <movie>` for a read-only metadata/hash report; add `--decode` for a full audio/video decode check. It does not listen, measure all perceptual defects, or grant approval. For loudness/true peak, use a verified analysis tool on intro/dialogue/outro as well as full mix; record filter/tool and output. For unchanged ranges, compare decoded audio/video hashes as appropriate, with equal sample/frame definitions.

## Review matrix

Check settled frames AND transition boundaries for cold open, title, all nameplates, single/two-camera, screen share, contextual photos, drawings, quote cards, goodbye, social cards and final fade. Verify no obsolete overlay briefly reappears. Check phone-size readability and show every newly changed component in a preview if acceptance is needed.

Listen to the first host introduction, every dialogue trim/crossfade, music dips/raises and entire outro fade. Watch the full final episode before claiming continuous QC. If only sampled, report the sample coverage. Do not promote a technical pass to subjective approval.

Record exact version, file hash, review scope, outstanding checks, user acceptance and date. “Works for now” maps to APPROVED-REVIEW, not final broadcast quality or publication.

## Credits and end-card content

Use verified platform-specific host, guest, Music Nerd handles and current website. Search current official sources, not old buttons or memory alone. If platforms differ, label them accurately rather than showing “Instagram / X” for an unverified shared handle. A historical handle is not a permanent brand configuration.

Use the approved closing sequence as a model: readable paper/tape cards, then a quiet logo/site hold, natural audio and visual fade, brief black tail. Do not invent a fixed duration; compute it from the stinger and audience reading time.

Maintain an asset-rights ledger with source URL, creator, license/permission, modifications and placement of attribution. Nonmonetization does not waive license terms. If moving a credit off video, prepare the required publication text and ensure it actually accompanies the eventual public upload; a private text file is not public credit. Do not include private notes or credentials in metadata.

Prepare factual titles and descriptions, verified host/guest/show links, relevant tags, and chapters beginning at 0:00 from verified final timing, not a stale raw transcript. Do not copy another show’s sales CTA or impose its title format. Re-time captions after all edits. Publication/guest delivery remains a separate authorized action; record actual URLs and receipts only after verification.

## Handoff and cleanup

For QuickTime, open the exact file and verify document URL/name/duration/paused state. If app-name resolution fails, the installed `/System/Applications/QuickTime Player.app` path may be used when verified. For Finder, reveal/select the actual canonical file. Report failure instead of claiming it opened.

Deliver requested previews as native attachments where supported; a private download URL or local path is not an attachment. Verify the file is accessible before claiming delivery.

On cleanup request, inventory sizes and dependencies, preserve originals/project/fonts/assets/final/credits/rebuild inputs, move only confidently disposable derivatives to recoverable Trash, and write a restore manifest. Don't empty Trash without the required explicit confirmation. Moving files to Trash does not reclaim disk space; measure and report honestly. Avoid touching unrelated projects or a blanket cleanup of Downloads/Codex.
