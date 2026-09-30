# Changelog

## 1.2.0 — 2026-09-30

- Citation modes, chosen once per paper and stored in `.paperdna/spec.md` (asked the first time PaperDNA writes the paper or first needs a citation). See `skills/paperdna/references/literature.md` §5.
  - A: Claude searches Semantic Scholar / arXiv / Crossref, fetches BibTeX from DOI, CVF or arXiv pages, and an independent subagent checks every new entry for fake citations (does not exist, wrong metadata) and hallucinated citations (the paper does not support the sentence citing it). Entries that fail are removed or turned into TODOs.
  - B: Claude writes `\cite{TODO:<key>}` placeholders, tells the user which papers to cite and why, and the user pastes the BibTeX.
- Updated the citation hard rule in `SKILL.md`, the spec template, the workflow and the review criteria.

## 1.1.0 — 2026-09-30

- Writing order: Method → Experiments → Conclusion → Introduction and Related Work → Abstract (`skills/paperdna/references/workflow.md` §3, also a hard rule in `SKILL.md`).
- Cross-reference rules: Method never references experiments (no "ablated in Sec. 4.3", no result numbers); Introduction never references method or experiment sections, tables or figures (Figure 1 excepted) and has no paper-organization paragraph. Main results may still appear in the Introduction as plain numbers.
- Removed guidance that contradicted these rules from the method, experiments, introduction and story-type guides; added checks to the review criteria and the introduction checklist.

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
