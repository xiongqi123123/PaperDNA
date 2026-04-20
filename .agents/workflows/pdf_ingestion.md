---
description: Automatically ingest a PDF document and update the reference library
---

# PDF Ingestion Workflow

This workflow automates the process of reading a local or remote PDF document, extracting evidence, and updating the user's reference library and long-term memory.

## Steps

1. **Analyze the Input**:
   - Identify if the user provided a local PDF file path or an online URL.
   - Read `.ai_context/custom_specs.md` to understand the `PDF Reading Settings` (e.g., Target Domain, Citation Formatting).
   - Read `.ai_context/pdf_ingestion_template.md` to understand the required extraction format.

2. **Parse the PDF**:
   - If it's an online URL, use standard web reading tools (e.g., `read_url_content`).
   - If it's a local file, you can extract the text using an available utility. If none exists, invoke `.ai_context/scripts/parse_pdf.py` on the provided local PDF path to gain a structured markdown representation of the text.
   - Wait for the text to be fully extracted.

3. **Execute PDF Reader Agent Logic**:
   - Read `.ai_context/prompts/10_pdf_reader_agent.md`.
   - Act as the PDF Reader Agent. Process the extracted text.
   - Summarize the core points: abstract, methods, results, and limitations.
   - Extract robust facts, data points, and terminologies.

4. **Update the Knowledge Base**:
   - **Reference Library**: Append a new entry to `.ai_context/memory/reference_library.json` containing the extracted summary, citation format, and key points.
   - **Hard Memory**: Append newly discovered concrete terminologies, units, or indisputable facts to `.ai_context/memory/hard_memory.json`.
   - **Soft Memory**: Append newly discovered author writing preferences or subjective style notes to `.ai_context/memory/soft_memory.json`.

5. **Report to User**:
   - Present a brief summary of the ingested PDF (Title, Authors, Abstract snippet) and confirm the reference library has been updated.
