---
name: AI-Vibe-Writing-Skills
description: Use this skill for style-aware writing, paper or thesis drafting, outline-first long-form writing, AI-tone reduction, reference-learning, and PDF-to-evidence ingestion within this workspace. It provides a spec-driven workflow plus local prompts, memory files, and PDF utilities.
---

# AI Vibe Writing Skills

Use this skill when the user wants any of the following:

- Write or rewrite content in a personalized style
- Draft papers, theses, grants, reports, or long-form technical writing
- Build an outline before writing
- Reduce "AI tone" and enforce writing constraints
- Learn from references and store reusable facts or style preferences
- Read a PDF and turn it into structured evidence for writing

## Core workflow

Follow this order unless the user explicitly asks for a narrower task:

1. Define the target in `.ai_context/custom_specs.md` and, for substantial writing, create or update a document spec from `.ai_context/document_spec_template.md`.
2. For long-form writing, create an outline using `.ai_context/outline_template.md`.
3. Read style and memory inputs before drafting:
   - `.ai_context/style_profile.md`
   - `.ai_context/error_log.md`
   - `.ai_context/memory/hard_memory.json`
   - `.ai_context/memory/soft_memory.json`
4. Draft or revise using the relevant prompt in `.ai_context/prompts/`.
5. Review for spec compliance, evidence coverage, and AI-tone issues.
6. If the user corrects wording or facts, write the correction back into the relevant memory or log file.

## Task routing

Pick the narrowest relevant prompt file from `.ai_context/prompts/`:

- `1_style_extractor.md`: infer style from prior writing samples
- `2_writer.md`: general drafting and rewriting
- `3_error_logger.md`: convert user corrections into negative constraints
- `4_grammar_checker.md`: grammar and spelling fixes with minimal rewriting
- `5_long_term_memory.md`: store durable facts and preferences
- `6_outline_manager_agent.md`: outline generation and validation
- `7_content_writer_agent.md`: section drafting under outline constraints
- `8_content_review_agent.md`: AI-tone and quality review
- `9_workflow_coordinator.md`: full outline -> draft -> review loop
- `10_pdf_reader_agent.md`: PDF reading and evidence extraction
- `11_context_compactor_agent.md`: compress long context when the thread gets large
- `12_router_agent.md`: route by section type or writing mode
- `13_latex_self_healing_agent.md`: fix LaTeX compilation issues when the task includes TeX

Read only the prompt files needed for the current request.

## Reference learning

When the user provides papers, notes, or citations to learn from:

1. Extract claims, terminology, data points, and reusable style features.
2. Store stable facts in `.ai_context/memory/hard_memory.json`.
3. Store style preferences in `.ai_context/memory/soft_memory.json`.
4. Store literature records in `.ai_context/memory/reference_library.json`.
5. Use `.ai_context/reference_learning.md` for the ingestion pattern.

## PDF ingestion

Use this path when the user wants to process PDFs:

1. Read `.ai_context/pdf_ingestion_template.md`.
2. If lightweight extraction is enough, use `.ai_context/scripts/parse_pdf.py`.
3. If MinerU is explicitly needed, use local helpers:
   - `run_magic_pdf.py`
   - `create_pdf.py`
   - `mineru_gui.py`
   - `magic-pdf.json`
   - `configs/layoutlmv3_base_inference.yaml`
4. Convert extracted content into structured notes and then into memory or reference entries.

## Working rules

- For long or high-stakes documents, do not skip the spec step.
- Prefer outline-first writing for anything longer than a short section.
- Grammar review should preserve the author's intent unless the user asks for rewriting.
- If a large rewrite is needed, present the revision plan first.
- If evidence is required, do not invent citations or unsupported claims.
- When updating memory files, preserve existing structure and append only justified entries.

## Local resources

Use these files as the skill's local resources, not as user-facing docs:

- `.ai_context/`: prompts, templates, style, memory, and reference workflow
- `.agents/workflows/ai_vibe_writing.md`: end-to-end writing workflow
- `.agents/workflows/pdf_ingestion.md`: PDF ingestion workflow
- `Local_AI_Style_Check/`: local AI-style checking utilities

Ignore `README.md` unless you need background context that is missing from the files above.
