# Audio, edit points and music

## Preserve speech and sync

Start from isolated original/enhanced source tracks and the approved edit map where possible. Record which version contains what mix; do not repeatedly add gain deltas to an unknown baked mix. Keep dialogue and music independently rebuildable. Keep sample-rate conversion explicit.

A requested filler cut must preserve meaning, timing, consonants, breath and natural room tone. Find the exact words by source transcript plus waveform and listening. ASR identifies candidate boundaries, not final cut points. Move picture and sound together or deliberately cover the audio edit with a synchronized alternate view; do not leave lips out of sync. Recheck every downstream cue when duration changes. Use small appropriate fades/crossfades to avoid clicks without smearing speech.

The pilot's two later filler removals were rejected and restored. This means those cuts are not a template for future automatic cleanup. When restoring, restore both picture and sound timing. Preview risky speech surgery before a full render.

## Anchor cues to words, not guessed seconds

For each episode record: source music path/hash, native duration, original fade, intro music start, first host-introduction phrase and measured output onset, dip start/end/curve, hold gain, outro speech anchor and start, full cue end and visual tail. Use the episode template in assets.

The dip belongs at the FIRST spoken introduction (“Hey y’all, this is Pete Rango…” in the pilot), not the later “Today I’m joined by…” sentence. Verify the anchor against the currently edited output, not a raw transcript whose timing shifted. A later recut invalidates old cue timestamps.

Pete requested a smooth modest 4–6dB reduction when speech begins, held afterward while the supplied music's automatic fade plays. The pilot uses a 5dB dip from −3 to −8dB stem gain. These are gain values relative to that source, NOT a −3dBFS peak or universal loudness target. For new source music, audition balance and measure output, preserving clear vocals without sudden pumping. If “−3dB” is ambiguous, explicitly state the interpretation or clarify before a consequential full render.

Use a smooth ramp (e.g. smoothstep/cosine in dB) around speech entrance; avoid a discontinuous step. Do not add a second unnecessary fade over an intentional source fade. Check dialogue peaks, music-only passages and transitions separately. Loudness/true-peak readings are objective evidence, not proof the mix sounds good. Avoid measured clipping and leave sensible delivery headroom; do not normalize the entire show blindly to a guessed target.

## Ending must fit the real music

Start the full outro cue near actual thanks/goodbyes, not far earlier in the conversation. Under speech, keep it supportive, then let it rise when the closing cards appear if the approved mix calls for that. Never restart or chop a cue merely to fit an old 17-second end card.

Compute `music_end = cue_start + decoded_source_duration`; `episode_end` must include music_end plus a short visual/black tail and align to frame/sample boundaries. Extend the visual sequence as needed. The supplied pilot cue is ~36.545s, NOT the older 16s stinger. Probe the file actually used.

Critical render trap: FFmpeg `amix=duration=first`, `-shortest`, an old `-t`, or an old `atrim` can silently truncate the cue and then pad silence. Mix with the intended complete duration (pilot uses longest, then explicit pad/trim to the new end); inspect the actual rendered tail waveform and listen through its last audible decay. A silent tail does NOT prove the fade completed. Compare the source envelope with the rendered tail before and after the old ending boundary.

## Revision isolation

Visual-only revision: copy the accepted audio stream where possible and compare packet or decoded-PCM hashes. Audio-only revision: copy picture if timeline is unchanged. If duration extends, preserve the unchanged body and verify splice/keyframes/PTS plus the new ending. Packet-copy is not a substitute for full decode and boundary inspection. Retain the prior accepted movie until the revised file is verified.

If the runtime cannot audition audio, say so plainly. Provide a focused intro/outro or edit-boundary preview and ask for listening approval; don't say “sounds natural,” “listened,” or “full QC passed” based on transcription/peak checks.
