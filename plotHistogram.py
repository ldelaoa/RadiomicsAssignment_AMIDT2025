def plotHistogram(df_Clean3,variableToPlot):
  plt.figure(figsize=(10, 6))
  plt.hist(df_Clean3[variableToPlot], bins=50, edgecolor='black')
  plt.xlabel(variableToPlot)
  plt.ylabel('Frequency')
  plt.title('Distribution of'+variableToPlot)
  plt.grid(True)
  plt.show()
