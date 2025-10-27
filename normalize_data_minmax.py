def normalize_data_minmax(df, cols_to_process):
    df_normalized = df.copy()
    # Remove rows with NaN values in the specified feature columns
    initial_rows = len(df_normalized)
    df_normalized = df_normalized.dropna(subset=cols_to_process)
    rows_removed = initial_rows - len(df_normalized)
    if rows_removed > 0:
        print(f"Removed {rows_removed} rows with NaN values in the specified feature columns.")
    if df_normalized.empty:
        print("After removing NaNs, the DataFrame is empty. Cannot perform normalization.")
        return df_normalized, MinMaxScaler() # Return empty df and unfitted scaler

    scaler = MinMaxScaler()

    # Apply normalization to the specified columns
    df_normalized[cols_to_process] = scaler.fit_transform(df_normalized[cols_to_process])

    return df_normalized, scaler
