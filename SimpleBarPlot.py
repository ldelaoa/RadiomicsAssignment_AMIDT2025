def SimpleBarPlot(significant_features):
  # Create a bar plot
  plt.figure(figsize=(10, 6))
  sns.barplot(x='p_value', hue='feature', data=significant_features, palette='viridis',legend=None)#"brief")
  plt.xlabel('pvalue')
  plt.ylabel('Feature')
  plt.show()
