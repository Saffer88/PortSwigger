# Local File Inclution (LFI)

## Lab 1 - File path traversal, simple case

Para este caso la vulnerabilidad se ve al abrir una foto cualquiera del catálogo, esta se ve de la siguiente manera:

https://0af300da03d97b4cc17981a900870058.web-security-academy.net/image?**filename=1.jpg**

Donde destaca la variable "filename", el cual corresponde al campo inyectable para el atacante, para este laboratorio se utiliza el ataque mas simple por lo cual se debe utilizar la siguiente sentencia:

**../../../../../../../../../../../../../../../../etc/passwd**

Esta se reemplaza por "1.jpg" y el laboratorio estará resuelto

## Lab 2 - File path traversal, traversal sequences blocked with absolute path bypass

Para este laboratorio se bloquea la capacidad de poder escalar directorios, sin embargo, solo basta con poner la ruta absoluta del archivo que queramos ejecutar para llevar acabo el ataque, por lo cual la manera de resolver el laboratio es con la siguiente sentencia:

**/etc/passwd**

## Lab 3 - File path traversal, traversal sequences stripped non-recursively

En este laboratorio ocurre que se sanitiza el uso de la sentencia "../" para poder subir directorios, este tipo de bloqueo puede ser de la siguiente manera:

```php
<?php
    $filename = $_GET['filename'];
    $newfilename = str_replace("../",'',$filename)
    include("example/dir".$newfilename);
?>
```

Es decir se reemplaza "../" por nada o un string vacio, por lo cual el ejecutar la secuencia habitual no subiremos directorios y por lo tanto el archivo que se quire ejecutar no lo hará. Para poder bypassear esta medida se puede ejecutar la siguiente sentencia:

**....//....//....//....//....//....//....//....//....//....//....//....//etc/passwd**

La sanitización borrará el primer string de tipo "../" por lo cual al tener ".. **.. /** /" solo quedará "../" y el ataque surgirá efecto en esta situación dado que se podrá escalar directorios y ejectuar el archivo deseado en la carpeta correcta.

## Lab 4 - Lab: File path traversal, traversal sequences stripped with superfluous URL-decode

Para este laboratorio el caracter "/" no es reconocido como tal, sin embargo, existe la ofuscación, para este laboratorio es necesario hacer uso de un url-encoder, puede usarse burpsuite o uno cualquiera de internet como el siguiente:

https://www.urlencoder.org/

por lo cual al url-encodear "/" nos quedará  "%2F" lo cual representa lo mismo, sin embargo, se tiene que usualmente no suele funcionar de esta forma por lo cual también se debe url-encodear "%" que queda de la siguiente manera "%25", finalmente se tiene la siguiente lo siguiente:

**". . /"  =    ". .%252f"**  

*Recordar que luego del "%" los siguientes dos bytes serán reconocidos como hexadecimal*

De esta manera para resolver el laboratorio se debe tener una sentencia de este tipo 

. .%252f. .%252f. .%252f. .%252f. .%252f. .%252f. .%252f. .%252f. .%252fetc/passwd

## Lab 5 File path traversal, validation of start of path

Para este laboratorio se tiene que el servidor pide partir de una ruta especifica para poder ejecutar la consulta, si se abre una imagen para ver la vulnerabilidad se puede observar los siguiente:

https://0a890008048ee539c3a92e0e0087002f.web-security-academy.net/image?**filename=/var/www/images/72.jpg**

Se puede observar que la ruta del archivo es totalmente distinta a la de los laboratorios anteriores teniendo de manera extra este path "filename=/var/www/images" el cual para este laboratorio, es la ruta en la que se pide partir si o si, en caso de poner alguna de las sentencias que se usaron en los laboratorios anteriores este no se ejecutará correctamente. Para poder resolver el laboratorio se debe tener una sentencia del siguiente tipo 

**/var/www/images/../../../../../../../etc/passwd **

## Lab 6 - File path traversal, validation of file extension with null byte bypass 

Para este laboratorio se tiene que el servidor verifica que el archivo tenga la extensión correspondiente, en estos laboratorios la vulnerabilidad está en una imagen del tipo "jpg" por lo cual lo que deberia estar sería la extensión ".jpg". Se tiene que para abrir por ejemplo /etc/passwd no se puede simplemente concatenar ".jpg" dado que el archivo passwd.jpg no existe, el sistema debe reconocer la extensión además de la ruta que se le está poniendo como input a la variable, una manera de hacer esto y de resolver el laboratorio es con un byte NULL con el fin de separar la ruta de la extensión de esta forma se tiene cada una por separado, de esta forma se tiene el archivo que se desea ejecutar y el sistema reconocera la extensión, es decir, se necesita una sentencia del siguiente tipo:

**../../../../../../../../../../../../../etc/passwd%00.jpg**

Lo cual esquivale a:

../../../../../../../../../../../../../etc/passwd .jpg