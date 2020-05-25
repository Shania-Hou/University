//测试用api示例
var models = require('../db');
var express = require("express");
var url = require("url")
var router = express.Router();
var mysql = require('mysql');
var $sql = require('../sqlMap');

//连接数据库
var conn = mysql.createConnection(models.mysql);

conn.connect();
var jsonWrite = function(res,ret){
    if(typeof ret === 'undefined'){
        res.json({
            code:'1',
            msg:'操作失败'
        });
    }else{
        res.json(ret);
    }
}

//增加用户接口
router.post('/addUser',(req,res) => {
    var sql_name = $sql.user.select_username;
    var sql = $sql.user.add;
    var params = req.body;
    console.log(params);
    conn.query(sql_name,params.username,function(err,result){
        if(err){
            console.log(err)
        }
        if(result[0] === undefined){
            conn.query(sql,[params.username,params.password,params.age,params.grade,params.email],function(err,result){
                if(err){
                    console.log(err);
                }else{
                    jsonWrite(res,result);
                }
            })
        }else{
            res.send("-1")  //当前注册username与数据库重复时，data返回-1
        }
    })
});

//查找用户接口
router.post('/checkUser',(req,res)=>{
    var sql_name = $sql.user.select_username;
    var sql_password = $sql.user.select_password;
    var params = req.body;
    conn.query(sql_name,params.username,function(err,result){
        if(err){
            console.log(err);
        }
        
        if(result[0] === undefined){
            res.send("-1")  //查询不出username，data返回-1

        }else{
            conn.query(sql_password,params.password,function(err,result){
                if(err){
                    console.log(err);
                }
                if(result[0] === undefined){
                    res.send("0")       //username正确而password错误  返回0
                }else{
                    jsonWrite(res,result);
                }
            })
        }
    })
})

//获取全部大学列表
router.get('/university', (req, res) => {
    const sql = $sql.university.select;
    conn.query(sql,function(err, result,fields){
      if (err) {
        console.log(err)
      } 
      if (result){
        console.log(result)
        res.send(result)
      }
    })
  })

//获取某省大学
router.get('/getUniversityByPro',(req,res)=>{
    var params = url.parse(req.url,true).query.pro;
    var sql = $sql.university.select_pro;
    console.log(params);
    // sql_year = req.params.year
    // console.log(sql_year);
    conn.query(sql,params,function(err,result,fields){
        if (err) {
            console.log(err)
        } 
        if (result){
            console.log(result)
            res.send(result)
        }
    })

})

//获取某年大学排名
router.get('/getUList',(req,res)=>{
    var params = url.parse(req.url,true).query.year;
    var sql = $sql.university.select_year;
    console.log(params);
    conn.query(sql,params,function(err,result,fields){
        if (err) {
            console.log(err)
        } 
        if (result){
            // console.log(result)
            res.send(result)
        }
    })
})

//获取某年某专业排名
router.get('/getUniversityByYearAndSpeciality',(req,res)=>{
    var params = url.parse(req.url,true).query
    var sql = $sql.speciality.select;
    console.log(params);
    conn.query(sql,[params.year,params.speciality],function(err,result,fields){
        if (err) {
            console.log(err)
        } 
        if (result){
            console.log(result)
            res.send(result)
        }
    })
})

//获取全部专业列表
router.get('/speciality2020_soft', (req, res) => {
    const sql = $sql.speciality.select2019;
    conn.query(sql,function(err, result,fields){
      if (err) {
        console.log(err)
      } 
      if (result){
        console.log(result)
        res.send(result)
      }
    })
  })


//推荐大学
router.get('/tuijian',(req,res)=>{
    var params = url.parse(req.url,true).query
    var sql = $sql.score.selectScore;
    console.log(params);
    conn.query(sql,[params.score,params.type],function(err,result,fields){
        if (err) {
            console.log(err)
        } 
        if (result){
            console.log(result)
            res.send(result)
        }
    })
})

module.exports = router;