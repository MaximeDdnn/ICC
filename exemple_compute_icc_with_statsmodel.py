import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from data_management.reformat_values_1col import reformat_values_1col
from compute_icc.compute_icc_with_statsmodel import compute_icc_with_statsmodel

# STASTMODEL

df = pd.DataFrame(data = [[20,21],[13,15],[15,14]])
print(df)
df_reformated= reformat_values_1col(df)

#data_lm = ols('values ~ C(timesteps) + C(subjects)', data=df_reformated).fit()
#table = sm.stats.anova_lm(data_lm, typa=2)  # Type 2 ANOVA DataFrame
#print('anova table output by statsmodel \n')
#data = {
#    'array' : df_reformated,
#    'anova_table' : table
#}

#print(data['array'])
#print(data['anova_table'])

ICC_data = compute_icc_with_statsmodel(df_reformated)

print(ICC_data['ICC'])
print(ICC_data['anova_table'])