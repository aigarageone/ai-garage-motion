<div align="center">

# AI Garage Motion

### Direct the idea. Build the motion. Finish the film.

A motion design skill for AI coding agents.<br>
From a rough idea to a storyboard, expressive animation, sound, and a reviewed video export.

**English** · [Українською](README.uk.md)

[Download the skill](https://github.com/aigarageone/ai-garage-motion/releases/latest/download/ai-garage-motion.zip) · [Start here](docs/GUIDE.md) · [Prompt examples](docs/PROMPTS.md)

</div>

---

You bring the idea. **AI Garage brings the workflow.**

Give your coding agent a clear way to direct and finish motion videos: develop the concept, plan each scene, build purposeful movement, shape the sound, review the draft, and deliver the actual export.

Use it for product explainers, launch videos, kinetic typography, interface animations, social clips, and visual stories. The agent works in English or Ukrainian, with the creative brief setting the language, format, and style.

## What you get

| Inside | What it helps you do |
| --- | --- |
| **AI Garage Motion skill** | Follow a complete production workflow, from concept to delivery |
| **Production references** | Direct scenes, camera, typography, sound, UI, characters, and assets |
| **English + Ukrainian guide** | Install the skill and make your first request |
| **Ready-to-use prompts** | Start with an idea, a product screen, or a reference video |
| **Project templates** | Keep the brief, storyboard, review, and delivery notes together |
| **Local installer** | Copy the skill into Claude Code or Codex without overwriting an existing install |

The package is a skill: instructions and small planning tools. Your agent uses its available animation and export tools to create the video. Video rendering can require additional software; paid AI services or licensed media may have separate costs. No API keys or paid service are required to install the skill.

## Install in a minute

You need a supported coding agent. The installer requires Python 3.9 or later. Git is needed only for the clone method; you can also download this repository with **Code → Download ZIP** and extract it.

```bash
git clone https://github.com/aigarageone/ai-garage-motion.git
cd ai-garage-motion
```

**Claude Code — all local projects**

```bash
python3 scripts/install.py --tool claude --scope user
```

**Codex — all local projects**

```bash
python3 scripts/install.py --tool codex --scope user
```

On Windows, use `py -3` instead of `python3`. The installer copies local files only. It does not install render software, configure an MCP server, send data, or change agent permissions. Existing installations are preserved; see the [guide](docs/GUIDE.md) for project-only installation, manual copying, updates, and troubleshooting.

Open a new agent session in your video project and invoke the skill:

| Agent | Invocation |
| --- | --- |
| Claude Code | `/ai-garage-motion` |
| Codex | `$ai-garage-motion` |

Then describe the video:

> Create a 15-second motion video about turning scattered ideas into a clear plan. Use English copy, 1920×1080, 60 fps, expressive typography, music, and synchronized sound design. Develop the storyboard, build and review the animation, and export an MP4 with editable source. Use original abstract shapes and no external assets.

## How the work flows

1. **Find the idea.** Define one message and a visual transformation that carries it.
2. **Direct the scenes.** Explore distinct options and build a timed storyboard.
3. **Build the motion.** Give type, camera, objects, and transitions a shared purpose.
4. **Shape the sound.** Connect music and effects to meaningful events.
5. **Review and refine.** Watch the draft, fix material issues, and check the final file.
6. **Deliver.** Share the MP4, editable source, and a clear record of what was verified.

Your brief overrides defaults. Ask for portrait, square, 4K, silence, a particular duration, or an existing project stack when that is what you need. The default target is a 1920×1080, 60 fps MP4 with H.264 video and AAC audio when sound is requested.

## Download, inspect, share

- [Skill ZIP](https://github.com/aigarageone/ai-garage-motion/releases/latest/download/ai-garage-motion.zip) — a single `ai-garage-motion/` folder, ready to copy or upload where custom skill ZIPs are supported.
- [English guide](docs/GUIDE.md) · [Український гід](docs/GUIDE.uk.md).
- [English prompts](docs/PROMPTS.md) · [Приклади українською](docs/PROMPTS.uk.md).
- [Read the skill](skills/ai-garage-motion/SKILL.md) · [Навичка українською](skills/ai-garage-motion/references/skill.uk.md).
- [Share this introduction](docs/SHARE.md).

Only the skill folder is installed. There are no bundled customer projects, private media, service credentials, or required third-party integrations. The installer has no network calls, telemetry, background processes, or package installation.

## Open source

Published by **AI Garage** under the [MIT License](LICENSE). You can use, adapt, and share the package, including commercially, while retaining the license notice. External media and services keep their own terms. The license grants no endorsement or exclusive rights to the AI Garage name.

For contributors: [package checks and release commands](docs/MAINTAINING.md).
