# Changelog

## 1.0.1 — 2026-09-30

- Codex support: `.codex-plugin/plugin.json` and `.agents/plugins/marketplace.json`. Install with `codex plugin marketplace add xiongqi123123/PaperDNA` and `codex plugin add paperdna@paperdna`.
- The skill moved to `skills/paperdna/` so Claude Code and Codex share one copy. The Claude Code command is still `/paperdna:paperdna`.
- The personal profile falls back to `~/.paperdna/profile/` when `${CLAUDE_PLUGIN_DATA}` is not available (for example in Codex).
- Added a square icon (`asset/paperdna_icon.png`).

## 1.0.0 — 2026-09-30

- First release as a Claude Code plugin: `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`. Install with `/plugin marketplace add xiongqi123123/PaperDNA` and `/plugin install paperdna@paperdna`.
- Writing guidance distilled from 1040 CVPR 2026 / ICCV 2025 award, oral and highlight papers: story types, six section guides, sentence bank, word choice and style, naming, and corpus statistics.
- Press-release principle against defensive writing (adapted from anti-defensive-writing-Skill, MIT).
- Personal profile kept in the plugin's data directory; personal word list read by the scanner through `--extra`.
