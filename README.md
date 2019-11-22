# Datathon2019
Equipo Abejas AA

Para resolver el problema planteado en el concurso, se implementó en python 3.7 una máquina de soporte vectorial(SVM) que utiliza una función lineal para clasificar los datos.

A partir de la base de datos proporcionada, es necesario convertir la información a un formato específico. El archivo "Parsedb.py" es en el que se lleva a cabo ésta interpretación de la base de datos.Se pasan los datos a un arreglo de numpy y se extrae la última columna(que indica si la persona tiene una enfermedad) para utilizarse como verificación del modelo. Se dividen los datos de manera aleatoria en conjuntos de prueba y entrenamiento, en una relación de 0.2. Estos arreglos se guardan en los siguientes archivos:

trainParam.npy : Contiene los parámetros que se obtuvieron con el examen de orina de cada persona en la base de datos y que se utilizaran para entrenar el modelo.

trainDiag.npy : Contiene las etiquetas de cada persona en el arreglo trainParam.npy, que indican si esta tiene una enfermedad crónica o no.

testParam.npy : Contiene los parámetros que se obtuvieron con el examen de orina de cada persona en la base de datos y que se utilizaran para probar el modelo.

testDiag.npy : Contiene las etiquetas de cada persona en el arreglo testParam.npy, que indican si esta tiene una enfermedad crónica o no.

El entrenamiento del modelo ocurre en el archivo "LinearSVC.py". Este utiliza los modulos de scikit para entrenar la SVM. Para evaluar el desempeño de nuestro modelo, se utiliza el párametro de exactitud (accuracy_score). Este evalua la cantidad de veces que el modelo clasifica correctamente tanto los datos de entrenamiento como los datos de prueba. Los resultados de exactitud obtenidos fueron los siguientes:
Exactitud sobre datos de entrenamiento: 0.9875
Exactitud sobre datos de prueba: 0.975

Ya con el modelo entrenado, la aplicación final fue implementada en Python con el módulo Tkinter. En esta se hace la petición de datos al usuario, para obtener la predicción acerca de si está en riesgo o no de padecer una enfermedad crónica en el riñón. La aplicación actual no requiere de todos los datos para hacer una predicción, así que un dato desconocido se puede dejar como un espacio en blanco. 
