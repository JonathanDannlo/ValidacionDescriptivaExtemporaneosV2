import os
import pandas as pd
import matplotlib.pyplot as plt

# Carga del archivo al dataframe de trabajo
file_path = "/content/EstudiantesExtemporaneos2024-1.xlsx"

if not os.path.isfile(file_path):
  raise FileNotFoundError(f"{file_path} not found.")

piam20241 = pd.read_excel(file_path)

#Analisis descriptivo poblacion segun estrato y zona de nacimiento
df_piam = piam20241[["ESTRATO","FACULTAD","DERECHOS_MATRICULA"]]
df_group = df_piam.groupby(["ESTRATO","FACULTAD"],as_index=False).mean()
df_pivot = df_group.pivot(index="ESTRATO",columns="FACULTAD",values="DERECHOS_MATRICULA")
df_pivot.plot(kind="bar",stacked=True)

plt.pcolor(df_pivot, cmap="RdBu")
plt.colorbar()
plt.title("Analisis descriptivo poblacion segun estrato y zona de nacimiento")
plt.xlabel("Facultad")
plt.ylabel("Estrato")
plt.show()
