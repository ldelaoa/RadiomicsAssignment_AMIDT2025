def CorrelationWithoutNames(df_train_data_FeaturesOnly):
  corr_matrix = df_train_data_FeaturesOnly.drop(columns=['PatientName']).corr().abs()
  print("Max",np.max(corr_matrix))
  print("Mean",np.mean(corr_matrix))
  print("Median",np.median(corr_matrix))

  plt.figure(figsize=(10, 8))
  plt.imshow(corr_matrix, cmap='coolwarm', interpolation='nearest')
  plt.colorbar()
  plt.title('Correlation Heatmap')
  plt.show()
