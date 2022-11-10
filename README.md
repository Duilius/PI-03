# PI-03
Proyecto Individual 3

# ACCIDENTES AÉREOS 

## INFORME TÉCNICO
![This is an image](https://raw.githubusercontent.com/Duilius/PI-03/7dd88dd794061cdce2c3915ee9b4630d7789d726/IMAGEN-CABEZERA.jpg)
# 1.Sobre la información proporcionada
	Hay información suficiente para obtner conclusiones importantes.	
	Sin embargo, es necesario saber los fines que se persiguen con el informe solicitado.
	
## La Base de Datos a entregar (Fatal_Aircraft)
Como resultado del trabajo realizado se entrega la Base de Datos denominada "Fatal_Aircraft".
El contenido se soporta en dos tablas:
	1. Tabla accidents
	2. Tabla acc_causes
### Tabla accidents:
	Hemos solucionado el problema de formato en campo fecha y eliminado carácteres extraños
	en la mayoría de las celdas.
	Esta tabla contiene la información proporcionada y con muy pocas transformaciones.
	date_acc: se formateó para ofrecerla como yyyy-mm-dd
	operator: se extrajó información acerca de si el operador es Comercial, Militar o Privado.
	type_oper: indica "Tipo de Operador" (Comercial, Militar o Privado)
	time_acc: debiera indicar la hora del accidente, pero la información no es confiable; se eliminó.
### Tabla acc_causes:	
	A fin de enriquecer el análisis se incorpora información respecto de las causas de los accidentes.
	Se muestra: fecha del accidente, ruta, descripción y tipo de error, básicamente.
	
	Las conclusiones o información adicional que se aporta con esta tabla es muy valiosa para, por ejemplo,
	saber que la causa más común de los accidentes fatales en avión es el "error humano".
# 2.Información valiosa No presente.
	Se destacan dos tipos de datos que podrían abonar en un informe de mayor caliad:
	La hora de los sucesos: por un tema meramente estadístico
	Fabricante de la nave (se puede identificar por el tipo/modelo de aeronave)
	Valor aproximado de:
		1. Seguros de vida
		2. Total imdemnizaciones
		3. Valor de la aeronave
		4. Costo por daños (bienes y servicios)

	Nuevamente, conocer los fines o usos de la información ayudaría a obtener un mejor análisis.
# 3.Causas de los Accidentes:
	Por razones obvias (identificar responsables y no afectar la confianza de las personas en los
				vuelos de avión) se encuentra información resumida acerca de las causas
	de los accidentes fatales en avión.

# 4. Probabilidades de enfrentar un accidente fatal de aviación:
	Son muy escasas las posibilidades de sufrir un accidente de avión, como pasajero; no solo por la
	gran cantidad de aerolineas y de personas que hacen uso de vuleos en aviones, sino por la cantidad
	de aerolíneas.

	Sin embargo, la seguridad de viajar en avión se obtiene por las mejoras tecnológicas en materiales,
	investigaciones, medición de variables climatológicas, instrumentos de navegación, construcción de piezas, capacita-
	ción de pilotos, etc, etc.
# 5.Recomendaciones
	1. Definir el propósito o uso de la información
	2. Definir indicadores de acuerdo a los objetivos perseguidos
	3. Mayor cruce de fuentes de información
