#portswigger

Primeramente se ingresa con las credenciales otorgadas para posteriormente guardar el JWT otorgado a dicho usuario

![[JWT/img/noexposedkey1.png]]

Luego se repite el proceso , es decir, se desloguea y se vuelve a loguear con el mismo usuario para poder tener dos tokens distintos.

###### Key 1

eyJraWQiOiJhNjM4YWNhNi1kZTdmLTQxNDgtOTZmYS0zMzBlMGZiYzgzMzQiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsInN1YiI6IndpZW5lciIsImV4cCI6MTcwNTE2NjE2OX0.squ9gBPwtkaF34MWDKYgln2HDOAmztsBsJF2nSmL0IHuRAdj81Vd2KcpNezpSdBcB1WavIA75ZNsjj9jqPdWVDg66d67o75JJKLynIecqDhSTErJqkeHV8-bIooMbVVol9Tk7MX6suaSgO1hxU7rZpoTjSNfE8GwZMQsKnHbIpPyrdGx4tUuZ7tRCkls9dsuCEGNwC0TnOngCEnu3jTn-rqEBPrG6XB5tvjoG8TPXZQujtd0eSpWW0hTapPk9AlnKjGFFhaV9wB_hqwHOT1fmdCSd3u9A7yL3ZcWLbPTedjjYIeVFt0NHAd3psSE-i-JvjrbwofFlYpE5kpH589Seg

###### Key 2

eyJraWQiOiJhNjM4YWNhNi1kZTdmLTQxNDgtOTZmYS0zMzBlMGZiYzgzMzQiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsInN1YiI6IndpZW5lciIsImV4cCI6MTcwNTE2NzE2OX0.aO4yIfGlDFKV-iTKPDUWsBfBWsq3M3xzgC9O_FU-76CbOq3ONe6gxleDkCpKXRwPtqmXUqvdorNvYx5ymXdlSzfntSAB8IugclRFDb-5R7q6oXBrd7hnrVvnE-4il6qMzi_01Hk6JpXbhX9zh6GWRd_25Cz5-wzlulfZKThFKC8RPc3re5slg-SK-suvP2uChqXMHXLKffm4mbrAVTjmEKziCm1zN8NXVny9rA1bhKk34aPxZVmhPUhti-8m2W9a5UXkpgVpxqp4pwE06szFiv8pDbeTeqhxkEXEBxpeOdgglY-TJtUEaPUXlw0-NRNoM9fGrqOzAboUrffGi6WaPw


Con los tokens obtenidos, se lanza el siguiente comando:


```bash
sudo docker run --rm -it portswigger/sig2n <token1> <token2> 
```


![[noexposedkey2.png]]

Obteniendo un resultado del siguiente tipo:
![[noexposedkey3.png]]
Con este resultado hay que probar uno a uno los **Tampered JWT** hasta que uno lance una petición exitosa o con un código de estado 200, por lo cual es recomendable usar un petición simple, en dónde, se pueda corroborar que el token esté efectivamente siendo funcional como se muestra a continuación.
![[noexposedkey4.png]]

Al momento de realizar el laboratorio la que sirvió en este caso en particular es la del n=1 destacado
![[noexposedkey5.png]]

Con el token listo, falta realizar la firma como en un típico ataque de algoritmo de confusión, por ende, se crea la llave simétrica de forma directa ya que el script lanzado nos ofrece la llave x 509, y no hay que realizar el proceso de manera manual.


![[noexposedkey9.png]]

![[noexposedkey10.png]]

Luego tan solo falta cambiar las cabeceras a los datos deseados, como en este caso el usuario administrator


![[noexposedkey11.png]]
Para posteriormente firmar 
![[noexposedkey12.png]]


Luego con todos los preaparativos listos tan solo falta realizar la petición para llegar a un directorio con permisos de usuario priviligeado


![[noexposedkey6.png]]

Obtenemos el acceso al directorio **admin** y finalmente borramos al usuario carlos para terminar con este laboratorio


![[noexposedkey7.png]]
![[noexposedkey8.png]]
