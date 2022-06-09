import pandas as pd 

file= pd.read_table('mortality_gen_liab_FH_20h2.bgen.stats') 
file2 = pd.read_table('splicestat/alz/alz.tsv') #, sep=' '
print(file2.columns)

mortality_df = file[['SNP', 'ALLELE1', 'ALLELE0', 'A1FREQ', 'BETA', 'SE', 'P_LINREG']]
mortality_df = mortality_df.assign(bzy_n = N)
mortality_df.columns = ['SNP', 'a1', 'a2', 'a1_freq', 'bzy', 'bzy_se', 'bzy_pval', 'bzy_n'] 

disease_df = file2[['variant_id', 'beta', 'standard_error', 'p_value']]
#disease_df['SE'] = (file2['OR_95U'] - file2['OR_95L'])/3.92
disease_df = disease_df.assign(bzx_n = N)
disease_df.columns = ['SNP', 'bzx', 'bzx_se', 'bzx_pval', 'bzx_n']

print(mortality_df.shape)
print(disease_df.shape)

gsmr_df = pd.merge(left = mortality_df, right = disease_df, on = 'SNP')

threshold = 5e-4 # Was 5e-8

gsmr_top = gsmr_df[(gsmr_df['bzx_pval']<=threshold) & (gsmr_df['bzy_pval']<=threshold)]

alleles = gsmr_top[['SNP', 'a1']]

print(gsmr_top.shape)
gsmr_top.to_csv('mortality_alz.txt', sep=' ', index=False, header=True)
alleles.to_csv('mortality_alz.allele', sep=' ', index=False, header=False)
