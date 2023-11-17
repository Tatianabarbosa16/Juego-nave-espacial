# Juego-nave-espacial
Vamos a explorar un juego simple llamado "Ataque Espacial" desarrollado en Python utilizando la biblioteca Pygame. El juego consiste en controlar una nave espacial y disparar a los enemigos que se mueven por la pantalla. El objetivo es obtener la mayor puntuación posible antes de que los enemigos lleguen a la parte inferior de la pantalla.
conceptos clave
Antes de sumergirnos en el código, es importante comprender algunos conceptos clave:

Pygame : Pygame es una biblioteca de Python diseñada para facilitar el desarrollo de videojuegos. Proporciona una serie de funciones y herramientas que permiten crear gráficos, reproducir sonidos y manejar eventos de manera sencilla.

Sprites : En el contexto de los juegos, un sprite es una imagen que se mueve por la pantalla. En nuestro juego, tanto la nave espacial como los enemigos son sprites.

Colisión : La colisión ocurre cuando dos sprites se superponen en la pantalla. En nuestro juego, queremos detectar cuando una bala disparada por la nave espacial colisiona con un enemigo.

Estructura del código
El código proporcionado se divide en varias secciones, cada una con un propósito específico. Veamos cada una de ellas:

Inicialización : En esta sección, se importan las bibliotecas necesarias, se establece el tamaño de la pantalla y se cargan los recursos del juego, como imágenes y sonidos.

Funciones auxiliares : Aquí se definen varias funciones que se utilizarán en el juego. Estas funciones incluyen la función para mostrar la puntuación, dibujar los sprites en la pantalla, disparar balas y detectar colisiones.

Bucle principal del juego : En esta sección, se define la función principal del juego llamada "gameloop". Esta función controla el flujo del juego, maneja eventos, actualiza las posiciones de los sprites y dibuja la pantalla. También se encarga de detectar colisiones y mostrar la puntuación.
