# Podcast thumbnails and episode covers

## Verified Recoup source and capability

The inspected local source is the corresponding path in the private episode manifest, repository https://github.com/recoupable/skills, commit `0fc34357ab1c9b501ce8fc24f885d7420d880e3d`. It is a source snapshot, not an installed FEED//FWD renderer. The working tree may be absent; source can be inspected read-only with `git show <commit>:<path>`.

- Specification: `skills/recoup-internal-podcast/references/podcast-packaging.md`.
- Actual renderer: `skills/recoup-internal-podcast/scripts/podcast/make_cover.py`; function `cover(W, H)`.
- Inputs: `--bg`, `--lockup`, `--cutout`, `--title`, `--guest`, `--role`, `--out`; optional `--fonts`.
- Outputs: `thumbnail-2000x1125.jpg` (16:9) and `cover-2000x2000.jpg` (square), JPEG quality 92.
- Dependencies: Pillow; fontTools and brotli to instantiate its bundled DM Sans variable font unless prepared font instances exist. Its original blue-sweep background and white Recoup lockup are private workspace assets, not bundled reusable FEED//FWD assets.
- Behavior: local deterministic compositing of an existing background, logo, real photo cutout and wrapped text. It is not a text-to-image service. Its command executes at module import, creates font caches and overwrites fixed output filenames: do not import/run it casually or aim at an existing approved output directory.

The separate `recoup-internal-content-make-thumbnails` skill makes animated eight-second MCP gallery-card films. It is NOT this podcast cover generator and should not be invoked for episode cover art.

## FEED//FWD integration

Thumbnail/cover production is an explicit episode packaging step, using the above renderer as an implementation reference rather than claiming an unmodified Recoup template is Music Nerd-ready. No external software or generator has been installed by adding this reference.

1. Confirm the intended destination/formats and current upload requirements. Use 16:9 and square when appropriate; do not promise acceptance solely from historical dimensions.
2. Locate approved Music Nerd / FEED//FWD artwork, #FF75D8 palette, fonts and the guest's supplied or otherwise permitted real photo. Verify provenance and image rights. Prefer procedural composition and real photography over generated imagery. Do not run background removal/model downloads, external generation or software installs merely because source instructions suggest them; follow current tools and permissions.
3. Draft the factual short title, guest name and optional role. Respect user copy. Use the pilot's collage/paper/tape system, not Recoup's blue sweep, DM Sans branding or sales positioning. Keep hierarchy simple and faces/title clear.
4. For implementation, first inspect any existing approved local cover template. If adapting the Recoup renderer is appropriate, inspect its license and code, use an approved execution environment/dependencies, explicitly parameterize Music Nerd assets/type/colors, and preserve editable source. Do not install or execute unrecognized source code without required approval. Do not claim a functional Music Nerd renderer exists until adapted and tested. The earlier local compositor was rejected and is not shipped as a reusable default; adapt the actual accepted episode artwork instead.
5. Render to a new versioned review directory, never the generator's default filenames over accepted art. Create both requested compositions intentionally, rather than cropping away text/faces for square. Keep actual logos, correctly spelled text and a real guest likeness. Long words/roles must not overflow; shorten or reflow with approval where meaning changes.
6. Review at full size and mobile thumbnail scale, including destination crop. Check title length, contrast, face quality, mask edges, margins, right-side overlap, logo visibility and whether square layout genuinely works. Avoid unsupported claims about the guest. Show the local drafts for review; do not upload them by default.
7. Record source assets/rights, fonts, renderer/version, exact copy, dimensions, output paths/hash and approval state. Store review artwork with the episode review assets and accepted artwork in `06_APPROVED/artwork` when accepted. Link it in packaging metadata. Publication remains separately authorized.

## Honest readiness

Report distinct states: source inspected, Music Nerd adaptation prepared, dependency check passed, actual images rendered, visually reviewed, approved, uploaded. A specification or source file alone does not mean a thumbnail was generated. Do not substitute the animated gallery-card generator or AI imagery without a relevant request.

## Renderer scope

No turnkey thumbnail compositor is shipped. Reuse the accepted episode artwork and source, parameterize inputs, and review every new guest/layout at phone size.

## Pilot thumbnail correction (2026-11-11)

Pete rejected the first webcam-frame tests: “for the image you should use the image provided by La Equis.” The supplied portrait was already present in the episode at `04_EDIT/full-review-2026-10-31-v01/assets/portrait-1-original.jpg`; the episode decision record documents provenance. Do not repeat the recording-frame substitution when a supplied guest image exists. Search the existing asset manifest and earlier episode decisions before choosing another source.

For the YouTube revision, prioritize one recognizable large face, one accurate short hook, strong mobile-size contrast and restrained show branding rather than a generic title slide. v03 offers “From songs to software” and “Why build your own tools?” based on the actual discussion; neither is a quote or approved publishing copy. Inspect at 360px width and full size. This v03 proposal was superseded by later review.

### Refinement after v03 feedback

Pete found v03 closer but messy and unintentional. For this episode, v04 reduces the composition to one photograph, a two-line hook, guest overline and small show mark. Remove orphan words, competing badges/footers, and decorative seams touching text. Review actual reference thumbnails and both 360px/240px previews. Do not claim design changes improve CTR without measurement. This intermediate design was superseded by later review.

### v05 explicit direction

Pete likes the photograph fading into black and wants FEED//FWD kept on one line, not stacked. Preserve that blend and horizontal wordmark in the thumbnail iteration. v05 changes only the wordmark and subtly enlarges the guest overline; main hook and photo remain pixel-identical to v04. This intermediate v05 state was superseded by the v07 handoff below.

## Final pilot handoff (2026-11-11)

The final v07 uses the guest-supplied portrait fading into black, horizontal FEED//FWD wordmark, a short two-line hook, and the official pink glasses-only Music Nerd signature. Pete explicitly preferred subtle glasses over another logo-and-text badge. Preserve that restrained hierarchy; do not replace supplied artwork with a recording frame or a generic/redrawn mark. The final PNG was saved with the episode artwork and used on the unlisted YouTube episode. The older make_cover.py prototype does NOT reproduce this accepted layout; do not present its output as the pilot template. Locate the accepted artwork and editable render source in the episode before adapting it.

Verify the actual image in YouTube Studio and the watch page, not only a local preview. Keep the uploaded file hash and destination in the episode publication record. The pilot's earlier render manifest still says DRAFT-REVIEW; record later approval/publication evidence separately rather than assuming that metadata proves final status.
