def map_string_to_int(df, columns):
  for column in columns:
    if column in df.columns:
        unique_strings = df[column].unique()
        string_to_int_map = {string: i for i, string in enumerate(unique_strings)}
        df[column] = df[column].map(string_to_int_map)
    else:
        print(f"Column '{column}' not found in the DataFrame.")
  return df
