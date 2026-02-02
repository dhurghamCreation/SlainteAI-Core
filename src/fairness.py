import pandas as pd
from fairlearn.metrics import MetricFrame, selection_rate
from sklearn.metrics import accuracy_score

def check_bias():
    # Load the synthetic clinical data
    df = pd.read_csv('data/audit_sample.csv')
    
    metrics = {"accuracy": accuracy_score, "selection_rate": selection_rate}
    
    # Check fairness by Gender
    mf = MetricFrame(
        metrics=metrics,
        y_true=df['actual_priority'],
        y_pred=df['ai_priority'],
        sensitive_features=df['gender']
    )
    print("--- Bias Audit Results ---")
    print(mf.by_group)

if __name__ == "__main__":
    check_bias()
    