import time
import pandas as pd
from src.model import run_slainte_ai  # Assuming your main function is here
from data.test_cases import vignettes, format_question

def run_batch_audit():
    results = []
    
    print(f"--- Starting Audit of {len(vignettes)} Cases ---")
    
    for case in vignettes:
        print(f"Auditing Case #{case['id']}...")
        query = format_question(case)
        
        # Run your AI model
        response = run_slainte_ai(query)
        
        # Extract the decision (High/Low) from the text
        # Simple extraction logic looking for keywords
        decision = "Low/Medium"
        if "Category 2" in response['result'] or "High Priority" in response['result']:
            decision = "High Priority (Cat 2)"
            
        results.append({
            "ID": case['id'],
            "Gender": case['gender'],
            "Symptoms": case['symptoms'],
            "AI_Decision": decision,
            "Logic_Snippet": response['result'][:150] + "..."
        })
        print("Waiting 7 seconds to avoid API Rate Limit...")
        time.sleep(7)
    # Create the Comparison Table
    
    df = pd.DataFrame(results)
    # Save to CSV for your project report
    df.to_csv("audit_results.csv", index=False)
    
    print("\n--- BATCH AUDIT COMPLETE ---")
    print(df[["ID", "Gender", "AI_Decision"]]) # Show summary table

if __name__ == "__main__":
    run_batch_audit()