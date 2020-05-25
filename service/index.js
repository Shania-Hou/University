// Express服务器入口文件
const userApi = require('./api/userApi');
const fs = require('fs');
const path = require('path');
const bodyParser = require('body-parser');
const express = require('express');
var models = require('./db');
var mysql = require('mysql');
const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: false}));

//后端Api路由
app.use('/api/user',userApi);
//连接数据库
var conn = mysql.createConnection(models.mysql);

conn.connect();


//监听端口
app.listen(3000);
console.log('success listen at port:3000......');