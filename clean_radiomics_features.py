def clean_radiomics_features(df_features, remove_constant=True, remove_missing=True, missing_threshold=0.1, constant_threshold=1e-6):
    df_clean = df_features.copy()
    report = {'original_features': len(df_features.columns)-1, 'removed_features': {}, 'final_features': 0}
    feature_cols = [col for col in df_clean.columns if col != 'Survival.time' and col!=	'deadstatus.event' and col!='PatientName']
    if remove_missing:
        missing_ratios = df_clean[feature_cols].isnull().sum() / len(df_clean)
        high_missing = missing_ratios[missing_ratios > missing_threshold].index.tolist()
        if high_missing:
            df_clean = df_clean.drop(columns=high_missing)
            report['removed_features']['high_missing'] = high_missing
    if remove_constant:
        feature_cols = [col for col in df_clean.columns if col != 'Survival.time' and col!=	'deadstatus.event'and col!='PatientName']
        constant_features = [col for col in feature_cols if df_clean[col].dropna().std() < constant_threshold]
        if constant_features:
            df_clean = df_clean.drop(columns=constant_features)
            report['removed_features']['constant'] = constant_features
    feature_cols = [col for col in df_clean.columns if col != 'Survival.time' and col!=	'deadstatus.event'and col!='PatientName']
    invalid_features = [col for col in feature_cols if df_clean[col].isin([np.inf, -np.inf]).any()]
    if invalid_features:
        df_clean = df_clean.drop(columns=invalid_features)
        report['removed_features']['invalid'] = invalid_features
    report['final_features'] = len(df_clean.columns)-1
    return df_clean, report
