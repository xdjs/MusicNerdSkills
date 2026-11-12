---
name: mn-feed-fwd-recap
description: Turn a FEED//FWD community-session recording into a source-backed Music Nerd Substack recap in Pete's voice, with separate notes, verified participant attribution, and selected screenshots. Also use to revise an existing FEED//FWD recap; not for producing or editing podcast video.
---

# FEED//FWD recap

Create a readable account of the session for people who missed it. Pete's priority is that the article sounds like him and reflects the actual conversation. Use the recording and his edits as the authority; previous recaps provide voice and formatting references, not a template that every event must fit.

## Establish the source and destination

Read the supplied recording or existing draft. Reuse a recent approved recap or user-edited writing sample when available, and preserve intentional titles, links, imagery, and editorial notes. Keep private transcripts and editorial checks separate from the article. Work outside unrelated code repositories. Do not create software issues for editorial work.

When starting from a recording, inspect metadata with ffprobe, extract mono 16 kHz audio with ffmpeg, and reuse a working local MLX Whisper installation/model if available. Verify cached environments actually import their dependencies. Use a task-specific working folder and leave source media untouched. Keep the recording local unless uploading is authorized. If Metal is unavailable in the sandbox, request the required execution permission rather than repeatedly retrying. Use available local-media analysis guidance when helpful.

Read the whole transcript before selecting an angle. Sample frames for visible names, screen shares, and context; review the original audio around selected quotes and ambiguous passages. Machine transcription is provisional evidence, not a verified quotation. Track timestamps, speaker confidence, proper-name corrections, and screenshot provenance in private notes. Do not guess a speaker's identity from voice alone. Verify links against the actual participant/project, especially namesakes. Check the Music Nerd Discord av-room text chat for links shared during the session when accessible; match the event date, sender, and demo rather than guessing URLs. Read chat without joining a voice call or posting. Preserve relevant shared-resource links in source notes even if they do not all belong in the article.

## Write from the conversation

Use the available Text Humanizer skill for voice and final editing. Its key principles also apply if the skill is unavailable:

- Write in Pete's first-person perspective when supported by his words or actions. Do not refer to him as an outside reporter. Never attribute another speaker's experience or opinion to him.
- Start from a specific exchange, demo, question, or reason for gathering. Do not invent a scene, emotion, opinion, or anecdote to make the opening personal.
- Preserve his ordinary wording, contractions, humor, uncertainty, and interests. Written samples and user edits take precedence over polished paraphrase. Do not manufacture slang or deliberate mistakes.
- Let the strongest moments determine the structure. Avoid a predictable summary of each speaker, repeated section formulas, inflated significance, forced contrasts, and generic claims about the future of music or technology.
- Use participant excerpts when their wording adds something. Verify quotations against audio, keep speakers clearly attributed, and paraphrase uncertain passages. If quotes are lightly edited, disclose that briefly. Never put synthesized summaries in quotation marks.
- Distinguish what was demonstrated from what somebody reported, proposed, offered, or promised. Discussion is not a partnership; an offer is not completed work.
- Finish with the actual unresolved question or concrete follow-up when it fits. Do not manufacture a lesson, optimistic conclusion, or invitation.

Edit the article as a whole for coherence, rhythm, repetition, and viewpoint. Check every factual claim and quotation against the evidence map. Quality comes from accurate, particular writing; do not optimize word substitutions for detector scores.

## Deliverables and review

Prepare the article with useful participant/project links and a few relevant, legible screenshots with factual captions. Select images for what they show, not to satisfy a fixed count. Check source frames for private messages, email addresses, invite codes, or other incidental private content before sharing. Preserve source timestamps and note any remaining image-quality limitation.

Keep detailed notes/transcript, follow-ups and owners, collaboration opportunities, and unresolved attribution questions separate from the public recap. Do not create redundant companion documents when the user only wants a draft edit. For a full recap, retain source notes alongside the article; use Google Docs when it is the established destination, following the available Docs/Drive skills.

When authorized to prepare the Substack draft, save it unpublished, use native headings and blockquotes, and verify the actual editor content and preview. A Saved indicator alone does not prove requested edits occurred. Preserve user edits and other document tabs. If an integration fails, use a supported browser fallback when available and report any incomplete destination work precisely.

Detector testing is optional, only when requested or already authorized. Follow Text Humanizer's bounded scan-and-revise process. Scan the actual saved version, report only observed results, and treat a score as classifier feedback, never proof of authorship. Do not promise 100% human or publish because a score passes.

Completion means the user has a reviewable article and its location, with source uncertainties or missing checks stated. Leave drafts unpublished and do not send messages to participants without explicit authorization.
