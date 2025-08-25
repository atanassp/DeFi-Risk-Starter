import pandas as pd
import matplotlib.pyplot as plt

# Dummy data: Replace with real DeFi stats later
data = {
    'Protocol': ['Aave', 'Maker'],
    'FINMA_Score': [80, 70],
    'TVL_USD': [5000000000, 8000000000]
}
df = pd.DataFrame(data)

# Risk score: Inverse of compliance and TVL
df['Risk_Score'] = 100 - df['FINMA_Score'] + (df['TVL_USD'].max() - df['TVL_USD']) / 1e9

# Plot
plt.bar(df['Protocol'], df['Risk_Score'], color='#FF4500')
plt.title('DeFi Risk by Swiss Regs')
plt.ylabel('Risk Score')
plt.savefig('risk_plot.png')
plt.show()

print(df)
