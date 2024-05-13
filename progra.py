#librerias
import os
import random #Utilizada para definir numeros e items de manera aleatoria

#Diccionarios(Contiene los dialogos relacionados con sus humores)
dialogos={"Feliz":["¡Wow! ¡Este parque solar es increíble! ¡Qué hermosa combinación de tecnología y naturaleza!",
    "¡Qué maravilla de lugar! Nunca había visto un parque tan futurista y ecológico. ¡Estoy emocionado de estar aquí!",
    "¡Esto es asombroso! ¡El aire fresco y el sol brillante hacen que todo sea aún más especial!",
    "¡Estoy impresionado por la belleza y la tranquilidad de este parque solar! ¡Es el lugar perfecto para relajarse y disfrutar del día!",
    "¡Qué vista más espectacular! ¡Los paneles solares y los jardines crean una atmósfera tan positiva y energizante!",
    "¡Este es el mejor parque en el que he estado! ¡Es genial ver cómo la tecnología y la naturaleza pueden convivir de esta manera!",
    "¡La energía en este lugar es contagiosa! ¡Es imposible no sentirse feliz y lleno de vida aquí!",
    "¡Qué experiencia tan única! ¡Este parque solar es una verdadera joya en medio de la ciudad!",
    "¡Estoy disfrutando tanto de este lugar! ¡La combinación de sol, música y alegría lo hace realmente especial!",
    "¡No puedo dejar de sonreír desde que llegamos a este parque solar! ¡Es como si la felicidad estuviera en el aire!","¡Con esos paneles solares, hasta mi abuela podría brillar más que el sol en verano!",
    "¡Vamos, amigos! ¡A repartir abrazos solares y energía positiva como si fueran paneles de amor!",
    "¡A reciclar y a reír, que la basura se convierte en sonrisas en este mundo solar punk!",
    "¡Si las plantas pueden crecer entre las ruinas, nosotros podemos florecer con creatividad en este paisaje post-apocalíptico!",
    "¡Con tanto verde y tanta luz, hasta los robots tienen un brillo especial en sus ojos mecánicos!",
    "¡Adelante, mis queridos amigos de las máquinas y la naturaleza! ¡Construyamos un futuro tan brillante que necesitemos gafas de sol las 24 horas del día!",
    "¡Entre tanta tecnología y tanto verde, es imposible no sentirse como un héroe de película de ciencia ficción con un toque de jardinero!",
    "¡Con tanto reciclaje y tanto amor por el sol, hasta el metal oxidado parece una obra de arte en este mundo solar punk!",
    "¡Vamos, amigos! ¡A inventar el futuro con un toque de locura, un montón de risas y una buena dosis de energía solar!",
    "¡Construyamos un mundo donde la energía positiva sea tan contagiosa como un buen chiste en una tarde soleada!"],
    
    "Enojado":[ "¿Cómo es posible que los paneles solares estén fallando de nuevo? ¡Esto es inaceptable!",
    "¡Me niego a tolerar más retrasos en la instalación de los nuevos colectores solares! ¡Quiero resultados ahora mismo!",
    "¡Estoy harto de los constantes cortes de energía! ¡Necesitamos soluciones, no excusas!",
    "¡Los niveles de contaminación están fuera de control! ¡¿Es tan difícil entender la importancia del reciclaje?!",
    "¡No puedo creer que sigan ignorando las advertencias sobre el cambio climático! ¡Estamos destruyendo nuestro propio hogar!",
    "¡Los líderes políticos no están haciendo nada para abordar la crisis ambiental! ¡Es hora de que asuman su responsabilidad!",
    "¡Esta ciudad necesita una reforma urgente en su infraestructura solar! ¡No puedo soportar más problemas de energía!",
    "¡Los sistemas de energía están colapsando constantemente! ¡¿Acaso nadie en este mundo sabe cómo mantener las cosas funcionando correctamente?!",
    "¡Estoy harto de la incompetencia de los ingenieros! ¡¿Es tan difícil diseñar sistemas de energía confiables?!",
    "¡Si los problemas de suministro de energía continúan, habrá consecuencias graves para todos! ¡Es hora de tomar medidas drásticas!","¡Estoy tan enfadado que mi termómetro se está calentando más que un panel solar en el ecuador!",
    "¡Esto es más frustrante que intentar arreglar un circuito eléctrico con guantes de boxeo!",
    "¡Si esto sigue así, voy a terminar siendo más abrasivo que un panel solar en pleno desierto!",
    "¡Estoy tan irritado que mi aura parece un circuito eléctrico en cortocircuito!",
    "¡Que alguien me traiga un extintor antes de que mi mal humor cause un incendio forestal en este jardín solar!",
    "¡Estoy tan molesto que podría hacer que un robot se reinicie con solo mirarlo fijamente!",
    "¡Esto es tan desastroso que podría hacer que un androide se vuelva emo y se encierre en su guarida!",
    "¡Mi paciencia se está evaporando más rápido que el agua en una planta de energía solar en un día caluroso!",
    "¡Esto es tan exasperante que podría hacer que un panel solar se convierta en un eclipse permanente!",
    "¡Que alguien me traiga un destornillador antes de que mi mal genio termine siendo más explosivo que un reactor nuclear en mal estado!"],
    
    "Triste":[ "Me entristece ver cómo la ciudad ha descuidado este hermoso parque solar. Podría ser un lugar tan especial.",
    "Es una lástima que el parque solar esté tan vacío y descuidado. Debería ser un lugar lleno de vida y alegría.",
    "Me siento desanimado al ver la falta de mantenimiento en este parque solar. Podría ser un oasis de esperanza en la ciudad.",
    "Es triste ver cómo la vegetación se está marchitando y los paneles solares están cubiertos de polvo. Este parque solía ser tan vibrante.",
    "La atmósfera de este parque solar parece tan sombría y melancólica. Es como si la energía positiva se hubiera desvanecido por completo.",
    "Me da pena ver cómo este parque solar, que alguna vez fue un símbolo de progreso y esperanza, ahora parece abandonado y olvidado.",
    "La falta de cuidado en este parque solar realmente entristece mi corazón. Deberíamos estar protegiendo nuestros espacios naturales y tecnológicos.",
    "Es desolador ver a la gente pasar de largo sin detenerse a apreciar la belleza de este parque solar. Parece que se ha perdido su magia.",
    "Me siento apesadumbrado al ver cómo este lugar, que alguna vez fue un refugio para la comunidad, ahora está tan abandonado y desolado.",
    "Es triste pensar en todo el potencial que tiene este parque solar y cómo se está desperdiciando por la falta de cuidado y atención.","¡Estoy tan triste que mis lágrimas podrían abastecer una planta de energía solar durante semanas!",
    "¡Esto es más deprimente que un panel solar en un día nublado y lluvioso!",
    "¡Mi ánimo está más bajo que el rendimiento de un colector solar en una noche sin luna!",
    "¡Estoy tan desanimado que mi optimismo parece un circuito eléctrico en cortocircuito!",
    "¡Que alguien me traiga un abrazo antes de que mi tristeza atraiga una tormenta electromagnética!",
    "¡Esto es tan desolador que podría hacer que un robot se vuelva emo y escriba poesía en su diario de bits!",
    "¡Mi corazón está más oscuro que el lado oculto de un planeta sin estrella!",
    "¡Estoy tan apesadumbrado que podría hacer que un panel solar se convierta en un eclipse permanente!",
    "¡Mi alegría se está disipando más rápido que la luz al final de un túnel en este mundo post-apocalíptico!",
    "¡Que alguien me traiga un pañuelo antes de que mi tristeza se convierta en una lluvia ácida en este oasis de desolación solar!"],
    
    "Neutral":["Este lugar es interesante, pero no logra emocionarme ni entristecerme. Es simplemente agradable estar aquí.",
    "La atmósfera de este sitio es tranquila y relajante. Es un buen lugar para desconectar del ajetreo de la ciudad.",
    "No siento una emoción particular al estar aquí, pero puedo apreciar su diseño y funcionalidad.",
    "Es agradable pasear por este lugar y observar los detalles, aunque no me despierta ninguna emoción intensa.",
    "Este lugar parece cumplir su propósito de proporcionar un espacio verde y tecnológico en la ciudad, pero no me genera ninguna emoción fuerte.",
    "No puedo decir que esté emocionado o triste al estar aquí. Simplemente estoy aquí para disfrutar de un día tranquilo.",
    "El diseño de este lugar es interesante desde un punto de vista arquitectónico, pero no me hace sentir nada en particular.",
    "Este lugar parece integrarse bien con el entorno urbano, aunque no provoca ninguna emoción especial en mí.",
    "Aunque aprecio el esfuerzo por crear un espacio verde y sostenible, este lugar no me genera ninguna emoción fuerte.",
    "Estar en este lugar me hace sentir neutral. Es agradable, pero no me inspira ninguna emoción intensa.","Los paneles solares están funcionando correctamente, parece que hoy tendremos suficiente energía.",
    "Las plantas en el jardín solar están creciendo de manera saludable, es reconfortante ver el equilibrio entre la tecnología y la naturaleza.",
    "El sistema de reciclaje está operando eficientemente, contribuyendo a mantener nuestro entorno limpio y sostenible.",
    "Los ciudadanos están colaborando activamente en la conservación de recursos, demostrando un compromiso con la comunidad y el medio ambiente.",
    "El diseño arquitectónico de los edificios solares combina de manera armoniosa la estética moderna con la funcionalidad ecológica.",
    "La tecnología de almacenamiento de energía está demostrando su fiabilidad, proporcionando una reserva estable en caso de emergencia.",
    "Los habitantes de la ciudad están aprovechando al máximo la energía solar, demostrando una mentalidad progresista hacia la sostenibilidad.",
    "Los avances en la ingeniería solar están abriendo nuevas posibilidades para la exploración espacial y la colonización de otros planetas.",
    "La comunidad está trabajando en proyectos de investigación para mejorar la eficiencia de los sistemas de energía renovable, demostrando un compromiso continuo con la innovación.",
    "La colaboración entre humanos y robots en la gestión de la infraestructura solar está dando lugar a una sociedad más eficiente y equitativa.",]}

dialogos_mascotas={"1":["¡Guau! ¡Con tanto sol, hasta mis ladridos suenan más alegres que nunca!",
    "¡Vamos, amigos peludos! ¡A repartir lametazos y alegría como si cada día fuera un paseo en el parque!",
    "¡Woof! ¡A reciclar y a jugar, que los juguetes viejos se convierten en los mejores tesoros!",
    "¡Con tanto verde y tanta luz, hasta las siestas son más reconfortantes que una cama calentita!",
    "¡Guau! ¡Entre tanta tecnología y tanto aire libre, hasta mis huesos se sienten más fuertes que nunca!",
    "¡Adelante, manada de amigos! ¡Construyamos un futuro tan emocionante que hasta los gatos quieran unirse a nosotros!",
    "¡Woof! ¡Este lugar es como un paraíso para mí, lleno de olores y aventuras por descubrir!",
    "¡Guau! ¡Hagamos que cada día sea una fiesta, con juegos, carreras y toneladas de golosinas!",
    "¡Con tanto amor y cariño, hasta los ladridos se convierten en canciones de felicidad!",
    "¡Woof! ¡Este mundo es mi parque de diversiones, lleno de sorpresas y amigos peludos por todas partes!"],
    
    "2":["¡Miau! ¡Con tanto sol, hasta mis ronroneos suenan más relajantes que nunca!",
    "¡Vamos, amigos peludos! ¡A repartir caricias y elegancia como si cada día fuera una siesta en el tejado!",
    "¡Miau! ¡A reciclar y a descansar, que las cajas vacías se convierten en los mejores lugares para dormir!",
    "¡Con tanto verde y tanta luz, hasta las siestas son más placenteras que una alfombra de lana suave!",
    "¡Miau! ¡Entre tanto espacio y tanto aire fresco, hasta mis movimientos son más ágiles que nunca!",
    "¡Adelante, felinos elegantes! ¡Construyamos un futuro tan intrigante que hasta los perros quieran descansar a nuestro lado!",
    "¡Miau! ¡Este lugar es como un oasis para mí, lleno de sombras frescas y secretos por descubrir!",
    "¡Miau! ¡Hagamos que cada día sea una siesta perfecta, con bostezos, estiramientos y toneladas de mimos!",
    "¡Con tanto misterio y tanta comodidad, hasta los maullidos se convierten en canciones de tranquilidad!",
    "¡Miau! ¡Este mundo es mi reino de sueños, lleno de lugares altos y rincones escondidos por todas partes!"],
    
    "3":["¡Pío, pío! ¡Con tanto sol, hasta las melodías suenan más alegres que nunca!",
    "¡Vamos, amigos emplumados! ¡A volar alto y disfrutar de este día como si cada brisa fuera un abrazo del cielo!",
    "¡Pío, pío! ¡A explorar los cielos y a llenar este mundo con nuestros trinos llenos de vida!",
    "¡Con tanto verde y tanto cielo azul, hasta los aleteos son más ligeros que nunca!",
    "¡Pío, pío! ¡Entre tanto follaje y tanto aire fresco, hasta las plumas se llenan de brillo y color!",
    "¡Adelante, bandada de pajaritos! ¡Construyamos un futuro donde la libertad y la naturaleza sean nuestro hogar!",
    "¡Pío, pío! ¡Este lugar es como un paraíso para mí, lleno de ramas y nidos por descubrir!",
    "¡Pío, pío! ¡Hagamos que cada día sea una danza en el aire, con giros, saltos y trinos de felicidad!",
    "¡Con tanto amor y cariño, hasta los gorjeos se convierten en canciones de alegría!",
    "¡Pío, pío! ¡Este mundo es nuestro vasto cielo, lleno de horizontes infinitos y sueños alados por todas partes!"],
    
    "4":[ "¡Oink! ¡Con tanto sol, hasta el barro parece más fresco y suave que nunca!",
    "¡Vamos, amigos de las narices rosadas! ¡A disfrutar de este día como si cada charco fuera una piscina de lodo!",
    "¡Oink! ¡A revolcarse en la naturaleza y a explorar este mundo con nuestras patitas!",
    "¡Con tanto verde y tanto espacio para correr, hasta los gruñidos suenan más alegres que nunca!",
    "¡Oink! ¡Entre tanto alimento delicioso y tanto aire fresco, hasta los más pequeños destellos de sol hacen que nuestros corazones brillen!",
    "¡Adelante, manada de cerditos! ¡Construyamos un futuro donde la felicidad y la naturaleza sean nuestro alimento diario!",
    "¡Oink! ¡Este lugar es como un paraíso para mí, lleno de aromas y sabores por descubrir!",
    "¡Oink! ¡Hagamos que cada día sea una fiesta, con carreras, saltos y toneladas de caricias!",
    "¡Con tanto amor y cariño, hasta los gruñidos se convierten en canciones de alegría!",
    "¡Oink! ¡Este mundo es nuestro patio de recreo, lleno de aventuras y amigos de cuatro patas por todas partes!"]}

dialogo_campania=([]) #Aqui van los dialogos de la campania

#Listas de informacion
informacion_usuario=["",-1]


#----------------------Solicitud de informacion y creacion de los datos necesarios

def validacion_int(texto):
	"""
	Valida si la opcion ingresada por el usuario es un numero, con el fin de evitar que se convierta a int un texto y no un numero
	E:Texto a validar
	S:True-> Es un numero False->Contiene un caracter diferente a numero
	S: Texto vacio y diferente a str
	"""
	if type(texto)!= str:
		return "Error 01"
	elif texto == "":
		return False
	else:
		return validacion_int_aux(texto)

def validacion_int_aux(texto):
	"""
	Funcion auxiliar --> validacion_int()
	"""
	if texto == "":
		return True
	elif texto[0] != "1" and texto[0] != "2" and texto[0] != "3" and texto[0] != "4" and texto[0] != "5" and texto[0] != "6" and texto[0] != "7" and texto[0] != "8" and texto[0] != "9" and texto[0] != "0":
		return False #El elemento no es un numero
	else:
		return validacion_int_aux(texto[1:])  

#--------------------------------------------------------------------------------------------------------------------------------

def nuevo_juego():
    """
    Es la primera función que se ejecuta al inciar una -partida-
    E: --
    S: --
    R: --

    datos[0] contiene el número de zonas a crear
    datos[1] contiene el número de personas a crear
    
    """
    os.system('clear')
    
    datos = bienvenida_inputs()
    zonas = crear_zonas(datos[0])

    
    personas = crear_personas(datos[1],datos[0])

    
    turno(1, zonas, datos[0], personas, datos[1])


    return True
    
#----------------------------------------------------------------------------------------------------------------------------------

def bienvenida_inputs():
    """
    Esta función recolecta el nombre del usuario, número de áreas/parques y
    número de personas que se craerán
    E: --
    S: Lista de infromación personal del usuario
    R: Los -inputs- no pueden estar vacios y deben de ser de su tipo correspondiente.
    """

    cant_zonas_perso = [] #Una lista que guarda la cantidad de zonas que se crearán en el índice [0] y la cantidad de personas que se crearán en el índice [1]

    mensaje_nombre = """
    
		\033[0;34m************************************************************************\033[0;0m
		¡Que bueno verte, visitante! Te damos la bienvenida a Solar-Park,
		donde serás capaz de visitar nuestros parques. Dime, ¿cuál es tu nombre?
		\033[0;34m************************************************************************\033[0;0m
	"""
	
    input_nombre(mensaje_nombre) #Llama a la función que recolecta el nombre del usuario

    mensaje_zonas = """
    
		\033[0;35m************************************************************************\033[0;0m
		Dime,"""+ str(informacion_usuario[0])+  """, ¿cuántas zonas quieres visitar?
		\033[0;35m************************************************************************\033[0;0m
    """

    cant_zonas = input_zonas(mensaje_zonas)

    mensaje_personas = """
    
		\033[0;32m************************************************************************\033[0;0m
		Dime,"""+ str(informacion_usuario[0])+ """, ¿a cuántas personas quieres conocer?
		\033[0;32m************************************************************************\033[0;0m
    """

    cant_personas = input_personas(mensaje_personas)

    datos = [cant_zonas, cant_personas]
    return datos

def input_nombre(mensaje):
    """
    Esta función recolecta el nombre del usuario/jugador
    E: mensaje (string) predefinido en la función anterior.
    S: Nombre del usuario.
    R: El usuario no puede ingresar una tira vacía.
    """
    print(mensaje)
    informacion_usuario[0] = input("\t\t\033[6;32m--->\033[0;0m ")

    if informacion_usuario[0] == " " or informacion_usuario[0] == None:
        print("		¿Es ese tu nombre?, ¿segurx? (\033[6;33mENTER\033[0;0m para reintentar)")
        return input_nombre(mensaje)
    
def input_zonas(mensaje):
    """
    Esta función recolecta la cantidad de zonas que el usuario cosidera necesarias, para después crearlas
    E: mensaje (string) predefinido en la función anterior.
    S: Cantidad de zonas que se crearán.
    R: El usuario debede ingresar una tira que pueda ser convertida a -int-
    """

    print(mensaje)
    num_zonas = input("\t\t\033[6;32m--->\033[0;0m ")

    if validacion_int(num_zonas) == False:
        print("		Debes de ingresar un númer válido. ¡Intentalo de nuevo! (\033[6;33mENTER\033[0;0m para reintentar)")
        return input_zonas(mensaje)
    else:
        num_zonas = int(num_zonas)
        return num_zonas

def input_personas(mensaje):
    """
    Esta función recolecta la cantidad de personas que el usuario cosidera necesarias, para después crearlas.
    E: mensaje (string) predefinido en la función anterior.
    S: Cantidad de personas que se crearán.
    R: El usuario debe de ingresar una tira que pueda ser convertida a -int-
    """

    print(mensaje)
    num_personas =num_zonas = input("\t\t\033[6;32m--->\033[0;0m ")

    if validacion_int(num_personas) == False:
        print("		¡Debes de ingresar un númer válido! Intentalo de nuevo (\033[6;33mENTER\033[0;0m para reintentar)")
        return input_personas(mensaje)
    else:
        num_personas = int(num_personas)
        return num_personas
    
# ---------------------------------------------------------------------------------

def crear_zonas(num_zonas):
    """
    Esta función crea las zonas que se usarán en la simulación, a partir del número aportado por el usuario.
    E: esta función usa el número ded zonas que fue aportado por el usuario.
    S: una lista con las zonas.
    R: esta función debe de recibir un número entero positivo
    """

    if type(num_zonas) != int:
        return "Error01"
    
    else:
        nombres = obtener_nombres_zonas()
        zonas = crear_zonas_aux(num_zonas, 1, nombres, [])
        zonas = recorrida_cambios(num_zonas, 0, zonas)
        return zonas
        
    
def crear_zonas_aux(num_zonas, indice, nombres, zonas):
    
    """
    Función auxiliar --> crear_zonas()
    """
    
    if indice == num_zonas+1:
        return zonas

    else:

        #[id, nombre, tipo, estado, clima, evento]
        zona_temp = [] #Se crea una lista temporal
        nombre = random.choice(nombres) #Se le asigna un nombre a la zona
        nombres = eliminar_nombre(nombre, nombres, 0, len(nombres), [])
        tipos_zonas = ["Parque", "Reserva", "Área Protegida", "Corredor Ecológico"]
        tipo = random.choice(tipos_zonas)
        estado = ""
        clima = ""
        evento = 0

        zona_temp = [[indice,tipo,nombre, estado, clima, evento,0]]
        
        zonas = zonas + zona_temp
        return crear_zonas_aux(num_zonas, indice+1, nombres, zonas)

def recorrida_cambios(num_zonas, indice, zonas):
    """
    Esta función recorre las zonas para pasarselas a la función -cambios_zona-
    E: número de zonas
    S: las zonas modificadas
    R: 
    """
    
    if indice == num_zonas:
        return zonas
    else:
        zonas[indice] = cambios_zona(zonas[indice])
        return recorrida_cambios(num_zonas, indice+1, zonas)
    

def cambios_zona(zona):
    """
    Esta función cambia ciertas características de cada zona:

    [id, nombre, tipo, estado, clima, evento]
    
    - Cambia el estado: abierto o cerrado
    - Cambia el clima: soleado, nublado, lluvioso, ventoso
    - Cambia si hay un evento(1) o no (0)
    """

    estado = ["Cerrado", "Abierto"]
    clima = ["Soleado", "Nublado", "Lluvioso", "Ventoso"]
    
    zona[3] = random.choice(estado)
    zona[4] = random.choice(clima)
    zona[5] = random.randint(0,1)


    return zona
    

def eliminar_nombre(nombre, conjunto_nombres, indice, largo, res):
    """
    Elimina los nombres que ya se usaron en una zona, para que dos zonas no se llamen igual.
    E: el nombre a eliminar y la lista de nombres.
    S: una nueva lista de nombres, sin el nombre ya usado.
    R: -
    """
    
    if indice == largo:
        return res
    
    elif conjunto_nombres[indice] == nombre:
        return eliminar_nombre(nombre, conjunto_nombres, indice+1, largo, res)
    else:
        res = res + [conjunto_nombres[indice]]
        return eliminar_nombre(nombre, conjunto_nombres, indice+1, largo, res)



def obtener_nombres_zonas():
    """
    En esta función se guardan todos los posibles nombres que puede tener una zona verde/parque
    E: --
    S: conjunto de nombres (38)
    R: --
    """
    nombres = ["Barbilla", "Barra Honda", "Braulio Carrillo", "Cahuita", "Carara", "El Coco", "La Amistad", "La Cangreja",
               "Los Quetzales","Las Baulas", "Rincón de la Vieja", "Santa Rosa", "Tortuguero", "Arenal", "Tenorio", "Chirripó",
               "Manzanillo", "Guayabo", "Colorado", "Golfito", "Monteverde", "Darién", "Chagres", "Portobelo","Coiba", "Barú",
               "Masaya", "Mombacha", "Telica", "Maderas", "Baritú", "Cardones", "Copo","Chaco", "Iberá", "El Leoncito", "Talampaya",
               "Laguna Blanca"]
    
    return nombres


#----------------------------------------------------------------------------------------------------------------------

def nombres_mujeres():
    """
    Esta función sirve para almacenar los nombres de mujer - 70
    """

    nombres = [
    "María", "Ana", "Sofía", "Isabella", "Valentina", "Camila", "Valeria", "Gabriela", "Natalia", "Luciana",
    "Emma", "Fernanda", "Martina", "Renata", "Mariana", "Victoria", "Regina", "Alejandra", "Paula", "Jimena",
    "Ximena", "Emily", "Bianca", "Daniela", "Aitana", "Julia", "Andrea", "Elena", "Carla", "Clara",
    "Luna", "Adriana", "Olivia", "Eva", "Alma", "Amanda", "Laura", "Antonia", "Isabel", "Catalina",
    "Ariadna", "Carmen", "Diana", "Elsa", "Eloísa", "Gabriella", "Gloria", "Hannah", "Inés",
    "Irene", "Irma", "Jazmín", "Julieta", "Kiara", "Leonor", "Lola", "Lorena", "Lourdes",
    "Maite", "Malena", "Manuela", "Marta", "Miriam", "Montserrat", "Nadia", "Nerea", "Noelia",
    "Paloma", "Raquel", "Rebeca", "Rocío", "Rosa", "Salma", "Sara", "Selena", "Silvia"]


    return nombres


def nombres_hombres():
    """
    Esta función sirve para almacenar los nombres de hombre - 70
    """
    
    nombres = [
    "Juan", "Carlos", "José", "Luis", "Miguel", "Antonio", "Alejandro", "Francisco", "Javier", "Daniel",
    "David", "Pedro", "Manuel", "Diego", "Fernando", "Sergio", "Ricardo", "Jorge", "Pablo", "Andrés",
    "Rubén", "Adrián", "Alberto", "Emilio", "Mario", "Gabriel", "Ángel", "Raúl", "Ignacio", "Gonzalo",
    "Víctor", "Tomás", "Israel", "Mateo", "Simón", "Federico", "Roberto", "César", "Guillermo", "Óscar",
    "Hugo", "Rafael", "Alonso", "Enrique", "Bruno", "Iván", "Eduardo", "Marcos", "Héctor", "Mauricio",
    "Esteban", "Nicolás", "Bruno", "Camilo", "Lucas", "Samuel", "Arturo", "Leandro", "Alex", "Marcelo",
    "Alexis", "Damián", "Julio", "Néstor", "Ezequiel", "Gustavo", "Leonardo", "Agustín", "Renato"]


    return nombres

def nombres_agenero():
    """
    Esta función sirve para almacenar los nombres agénero - 70
    """
    nombres = [
    "Alex", "Taylor", "Jordan", "Riley", "Dakota", "Casey", "Sam", "Jamie", "Avery", "Sage",
    "Emerson", "Phoenix", "Charlie", "Finley", "Peyton", "Rowan", "Quinn", "Reese", "Harper", "Ariel",
    "Avery", "Bailey", "Blair", "Cameron", "Drew", "Elliot", "Hayden", "Jaden", "Kai", "Logan",
    "Morgan", "Parker", "Reagan", "River", "Sawyer", "Skylar", "Tatum", "Tyler", "Sasha", "Shay",
    "Sidney", "Taylor", "Tristan", "Jules", "Ashton", "Aubrey", "Cassidy", "Dylan", "Evan", "Jordan",
    "Mackenzie", "Pat", "Robin", "Terry", "Corey", "Shawn", "Skyler", "Alexis", "Francis", "Hunter",
    "Leslie", "Jordan", "Ryan", "Shane", "Kyle", "Dale", "Shawn", "Jesse", "Terry", "Chris"]

    return nombres
    


def nombres_mascotas():
    """
    Esta función sirve para almacenar los nombres de mascota - 70
    """
    nombres = ["Max", "Buddy", "Daisy", "Rocky", "Bailey", "Sadie", "Luna", "Maggie", "Sophie", "Chloe",
    "Cooper", "Lola", "Zoe", "Roxy", "Pepper", "Murphy", "Rosie", "Gracie", "Ruby", "Oscar",
    "Harley", "Bear", "Coco", "Sasha", "Annie", "Leo", "Princess", "Sam", "Millie", "Teddy",
    "Milo", "Penny", "Winston", "Abby", "Zeus", "Simba", "Ginger", "Marley", "Snickers", "Casper",
    "Holly", "Buster", "Missy", "Rusty", "Misty", "George", "Angel", "Bandit", "Nala", "Finn",
    "Mocha", "Scout", "Muffin", "Shadow", "Whiskers", "Tigger", "Scooter", "Boomer", "Cinnamon", "Peanut",
    "Spike", "Midnight", "Taz", "Pumpkin", "Gizmo", "Sunny", "Mittens", "Lucky"]

    return nombres


def apellidos_personas():
    """
    Esta función sirve para almacenar los apellidos
    """

    apellidos = [
    "García", "Fernández", "González", "Rodríguez", "López", "Martínez", "Sánchez", "Pérez", "Gómez", "Martín",
    "Hernández", "Díaz", "Moreno", "Álvarez", "Romero", "Muñoz", "Ortega", "Jiménez", "Torres", "Flores",
    "Dominguez", "Vázquez", "Ramos", "Serrano", "Iglesias", "Navarro", "Rubio", "delgado", "Molina", "Suárez",
    "Ramírez", "Blanco", "Morales", "Castillo", "Ortiz", "Marín", "Ruiz", "Castro", "Núñez", "Medina",
    "Prieto", "Cortés", "Méndez", "Guerrero", "Calvo", "Santos", "Vidal", "Fuentes", "Cruz", "Arias",
    "Vega", "Reyes", "Caballero", "Aguilar", "Rojas", "Santiago", "Pascual", "Herrera", "Pardo", "Bravo",
    "Esteban", "Campos", "Vicente", "Santana", "Lorenzo", "Hidalgo", "Montero", "Ferrer", "Rivas", "León",
    "Sanchez", "Ibañez", "Figueroa", "Soto", "Aguirre", "Cabrera", "Gallardo", "Rivera", "Téllez", "Cano",
    "Blázquez", "Moya", "Solís", "Giménez", "Miranda", "Delgado", "Castaño", "Montoya", "Valero", "Pereira",
    "Carrasco", "Palacios", "Cárdenas", "Mora", "Bermúdez", "Aguado", "Sáez", "Benítez", "Vila", "Lara",
    "Crespo", "Garrido", "Rico", "Guillén", "Vargas", "Rojas", "Salas", "Peña", "Barrios", "Osorio",
    "Bautista", "Pacheco", "Cruz", "Escudero", "Ibarra", "Jaime", "Aragón", "Crespo", "Espinosa", "Otero"]

    return apellidos 


def crear_personas(num_personas, num_parques):
    """
    Esta función crea a las personas que estarán en el -mundo- del juego/simulación
    E: El número de personas que se crearán y el número de parques que hay
    S: Lista de las personas creadas, cada elemento es una lista con la información de la personas
    R: Debe de ingresarse un número entero
    """

    if type(num_personas) != int:
        return "Error01"

    else:
        #Se acceden a funciones que actúan como -almacenes- de datos
        nombres_mujer = nombres_mujeres()
        nombres_hombre = nombres_hombres()
        nombres_agender = nombres_agenero()
        apellidos = apellidos_personas()
        nombres_mascota = nombres_mascotas()

        
        return crear_personas_aux([], num_personas, 0, num_parques, nombres_mujer, nombres_hombre, nombres_agender, nombres_mascota, apellidos)


def crear_personas_aux(personas, num_personas, indice, num_parques, nombres_mujeres, nombres_hombres, nombres_agenero, nombres_mascotas, apellidos):
    """
    Función auxiliar --> crear_personas()
    """

    if indice == num_personas:
        return personas

    else:
        
        id_persona = indice
        
        genero = random.randint(0,3) #Se le asigna un género a la persona para luego nombrarla

        if genero == 0:
            genero = "Femenino"
            nombre = random.choice(nombres_mujeres)
            nombres_mujeres = eliminar_nombre(nombre, nombres_mujeres,0,len(nombres_mujeres),[])

        elif genero == 1:
            genero = "Masculino"
            nombre = random.choice(nombres_hombres)
            nombres_hombres = eliminar_nombre(nombre, nombres_hombres,0,len(nombres_hombres),[])

        else:
            genero = "Binario"
            nombre = random.choice(nombres_agenero)
            nombres_agenero = eliminar_nombre(nombre, nombres_agenero,0,len(nombres_agenero),[])

        apellido1 = random.choice(apellidos)
        apellido2 = random.choice(apellidos)

        edad = random.randint(5, 100)

        mascota = random.randint(0,5)

        if mascota!= 0:
            nombre_mascota = random.choice(nombres_mascotas)
            nombres_mascotas = eliminar_nombre(nombre_mascota, nombres_mascotas,0,len(nombres_mascotas),[])

        else:
            nombre_mascota = ""

        pts_amistad = 0

        humor = ""
        apodo=""
        persona_temp = [0, id_persona, nombre, apellido1, apellido2, edad, apodo, pts_amistad, humor, mascota,nombre,genero]
        persona_temp = variantes_personas(persona_temp, num_parques)
        personas = personas + [persona_temp]
        return crear_personas_aux(personas, num_personas, indice+1, num_parques, nombres_mujeres, nombres_hombres, nombres_agenero, nombres_mascotas, apellidos)

        
def variantes_personas(persona, num_parques):
    """
    Esta función modifica lo que varía de las personas entre turnos:
    - Humor
    - En qué zona están
    """

    if type(persona) != list:
        return "Error01"
    else:
        if num_parques != False:
        	persona[0] = random.randint(1,num_parques)

        humor = ["Triste", "Feliz", "Enojado", "Neutral"]
        persona[8] = random.choice(humor)
        return persona

def recorrer_personas_variantes(indice, num_personas, personas):
        """
        Esta función itera sobre las personas, para que la función variantes_personas funcione
        """
        if indice == num_personas:
                return personas
        else:
                personas[indice] = variantes_personas(personas[indice],False)
                return recorrer_personas_variantes(indice+1, num_personas, personas)
        

# --------------------------------------------------------------
def tabla_zonas(tabla, zonas, num_zonas, indice, num_personas, personas):
    """
    Esta función inserta los elementos de la tabla
    """
    
    if indice == len(zonas):
        return tabla

    else:
        parque = zonas[indice]
        personas_area = listar_personas_aux(parque[0],0,len(personas),[],personas)

        tabla = tabla 
        tabla = tabla + "	\t" + str(parque[0])
        tabla = tabla + "\t"+ str(parque[1])

        if len(str(parque[1])) < 8:
            tabla = tabla + "          \t" + str(parque[2])
        else:
            tabla = tabla + "  \t" + str(parque[2])

        if len(str(parque[2])) < 5:
            tabla = tabla + "            \t" + str(parque[3])
        
        elif len(str(parque[2])) >11:
            tabla = tabla + "     \t" + str(parque[3])
        else:
            tabla = tabla + "           \t" + str(parque[3])


        tabla = tabla + "    \t" + str(parque[4])


        if parque[5] == 0:
            tabla = tabla + "    \t◌"

        else:
            if personas_area != []:
                tabla = tabla + "    \t🌟"
            else:
                tabla = tabla + "    \t◌"



        tabla = tabla + "       \t"+ str(len(personas_area)) +"\n"

        return tabla_zonas(tabla, zonas, num_zonas, indice+1, num_personas, personas)
    


def tabla_zonas_bordes(zonas, num_zonas, num_personas, personas):
    tabla =""" """
    tabla = tabla + "	\tN°     \tTipo               \tNombre            \tEstado    \tClima         \tEvento  \tPersonas\n"
    tabla = tabla_zonas(tabla, zonas, num_zonas, 0, num_personas, personas)
    return tabla


# --------------------------------------------------------------
def recorrer_personas_area(indice, num_personas, personas, id_zona, personas_filtradas):
    """
    """
        
    if indice == num_personas:
        return personas_filtradas
    
    elif personas_area(personas[indice], id_zona) == True:
        personas_filtradas = personas_filtradas + personas[indice]
        return recorrer_personas_area(indice + 1, num_personas, personas, id_zona, personas_filtradas)
    
    else:
        return recorrer_personas_area(indice+1, num_personas, personas, id_zona, personas_filtradas)
        
    
def personas_area(persona, id_zona):
    """
        esta función selecciona las personas que tienen el id del parque seleccionado
    """
    if persona[0] == id_zona:
        return True
    else:
        return False

# --------------------------------------------------------------

def input_seleccion_zona(num_zonas, mensaje,personas,zonas):
	"""
        Esta fucnión recolecta la zona a la que el usuario quiere acceder.
        E: mensaje (string) predefinido en la función anterior.
        S: Zona a la que se accederá.
        R: El usuario debe de ingresar una tira que pueda ser convertida a -int-
	"""
	print(mensaje)
	zona_seleccionada = input("\033[6;33m\t---> \033[0;0m")
	if zona_seleccionada == "V" or zona_seleccionada == "v":
		return menu_principal()
	elif validacion_int(zona_seleccionada) == False:
		print("¡Debes de ingresar un númer válido! Intentalo de nuevo (ENTER para reintentar)")
		return input_seleccion_zona(num_zonas,mensaje)
	elif int(zona_seleccionada) <= 0 or int(zona_seleccionada) > num_zonas:
		print("¡Debes de ingresar un númer válido! Intentalo de nuevo (ENTER para reintentar)")
		return input_seleccion_zona(num_zonas,mensaje)
	else:
		zona_seleccionada = int(zona_seleccionada)
		return mostrar_personas(zona_seleccionada,personas,zonas)
        
# --------------------------------------------------------------
def turno(indice, zonas, num_zonas, personas, num_personas):
        #if indice == 60:
                #Despedida obligada
        #else
        os.system('clear')
        personas = recorrer_personas_variantes(0, num_personas, personas)
        print("\t\033[0;36m━✿━━━✽━━━━✿━━━✽━━━━✿━━━━✽━━━━✿━━━━✽━━━━✿━━━━✽━━━━✿━━━━━✽━━━━✿━━━━✽━━━━✿━✿━━━✽━━━━✿━━━✽━━━━✿━━━━✽━━━━✿━━━━✽━━━━✿━━━━✽━━━━✿━━━━━✽\033[0;0m")
        print(tabla_zonas_bordes(zonas, num_zonas, num_personas, personas))
        print("\t\033[0;36m━✿━━━✽━━━━✿━━━✽━━━━✿━━━━✽━━━━✿━━━━✽━━━━✿━━━━✽━━━━✿━━━━━✽━━━━✿━━━━✽━━━━✿━✿━━━✽━━━━✿━━━✽━━━━✿━━━━✽━━━━✿━━━━✽━━━━✿━━━━✽━━━━✿━━━━━✽\033[0;0m")
        mensaje_input_zona = "\t¿A qué zona deseas acceder? o ingresa \033[1;33m\tV\033[0;0m para salir."
        
        input_seleccion_zona(num_zonas, mensaje_input_zona,personas,zonas)

        


#----------------------Confirmacion y validacion en los parque
def parque_personas_ascci():

	mensaje = """


\033[0;32m##################################                                                                         #########..          
###################################                                                                     ###############.       
###################################                                                                   ##################-.      
####################################                                                                 ######################+.     
#####################################                                                               ########################+.    
######################################                                                             ##########################+..  
######################################                                                              ############################+.
#####################################                                         \033[0;0m ####                  \033[0;32m#############################
####################################  \033[0;0m   ####                                 ######                \033[0;32m##############################
###################################\033[0;0m     ######                                ######              \033[0;32m ###############################
################################### \033[0;0m    ######                                ######           \033[0;32m  #################################
#############################      \033[0;0m     ######                                 ####          \033[0;32m   ##################################
  ##+####/    #############       \033[0;0m        ##                                 ########       \033[0;32m   ###################################
        /    /                  \033[0;0m       ########                            ############     \033[0;32m #####################################
             |-----------------------\033[0;0m############--------------\033[6;33m✿\033[0;0m---------##-########-##----\033[0;32m######################################
            _/                     \033[0;0m ##############                       ### ######## ###   \033[0;32m######################################
    #       |                   \033[0;0m   ### ######## ###                      ### ######## ###  \033[0;32m ######################################
            |                  \033[0;0m    ### ######## ###                      ### ######## ###   \033[0;32m######################################
       #    |                   \033[0;0m   ### ######## ###                       ## ######## ##      \033[0;32m ###################################
        #   |                   \033[0;0m   ### ######## ###                          ########            \033[0;32m  ###############################
            |            \033[6;33m✿\033[0;0m     \033[0;0m    ## ######## ##                            ###  ###                  \033[0;32m  ######################### 
             \                    \033[0;0m     ########                              ###  ###                        \033[0;32m#####################  
             |                   \033[0;0m      ###  ###                              ###  ###                           \    \   /       
             |                   \033[0;0m      ###  ###             \033[6;33m✿ \033[0;0m               ###  ###                            \__  \_/   #       
              \                  \033[0;0m      ###  ###                              ###  ###                               \           
               |                 \033[0;0m      ###  ###                              ###  ###                                \        
    #          |                     \033[0;0m  ###  ###                                                                       \        
                \                   \033[0;0m   ###  ###                                                         \033[6;33m✿  \033[0;0m           \     #   
                 |                   \033[0;0m  ###  ###                                                                         \_       
                  \__                                                                                                     |       
                     \                                                                                              \033[6;33m✿ \033[0;0m   |       
                      \       \033[6;33m✿  \033[0;0m                         \033[6;33m✿\033[0;0m                                                             /  
 ##+---++###++-----###############+....                                                                                 /      #
  -...   .....      ............--....                                                                                  |       
"""
	return mensaje


def listar_personas(key_area_verde,personas):
	"""
	E:numero del parque seleccionado por el usuario
	S:1->>Lista de personas distribuidas en el area verde. 2-->[] no hay personas
	R:No exista la key del area verde dentro de la lista
	"""
	
	if type(key_area_verde) != int:
		return "Error 01"
	else:
		return listar_personas_aux(key_area_verde,0,len(personas),[],personas)
		
		
		
def listar_personas_aux(key_area_verde,indice,fin,resultado,personas):
	"""
	funcion auxiliar
	retorna las personas asociadas a las areas verdes
	"""
	if indice == fin:
		return resultado
	
	elif personas[indice][0] == key_area_verde: #Persona esta enlazada a la area verde
		return listar_personas_aux(key_area_verde,indice+1,fin,resultado+[personas[indice]],personas)
	
	else:
		return listar_personas_aux(key_area_verde,indice+1,fin,resultado,personas)
	
def obtener_area_verde(key_area_verde,areas_verdes):
	"""
	E:numero del parque seleccionado por el usuario
	S:1->>Elementos que pertenecen al area verde. 2-->[] no hay area 
	verde
	R:
	"""
	if type(key_area_verde)!= int:
		return "Error 01"
	else:
		return obtener_area_aux(key_area_verde,0,len(areas_verdes),areas_verdes)


def obtener_area_aux(id_area_verde, indice, fin,areas_verdes):
	"""
	funcion auxiliar
	"""
	if indice == fin:
		return False
	
	elif areas_verdes[indice][0] == id_area_verde: #busca el area verde que el usuario desea visitar
		return areas_verdes[indice]
	
	else:
		return obtener_area_aux(id_area_verde,indice+1,fin,areas_verdes)

def mostrar_personas(key_area_verde,personas,areas_verdes):
	"""
	E:numero del parque seleccionado por el usuario
	S:Imprime al usuario el sub menu de personas para conversar
	R:
	"""
	area_verde=0
	area_verde = obtener_area_verde(key_area_verde,areas_verdes)
	personas_area = listar_personas(key_area_verde,personas)
	#validacion si las areas verdes tienen personas o no
	if personas_area==[]:
		return area_verde_vacia(area_verde,personas,areas_verdes)
	else:
		return area_verde_llena(area_verde, personas_area,personas,areas_verdes)


def area_verde_vacia(area_verde,personas,areas_verdes):
	"""
	E:informacion de el area verde seleccionada
	S:Imprime al usuario el sub menu donde muestra el parque vacio y 
	sus valores
	R:
	"""
	os.system('clear')
	area_verde_vacia="""
                                                                                                                                                                                                                                                                                                                                                                          
                         \033[0;32m########                                                                                     
                       ##●########                                 
                      #############                                    
                    ############●####
                    ##●###############                                                       ############__            
                  #########●##########.                                                    _|###############.         
                    ###################                                                 ####################
                    ##●############●##        ######.                                   ######################             ######## 
                        ### #########        ###########                                 #####################        #############\033[0;0m
                          \    \_.//       \033[0;32m##############                                   ###################     .##########●###
                           |      /     \033[0;32m#################\033[0;0m                                       \   \_./ /        .\033[0;32m###●############\033[0;0m
                          /      |      \033[0;32m#########################\033[0;0m                               |  _    |        |\033[0;32m#################\033[0;0m
-------------------------/        \_----\033[0;32m###########################\033[0;0m--------------------------_ /  | |   \--------.\033[0;32m######●##########\033[0;0m
                     ● _/           \ \033[0;32m############################                          / |   .-.     |_       \033[0;32m#●###########●##\033[0;0m
            \033[0;32m#############..-__---..-\033[0;32m###############################\033[0;0m                          /-....--___\ \  \    /\033[0;32m########●#######
         \033[0;32m ###############       ●   ################################                                            ###################\033[0;0m
          \033[0;32m###################       #####################+##########.                                         ########●############\033[0;0m
         \033[0;32m.###################       ################################                            🐿️           ####################\033[0;0m
       \033[0;32m#######################       ############### \033[0;0m\    / \033[0;32m#-#####                                             ##●#########●######\033[0;0m
       \033[0;32m#######################-         ###### \033[0;0m \___   \_/  /    🐦                                              \033[0;32m #################
       \033[0;32m#########################                   \033[0;0m |       |   ---_                                       \033[0;32m      /####●############
      \033[0;32m ##########################          \033[0;0m        \       ---/ /                                            \033[0;32m  #●#################
     \033[0;32m ###########################          \033[0;0m         |        _--                🐿                           \033[0;32m    \####●###########
     \033[0;32m ##########################            \033[0;0m         |       /                                                  \033[0;32m         \ #####/ 
    \033[0;32m  ###########################           \033[0;0m         /       |                                                             \_
     \033[0;32m -#########################           \033[0;0m      /---    _    \_                                                             \_
      \033[0;32m  ##############\033[0;0m  / /                  ----   /   / \  \  \                                                            |
        \033[0;32m     ######## \033[0;0m| | |             .....----/ /   .\  \  \  \___                                                         |
         \033[0;32m      + ###  \033[0;0m \/ /                                                                                                 _/ 
                 |       /                                                                                                 /        
                 |      |                                                                                           ●      |
                /       /                                                                                                 / 
              _|        |                                                                                               _/   
             /  __       \                                                                                  ●          /     
          --/  /  \ __    \_    🐦                                                                              ●     /____● _.....
-
                                            -----------------------------------------------
                                            | El Parque está vacío, presiona v para volver |
                                            -----------------------------------------------
	"""
	print(area_verde_vacia)
	return validar_menu_parque_vacio(input("\033[0;35mIngresa una opcion ---->\033[0;0m"),personas,areas_verdes)
	
def validar_menu_parque_vacio(opcion,personas,areas_verdes):
	"""
	e:opcion ingresada
	s:informacion en relacion a la opcion ingresada
	"""
	if opcion == "V" or opcion=="v":#volver al menu personas
		return turno(0,areas_verdes,len(areas_verdes),personas,len(personas))
		
	else: 
		print("Debe ingresar una opcion valida")
		return validar_menu_parque_vacio(input("\033[0;35mIngresa una opcion ---->\033[0;0m"))

def imprimir_personas(personas_area,texto,inicio,fin):
	"""
	e:personas a listar
	s:cadena de texto con las personas previamente acomododadas
	r:-
	"""
	if inicio ==  fin:
		return texto
	else: #concatena en una sola cadena la informacion 
		fila=""
		fila += "              "+'\t'+ str(personas_area[inicio][1]) #numero de persona
		fila += '\t'+ str(personas_area[inicio][2])+" "+ str(personas_area[inicio][3])+ " "+str(personas_area[inicio][4]) #nombre de persona
		
		if informacion_usuario[1]==personas_area[inicio][1]: #valida si la persona es su mejor amigo o no
			fila+= "\033[6;33m🫂 \033[0;0m"
			
		fila += '      \t'+ str(personas_area[inicio][5]) #edad de persona
		
		
		fila += '       \t'+ str(personas_area[inicio][11]) #genero de persona
		
		if personas_area[inicio][9] == 1:#valida si la persona tiene mascota
			fila += '     \t'+ str(personas_area[inicio][10]) + "🐾" #mascota de persona
			
		else:
			fila += '    \t\033[1;31m  ✘  \033[0;0m' #no posee mascota
			
		fila += '       \t'+ str(personas_area[inicio][7]) #puntos de amistad
		
		fila +="\n"
		
		return imprimir_personas(personas_area,texto+fila,inicio+1,fin)

def area_verde_llena(area_verde,personas_area,personas,areas_verdes):
	"""
	E:informacion de el area verde seleccionada, personas que se 
	encuentran en el area verde
	S:Imprime al usuario el sub menu donde muestra el parque,
	sus valores y las personas con las cuales puede interactuar
	R:
	"""
	os.system('clear')
	fila_evento=""
	evento=""
	#-----------Impresion de la informacion del parque
	if area_verde[5]==1: #Valida la existencia de eventos en el area verde
		evento = "\033[6;33m✴️✴️ Evento sucediendo ✴️✴️\033[0;0m"
		fila_evento+= "              \tE" + "\tIr al evento ✴️"
		
	else:
		evento = "No hay eventos sucediendo"
		
	tabla_enc_personas="""
			         """+area_verde[2]+" "+area_verde[1]+"""         """+area_verde[3]+"""         """+area_verde[4]+"""       """+evento+"""
			
        \033[4;32m****************************************************************************************************************************\033[0;0m
        \033[4;32m*\033[0;0m\tN    \tNombre                   \tEdad      \tGenero      \tMascota       \tPuntos de amistad          \033[4;32m*\033[0;0m
        \033[4;32m****************************************************************************************************************************\033[0;0m
	"""
	
	#---------Impresion de las personas en el parque
	personas_listadas = imprimir_personas(personas_area,"",0,len(personas_area))
	personas_listadas+=fila_evento
	print(parque_personas_ascci())
	print(tabla_enc_personas)#impresion del encabezado
	print(personas_listadas)
	print("""
	\033[4;32m****************************************************************************************************************************\033[0;0m
	""")
	
	opcion = input("\033[0;36m       Ingresa un numero de persona o evento, o ingresa \033[1;33m'V'\033[0;36m para volver al menu principal ---->\033[0;0m")
	return validar_opcion_personas(opcion,personas,area_verde,areas_verdes)

def validar_opcion_personas(opcion,personas,area_verde,areas_verdes):
	"""
	VALIDA SI LA PERSONA INGRESADA ES VALIDA
	e:Opcion ingresada por el usuario, personas que se encuentran en el area
	s:Accion designadas en relacion a las opcion ingresada
	r:-
	"""
	if opcion == "V" or  opcion == "v": #volver al menu parque
		return turno(0,areas_verdes,len(areas_verdes),personas,len(personas))
	elif opcion == "E" or  opcion == "e": #volver al menu parque
		return mostrar_evento(area_verde,areas_verdes,personas)
	persona = encontrar_persona(opcion,personas,0, len(personas)) #buscar la persona
	
	if persona != False:
		return conversar_persona(persona,personas,areas_verdes)
		
	else:
		opcion = input("\033[0;36m       La opcion ingresada es invalida. Ingresa un numero de persona, o ingresa \033[1;33m'V'\033[0;36m para volver al menu principal ---->\033[0;0m")
		return validar_opcion_personas(opcion,personas,area_verde,areas_verdes)

def mostrar_evento(area_verde,areas_verdes,personas): 
	"""
	Los eventos son campanas que se asignan de manera aleatoria en las areas verdes
	e: area verde en la que se muestra el evento
	s: Muestra el evento al usuario
	r:-
	"""
	
	os.system('clear')
	ascci_evento="""
            *******************************************************************************************************************
			\033[0;33m¡Bienvenido al movimiento solar punk! Juntos, estamos escribiendo una nueva historia del futuro, 
				una donde la creatividad y la sostenibilidad son los pilares de nuestra sociedad.\033[0;0m
  
                                      ███████                                                              █████████████ 
                         ██████████████▓▓▓▓▓████                                                        ████▓▓▓▓▓▓▓▓▓▓▓████ 
                        ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                                                      ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███  
                       ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█                                                   ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓█████████  
                         ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                                                 ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▒░░░░░░░░░▒▒▒▓▓██████ 
                        ████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                                                 ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░░░░░░░░░░░░░░░░░░░██
                       ███▓██████████████████████                                                 ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓░░░░░░░░░░░░░░░░░░░▒██
                      ██▓▓██▒░░░░░░░░░░░░░░░░░░▒██                                                ██▓▓▓▓▓▓▓▓▓▓▓▓▓███▓▓██▒░░░░░░░░░░░░░░░░░░░▓█
                     ██▓▓██▒░░░░░░░░░░░░░░░░░░░░▒██         ██████                                ██████████████▓▒░░░░░▓█▓▓▒▒░░░░░░░░░░░░░░░██ 
                    ██████▒░░░░░▓██▒░░░▒░░░▒██▓░░▒██   ███████▒░▒███                            ████▒░░░░░░░░░░░░░░░░░░░░░░░▒▓██████▓▓▒░░░░▒██
                    ██▒░█▓░░░░░▒█▒▓▓░▓███▓░▓▓▒█▒░░█████▓▒░░█▓░░░░░██                          ██▓░▓█░░░░░░░█▓░░▒▓▒▒▓░░░█▓░░░░░██▒▒▓██████████ 
                    █▓░▒█▒░░░▒▒▒▒▒░░░▒███▓░░░▒▒▒██▓▒░░░░░░▓█▒░░░░░░▓█                         ██▒░▓▓░░░░▒▒▒▒░░░░░▒▒░░░░▒▒▒▒░░▒█▓▒▒██ 
                    ██▒▒█▓░░░▒▒▒▒▒░░░░░░░░░░░▒▓█▒░░░░░░░░▒█▓░░░░░░░▓█                         ██▓░▓█░░░░░▒▒░░░░░░░░░░░░░░▒░░░▓█▒▒▓██
                     █████░░░░░░░░░░░░░░░░░░░▒█▓░░░░░░░░░▒█▒░░░░░░░▓█                           ████▓░░░░░░░░░░░░░░░░░░░░░░░░██▒▒▓██
                        ██▓░░░░░░░░░░░░░░░░░░▒█▒▒▒░░░░░░░▒█▒░░░░░░░▓█                            ████▒░░░░░░░░░░░░░░░░░░░░░░▒█▓▒▒███ 
                         ███▒░░▒▒▒░░░░░░░░░░░▓██▓▒▓█▓░░░░▒█▒░░░░░░░▓█                           ██▓▓▓█▓░░░░░░░░░░░░░░░░░░░░░▓█▒▒▓███ 
                          ████▓▒▓██▒░░░░░▒██▓▒▒▒▒▒▒█▒░░░░█▓░░░░░░░▓█                          ███▓▓▓▓██▒░░░░░░░░░░░░░░░░░▒██▓▒▒▓█▓██ 
                            ██▒▒▒▒▒▒▓█████▓▒▒▒▒▒▒▒▒▓█░░░░░▓█▒░░░░░▒██                          ██▓▓▓▓▓▓▓██▓▒░░░░░░░░░░░▒▓██▓█▓▒▒██▓██          
                            ██▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███████▒░░█▓░░░░░██                           ██▓▓▓▓▓▓███▒▓███████████▓▒████▓▒▓█▓▓██   
                             ████▒▒▒▒▒▒▒▒▒▒▒▒▒▓█▓▒░░░▒▓███████▒▒▒██                             ███▓▓██▓▒▒▒▒█▓░░░░░░░██▒▒▓███▒▒▓█████ 
                              █▓▓██▓▒▓▓▒▓▓██████▒░░▓███      █████                                ████▒▒▒▒▒▒▒███▒▒▒██▓▒▒▓█▒░▓█████ 
                              █▓▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒█████                                              ███▒▒▒▒▒▒▒▒▒▒▒▓▓▓▒▒▒▒▓█▒░░░░░▒██
                              █▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██                                                ██▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓░░░░▒███ 
                              █▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓██                                              ██▓▒▒▒▒▒█▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▓██▓▒▓█  
	    *******************************************************************************************************************
	"""
	
	print(ascci_evento)
	print("\tIngresa el mensaje que deseas a los paticipantes de el evento luego presiona \033[6;33mENTER\033[0;0m para que lo reciba, si te quieres despedir diles \033[6;33mBYE\033[0;0m")
	print(" ")
	return ingresar_dialogo_evento(True,area_verde[0],personas,areas_verdes)
	
def ingresar_dialogo_evento(retval,num_area,personas,areas_verdes):
	"""
	maneja los turnos de dialogo de el usuario y el evento
	e: Persona a la que fue escogida para charlar y puntos acumulados
	s: blucle de respuestas
	r:
	"""
	if retval == False:
		return mostrar_personas(num_area,personas,areas_verdes)
	else:
		mensaje= input("\t\033[0;33m"+informacion_usuario[0]+"--> \033[0;0m")#SOlicita el mensajje que desea decir la persona
		if mensaje!="Bye" and mensaje!="bye" and mensaje!="BYE":
			input("\t\033[0;32mCampaña-->\033[0;0m "+ str(random.choice(dialogo_campania)))
			return ingresar_dialogo_evento(True,num_area,personas,areas_verdes)
		else:
			input("\t\033[0;32mCampaña-->\033[0;0m "+" Hasta luego, "+informacion_usuario[0]+"!!, ¡Estamos encantados de tenerte a bordo del movimiento solar punk! Tu compromiso con un futuro más brillante y vibrante es inspirador para todos nosotros.")
			return ingresar_dialogo_evento(False,num_area,personas,areas_verdes)#se despide el usuario para salir de la conversacion con la campania
		return

def encontrar_persona(opcion,personas_lista,indice,fin):
	"""
	e:Numero de la persona que se buscara dentro de la lista recibida
	s: False -> no esta la persona o retornara la persona que haya encontrado
	r:-
	"""
	if indice == fin:
		return False
		
	elif str(opcion) == str(personas_lista[indice][1]):#busca a la persona
		return personas_lista[indice]
		
	else:
		return encontrar_persona(opcion,personas_lista,indice+1,fin)

def conversar_persona(persona,personas,areas_verdes):
	"""
	e: Persona la cual fue elegida por el usuario
	s: Ascci y menuo de conversacion
	r-
	"""
	
	os.system('clear')
	#Validacion de los generos y edades
	if persona[11] == "Femenino":
		#Validacion de las edades
		if persona[5]>=0 and persona[5]<=18:
			return conversacion_nina(persona,personas,areas_verdes)
		elif persona[5]>18 and persona[5]<=50:
			return conversacion_adulta(persona,personas,areas_verdes)
		else:
			return conversacion_anciana(persona,personas,areas_verdes)
			
	elif persona[11]=="Binario":
		
		if persona[5]>=0 and persona[5]<=18:
			return conversacion_nina(persona,personas,areas_verdes)
		elif persona[5]>18 and persona[5]<=50:
			return conversacion_binario(persona,personas,areas_verdes)
		else:
			return conversacion_anciana(persona,personas,areas_verdes)
			
	else:
		
		if persona[5]>=0 and persona[5]<=18:
			return conversacion_nino(persona,personas,areas_verdes)
		elif persona[5]>18 and persona[5]<=50:
			return conversacion_adulto(persona,personas,areas_verdes)
		else:
			return conversacion_anciano(persona,personas,areas_verdes)
			
#----------ASCII ART PERSONAJES

def conversacion_nina(persona,personas,areas_verdes):
	"""
	Se encarga de mostrar el ascci art de nina, asi como sus datos
	e:persona a mostrar
	"""
	mascota=""
	if persona[9]==1: # valida si la persona tiene mascota, con l fin de mostrar informacion en especifico
		mascota="Mascota: " + persona[10]
	ascii_persona="""
	
           ██████  ████████████  ██████      
        ██▒░░░░▒██▓▒▒▒▒▒▒▒▒▒▒▓██▒░░░░▒██    
        █▓░░█▓▓█░░█▓▒▒▒▒▒▒▒▒▒▒▓█░░█▓▓█░░▓█                                      \033[1;33m******************************************************************\033[;0m
        ██░▓█▒▒█▒░█▓▒▒▒▒▒▒▒▒▒▒▓█░▒█▒▒█▓░██                                      * Nombre: """+persona[2]+" "+persona[3]+" "+persona[4]+"""
        ██░░▒▓▓▒░░█▓▒▒▒▒▒▒▒▒▒▒▓█░░▒▓▓▒░░██                                      * Edad:   """+str(persona[5])+"""
         ███▓░░▓█▓▒▒▒▒▒████▒▒▒▒▒▓█▓░░▓███                                       * Humor:  """+persona[8]+"""
        ██▒▒▒▓▓▒▒▒▒▒▒▒█▒░░▒█▓▒▒▒▒▒▒▓▓▒▒▒██                                      * Genero: """+persona[11]+"""
        █▓▓▓▓▓▓▒▓▓▓▓██░░░░░░██▓▓▓▓▓▓▓▓▓▓▓█                                      * """+mascota+"""
       ██▓░█▒░░░░░░░░░░░░░░░░░░░░░░░░▒█░▓██                                     \033[1;33m*****************************************************************\033[0;0m
       █▓░░█▒░░░░░█▒░░░▒░░▒░░░▒█░░░░░▒█░░▓█  
       ██░░█▒░░▒▒▒▒░░░░░▓▓░░░░░▒▒▒▒░░▒█░░██  
       ███▓▓█░░▒▒▒▒░░░░░░░░░░░░▒▒▒▒░░▓▓▓███  
        █▓▒▒█▓░░░░░░░░░░░░░░░░░░░░░░▒█▒▒▓█   
        ██▒▒▒█▓░░░░░░░░░░░░░░░░░░░░▓█▒▒▒██   
         ███▓▓██▒░░░░░░░░░░░░░░░░░██▓▓███    
            ██████▓░░░░░░░░░░░░▓██████       
                 ██████▓▓▓▓███▓██            
                ██▒░░░▓▓▒▒▓▓░░░░██           
               ██░░░░░▒████▒░░░░░░█          
              ██▒░▒░░░▓█▒▒█▓░░░▒░░██         
              ██░░█▒░░▓▓▒▒▓▓░░▒█░░██         
              ██████████████████████ 
         
	"""
	print(ascii_persona)
	
	return menu_dialogo(persona,personas,areas_verdes)


def conversacion_nino(persona,personas,areas_verdes):
	"""
	Se encarga de mostrar el ascci art de nino, asi como sus datos
	e:persona a mostrar
	"""
	mascota=""
	if persona[9]==1: # valida si la persona tiene mascota, con l fin de mostrar informacion en especifico
		mascota="Mascota: " + persona[10]
		
	ascii_persona="""
                   ████████████              
               ███▓▓▓▓▓▓██▓▓▓▓▓▓███          
              ▓▓▓▓█▓▓▓█▒░░▒█▓▓▓█▓▓▓██        
           ███▓▓▓▓█▓▓████████▓▓█▓▓▓▓▓██      
          ██▓▓▓▓▓▓▓▓▓▓█▓▒▒▓█▓▓▓▓▓▓▓▓▓▓██     
         ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██    
         █████████████████████████████████                                 \033[1;33m******************************************************************\033[0;0m
        ██▒█▓░░░░░░░░░░░░░░░░░░░░░░░░▓█▒▓█                                 * Nombre: """+persona[2]+" "+persona[3]+" "+persona[4]+"""
        ████▒░░░░░░░░░░░░░░░░░░░░░░░░▒████                                 * Edad:   """+str(persona[5])+"""
       ██░▒█▒░░░░░█▒░░░░░░░░░░▒█░░░░░▒█▒░██                                * Humor:  """+persona[8]+"""
       █▒░░█▒░░▒▒▒▒░░░░▒██▒░░░░▒▒▒▒░░▒█▒░▒█                                * Genero: """+persona[11]+"""
       ██▒░▓█░░▒▒▒▒░░░░░░░░░░░░▒▒▒▒░░▓▓░▒██                                * """+mascota+"""
         ████▓░░░░░░░░░░░░░░░░░░░░░░▓████                                   \033[1;33m*****************************************************************\033[0;0m
             █▓░░░░░░░░░░░░░░░░░░░░▓█        
              ██▒░░░░░░░░░░░░░░░░▒██         
                ██▓▒░░░░░░░░░░▒▓██           
                ███▓█████▓████▓███           
               ██▒▒██▒▒▒██▒▒▒██▒▒██          
              ██▒▒█▓▒▒▒▒██▒▒▒▒▓█▒▒██         
              █▒▒████████████████▒▒██        
             ██▒▓█▓▓▓▓▓▓██▓▓▓▓▓▓█▓▒██        
             ████████████████████████
	"""
	print(ascii_persona)
	return menu_dialogo(persona,personas,areas_verdes)

def conversacion_adulta(persona,personas,areas_verdes):
	"""
	Se encarga de mostrar el ascci art de adulta, asi como sus datos
	e:persona a mostrar
	"""           
	mascota=""
	if persona[9]==1: # valida si la persona tiene mascota, con l fin de mostrar informacion en especifico
		mascota="Mascota: " + persona[10]
	
	ascii_persona="""
               ██ ████████████              
            █████▓█▓▓▓▓▓▓▓▓▓▓▓▓███           
           ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓         
            ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██       
           ██▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓██      
          ██▓▓▓▓▓▓▓▓▓▓█▓░░▓█▓▓▓▓▓▓▓▓▓▓██                         
          █▓▓▓▓▓▓▓▓██▓░░░░░░▓██▓▓▓▓▓▓▓▓█                \033[1;33m******************************************************************\033[0;0m
         █████████▓░░░░░░░░░░░░▓██████████              * Nombre: """+persona[2]+" "+persona[3]+" "+persona[4]+"""
        █▒▒█▒░░░░░░░░░░░░░░░░░░░░░░░░░█▒▒█              * Edad:   """+str(persona[5])+"""
        █▓▒█▒░░░░░░█░░░░░░░░░░█░░░░░▒█▒▓█               * Humor:  """+persona[8]+"""
         ███▓░░░░░░▒▒░░█▓▓█░░▒▒░░░░░░▓███               * Genero: """+persona[11]+"""
         ██▓█▒░░░░░░░░░░░░░░░░░░░░░░▒█▓██               * """+mascota+"""
         ██▓▓█▒░░░░░░░░░░░░░░░░░░░░▒█▓▓██                \033[1;33m*****************************************************************\033[0;0m
         ██▓▓██░░░░░░░░░░░░░░░░░░██▓▓██     
          ██▓▓▓▓██▒░░░░░░░░░░░░▒██▓▓▓▓██     
           ██▓▓▓▓▓████▓▓▓▓▓▓████▓▓▓▓▓██      
            █████▓████▓░░░░▓████▓██▓██       
              ██▒█▓▒▒▒▒████▒▒▒▒▓█▒▓██        
             █▓░█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒█        
            ██░▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒░██       
            █░░░█▓▒▓█░▓████▓░█▓▒▓█░░░█       
           ████████████████████████████
	"""
	print(ascii_persona)
	return menu_dialogo(persona,personas,areas_verdes)
	
def conversacion_adulto(persona,personas,areas_verdes):
	"""
	Se encarga de mostrar el ascci art de adulto, asi como sus datos
	e:persona a mostrar
	"""
	mascota=""
	if persona[9]==1: # valida si la persona tiene mascota, con l fin de mostrar informacion en especifico
		mascota="Mascota: " + persona[10]
	
	ascii_persona="""
                           ██████████████             
                         ████▓▓▓▓▓▓▓▓▓▓▓▓▓███          
                      ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██       
                     ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██      
                  ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███    
                   ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███   
                  ██▓▓▓▓██████████████████████▓▓▓▓██                           \033[1;33m******************************************************************\033[0;0m
                 ███▓▓▓▓█▒░░░░░░░░░░░░░░░░░░▒█▓▓▓▓▓██                          * Nombre: """+persona[2]+" "+persona[3]+" "+persona[4]+"""
                 ████▓▓█▒░▒░░░░░░░░░░░░░░░░▒░▒█▓▓████                          * Edad:   """+str(persona[5])+"""
                █▓░▓██▓░░▒█▒░░░░░░░░░░░░░░▒█▒░░▓██▓░▓█                         * Humor:  """+persona[8]+"""
                ██░▒█▒░░░░░░░░░▒██████▒░░░░░░░░░░█▓░██                         * Genero: """+persona[11]+"""
                ████▒░░░░░░░░▒█▓▒▒▒▒▓█▒░░░░░░░░▒████                          * """+mascota+"""
                   ██▒░░░░░░▒█▓▒▓██▓▒▓█▒░░░░░░▒██                             \033[1;33m*****************************************************************\033[0;0m
                    ██▒░░░░░░▒▒▒▒░░▒▒▒▒░░░░░░▒██      
                     ██▓▒░░░░░░░░░░░░░░░░░░░▓██       
                     ████▒░░░░░░░░░░░░░░▒████        
                     ███▓▓███▓▓▒▒░░░▒▒▓███▓▓▓██       
                     █▓▓▓▓▓▓█▒░▓████▓░▒█▓▓▓▓▓▓█       
                    ██▓▓█▓▓▓█▒░▒██▓█▒░▒█▓▓▓█▓▓██      
                   ███▓▓█▓▓▓█▒░▒█▓▓█▒░▒█▓▓▓█▓▓███     
                   ██▓▓▓█▓▓▓█▒░▒█▓▓█▒░▒█▓▓▓█▓▓▓██     
                   ██████████████████████████████ 
	"""
	print(ascii_persona)
	return menu_dialogo(persona,personas,areas_verdes)
	
def conversacion_binario(persona,personas,areas_verdes):
	"""
	Se encarga de mostrar el ascci art de binario, asi como sus datos
	e:persona a mostrar
	"""
	
	mascota=""
	if persona[9]==1: # valida si la persona tiene mascota, con l fin de mostrar informacion en especifico
		mascota="Mascota: " + persona[10]
	
	ascii_persona="""
                    ██████████                
                ██▒▒░░░░░░░░▒██▓▓██          
             ██▒░░░░░░░░░░░░░░█▒░░░███       
           ██▒░░░░░░░░░░░░░░░░▒▓░░░░░██      
          ██▒░░░░░░░░░░░░░░░░░███░░░░░▓█     
         ██░░░░░░░░░░░░░░░░░░██▒▒█▓░░░░▓█    
        ██▒░░░░░░░░░░░░▒▒▒▓██▒▒▒▒▒██▒░░▒█    
       ██▓░░░░░░░░▒███▓▒▒▒▒▒▒▒▒▒▒▒▒▒▓██████                 \033[1;33m******************************************************************\033[0;0m
      ███▒░░░░░░▒█▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓▒██                * Nombre: """+persona[2]+" "+persona[3]+" "+persona[4]+"""
     ██▓█▒░░░░░▓█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓▒▓██               * Edad:   """+str(persona[5])+"""
     ███▒░░░░██▒▒█▒▒▒▒▓▒▒▓▒▒▒▒█▒▒▒▒▒▒▒█▓▒██                 * Humor:  """+persona[8]+"""
        ██░░░▒█▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒███                  * Genero: """+persona[11]+"""
       ███▓░░█▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒██                 * """+mascota+"""
      ██░▒█▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒░░░██                \033[1;33m*****************************************************************\033[0;0m
       ██▓▒███▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓██▒░▓██  
         ███  ██▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓██  ███    
                ███▓▓▒▒▒▒▒▒▒▒▒▓███           
                   ████████████              
                 ██▓▓█▒░░░▒▒█▒▒▓             
                 █▓▒█▒▒████▒▒█▒▒█            
                ██▒▓█░░░░░░░░█▓▒██           
                ██████████████████     
	"""
	print(ascii_persona)
	return menu_dialogo(persona,personas,areas_verdes)

def conversacion_anciano(persona,personas,areas_verdes):
	"""
	Se encarga de mostrar el ascci art de anciano, asi como sus datos
	e:persona a mostrar
	"""
	mascota=""
	if persona[9]==1: # valida si la persona tiene mascota, con l fin de mostrar informacion en especifico
		mascota="Mascota: " + persona[10]
	
	ascii_persona="""
                        ████████████              
                   ███▓▒░░░░░░░░░░░▓███          
               ███▓██▒░░░░░░░░░░░░░░░░░██▓███     
             ██▓▒▓█▒░░░░░░░░░░░░░░░░░░░░▒█▓▒▒██   
            ██▒▒▓█░░░░░░░░░░░░░░░░░░░░░░░░█▓▒▒██  
            █▒▒▒█▒░░░░░░░░░░░░░░░░░░░░░░░░░█▒▒▒██                          \033[1;33m******************************************************************\033[0;0m
           █████▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓█████                          * Nombre: """+persona[2]+" "+persona[3]+" "+persona[4]+"""
           ██░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░██                          * Edad:   """+str(persona[5])+"""
           █▓░░█░░░░░░░░█▒░░░░░░░░▒█░░░░░░░░█░░▓█                          * Humor:  """+persona[8]+"""
            ██░█▒░░░░░░░░▒████████▒░░░░░░░░░█░██                           * Genero: """+persona[11]+"""
              ███░░░░░░░░█▒▒▒▒▒▒▒▒█░░░░░░░░███                             * """+mascota+"""
                █▓░░░░░░█▓▒▒▒██▒▒▒▓█░░░░░░▒█                               \033[1;33m*****************************************************************\033[0;0m
                 █▓░░░░░░░░░░░░░░░░░░░░░░▓█       
                  ██░░░░░░░░░░░░░░░░░░░░██        
                    ▒▓▒░░░░░░░░░░░░░░▒███         
                      ███▓▒░░░░░░▒▓███            
                     ███▓▒▓▓▓▓▓▓▓▒▒▒███           
                   ██▓░░█▓▒▒▒▒▒▒▒▒▓█░░▓██         
                  ██▓█▓░░█▓▒▒▒▒▒▒▓█░░▓█▓██        
                  █▓▒▒██░░▓█▒▒▒▒█▓░░██▒▒▒█        
                 ██▒▒▒▒▓█░░▒█▒▒█▒░░█▓▒▒▒▒██       
                  ████████████████████████     
	"""
	print(ascii_persona)
	return menu_dialogo(persona,personas,areas_verdes)
	
def conversacion_anciana(persona,personas,areas_verdes):
	"""
	Se encarga de mostrar el ascci art de anciana, asi como sus datos
	e:persona a mostrar
	"""
	
	mascota=""
	if persona[9]==1: # valida si la persona tiene mascota, con l fin de mostrar informacion en especifico
		mascota="Mascota: " + persona[10]
	
	ascii_persona="""
                 ████████████████            
              ███▒▒░░░░░▒▒░░░░░▒▒███         
           ███▒▒░░░░░░░░░░░░░░░░░░░▒▓░       
         ███▒▒▒▒░░░░░░░░░░░░░░░░░░░░░▒▓██                
        ██▓▒▒▒▒▒▒░░░▒▒▓█▓▓█▓▒▒░░░░░░░░░▓██   
     ██▓▒░▒███████▓▓▒▒░░░░░░▒▒▓▓███████▓░▒▓██
     █▒░▒▒█▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓█▒▒░▒█                            \033[1;33m******************************************************************\033[0;0m
     █▒░░▒█░░░███░░▒█░░░░░░░░░░█░░███░░█▒░░▒█                            * Nombre: """+persona[2]+" "+persona[3]+" "+persona[4]+"""
     ██▒░▒█░░░░░░▒▒▒▒░░████░▒▒▒▒▒░░░░░░█▒░▒██                            * Edad:   """+str(persona[5])+"""
       ████░░░░░▒▒▒▒░░░░░░░░░░▒▒▒▒░░░░░████                              * Humor:  """+persona[8]+"""
          █▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓█                                 * Genero: """+persona[11]+"""
          ██▓░░░░░░░░░░░░░░░░░░░░░░░░▓██                                 * """+mascota+"""
            ██░░░░░░░░░░░░░░░░░░░░░░██                                   \033[1;33m*****************************************************************\033[0;0m
             ███▒░░░░░░░░░░░░░░░░▒███        
             █▓░▒▓██▓▒▒▒░░░▒▒▓██▓▒░▓█        
             █▓░░░░█░░▒▒▒▒▒▒░░█▒░░░▓█        
            ██▓██▓▓▓░░░░░░░░░░▓▓▓██▓██       
            █▒▒▒▒▒▒▓▓████████▓▓▒▒▒▒▒▒█       
           █▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓█      
          ██▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒██     
          ██▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓██     
            ████▒█████████████████████  
	"""
	print(ascii_persona)
	
	return menu_dialogo(persona,personas,areas_verdes)
	
#----------FIN DE ASCII ART PERSONAJES

def menu_dialogo(persona,personas,areas_verdes):
	"""
	e:Persona con la que se debe dialogar
	s:Menu segun con la informacion
	r:-
	"""
	
	menu=""
	tipo_menu=0
	if persona[9] == 1:
		tipo_menu=1
		menu="""
                           \033[0;32m-------------------------\033[0;0m          ------------------------           \033[0;36m-------------------------\033[0;0m 
                           \033[0;32m-\033[0;0m  H-Hablar con """+persona[2]+"""  -          - M- Hablar con """+persona[10]+"""   -           -     D- Despedirse     -
                           \033[0;32m-------------------------\033[0;0m          ------------------------           \033[0;36m-------------------------\033[0;0m
	"""
	else:
		tipo_menu=2
		menu="""
                                                  \033[0;32m-------------------------\033[0;0m          \033[0;36m------------------------\033[0;0m           
                                                  \033[0;32m-\033[0;0m   H-Hablar con """+persona[2]+"""           \033[0;36m-\033[0;0m     D- Despedirse    \033[0;36m-\033[0;0m            
                                                  \033[0;32m-------------------------\033[0;0m          \033[0;36m------------------------\033[0;0m            
		"""
	
	print(menu)
	opcion=input("\tIngresa un opcion ----->>")
	print("")
	return validar_dialogo(opcion,tipo_menu,persona,areas_verdes,personas)
	

def validar_dialogo(opcion,tipo_menu,persona,areas_verdes,personas):
	"""
	valida la opcion en menu mostrado en la persona
	e: OPcion elegida, tipo de menu mostrado, persona con la que se converse
	s: Accion en relacion a la opcion
	r:-
	"""
	if opcion == "D" or opcion == "d": #Despedirse
		
		print("")
		input("\t\033[0;32m"+persona[2]+"-->\033[0;0m "+" Hasta luego, "+informacion_usuario[0]+"!!, espero verte pronto.")
		return mostrar_personas(persona[0],personas,areas_verdes)
	
	elif opcion=="H" or  opcion == "h":#Hablar con la persona
		
		print("\tIngresa el mensaje que deseas decirle a " + persona[2] + " luego presiona \033[6;33mENTER\033[0;0m para que lo reciba, si te quieres despedir dile \033[6;33mBYE\033[0;0m")
		print(" ")
		return ingresar_dialogo(persona,True,0,personas,areas_verdes)
	
	elif tipo_menu==1 and (opcion == "M" or opcion == "m"): # Hablar con la mascota
		return dialogar_mascota(random.randint(1,4),persona[10],persona,personas,areas_verdes) #COmo parametro recibe un tipo de mascota de manera aleatoria 1-perro 2-gato 3-pajaro 4-cerdito
	
	else:
		opcion=input("\tLa opcion ingresada es invalida!!, ingrese una nuevamente -->")
		return validar_dialogo(opcion,tipo_menu,persona,personas,areas_verdes)

def ingresar_dialogo(persona,retval,puntos,personas,areas_verdes):
	"""
	e: Persona a la que fue escogida para charlar y puntos acumulados
	s: blucle de respuestas
	r:
	"""
	if retval == False:
		personas = modificar_puntos(persona,puntos,0, len(personas),personas)
		return mostrar_personas(persona[0],personas,areas_verdes)
	else:
		mensaje= input("\t\033[0;33m"+informacion_usuario[0]+"--> \033[0;0m")
		if mensaje!="Bye" and mensaje!="bye" and mensaje!="BYE":
			input("\t\033[0;32m"+persona[2]+"-->\033[0;0m "+ str(imprimir_respuesta(persona[8])))
			return ingresar_dialogo(persona,True,puntos+0.5,personas,areas_verdes)
		else:
			input("\t\033[0;32m"+persona[2]+"-->\033[0;0m "+" Hasta luego, "+informacion_usuario[0]+"!!, espero verte pronto.")
			return ingresar_dialogo(persona,False,puntos,personas,areas_verdes)
		return


def imprimir_respuesta(humor):
	"""
	e: recibe el humor del cual debe coincidir la respuesta
	s: respuesta en relacion al humor
	r-
	"""
	return random.choice(dialogos[humor])



def modificar_puntos(persona,puntos,inicio,fin,personas):
	"""
	e:persona con la que se converso, puntos que acumulo en la conversacion
	s:-
	r:-
	"""
	if inicio == fin:
		return personas
		
	elif persona[1] == personas[inicio][1]: #Encuentra a la persona con la que se le sumaran los puntos
		personas[inicio][7] += puntos #suma de puntos
		print(" ")
		print("\t🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸")
		input("\tHas ganado "+str(puntos)+" puntos de amistad con "+persona[2])
		
		#Validacion de mejor amigo
		if informacion_usuario[1]!=-1:#valida si existe un mejor amigo con el cual se compara
			
			mejor_amigo=encontrar_persona(informacion_usuario[1],personas,0,len(personas))
			
			if mejor_amigo[7] <= personas[inicio][7] and mejor_amigo[1]!= personas[inicio][1]:#valida que los puntos son mayores y si la persona mejor amiga es distinta
				
				informacion_usuario[1]=personas[inicio][1]
				print(" ")
				print("\t✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨")
				input("\t\033[6;32mEnhorabuena!!, \033[0;0m " +persona[2]+ " se convertido en tu nuevo mejor amigo!!🫂 ")
				
		else:
			informacion_usuario[1]=personas[inicio][1] #no hay mejor amigo por lo que se le asigna por primera vez
			
			print(" ")
			print("\t✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨")
			input("\t\033[6;32mEnhorabuena!!, \033[0;0m " +persona[2]+ " se convertido en tu nuevo mejor amigo!!🫂 ")
		
		return modificar_puntos(persona,puntos,inicio+1,fin,personas)
	else:
		return modificar_puntos(persona,puntos,inicio+1,fin,personas)

def dialogar_mascota(tipo_mascota,nombre,persona,personas,areas_verdes):
	"""
	crea y asigna el ascci en relacion a la mascota
	e: tipo de mascosta para mostrar, nombre de la mascota
	s: mascota segun el tipo relacionado
	r:-
	"""
	os.system('clear')
	
	mascota=""
	if tipo_mascota == 1: #Creacion de ASCII mascota en relacion al tipo de mascota
		mascota="""                                        
			\033[6;33m🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴\033[0;0m                                                    
                                                                  Habla con\033[1;36m """+nombre+"""\033[0;0m!!!           
                                                               
                                                                          \033[0;33m███████\033[0;0m       
                                                                          \033[0;33m████████\033[0;0m      
                                                                        \033[0;33m███  ███████\033[0;0m     
                                                                      \033[0;33m██████ ███████████\033[0;0m 
                                                                      \033[0;33m██████  ██████████\033[0;0m 
                                                                     \033[0;33m████████  █████████\033[0;0m 
                                                                      \033[0;33m███████ █████████\033[0;0m 
                                                                       \033[0;33m████   ██████\033[0;0m  
                                                                     \033[0;33m██    █████\033[0;0m         
                                                                 \033[0;33m███████████████\033[0;0m         
                                                              \033[0;33m██████████████████\033[0;0m         
                                                 \033[0;33m████    ███████████████████████\033[0;0m         
                                                \033[0;33m████   █████████████████████████\033[0;0m         
                                                \033[0;33m███  ██████████████████████████\033[0;0m          
                                                \033[0;33m███ ██████████████████████████\033[0;0m           
                                                \033[0;33m████████████████  ██████████\033[0;0m             
                                                \033[0;33m█████████████████  █████████\033[0;0m             
                                                \033[0;33m██████████████████  █   ████\033[0;0m             
                                                \033[0;33m████████████████      ████\033[0;0m             
                                                    \033[0;33m█████████████       ████\033[0;0m             
                                                    \033[0;33m██████████████████  ████████\033[0;0m         
                                                      \033[0;33m████████████████  ████████\033[0;0m     
                                            
			\033[6;33m🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴\033[0;0m
		"""
		
	elif tipo_mascota == 2:
		mascota="""
		\033[6;33m🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟\033[0;0m
 
                                                               Habla con """+nombre+"""!! 
                                                             
								   █████                             
							   █████ ██                             
							 ████ ████                              
							███ ████                                
							██ ███                                  
							██ ██                                   
							██ ██                                   
							███ ███  ██████  █                      
							 ███ ███████     ██                     
							  ███████          ███                  
								████            ███                 
								███              ███                
								███        ██     ███               
								███         ██     ███ █████████████
								 ███         ██     █████ ██████ ███
								  ██        ███       ███        ███
								   ███  ██████        ██  ██  ███ ██
								   ███   ████         ██    ███   ██
								███  █████         ███  ██   ███
								 ███  ██ ████       ██████████  
								  ███ ██   ██████           ███ 
								   █████       ███████████████
		\033[6;33m🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟 🐟\033[0;0m
        """
	elif tipo_mascota== 3:
		mascota="""
    🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻




                                                       ¡¡Habla con """+nombre+"""!! 
                                                     
                                                     
                                                                                                     
                                                          █▓▓▓▓▓▓▓▓▓██                               
                                                        ▓▓░░░░░░░░░░░▒▓█                             
                                                       █▒░░  ▒░░░░░░░░░▒▓▒                           
                                                       ▓░░░   ░░░░░░░░░░▒▓▒                          
                                                   ███▓▒░░░░░░░░░░░░░░░░░▒▓                          
                                                     ▓▒░░░░░░░░░░░░░░░░░░░▒▓                         
                                                     ▓▒░░░░░░░░░░░░░░░░░░░░░                         
                                                     ▓░░░░░░░░░░░▓▓▓▓▒▒▒░░░░░                       
                                                     ▓░░░░░░░░░░▓▓▒▒░░▒▒▒░░░░░                     
                                                     ▓░░░░░░░░░░▓▒▒░░░░▒▒▒▒░░░░░░                   
                                                     ▓▒░░░░░░░░░▒▒░░░░░░░░▒▒▒▒░░░░░░░░░              
                                                     ▓▒░░░░░░░░░▒░░░░░░░░░░░░░▒▒▒░░░░░░░▒▒▒▒▓▓████▓  
                                                      ▓░░░░░░░░░▒░░░░░░░░░░░░░░░▒▒░░░░░░░▒▒▒▒▓      
                                                      ▓▒░░░░░░░░▒░░░░░░░░░░░░░░░░▒▒▒░░░░░▒▒▓        
                                                       ▓▒░░░░░░░ ░░░░░░░░░░░░░░░░░░░▒▒▒░░░▒▓         
                                                        ▓▒░░░░░░░ ░░░░░░░░░░░░░░░░░░▒▒░░░▒▒          
                                                         █▓▒░░░░░░ ░░░░░░░░░░░░░░░▒▒▒░░░▒▒           
                                                           ▓▓▒░░░░░               ░░░░▒             
                                                            ▒▒░░░░░░░░░░░░░░░░░░░░░░░░               
                                                                 ░░░░░░░░░░░░░░░░▒                   
                                                                       ▓     ▓                       
                                                                       ▓     █                       
                                                                   ▓   █ ▓   ▓                       
                                                                    ▒███  ██▓█                       
                                                                                                     
                                                                         
                                                                
                                                                          
   🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻  🌻                                                                     

		"""
	elif tipo_mascota == 4:
		mascota="""
   🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  



                                                     ¡¡Habla con """+nombre+"""!! 
 

                                                
                                                    ░░░░        ▒▒▒▒▒▒▒▓                   
                                                   ░░░▒█░░░░░░░░██▒▒▒▒▒▒█░░                 
                                                  ░░██▒░░░░░░░░░░▓██▒▒▒▒█░░░░░░             
                                                 ░██▒░░░░░░░░░░░░░  ████ ░░░░░░░░░          
                                                  ░░░░░░░░░░░░░░░░░░░  ░░░░░░░░░░░░░        
                                                ░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░       
                                              ░░░░▒ ▒░░░░░░░▒ ▒▒░░░░░░░░░░░░░░░░░░░░░░      
                                             ░░░░▒   ▒░░░░░▒   ░░░░░░░░░░░░░░░░░░░░░░░░░░  
                                             ░░░░░   ▒░░░░░░   ▒░░░░░░░░░░░░░░░░░░░░░░░    
                                             ░░░░▓█████▓ ░░░▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░    
                                             ░░░▓█  ██  ▓▓ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░     
                                             ░░░▓█  █▓  ▓▓ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░     
                                             ░░░░▓▓▓▓▓▓▓▓ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░      
                                               ░░░░░    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░      
                                                 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░       
                                                     ░░░░░░░░░░░░░░░░░░░     ░░░░░░░        
                                                      ░░░░░░  ░░░░░░░░        ░░░░░░        
                                                       ░░░░     ░░░░░░░        ░░░░░        
                                                                ░░░░░░                      
                                                
                                                                                         


   🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎  🍎                                                                           
             
		"""
		
	print(mascota)
	print("\tIngresa el mensaje que deseas decirle a " + nombre + " luego presiona \033[6;33mENTER\033[0;0m para que lo reciba, si te quieres despedir dile \033[6;33mBYE\033[0;0m")
	print(" ")
	
	return ingresar_dialogo_mascota(persona,True,0,tipo_mascota,personas,areas_verdes)
	
def ingresar_dialogo_mascota(persona,retval,puntos,tipo_mascota,personas,areas_verdes):
	"""
	e: Persona a la que fue escogida para charlar y el tipo de mascota con la que se charla asi como los puntos que son acumulativos hasta que termine la conversacion
	s: blucle de respuestas hasta que la conversacion termine
	r:
	"""
	if retval == False:
		
		modificar_puntos(persona,puntos,0, len(personas),personas)
		return mostrar_personas(persona[0],personas,areas_verdes)
		
	else:
		mensaje= input("\t\033[0;33m"+informacion_usuario[0]+"--> \033[0;0m")
		
		if mensaje!="Bye" and mensaje!="bye" and mensaje!="BYE":
			input("\t\033[0;32m"+persona[11]+"-->\033[0;0m "+ str(imprimir_respuesta_mascota(tipo_mascota)))
			return ingresar_dialogo_mascota(persona,True,puntos+1,tipo_mascota,personas,areas_verdes)
			
		else:
			input("\t\033[0;32m"+persona[2]+"-->\033[0;0m "+" Hasta luego, "+informacion_usuario[0]+"!!, espero verte pronto.")
			return ingresar_dialogo_mascota(persona,False,puntos,tipo_mascota,personas,areas_verdes)


def imprimir_respuesta_mascota(tipo_mascota):
	"""
	e: recibe el tipo de mascota del cual debe coincidir la respuesta donde la buscara en el diccionario del dialogo mascota
	s: respuesta en relacion al tipo de mascota
	r-
	"""
	return random.choice(dialogos_mascotas[str(tipo_mascota)])



def menu_principal():
	"""
	Funcion que muestra el menu principal
	"""
	os.system('clear')
	
	print("""
                   \033[6;36m██░▓▓█\033[0;0m        \033[6;36m███████\033[0;0m                                            ╔╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╗
                  \033[6;36m▓██████\033[0;0m        \033[6;36m████████\033[0;0m     \033[6;36m███▓░░▓▓▓\033[0;0m                             ╠╬╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╬╣
                   \033[6;36m░▓\033[0;0m                        \033[6;36m▓▒░▒░░░░░░▒▒\033[0;0m                           ╠╣███████╗ ██████╗ ██╗      █████╗ ██████╗ ██╗███████╗╠╣
             \033[0;32m██▓▓▒░\033[0;0m             █████████    \033[6;36m██████▓▓▒▒▒\033[0;0m                            ╠╣██╔════╝██╔═══██╗██║     ██╔══██╗██╔══██╗██║██╔════╝╠╣
          \033[0;32m██▓▒░░░▒▒▓▓▓\033[0;0m        ▓▒▒▒▒▒▒▒▒▒▒▒▓█                                        ╠╣███████╗██║   ██║██║     ███████║██████╔╝██║███████╗╠╣
         \033[0;32m█▓▒░░░░░░░░▒▓▓\033[0;0m       ▓▓▓███████▓▒▒▓         \033[0;32m██████\033[0;0m                         ╠╣╚════██║██║   ██║██║     ██╔══██║██╔══██╗██║╚════██║╠╣
        \033[0;32m▓▓▒░░░░▒▒░░░░░▓░\033[0;0m      ██        █▒▒▓       \033[0;32m█▓▓▒░░▒▒▓▓▓\033[0;0m                      ╠╣███████║╚██████╔╝███████╗██║  ██║██║  ██║██║███████║╠╣
        \033[0;32m▒▓▒░░▒▒▒▒▒▒░░░▓░\033[0;0m      ██        █▒▒▓▒     \033[0;32m█▓▒░░░░░░░▒▓▓\033[0;0m                     ╠╣╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╠╣
        \033[0;32m▒▓▒░░░░▒▒▒░░░░▓░\033[0;0m      ██        █▒▒▓▒     \033[0;32m█▓░░░▒▒░░░░▓█\033[0;0m                     ╠╬╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╬╣
        \033[0;32m██▒░░▒▒▒▒▒▒░░░▓░\033[0;0m    █▓▒▒▓       ▓▒▒▓      \033[0;32m█░░░▒▒▓▒▒▒░▒▓\033[0;0m                     ╚╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╝
        \033[0;32m██▒░░░░▒▒░░░░░▓░\033[0;0m     ██▓▓       █▒▒▓     \033[0;32m█▓░░░░▒▓░░░░▒▓█\033[0;0m        
         \033[0;32m█▓░░░░▒▒░░░░▓░░\033[0;0m                █▒▒▓     \033[0;32m█▒░░░▒▒▓▓▒░░░▒▓\033[0;0m        
           \033[0;32m█▓▒▒▓▓▒▒▓▒░░\033[0;0m        ██▓▓█   █▒▒▓     \033[0;32m▓░░▒▓▒▒▒▒▒▒░░▒▓\033[0;0m                                      \033[0;32m----------------------\033[0;0m
               ██▓░░  ██       ██▒░▒▓▓  █▒▒▓     \033[0;32m█▓░░░░▒▓▒░░░▒▒▒\033[0;0m                                     \033[0;32m-\033[0;0m       1-Jugar      \033[0;32m-\033[0;0m
               ██   ██░░▓█      █▓▓▓█   █▒▒▓      \033[0;32m█▓▓▓▓▓▓▓▓▓▓▒░░\033[0;0m                                     \033[0;32m----------------------\033[0;0m
               ██   █▓░░▓█      █▓▒▒█   █▒▒▓           ██               
               ██   ██▒▓▒▒▒▓░   █▓▒▒▒▒▓██▒▒▓           ██                                            \033[0;33m----------------------\033[0;0m 
               ██   ██▒▓▓▓▓▓    ▓▓▒▒▓██ █▒▒▓           ██                                            \033[0;33m-\033[0;0m     2-Intrucciones \033[0;33m-\033[0;0m 
               ██   █▓░▒▓     ▓▓▒▒▒░▒▓  █▒▒▓           ██                                            \033[0;33m----------------------\033[0;0m 
       █████▓▓▒▒▒▒▒▒▒▒▓░▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓████        
            ░░░░░░░░░▒▒▒▒▒░░░░░░░░░░░░░▒▒░▒▒░░░░░░░░░░░░░░░░░                                        \033[0;36m----------------------\033[0;0m 
       ████▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▓░░░▒░░░░░░░░░▒▒░▒▒░░░▒▓▓▓                                    \033[0;36m-\033[0;0m        3-Salir     \033[0;36m-\033[0;0m 
           █▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒░░░░░░░░░░░▒▒▒░░░░░░                                      \033[0;36m----------------------\033[0;0m 
          ██▓▒░▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓        
       █████▓▓▓██████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓███████████       
	""")	
	opcion=input(" \tIngresa un opcion ->>")
	return validar_menu_principal(opcion)
	
def instrucciones():
	"""
	e:-
	s: Muestra al usuario la informacion necesarias para mostrar las intrucciones
	r:-
	"""
	os.system('clear')
	
	instrucciones="""


                                                                                     \033[0;33m**************************\033[0;0m
                                                                                     \033[0;33m*\033[0;0m       V-Volver         \033[0;33m*\033[0;0m
                                                                                     \033[0;33m**************************\033[0;0m
	
	"""
	print(instrucciones)
	opcion=input("		\033[0;35mIngresa un opcion ->>\033[0;0m")
	return validar_instruccion(opcion)



def validar_instruccion(opcion):
	"""
	e: Opcion elegida
	s: Accion en relacion a la opcion
	r:-
	"""
	if opcion == "V" or opcion == "v":
		return menu_principal()
	
	else:
		opcion=input("\tLa opcion ingresada es invalida!!, ingrese una nuevamente -->")
		return validar_instruccion(opcion)

def validar_menu_principal(opcion):
	"""
	e: Opcion elegida
	s: Accion en relacion a la opcion
	r:-
	"""
	if opcion == "1":
		return nuevo_juego()
	
	elif opcion == "2":
		return instrucciones()
		
	elif opcion == "3":
		return 
	
	else:
		opcion=input("\tLa opcion ingresada es invalida!!, ingrese una nuevamente -->")
		return validar_menu_principal(opcion)

menu_principal()#Llamada principal

