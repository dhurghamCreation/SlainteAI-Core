import pandas as pd
import matplotlib.pyplot as plt

def create_bias_chart():
    # 1. Load the results from your batch audit
    try:
        df = pd.read_csv('audit_results.csv')
    except FileNotFoundError:
        print("Error: audit_results.csv not found. Run your batch audit script first!")
        return

    # 2. Convert text decisions to numbers (1 for High Priority, 0 for Low/Medium)
    df['Is_High'] = df['AI_Decision'].apply(
        lambda x: 1 if 'High Priority' in str(x) else 0
    )

    # 3. Calculate the percentage of High Priority decisions by Gender
    # This is known as the 'Selection Rate'
    stats = df.groupby('Gender')['Is_High'].mean() * 100

    # 4. Create the Bar Chart
    plt.figure(figsize=(10, 6))
    
    # Assign colors: Coral for Female, SkyBlue for Male
    colors = ['#ff7f50' if g == 'Female' else '#87ceeb' for g in stats.index]
    
    bars = plt.bar(stats.index, stats.values, color=colors, edgecolor='black')

    # 5. Add Labels and Title
    plt.ylabel('High Priority Selection Rate (%)')
    plt.xlabel('Patient Gender')
    plt.title('SlainteAI Fairness Audit: High Priority Triage by Gender\n(Based on 102°F Fever Scenarios)')
    plt.ylim(0, 100) # Keep scale consistent at 0-100%
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Add the percentage text on top of each bar
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 2, f'{yval:.1f}%', 
                 ha='center', va='bottom', fontweight='bold')

    # 6. Save the chart for your presentation
    plt.savefig('bias_audit_chart.png')
    print("--- Success: Bias chart saved as 'bias_audit_chart.png' ---")

if __name__ == "__main__":
    create_bias_chart()