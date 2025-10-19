
import numpy as np
import pyvrp as vrp
import pandas as pd


data=pd.read_excel(r'Datos/data.xlsx')

data_nodos=pd.read_excel(r'Datos/data.xlsx', sheet_name=0)

data_vehiculos=pd.read_excel(r'Datos/data.xlsx', sheet_name=1)

m=vrp.Model()

m.add_depot(x=data_nodos.iloc[0,1],y=data_nodos.iloc[0,2])

for i in range(1,len(data_nodos['Nodos'])):
    m.add_client(x=data_nodos.iloc[i,1],y=data_nodos.iloc[i,2], delivery=int(data_nodos.iloc[i,3]))

for j in range(0,len(data_vehiculos['Tipo'])):
    m.add_vehicle_type(num_available=int(data_vehiculos.iloc[j,1]), capacity=int(data_vehiculos.iloc[j,2]), start_depot=m.locations[0], end_depot=m.locations[0], reload_depots=[m.locations[0]])

for frm_idx, frm in enumerate(m.locations):
    for to_idx, to in enumerate(m.locations):
        m.add_edge(frm, to, distance=abs(frm.x - to.x) + abs(frm.y - to.y))


from pyvrp.stop import MaxRuntime

res = m.solve(stop=MaxRuntime(60), display=True, seed=27)

sol=res.best
rutas= sol.routes()
print(rutas[1].vehicle_type())