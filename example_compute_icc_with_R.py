import pandas as pd
import rpy2.robjects as ro
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri
from rpy2.robjects.conversion import localconverter
from compute_icc.compute_icc_with_R import compute_icc_with_R

# CODE DESCRIPTION :
# code exemple to compute ICC with R package

# first, we create a dataframe with dummy measures. There are 3 subjects (per row) and 2 measures (test-retest)
# per subject.

pd_df = pd.DataFrame([[20,21],[13,15],[15,14]])
print(type(pd_df))


# we convert the panda-dataframe into a R-dataframe
with localconverter(ro.default_converter + pandas2ri.converter):
    r_from_pd_df = ro.conversion.py2rpy(pd_df)
print(r_from_pd_df)

# we import the R-packages
psych = importr('psych')
ICC = ro.r['ICC']

result = ICC(r_from_pd_df)

#print('anova table output by R \n')
#print(result[0])

table_icc, table_anova = compute_icc_with_R(pd_df, LMER=False)

print(table_anova)
print(table_icc)

