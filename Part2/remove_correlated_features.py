def remove_correlated_features(df_features,feature_cols, threshold=0.9):

    # Calculate correlation matrix
    corr_matrix = df_features[feature_cols].corr().abs()

    # Find pairs with correlation above threshold
    upper_tri = corr_matrix.where(np.triu(np.ones_like(corr_matrix, dtype=bool), k=1))

    # Find features to drop
    to_drop = [column for column in upper_tri.columns if any(upper_tri[column] > threshold)]

    print(f"Removing {len(to_drop)} highly correlated features (r > {threshold})")

    # Return cleaned dataframe
    cleaned_features = [col for col in feature_cols if col not in to_drop]
    df_cleaned = df_features[["PatientName"]+cleaned_features]

    return df_cleaned, to_drop
