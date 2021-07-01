import rpy2.robjects as ro
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri
from rpy2.robjects.conversion import localconverter

def compute_icc_with_R(df, LMER):
    psych = importr('psych')
    ICC = ro.r['ICC']
    # calcul of ICC3
    # then, we convert the pandas df in R df
    with localconverter(ro.default_converter + pandas2ri.converter):
        rdf = ro.conversion.py2rpy(df)

    # the R df is now the input of te compute_icc function from R

    result = ICC(rdf, lmer = LMER)
    table_icc = result[0]
    table_anova = result[1]

    # we convert back the output_oasis_curvature R data_for_icc in panda dataframe
    with localconverter(ro.default_converter + pandas2ri.converter):
        df_table_icc = ro.conversion.rpy2py(table_icc)
        df_table_anova = ro.conversion.rpy2py(table_anova)
    return df_table_icc, df_table_anova