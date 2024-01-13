

En primera instancia se inicia sesión con las credenciales que fueron otorgadas **wiener:peter**, para posteriormente capturar la petición en donde se encuentra el JWT. **Para este laboratorio se asume que el servidor almacena su llave pública en un archivo X.509 PEM**. 

![[asd1.png]]

Para proseguir se necesita encontrar la llave pública del servidor, como esto es un laboratorio controlado literalmente se nos dice en donde se encuentra.

![[pathkeys.png]]

Se puede ingresar a la dirección en donde se encuetra y obtener dicha llave pública.

![[exposedkey.png]]
Con esto se procede a crear una nueva llave de tipo RSA, en donde, como llave se utilizará la pública encontrada en el servidor.

![[newrsakeywithexposedkey.png]]

Se copia la llave RSA creada como un tipo PEM

![[copypemkey.png]]

Luego se tiene que convertir este formato PEM a un formato de base64

![[base64decodedkey.png]]

Posteriormente se crea una llave de tipo simetrica, para luego insertar la llave que tenemos en base64 en su parámetro **"k"**.

![[simetrickeywithbase64.png]]

De esta forma ya se tiene todo lo necesario para que el servidor reconozca la firma como una legitima, sin embargo, no hay que olvidar cambiar las cabeceras del JWT por las deseadas. Dado la naturaleza del ataque también de suma importancia cambiar la cabecera **alg** a **HS256**

![[changeheaders.png]]

Finalmente se debe firmar el JWT con los parámetros cambiados y con la llave que creamos.


![[signature.png]]

De esta forma se puede proceder al ingreso a rutas privilegiadas como usuario administrador o para este caso como el usuario **administrator** 

![[adminpath.png]]

![[success.png]]

Finalmente, para resolver el laboratorio se borra al usuario **carlos**.

![[solvedlab.png]]

