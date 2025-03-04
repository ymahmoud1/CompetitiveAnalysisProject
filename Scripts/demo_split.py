def demo_split(df):  
    df = split_and_expand(df, "Target Demographics (keep consistencies as much as possible)", "Demographics Split")
    return df

def split_and_expand(df, col_name, new_col_name):
        import pandas as pd
        df[col_name] = df[col_name].fillna("")
        df[col_name] = df[col_name].replace("and", ",")
        df[new_col_name] = df[col_name].str.split(",")
        df = df.explode(new_col_name)
        return df


def get_output_schema():
    import pandas as pd
    return pd.DataFrame({
 			'US Ranking' : prep_decimal(),
            'University Name' : prep_string(),
            'School Name' : prep_string(),
            'Program Name' : prep_string(),
            'Program Category' : prep_string(),
 			'Certificate' : prep_string(),
 			'City' : prep_string(),
            'State' : prep_string(),
             'Length in Days (put average number of days if different lengths are listed)' : prep_decimal(),
             'Modality' : prep_string(),
             'Location' : prep_string(),
             'Total Cost (if cost per credit is not listed. Put the latest cost)' : prep_decimal(),
             "Total Online Format Cost (if cost per credit is not listed and online vs in person cost is different)" : prep_decimal(),
             'Target Demographics (keep consistencies as much as possible)' : prep_string(),
             'Unique Value' : prep_decimal(),
             'Demographics Split': prep_string(),
 			})