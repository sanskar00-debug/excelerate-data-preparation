import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1. Load Dataset
df = pd.read_csv('cleaned_opportunities.csv')

# Global Theme Settings
card_bg = '#FFFFFF'
canvas_bg = '#F4F6F9'
border_color = '#E2E8F0'
text_muted = '#64748B'
text_dark = '#0F172A'
top_cats = df['category'].value_counts().head(8).index

plt.rcParams['font.family'] = 'sans-serif'


def format_spines(ax):
  ax.set_facecolor(card_bg)
  for spine in ax.spines.values():
    spine.set_color(border_color)
  ax.grid(True, linestyle='--', alpha=0.4, color='#CBD5E1', axis='x')
  ax.tick_params(colors=text_dark, labelsize=10)


# ==============================================================================
# Visual 1: Program Duration Unit Breakdown (Lollipop Chart)
# ==============================================================================
fig, ax = plt.subplots(figsize=(10, 6), facecolor=canvas_bg)
format_spines(ax)

dur_counts = df['duration_type'].value_counts().sort_values(ascending=True)
y_pos = range(len(dur_counts))
ax.hlines(
    y=y_pos, xmin=0, xmax=dur_counts.values, color='#93C5FD', lw=3, zorder=2
)
ax.scatter(dur_counts.values, y_pos, color='#2563EB', s=160, zorder=3)

total_valid_dur = len(df.dropna(subset=['duration_type']))
for y, val in zip(y_pos, dur_counts.values):
  pct = (val / total_valid_dur) * 100
  ax.text(
      val + 55,
      y,
      f'{val:,} ({pct:.1f}%)',
      va='center',
      fontsize=9.5,
      fontweight='bold',
      color=text_dark,
  )

ax.set_yticks(y_pos)
ax.set_yticklabels(
    [str(x).capitalize() for x in dur_counts.index],
    fontsize=10.5,
    fontweight='bold',
    color=text_dark,
)
ax.set_xlim(0, 4900)
ax.set_title(
    '1. Program Structuring: Duration Measurement Units',
    fontsize=14,
    fontweight='bold',
    color=text_dark,
    pad=15,
)
ax.set_xlabel(
    'Number of Programs', fontsize=11, fontweight='600', color=text_muted
)
plt.tight_layout()
plt.savefig(
    'visual_1_duration_units.png',
    dpi=300,
    bbox_inches='tight',
    facecolor=canvas_bg,
)
plt.close()
print('✓ Saved: visual_1_duration_units.png')

# ==============================================================================
# Visual 2: Monetization Model: Free vs. Paid Access (100% Stacked)
# ==============================================================================
fig, ax = plt.subplots(figsize=(10, 6), facecolor=canvas_bg)
format_spines(ax)

cat_df = df[df['category'].isin(top_cats)].copy()
cat_df['Pricing Tier'] = np.where(
    cat_df['fee'] > 0, 'Paid Program', 'Free Access'
)
ct_monetize = (
    pd.crosstab(
        cat_df['category'], cat_df['Pricing Tier'], normalize='index'
    )
    * 100
)
ct_monetize = (
    ct_monetize[['Free Access', 'Paid Program']].reindex(top_cats).iloc[::-1]
)

ct_monetize.plot(
    kind='barh', stacked=True, color=['#0D9488', '#F59E0B'], ax=ax, width=0.62
)
for c in ax.containers:
  labels = [f'{w:.1f}%' if w > 5 else '' for w in c.datavalues]
  ax.bar_label(
      c,
      labels=labels,
      label_type='center',
      color='white',
      fontweight='bold',
      fontsize=9,
  )

ax.set_title(
    '2. Monetization Strategy: Free Access vs. Paid by Category',
    fontsize=14,
    fontweight='bold',
    color=text_dark,
    pad=15,
)
ax.set_xlabel(
    'Proportion (%)', fontsize=11, fontweight='600', color=text_muted
)
ax.set_ylabel('')
ax.legend(
    ['Free Access (Fee = $0)', 'Paid Tier (Fee > $0)'],
    loc='lower center',
    bbox_to_anchor=(0.5, -0.2),
    ncol=2,
    frameon=True,
    facecolor=card_bg,
    edgecolor=border_color,
)
plt.tight_layout()
plt.savefig(
    'visual_2_monetization_split.png',
    dpi=300,
    bbox_inches='tight',
    facecolor=canvas_bg,
)
plt.close()
print('✓ Saved: visual_2_monetization_split.png')

# ==============================================================================
# Visual 3: Micro-Scholarship Inclusion Benchmark
# ==============================================================================
fig, ax = plt.subplots(figsize=(10, 6), facecolor=canvas_bg)
format_spines(ax)

schol_pct = (
    cat_df.groupby('category')['microscholarship']
    .apply(lambda x: (x > 0).mean() * 100)
    .reindex(top_cats)
    .sort_values()
)
bars = ax.barh(
    schol_pct.index,
    schol_pct.values,
    color='#6366F1',
    height=0.55,
    edgecolor='#4338CA',
)

for bar in bars:
  w = bar.get_width()
  ax.text(
      w + 1.2,
      bar.get_y() + bar.get_height() / 2,
      f'{w:.1f}%',
      va='center',
      fontsize=9.5,
      fontweight='bold',
      color=text_dark,
  )

ax.set_xlim(0, 110)
ax.set_title(
    '3. Micro-Scholarship Inclusion Rate by Category',
    fontsize=14,
    fontweight='bold',
    color=text_dark,
    pad=15,
)
ax.set_xlabel(
    '% Opportunities Offering Micro-Scholarship',
    fontsize=11,
    fontweight='600',
    color=text_muted,
)
ax.set_ylabel('')
plt.tight_layout()
plt.savefig(
    'visual_3_scholarship_rate.png',
    dpi=300,
    bbox_inches='tight',
    facecolor=canvas_bg,
)
plt.close()
print('✓ Saved: visual_3_scholarship_rate.png')

# ==============================================================================
# Visual 4: Feature & Add-On Adoption Rate
# ==============================================================================
fig, ax = plt.subplots(figsize=(10, 6), facecolor=canvas_bg)
format_spines(ax)

features = {
    'Student Testimonial': (df['Testimonial_clean_id'].notna()).mean() * 100,
    'Career Add-On': (df['CareerAddOn_clean_id'].notna()).mean() * 100,
    'Reward / Incentive': (df['Reward_clean_id'].notna()).mean() * 100,
    'Panelist / Mentor': (df['Panellist_clean_id'].notna()).mean() * 100,
    'Active Cohort': (df['Cohort_clean_id'].notna()).mean() * 100,
    'Eligibility Criteria': (df['Eligibility_clean_id'].notna()).mean() * 100,
    'Digital Badge': (df['Badge_clean_id'].notna()).mean() * 100,
}
s_feat = pd.Series(features)
colors = [
    '#EF4444',
    '#F97316',
    '#F59E0B',
    '#10B981',
    '#06B6D4',
    '#3B82F6',
    '#6366F1',
]
bars = ax.barh(
    s_feat.index, s_feat.values, color=colors, height=0.55, edgecolor=border_color
)

for bar in bars:
  w = bar.get_width()
  ax.text(
      w + 1.2,
      bar.get_y() + bar.get_height() / 2,
      f'{w:.1f}%',
      va='center',
      fontsize=9.5,
      fontweight='bold',
      color=text_dark,
  )

ax.set_xlim(0, 105)
ax.set_title(
    '4. Feature & Add-On Adoption Rate Across Catalog',
    fontsize=14,
    fontweight='bold',
    color=text_dark,
    pad=15,
)
ax.set_xlabel(
    '% of Opportunities with Feature Present',
    fontsize=11,
    fontweight='600',
    color=text_muted,
)
plt.tight_layout()
plt.savefig(
    'visual_4_feature_adoption.png',
    dpi=300,
    bbox_inches='tight',
    facecolor=canvas_bg,
)
plt.close()
print('✓ Saved: visual_4_feature_adoption.png')

# ==============================================================================
# Visual 5: Catalog Feature Correlation Heatmap
# ==============================================================================
fig, ax = plt.subplots(figsize=(10, 6), facecolor=canvas_bg)
ax.set_facecolor(card_bg)

corr_vars = pd.DataFrame({
    'Duration (Days)': df['duration_standard_days'].clip(upper=365),
    'Fee ($)': df['fee'].clip(upper=1000),
    'Scholarship ($)': df['microscholarship'].clip(upper=1000),
    'Auto-Approve': df['is_auto_approve'].astype(float),
    'Has Badge': df['Badge_clean_id'].notna().astype(float),
    'Has Cohort': df['Cohort_clean_id'].notna().astype(float),
    'Has Reward': df['Reward_clean_id'].notna().astype(float),
    'Has Add-On': df['CareerAddOn_clean_id'].notna().astype(float),
}).corr()

sns.heatmap(
    corr_vars,
    annot=True,
    fmt='.2f',
    cmap='vlag',
    center=0,
    vmin=-0.4,
    vmax=0.4,
    square=True,
    linewidths=1.5,
    linecolor='#F1F5F9',
    cbar_kws={'shrink': 0.8},
    ax=ax,
)

ax.set_title(
    '5. Metric & Feature Correlation Matrix',
    fontsize=14,
    fontweight='bold',
    color=text_dark,
    pad=15,
)
ax.tick_params(colors=text_dark, labelsize=9.5)
plt.tight_layout()
plt.savefig(
    'visual_5_feature_correlation.png',
    dpi=300,
    bbox_inches='tight',
    facecolor=canvas_bg,
)
plt.close()
print('✓ Saved: visual_5_feature_correlation.png')

print('\nAll 5 visuals saved at 300 DPI!')