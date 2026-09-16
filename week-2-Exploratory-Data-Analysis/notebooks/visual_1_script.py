import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
df = pd.read_csv(r'C:\Users\intel\Desktop\Datasets\cleaned_opportunities.csv')

# Configure Figure & Palette
plt.rcParams['font.family'] = 'sans-serif'
fig, ax = plt.subplots(figsize=(12, 6), facecolor='#F4F6F9')
ax.set_facecolor('#FFFFFF')

for spine in ax.spines.values():
  spine.set_color('#CBD5E1')

# Aggregate monthly postings using 'ME' (Month End)
df['created_dt'] = pd.to_datetime(df['created_at'], errors='coerce')
monthly = (
    df.set_index('created_dt').resample('ME')['opportunity_id'].count().dropna()
)

# Plot Trajectory Area
ax.plot(
    monthly.index,
    monthly.values,
    color='#2563EB',
    lw=2.5,
    marker='o',
    markersize=5,
)
ax.fill_between(monthly.index, monthly.values, color='#93C5FD', alpha=0.3)

# Title & Typography
ax.set_title(
    'Monthly Opportunity Creation Trajectory',
    fontsize=15,
    fontweight='bold',
    color='#0F172A',
    pad=15,
)
ax.set_ylabel(
    'New Postings / Cohorts', fontsize=11, fontweight='bold', color='#475569'
)
ax.set_xlabel('Created Date', fontsize=11, fontweight='bold', color='#475569')
ax.set_ylim(0, 1150)
ax.grid(True, linestyle='--', alpha=0.5, color='#E2E8F0')
ax.tick_params(colors='#475569', labelsize=10)

# 4-Month Interval Date Formatting
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=4))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
fig.autofmt_xdate(rotation=30)

plt.tight_layout()
plt.savefig(
    'visual_1_timeline_trajectory.png',
    dpi=300,
    bbox_inches='tight',
    facecolor='#F4F6F9',
)
print('✓ Saved cleanly: visual_1_timeline_trajectory.png')
plt.show()
