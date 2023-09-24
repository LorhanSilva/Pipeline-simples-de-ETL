import pandas as pd
from Interface import janela


# Carregando arquivo .csv em um DataFrame.
arq = pd.read_csv("Data/Pessoa_Data.csv", sep=',', names=["nome", "idade", "contato", "tipo_de_contato"], header=0)
#print(arq)

# Matriz com os novos dados obtidos a partir da interface.
mt = janela()
#print(mt)

# Adicionado dados da matriz no Dataframe e carregando de volta p/ o csv.
arq = arq._append(pd.DataFrame(mt, columns=arq.columns), ignore_index=True)
arq.to_csv("Data/Pessoa_Data.csv", index=False)

# Carregar p/ arquivo .xlsx (planilha) com coluna 'ID'.
arq.to_excel('Data/Planilha_pessoa.xlsx', index_label='ID')
