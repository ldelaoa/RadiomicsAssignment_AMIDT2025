def bootstrap_forward_selection(df_features, survival_data, all_features, n_bootstraps=100,
                                selection_threshold=0.6, ImprovementP=0.1, criterion='p-value'):
    merged_data = survival_data.merge(df_features, on='PatientName')
    selected_features_counts = Counter()
    total_samples = len(merged_data)

    print(f"Starting Bootstrap Forward Selection ({n_bootstraps} iterations) using criterion: {criterion}...")

    for i in tqdm(range(n_bootstraps)):
        bootstrap_sample = resample(merged_data, replace=True, n_samples=total_samples, random_state=i)
        current_selected_features = []
        remaining = all_features[:]

        while remaining:
            best_feature = None
            best_criterion_value = None
            improved = False

            for feature in remaining:
              temp_features = current_selected_features + [feature]
              try:
                  cph = CoxPHFitter(penalizer=1)
                  cph.fit(bootstrap_sample[['Survival.time', 'deadstatus.event'] + temp_features].dropna(),
                          duration_col='Survival.time', event_col='deadstatus.event', show_progress=False)

                  if criterion == 'p-value':
                      last_feature_p_value = cph.summary['p'].iloc[-1]
                      if last_feature_p_value < ImprovementP:
                          if best_criterion_value is None or last_feature_p_value < best_criterion_value:
                              best_criterion_value = last_feature_p_value
                              best_feature = feature
                              improved = True
                  elif criterion == 'concordance':
                      concordance = cph.concordance_index_
                      if best_criterion_value is None or concordance > best_criterion_value:
                          best_criterion_value = concordance
                          best_feature = feature
                          improved = True
              except Exception:
                  continue

            if improved and best_feature:
                current_selected_features.append(best_feature)
                remaining.remove(best_feature)
            else:
                break

        selected_features_counts.update(current_selected_features)

    print("\nBootstrap Forward Selection Complete.")
    print(f"Feature selection counts across {n_bootstraps} bootstraps:")
    print(selected_features_counts)

    frequently_selected_features = [feature for feature, count in selected_features_counts.items()
                                    if count / n_bootstraps >= selection_threshold]

    return frequently_selected_features
