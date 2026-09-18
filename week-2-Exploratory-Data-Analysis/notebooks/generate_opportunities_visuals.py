import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 1. Load Data
df = pd.read_csv(r'C:\Users\intel\Desktop\Datasets\cleaned_opportunities.csv')

# Global Theme Settings
card_bg = '#FFFFFF'
canvas_bg = '#F4F6F9'
border_color = '#E2E8F0'
text_muted = '#64748B'
text_dark = '#0F172A'
top_cats = df['category'].value_counts().head(6).index

plt.rcParams['font.family'] = 'sans-serif'


def format_spines(ax):
  ax.set_facecolor(card_bg)
  for spine in ax.spines.values():
    spine.set_color(border_color)
  ax.grid(True, linestyle='--', alpha=0.4, color='#CBD5E1')
  ax.tick_params(colors=text_muted, labelsize=10)


# ==============================================================================
# Visual 1: Monthly Opportunity Creation Trajectory
# ==============================================================================

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

# ==============================================================================
# Visual 2: Program Duration Distribution
# ==============================================================================
fig, ax = plt.subplots(figsize=(10, 6), facecolor=canvas_bg)
format_spines(ax)

clean_dur = df[
    (df['duration_standard_days'] > 0) & (df['duration_standard_days'] <= 365)
]['duration_standard_days']
sns.histplot(
    clean_dur,
    bins=30,
    kde=True,
    color='#0D9488',
    ax=ax,
    edgecolor='#0F766E',
    alpha=0.6,
)

ax.set_title(
    'Program Duration Distribution (≤ 1 Year)',
    fontsize=14,
    fontweight='bold',
    color=text_dark,
    pad=15,
)
ax.set_xlabel(
    'Duration (Standard Days)', fontsize=11, fontweight='600', color=text_muted
)
ax.set_ylabel(
    'Opportunity Frequency', fontsize=11, fontweight='600', color=text_muted
)

plt.tight_layout()
plt.savefig(
    'visual_2_duration_distribution.png',
    dpi=300,
    bbox_inches='tight',
    facecolor=canvas_bg,
)
plt.close()
print('✓ Saved: visual_2_duration_distribution.png')

# ==============================================================================
# Visual 3: Approval Protocol by Category (100% Stacked Bar)
# ==============================================================================
fig, ax = plt.subplots(figsize=(10, 6), facecolor=canvas_bg)
format_spines(ax)

sub_df = df[df['category'].isin(top_cats)]
crosstab_approval = (
    pd.crosstab(
        sub_df['category'], sub_df['is_auto_approve'], normalize='index'
    )
    * 100
).reindex(top_cats)

crosstab_approval.plot(
    kind='barh', stacked=True, color=['#64748B', '#10B981'], ax=ax, width=0.6
)
ax.set_title(
    'Application Approval Protocol by Category (%)',
    fontsize=14,
    fontweight='bold',
    color=text_dark,
    pad=15,
)
ax.set_xlabel(
    'Percentage Share (%)', fontsize=11, fontweight='600', color=text_muted
)
ax.set_ylabel('')
ax.legend(
    ['Manual Review', 'Auto-Approve'],
    loc='lower right',
    frameon=True,
    facecolor='#FFFFFF',
    edgecolor='#CBD5E1',
    fontsize=10,
)

plt.tight_layout()
plt.savefig(
    'visual_3_approval_protocol.png',
    dpi=300,
    bbox_inches='tight',
    facecolor=canvas_bg,
)
plt.close()
print('✓ Saved: visual_3_approval_protocol.png')

# ==============================================================================
# Visual 4: Currency Denomination Breakdown
# ==============================================================================
fig, ax = plt.subplots(figsize=(10, 6), facecolor=canvas_bg)
format_spines(ax)

curr_filtered = df[
    df['category'].isin(top_cats)
    & df['currency_type'].isin(['USD', 'INR', 'EUR'])
]
crosstab_curr = pd.crosstab(
    curr_filtered['category'], curr_filtered['currency_type']
).reindex(top_cats)

crosstab_curr.plot(
    kind='bar',
    color=['#3B82F6', '#F59E0B', '#EC4899'],
    ax=ax,
    width=0.75,
    rot=20,
)
ax.set_title(
    'Currency Denomination Mix Across Top Categories',
    fontsize=14,
    fontweight='bold',
    color=text_dark,
    pad=15,
)
ax.set_ylabel(
    'Opportunity Count', fontsize=11, fontweight='600', color=text_muted
)
ax.set_xlabel('')
ax.legend(
    title='Currency',
    frameon=True,
    facecolor='#FFFFFF',
    edgecolor='#CBD5E1',
    fontsize=10,
)

plt.tight_layout()
plt.savefig(
    'visual_4_currency_mix.png',
    dpi=300,
    bbox_inches='tight',
    facecolor=canvas_bg,
)
plt.close()
print('✓ Saved: visual_4_currency_mix.png')

print('\nAll 4 individual high-res PNG visuals generated successfully!')
