# joboAdvisor

JOBO es un programa del Aytm. de Madrid para fomentar la cultura entre los jovenes. Mediante tu carnet JOBO puedes asistir gratis a espectáculos que se realizan en los distintos 
teatros y espacios de gestión municipal. Para conseguir las entradas para estos no hay ninguna newsletter ni nada parecido. Tienes que meterte en su pagina web y ver si han 
publicado nuevos espectaculos. Ante la incomodidad de tener que meterte periodicamente a ver si encuentras algo nuevo (y que no se haya agotado ya) he desarrollado esta
herramienta. 

joboAdvisor automatiza la busqueda de nuevos espectaculos y te envía un mail en el caso de que haya un nuevo espectáculo disponible.

## Instalación y uso

En primer lugar tienes que ejecutar el script init.py. Este script simplemente te crea una base de datos donde se añadiran los espectáculos de los que ya se te ha avisado
para no enviarte mails redundantes.

Después tienes que tener el archivo config.json configurado con tus datos, por un lado necesitamos el mail y contraseña con el que accedes a JOBO y por otro el mail y contraseña
desde el que quieres que se envíe la información con los espectáculos nuevos. Luego tienes que introducir la lista de mails a los que quieres que se envíe la información. Por
último tienes que añadir la dirección donde tienes el archivo "chromedriver.exe" (te lo puedes descargar desde aquí https://chromedriver.chromium.org/).

Una vez has seguido los dos pasos anteriores ya puedes ejecutar el script main.py que es el que hace la busqueda de nuevos espectaculos mediante web scrapping. 

Si quieres automatizar el proceso para que esta busqueda se haga de manera periódica configura el archivo joboAdvisor.bat para que ejecute el archivo main.py
