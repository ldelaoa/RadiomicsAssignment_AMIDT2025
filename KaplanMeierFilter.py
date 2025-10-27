def KMF(df2plot)
  kmf = KaplanMeierFitter()
  medianPredict = np.median(df2plot['partial_hazards'])
  # Create boolean masks for the two risk groups
  low_risk_mask = (df2plot['partial_hazards'] <= medianPredict)
  high_risk_mask = (df2plot['partial_hazards'] > medianPredict)

  # Fit and plot survival curve for the low risk group
  kmf.fit(df2plot[low_risk_mask]['Survival.time'], event_observed=df2plot[low_risk_mask]['deadstatus.event'], label='Low Risk')
  ax = kmf.plot_survival_function()

  # Fit and plot survival curve for the high risk group
  kmf.fit(df2plot[high_risk_mask]['Survival.time'], event_observed=df2plot[high_risk_mask]['deadstatus.event'], label='High Risk')
  kmf.plot_survival_function(ax=ax)

  plt.title('Kaplan-Meier Survival Curves by Risk Group (Training Data)')
  plt.xlabel('Time')
  plt.ylabel('Survival Probability')
  plt.show()
