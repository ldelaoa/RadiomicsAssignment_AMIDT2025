def fit_cox_regression(df_features, survival_data, feature_cols, penalizer=0.0):
    merged_data = survival_data.merge(df_features, on='PatientName')
    data = merged_data[['Survival.time', 'deadstatus.event'] + feature_cols].dropna()
    scaler = StandardScaler()
    data[feature_cols] = scaler.fit_transform(data[feature_cols])
    cph = CoxPHFitter(penalizer=penalizer)
    cph.fit(data, duration_col='Survival.time', event_col='deadstatus.event')
    summary = {
        'n_samples': len(data),
        'n_features': len(feature_cols),
        'concordance_index': cph.concordance_index_,
        'feature_coefficients': dict(zip(feature_cols, cph.params_)),
        'scaler': scaler
    }
    return cph, summary
