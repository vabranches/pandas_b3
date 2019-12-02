import pandas as pd

# Arquivos
myfile ='arquivos/COTAHIST_A2019.TXT'
mylayout = 'arquivos/LAYOUT_B3.csv'

# Importar Layout
dl = pd.read_csv(mylayout)

# Spec Colunas
subset = dl[['INICIAL', 'FINAL']]
col_spec = [tuple(x) for x in subset.values]

# Nomes das Colunas
col_names = list(dl['CAMPO'])

# Importar Arquivo
df = pd.read_fwf(myfile,colspecs=col_spec,Header=True)

# Definir Nomes das Colunas
df.columns = [col_names]    

# Selecionar Colunas Necessarias
amostra = df.iloc[:, [1,3,5,9,10,11,12,13,24,25]]

# Selecionar Registros Necessarios
amostra.where(amostra['CODNEG']=='PETR4T')