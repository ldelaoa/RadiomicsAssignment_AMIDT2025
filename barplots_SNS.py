def barplots_SNS(significant_features):
  sns.set_color_codes("pastel")
  sns.barplot(x="feature", y="p_value", data=significant_features,color="b")
  sns.set_color_codes("muted")
  sns.barplot(x="feature", y="p_value", data=significant_features, color="b")
  ax.set(xlim=(0, 24), ylabel="")
  sns.despine(left=True, bottom=True)
