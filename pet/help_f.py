def get_rescuer_feature(df):
    rg = df['RescuerID'].value_counts()
    df['RescuerID'] = df['RescuerID'].apply(lambda x: rg[x])
    return df
