# Episode packaging and recap coordination

The video and writing form one episode workflow. Keep one episode record and evidence set. The sibling `mn-feed-fwd-recap` skill handles the long-form article craft; this skill owns orchestration and consistency with the accepted edit.

## Scope and source handoff

- For a full episode workflow, inventory video, title, description, tags, chapters/timestamps, captions, artwork, credits and recap. Respect the requested scope: a small audio fix is not an instruction to write a new article. Prepare a long-form recap when requested or established for this episode; otherwise mark it not requested and offer it rather than inventing another deliverable.
- Load the installed `mn-feed-fwd-recap` skill by name for recap work. Its existing remit is FEED//FWD community-session recaps for Music Nerd Substack. Reuse its voice, evidence, attribution and review method for a podcast companion article, but do not assume a podcast happened on Discord, has an av-room chat, requires Google Docs/Substack, or has community-session participants. Verify format, people and destination from the actual episode.
- Pass the exact accepted version/hash, final media, existing transcript and source-to-output map, corrected names, verified links, rights ledger, current outline/draft and user edits. Reuse prior transcription and research; do not retranscribe unchanged material merely because the writing step starts.
- Read the whole relevant transcript and check quotes against original audio. Distinguish raw source times from final chapter times. A recap may describe the broader recording only when that scope is explicit; do not imply cut material is in the published episode.

## Reviewable episode package

1. **Title:** a clear, factual topic/guest promise, preserving the established show identity. Avoid sensational claims, unsupported affiliations or copying another show's formula.
2. **Description:** an accurate concise opening, specific topics discussed, guest/host/show identities and verified useful links. Preserve intentional user copy. Do not add an unrequested sales CTA or commitments.
3. **Tags:** relevant names, show and topics actually covered. Tags are not a substitute for context or evidence.
4. **Chapters:** begin at 0:00, use the exact final export timeline, verify each boundary and label, keep times ascending and within duration. Follow current destination requirements. Any later cut or new intro requires recalculation.
5. **Captions:** correct speaker names and terms; retime after cuts; check placement/readability and export against final media.
6. **Credits:** carry required attribution, source/license links and modification notes from the rights ledger and PUBLICATION-CREDITS.txt into the actual public description or allowed public credit location. No silent omission because the video is not monetized.
7. **Recap, when in scope:** invoke mn-feed-fwd-recap for an accurate article in Pete's voice, verified quotes and selected relevant images. Keep private evidence/uncertainties separate. Do not duplicate the description as a long article or force a speaker-by-speaker template.
8. **Thumbnails and artwork:** follow [thumbnail-production.md](thumbnail-production.md), which documents the actual Recoup podcast cover generator and the Music Nerd adaptation workflow. Prepare requested 16:9 thumbnails/square covers using approved branding and factual copy; verify rights, typography, crop and mobile legibility. Do not claim the referenced renderer is already installed or Music Nerd-ready.

## Files, approvals and completion

Store local packaging under the episode's `07_DISTRIBUTION/metadata`; keep the recap and source notes under the established `08_FOLLOWUP/recap` or existing agreed destination. Do not move an existing user draft just to match these defaults. Record paths/status in the episode manifest, and distinguish private source notes from public copy.

Bind each packaging item to the export version and SHA-256 it was checked against. Whenever the accepted export changes, invalidate chapter/caption timing readiness and recheck descriptions, screenshots and recap references affected by the edit; do not leave stale items marked ready. An 8-second intro change shifts later chapter/caption times even if dialogue content is unchanged.

Present video and writing as a coherent review package. Track each requested item as ready, needs review, blocked or not requested. Verify final version/timestamps/handles/credits across the package. Preserve user edits during regeneration.

Preparing local copy does not authorize placing drafts in third-party editors, uploading files, publishing or messaging guests. Follow the user's exact destination/action authorization and applicable confirmations. After an authorized publication, verify actual visible content and URLs before recording a receipt; otherwise leave the package unpublished and report what remains.

## YouTube handoff

Use the existing verified channel and the exact approved video/artwork. Keep visibility unlisted when requested; unlisted approval is not public-release approval. Verify processing/checks, actual thumbnail, saved title and full description, chapters and required photo credits. Channel verification for longer uploads does not by itself make external description links clickable; report that limitation separately. Return the verified watch URL and visibility, and record the uploaded media/artwork versions. Do not create a second upload merely to change its thumbnail.
