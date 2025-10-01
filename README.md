# Sobre este repositorio
Este repositorio busca exponer ejemplos y explicar la funcionalidad de la librería PyVRP para la solución de Problemas de Enrutamiento de Vehículos.
Por el momento es una implementación de ejemplo, que busca ser prontamente una implementación aplicada a un caso real.

Se presentan dos archivos jupyter notebook con ejemplos de VRP, con el objetivo de explicar y demostrar algunas de las capacidades de la librería.

# Requisitos

Para poder ejecutar los códigos es necesaria la instalación de la librería PyVRP
```
pip install pyvrp
```
La documentación de esta librería se encuentra aquí:  https://pyvrp.org/index.html

Repositorio de GitHub de PyVRP:  https://github.com/PyVRP/PyVRP/

Referencia:  Wouda, N.A., L. Lan, and W. Kool (2024). PyVRP: a high-performance VRP solver package. INFORMS Journal on Computing, 36(4): 943-955. https://doi.org/10.1287/ijoc.2023.0055 https://arxiv.org/abs/2403.13795


# Sobre los Vehicule Routing Problem (VRP)

Los problemas de enrutamiento de vehiculos o vehicule routing problem, es un problema de optimización combinatorial y de programación entera de complejidad alta que responde a la pregunta: 
**¿Cuál es el conjunto óptimo de rutas que una flota de vehículos debe recorrer para entregar servicios a un conjunto dado de clientes?**. 
El problema es una generalización del problema del vendedor ambulante, o travelling salesman problem (TSP), que es el caso donde solo se requiere una ruta para visitar todos los destinos, 
y la problematica es encontrar el orden óptimo de visita. El VRP, aparte de buscar el orden óptimo de visita de los destinos por cada ruta, busca múltiples rutas para ser llevadas a cabo 
por muchos "vendedores" o vehiculos. En términos de complejidad computacional, tanto el VRP como el TSP son NP-hard, esto quiere decir, evitando las definiciones matemáticas, que son problemas
especialmente dificiles de resolver y es posible que encontrar soluciones exactas sea prácticamente imposible en tiempos de años, décadas o incluso siglos(sin exagerar), por lo que es recomendable
aproximar soluciones, sobre todo con VRP de gran tamaño.

Por facilidad de implementación, se usa la librería Pyvrp. Esta librería nos permite crear un modelo de VRP (Vehicule Routing Problem) 
y solucionarlo a través de un Algoritmo Genético Híbrido con Búsqueda Local (HGS). Este Algoritmo funciona, a grandes rasgos, 
creando aleatoriamente muchas posibles soluciones al problema, denominadas población, de las cuales se seleccionan las dos mejores 
tomando en cuenta la función objetivo a optimizar (en este caso costo o distancia recorrida por los vehículos). Estas dos mejores soluciones
se denominan "padres" y son "cruzadas" o mezcladas para generar otra solucion denominada "descendencia" que hereda aspectos de sus soluciones
padres (por ejemplo, mantener la primera parte de las rutas de uno de sus padres, y el resto de su segundo padre). Luego, este descendiente 
es "educado", esto consiste en que es sujeto a un proceso de mejoramiento llamado búsqueda local, que cambia aspectos de esta posible solución
para que su desempeño comparado a la función objetivo mejore(por ejemplo, intercambiar el orden de visita de los distintos destinos, visitando
un destino más, entre otras opciones). Después de este proceso, el descendiente se incorpora a la población y se repite el proceso, seleccionando
otros padres, generando descendencia y educandola, hasta obtener una solución que sea lo suficientemente satisfactoria.
