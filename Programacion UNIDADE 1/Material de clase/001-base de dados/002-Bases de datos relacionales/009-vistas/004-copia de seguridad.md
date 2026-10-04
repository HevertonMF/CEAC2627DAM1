1.-Abrís terminal (de Linux, no de MySQL) - si hace falta, exit;

2.-Ponéis esto:
mysqldump -u root -p [tubasededatos] > copiadeseguridad.sql

3.-Por ejemplo:
sudo mysqldump -u root -p empresadan2627 > copiadeseguridad.sqlexit
4.-Acabáis de hacer una copia de seguridad y eso es SAGRADO

5.-Opcionalmente, en el ordenador de destino (te llevas la base a otro ordenador):
sudo mysql -u root -p empresadan2627 < copiadeseguridad.sql

mysqldump -u root -p empresadan2627 > backup.sql


