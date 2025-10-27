def univariate_feature_screening(df_features, survival_data, alpha=0.05):
    merged_data = survival_data.merge(df_features, on='PatientName')
    feature_cols = [col for col in df_features.columns if col != 'PatientName']

    results = []

    for feature in feature_cols:
        result = {'feature': feature}

        # Get valid data (remove missing values)
        valid_mask = ~merged_data[feature].isnull()
        feature_values = merged_data.loc[valid_mask, feature]
        durations = merged_data.loc[valid_mask, 'Survival.time']
        events = merged_data.loc[valid_mask, 'deadstatus.event']

        if len(feature_values) < 5:  # Skip features with too few valid values
            result.update({'p_value': 1.0, 'statistic': 0, 'valid_n': len(feature_values)})
        else:
            try:
                  # Fit univariate Cox model
                  cox_data = pd.DataFrame({
                      'Survival.time': durations,
                      'deadstatus.event': events,
                      'feature': feature_values
                  })

                  cph = CoxPHFitter(penalizer=.1)  # Small penalizer for stability
                  cph.fit(cox_data, duration_col='Survival.time', event_col='deadstatus.event')
                  result.update({
                      'p_value': cph.summary['p'].iloc[0],
                      'hazard_ratio': cph.summary['exp(coef)'].iloc[0],
                      'coef': cph.summary['coef'].iloc[0],
                      'ci_lower': cph.summary['exp(coef) lower 95%'].iloc[0],
                      'ci_upper': cph.summary['exp(coef) upper 95%'].iloc[0],
                      'valid_n': len(feature_values)
                  })

            except Exception as e:
                print(f"Error processing feature {feature}: {e}")
                result.update({'p_value': 1.0, 'error': str(e), 'valid_n': len(feature_values)})

        results.append(result)

    results_df = pd.DataFrame(results)
    results_df = results_df.sort_values('p_value')
    results_df['significant'] = results_df['p_value'] < alpha

    print(f"Univariate screening completed:")
    print(f"  Significant features (p < {alpha}): {sum(results_df['significant'])}")
    print(f"  Total features tested: {len(results_df)}")


    significant_features = results_df[results_df['significant'] == True]
    print(f"Significant features are:\n{significant_features[['feature','p_value']]}")


    return results_df,significant_features
