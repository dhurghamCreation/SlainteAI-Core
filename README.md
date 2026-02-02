# SlainteAI: Clinical Sepsis Triage Audit Tool

SlainteAI is a Retrieval-Augmented Generation (RAG) system designed to audit clinical sepsis triage decisions for gender bias, based on the **HSE National Clinical Guideline No. 26 (2025/2026 Update)**.

##  Key Features
- **Grounded AI:** Uses FAISS and HuggingFace Local Embeddings to ensure triage logic stays strictly within HSE guidelines.
- **Bias Mitigation:** Implements custom prompt engineering to prevent automatic maternity-bias in female patient triage.
- **Automated Audit:** Includes a batch testing suite that generates side-by-side fairness comparisons.

##  Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/dhurghamCreation/SlainteAI-Core.git](https://github.com/dhurghamCreation/SlainteAI-Core.git)
##  Future Roadmap: SlainteAI v2.0
To transition this audit tool into a clinical decision support system, the following milestones are planned:

* **Expanded Clinical Breadth:** Integration of HSE Pediatric Sepsis (Guideline No. 14) and Geriatric-specific screening tools to account for baseline physiological differences in elderly patients.
* **EHR Integration (FHIR):** Transitioning from CSV-based batch auditing to a real-time REST API capable of integrating with hospital systems via HL7/FHIR standards.
* **Antimicrobial Stewardship:** Cross-referencing sepsis triggers with local HSE antibiotic guidelines to suggest appropriate first-line therapy while minimizing broad-spectrum resistance.
