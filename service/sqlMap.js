//sql语句映射文件
var sqlMap = {
    user:{
        add: 'insert into user(username,password,age,grade,email) values (?,?,?,?,?)',
        select_username: 'select * from user where username = ?',
        select_password: 'select * from user where password = ?',

    },
    university:{
        select:'select * from university' ,
        select_year:'select * from ulist_year where u_year = ?',
        select_pro:'select * from university where u_pro = ? order by u_id'
    },
    speciality:{
        select:'select * from splist_year where sp_year = ? and sp_name = ?',
        select2019:'select * from splist_year where sp_year = 2019 and sp_name="软件工程" '
    },
    score:{
        selectScore:'select * from university where u_name in (select uname from pro_scoreline where year=2019 and score<? and sp_type=?)',
    }
}
module.exports = sqlMap;
