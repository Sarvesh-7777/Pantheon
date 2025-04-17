import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# RTT data (based on your table)
data = {
    'Scheme': ['BBR', 'Cubic', 'Vegas', 'BBR', 'Cubic', 'Vegas'],
    'Latency': ['High', 'High', 'High', 'Low', 'Low', 'Low'],
    'RTT': [119.89  ,120.30,  105.63 ,131.71,1372.64, 54.70]
}


df = pd.DataFrame(data)

# Plot settings
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Scheme', y='RTT', hue='Latency', palette='muted')

# Labels and title
plt.title('95th Percentile RTT by Congestion Control Scheme')
plt.ylabel('95th Percentile RTT (ms)')
plt.xlabel('Congestion Control Scheme')
plt.tight_layout()

# Save plot
plt.savefig("rtt_comparison_plot.png", dpi=300)
plt.show()
