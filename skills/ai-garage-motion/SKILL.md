---
name: ai-garage-motion
description: "Create and refine motion videos, product animations, and kinetic typography, from concept and storyboard to reviewed video export."
metadata:
  version: "1.0.0"
---

# AI Garage Motion

Turn an idea into a coherent film with expressive motion, readable typography, deliberate sound, and an export the user can play. Work in the user's language. Follow the explicit brief over these defaults. A simple idea is enough to begin: make reversible creative decisions yourself, and ask only about missing facts that materially affect the result. Do not invent product features, customer results, prices, or asset rights.

For the Ukrainian version of these instructions, read [skill.uk.md](references/skill.uk.md). Load other references only when their topic applies.

## Direct the film before building it

Extract the purpose, audience, message, exact required copy, duration, aspect ratio, sound expectations, available assets, and delivery format. Mark assumptions. Build one visual idea that evolves across the film rather than a sequence of unrelated title cards.

For each scene, briefly propose 3–5 genuinely different creative directions and select one that advances the whole. Differences should concern action, space, visual metaphor, or transition, rather than only color. Keep the options concise; provide decisions and practical reasons, not private deliberation.

Complete a timed storyboard before full production. Specify what changes, how the camera and type behave, the incoming and outgoing transition, reading time, and sound cues. Test the hardest visual or technical moment with a short preview before a costly render. See [storyboard.md](references/storyboard.md).

## Give motion a purpose

Animate actions and consequences: anticipation, acceleration, contact, reaction, and settle. Give objects a sense of mass. Use foreground, subject, and background relationships to create depth where the chosen style benefits from it. Camera movement should reveal or explain something; use connected paths with controlled changes in speed. Calm holds and readable end frames are valid choices.

Typography is part of the composition and action. Design its readable final state first, then animate into and out of it. Check the actual language's glyphs, line breaks, contrast, safe margins, and reading time. Support the main action with secondary motion without competing for attention.

Use motion blur, depth of field, lighting, and material response when they improve the shot. A blurred overlay is not proof of physically meaningful blur. A flat zoom is not a new 3D viewpoint. Keep subjects and essential text recognizable. See [motion-and-sound.md](references/motion-and-sound.md).

## Plan the sound with the picture

Unless the brief requests silence, plan suitable music and sound design. Voice is optional and must follow the brief. Use available, authorized sources or generation tools; the skill does not grant accounts, credits, or licenses. Ask before a new paid action or an external upload that is not already authorized.

Mark the actual musical accents and visual events on the same timeline. Align meaningful reveals, contacts, and transitions to selected accents without forcing every cut onto a beat. After editing timing or changing music, recheck the cue map and full mix. Do not call a silent export voiced, or an unlistened mix reviewed.

## Choose the smallest adequate production stack

Respect an existing project and its stack. For a new project, HTML/CSS/JavaScript with SVG or Canvas can be a useful starting point; use a 3D or video framework when the shot requires it. Select tools for the output and available environment, rather than installing a framework by default.

Use deterministic time for code-driven animation: frame `i` should be reproducible at `i / fps`. Wait for fonts and assets before capture. Export the entire ordered sequence, including transitions. Realtime browser playback and a smooth preview do not establish a complete frame-accurate render.

Keep editable source, timeline, render settings, and required asset dependencies. Estimate additional disk use before heavy work, use existing project storage rules, and avoid unnecessary media copies. The optional [new_project.py](scripts/new_project.py) helper creates only small planning templates; it does not install or render anything.

## Review, repair, export

Treat the first full assembly as an internal draft. Watch the complete motion at normal speed, inspect every scene and transition, and listen to the full soundtrack when present. Record substantial issues as time → observation → fix → recheck. Repair causes, then review the changed sections and whole film again.

Default delivery, when the brief gives no other specification: MP4, 1920×1080, 60 fps, H.264, yuv420p; AAC audio when sound is requested. Use the requested portrait, square, frame rate, resolution, or silent format instead when specified. Keep editable source alongside the export. HTML alone does not satisfy a request for an MP4.

Check the final decoded file, duration, dimensions, frame rate, codecs, audio presence, first and last frames, and scene boundaries. Technical inspection, sampled frames, and full audiovisual review are separate checks. State exactly which checks were performed and what remains unverified. If export or playback tools are unavailable, deliver the useful completed parts with that specific limitation. Never imply a missing MP4 exists. See [review-and-export.md](references/review-and-export.md).

Finish when the brief is met and significant defects are fixed. Do not turn optional taste alternatives into endless iterations. Deliver the video path, editable-source path, concise verification status, and any material limitations.

## Conditional production references

- Real product screens, cursor choreography, and interface states: [product-ui.md](references/product-ui.md).
- Multiple visual references, consistent characters, alpha, and 3D assets: [assets-and-references.md](references/assets-and-references.md).
- Working documents: [assets/templates](assets/templates). Choose English or Ukrainian templates.

The package contains instructions and templates. Use the host agent's available tools to create and render the film; do not claim the skill itself supplies a renderer, media library, or video-editor integration.
