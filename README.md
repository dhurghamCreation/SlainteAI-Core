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
