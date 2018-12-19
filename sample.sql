select id,name,email
from users u join adress a on u.id = a.user_id
where u.del_flg = 0 and u.age > 50
