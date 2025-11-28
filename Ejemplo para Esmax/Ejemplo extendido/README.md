## Sobre el ejemplo.

- El archivo de ejemplo 'ejemplo_esmax_10cleintes.ipynb' presenta un ejemplo resumido, con un subconjunto de datos extraídos desde datos proporcionados, basados en la Planta Maipú.
Se extrajeron 10 clientes; Curicó, Melipilla, Chimbarongo, Pichilemu, Molina, Calera de Tango, Puente Alto, San Bernardo, Reocletay Cerrillos, con su respectiva demanda o pedidos. También se asumieron 16 vehículos, repartidos en 3 categorías con capacidades de carga distintas, todos en la Planta Maipú. Se asume que todos los camiones comienzan y terminan en la Planta Maipú. 
- Para calcular las distancias entre todos los nodos, se usó Google Maps para obtener las distancias aéreas aproximadas.
- El resultado es una combinación de clientes a los que visitar en orden, para cada vehículo.
- Se explora la escalabilidad del problema. Suponiendo que existen n nodos, agregar un nodo más significa introducir a la matriz n distancias si el problema es simétrico (es decir, que la distancia entre la ida y la vuelta sea la misma) o 2n distancias distintas en caso asimétrico.
- Agregar vehículos no supone mayor problema. 

#### Variables usadas en el ejemplo

- Respecto a Nodos (Planta + Clientes): Pedido (en caso de la planta es 0)
- Respecto a Distancias: Una matriz completa con distancias entre todos los nodos.
- Respecto a los vehículos: Capacidad de carga, número de vehículos disponible por tipo, planta en la que comienza sus operaciones y planta donde debe terminar sus operaciones.


## Sobre los pasos a seguir a continuación y para futuras iteraciones

- Es necesaria la presencia de una matriz de distancias, contando con las distancias entre clientes y plantas, para la resolución del problema. Una matriz con las distancias reales y no aproximadas es clave para acercarse al caso real. Esta matriz es necesaria ya que el algoritmo busca optimizar principalmente para rutas donde el vehículo visita varios clientes uno detrás de otro, en lugar de sólo un cliente.
-  La naturaleza del resultado es una ruta, es decir, a cuales clientes y en que orden deben ser visitados para cada vehículo. Es posible que algunos vehículos no sean utilizados en algunas iteraciones, ya que su uso puede incurrir en mayor gasto.
-  Según el entendimiento del problema, los clientes, o estaciones de servicio, así como la planta y los vehículos, tienen horarios de funcionamiento 24/7, lo que dificulta el determinar un horario para cada ruta, ya que esto implicaría simplemente "despachar cuanto antes". Para iteraciones futuras, es posible incorporar ventanas de tiempo para la Planta, los clientes y los vehículos, siendo las ventanas de tiempo definidads con horario de inicio de actividades u horario de inicio de recepción, y un horario de fin de actividades o fin de horario de recepción.
-  El entendimiento del problema es que se hace una planificación diaria
-  Es posible incorporar costos fijos y variables para cada camión, lo que afecta la elección de camiones para cada ruta. Estos costos variables son por distancia de la ruta.

#### Variables ideales para incorporar al modelo

- Respecto a Nodos (Planta + Clientes): Pedido (en caso de la planta es 0), horario de inicio de atención y horario de fin de atención.
- Respecto a Distancias: Una matriz completa con distancias entre todos los nodos.
- Respecto a los vehículos: Capacidad de carga, número de vehículos disponible por tipo, planta en la que comienza sus operaciones, planta en la que termina sus operaciones, costo fijo asociado al uso del vehículo, costo variable asociado a distancia recorrida, horario de inicio de funcionamiento y horario de fin de funcionamiento.
