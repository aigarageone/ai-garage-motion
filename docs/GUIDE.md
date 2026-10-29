# Your first motion video with AI Garage

[Українською](GUIDE.uk.md) · [Home](../README.md)

Start with an idea you can say in one sentence. Install the skill, open your coding agent in a working folder, and describe the film. AI Garage Motion supplies the production workflow; your agent supplies the available coding, animation, audio, and export tools.

## 1. Choose how to install

### Repository + local installer

Install Python 3.9+ if you do not already have it. Download the repository using **Code → Download ZIP**, extract it, and open a terminal in the extracted repository folder. Alternatively:

```bash
git clone https://github.com/aigarageone/ai-garage-motion.git
cd ai-garage-motion
```

Choose one command:

```bash
# Claude Code: all local projects
python3 scripts/install.py --tool claude --scope user

# Codex: all local projects
python3 scripts/install.py --tool codex --scope user
```

For a single existing project, use its path instead:

```bash
python3 scripts/install.py --tool claude --scope project --project /path/to/your-project
python3 scripts/install.py --tool codex --scope project --project /path/to/your-project
```

Run only the command for the agent you use, or both if you use both. On Windows, replace `python3` with `py -3` and use your own quoted project path, such as `"C:\Projects\motion-demo"`. Add `--dry-run` to inspect the intended location without writing files.

### Skill ZIP + manual copying

Download [ai-garage-motion.zip](https://github.com/aigarageone/ai-garage-motion/releases/latest/download/ai-garage-motion.zip) and extract it. Copy the complete `ai-garage-motion` folder into one of these locations:

| Agent | This project only | All your local projects |
| --- | --- | --- |
| Claude Code | `.claude/skills/ai-garage-motion/` | `~/.claude/skills/ai-garage-motion/` |
| Codex | `.agents/skills/ai-garage-motion/` | `~/.agents/skills/ai-garage-motion/` |

`~` means your home directory. The final file must be exactly `.../ai-garage-motion/SKILL.md`, with `references/`, `scripts/`, `assets/`, and `agents/` beside it. Do not copy only `SKILL.md` or leave an extra nested `ai-garage-motion/ai-garage-motion/` folder.

The ZIP can also be uploaded where your agent supports custom skill ZIPs. In Claude's web/desktop settings, use **Customize → Skills** and the custom-skill upload option, then enable the skill. The interface may vary by account and version. Local Claude Code folders do not automatically install the skill into Cowork or cloud sessions; use the account's enabled custom skills for those environments. Available tools and render limits can differ.

The generic manual route for another agent is to read its official skill documentation and copy the same folder into its supported location. The package does not claim a native video-editor plugin or universal agent compatibility.

## 2. Confirm the skill is available

Open a new session in your video project. In Claude Code, invoke `/ai-garage-motion`; in Codex, invoke `$ai-garage-motion` or select it from the available skills. Ask:

> Use AI Garage Motion. Confirm that you can read its SKILL.md and production references, then summarize the workflow before we begin.

If it is missing, inspect the exact folder path and nesting, start a new session, and check whether your organization limits custom skills. See the current official [Claude Code skill documentation](https://code.claude.com/docs/en/skills) and [Codex skill documentation](https://developers.openai.com/codex/skills/). Installation paths were checked on 29 October 2026.

## 3. Give the agent a useful brief

A good first request contains the idea, language, duration, shape, and sound preference:

```text
Use AI Garage Motion to create a 15-second video about turning scattered
ideas into a clear plan. Copy: "Less noise. More direction."
English, landscape 1920×1080, 60 fps. Use original abstract shapes,
expressive typography, music, and synchronized sound design. No voice.
Develop the concept and timed storyboard, test the hardest transition,
build the animation, review the full draft, fix significant issues,
and deliver an MP4 with editable source. Use available local tools.
Ask before any new paid service or external upload.
```

Do not need a technical production plan? The agent can choose the implementation. Need a specific engine, style, font, or existing project? Say so. Provide approved logos, product screenshots, and exact copy when they matter. If you want an intermediate approval, explicitly request a storyboard or preview checkpoint.

## 4. Keep a small project record

Optional: from this repository, create planning documents in a new folder:

```bash
python3 skills/ai-garage-motion/scripts/new_project.py ./my-motion-project --language en
```

The same helper lives inside the installed skill. It creates `BRIEF.md`, `STORYBOARD.md`, `REVIEW.md`, and `DELIVERY.md`. It refuses an existing destination and does not generate media or install dependencies. Keep source assets, generated masters, and exports in locations suitable for your project's disk budget.

## 5. Know what completion means

Expect the concept and timed storyboard, a preview of the main risk, a complete draft followed by corrections, the requested video file, and editable source with reproduction instructions. The delivery should identify actual checks, rather than treating a rendered file as automatically reviewed.

If the environment lacks a renderer, encoder, audio tool, or playback capability, the agent should name the missing step and deliver the completed parts. An HTML preview is useful but does not replace a requested MP4. Static screenshots do not prove smooth motion; audio metadata does not prove listening.

For code-driven export, deterministic frame capture and an encoder such as FFmpeg may be needed. The skill does not install them automatically or include third-party media. The [export reference](../skills/ai-garage-motion/references/review-and-export.md) explains the delivery checks and example commands.

## Updates and privacy

The installer refuses to overwrite an existing skill. Compare the new files with your installed version and preserve local edits before replacing it manually. No automatic updater is installed.

Installation is local and contains no telemetry or network requests. Your agent and any media service you choose still have their own data policies. Review screenshots and supplied assets before using them in a public film. Store API keys outside this repository and outside deliverable source packages.

Continue with [ready-to-use prompts](PROMPTS.md) or [share the guide](SHARE.md).
