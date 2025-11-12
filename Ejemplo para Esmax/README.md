## Sobre el ejemplo.

- El archivo de ejemplo 'ejemplo_esmax.ipynb' presenta un ejemplo resumido, con un subconjunto de datos extraídos desde datos proporcionados, basados en la Planta Maipú.
Se extrajeron 5 clientes, Curicó, Melipilla, Chimbarongo, Pichilemu y Molina, con su respectiva demanda o pedidos. También se asumieron 3 vehículos, con capacidades de carga distintas, todos en la Planta Maipú. Se asume que todos los camiones comienzan y terminan en la Planta Maipú. 
- Para calcular las distancias entre todos los nodos, se usó Google Maps para obtener las distancias aproximadas.
- El resultado es una combinación de clientes a los que visitar en orden, para cada vehículo, donde los resultados se ven a continuación, incluso logrando cumplir esa ruta solo con dos camiones de los tres ingresado al sistema:

![gif-resultado](https://github.com/user-attachments/assets/baf79a26-d990-4a9c-b7e4-f8948a6ca717)




## Sobre los pasos a seguir a continuación y para futuras iteraciones

- Es necesaria la presencia de una matriz de distancias, contando con las distancias entre clientes y plantas, para la resolución del problema. Una matriz con las distancias reales y no aproximadas es clave para acercarse al caso real. Esta matriz es necesaria ya que el algoritmo busca optimizar principalmente para rutas donde el vehículo visita varios clientes uno detrás de otro, en lugar de sólo un cliente.
-  La naturaleza del resultado es una ruta, es decir, a cuales clientes y en que orden deben ser visitados para cada vehículo. Es posible que algunos vehículos no sean utilizados en algunas iteraciones, ya que su uso puede incurrir en mayor gasto.
-  Según el entendimiento del problema, los clientes, o estaciones de servicio, así como la planta y los vehículos, tienen horarios de funcionamiento 24/7, lo que dificulta el determinar un horario para cada ruta, ya que esto implicaría simplemente "despachar cuanto antes". Para iteraciones futuras, es posible incorporar ventanas de tiempo para la Planta, los clientes y los vehículos, siendo las ventanas de tiempo definidads con horario de inicio de actividades u horario de inicio de recepción, y un horario de fin de actividades o fin de horario de recepción.
-  El entendimiento del problema es que se hace una planificación diaria
-  Es posible incorporar costos fijos y variables para cada camión, lo que afecta la elección de camiones para cada ruta. Estos costos variables son por distancia de la ruta.
