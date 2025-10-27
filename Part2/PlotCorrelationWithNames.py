def PlotCorrelationWithNames(df_train_data_FeaturesOnly):
  corr_matrix = df_train_data_FeaturesOnly.drop(columns=['PatientName']).corr().abs()
  print("Max",np.max(corr_matrix))
  print("Mean",np.mean(corr_matrix))
  print("Median",np.median(corr_matrix))

  mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
  f, ax = plt.subplots(figsize=(11, 9))
  cmap = sns.diverging_palette(230, 20, as_cmap=True)
  sns.heatmap(corr_matrix, mask=mask, cmap=cmap, vmax=.3, center=0,square=True, linewidths=.5, cbar_kws={"shrink": .5})
  plt.show()
