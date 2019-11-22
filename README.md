# Datathon2019
Equipo Abejas AA

Para resolver el problema planteado en el concurso, se implementó en python 3.7 una máquina de soporte vectorial que utiliza una función lineal para clasificar los datos.
A partir de la base de datos proporcionada, es necesario convertir la información a un formato específico. El archivo "Parsedb.py" es en el que se lleva a cabo ésta interpretación de la base de datos.Se pasan los datos a un arreglo de numpy y se extrae la última columna(que indica si la persona tiene una enfermedad) para utilizarse como verificación del modelo. Se dividen los datos de manera aleatoria en conjuntos de prueba y entrenamiento, en una relación de 0.2. Estos arreglos se guardan en los siguientes archivos  
