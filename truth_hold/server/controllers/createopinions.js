//引入server/qcloud.js文件，qcloud.js文件是mysql的软件工具包，引入后我们也可以使用knex来操作数据库了
const {mysql} = require('../qcloud')

//module.exports是向外暴露代码，后面跟着箭头函数（就是函数的一种简写形式，在ES6语法的讲解中提过）
module.exports = async (ctx) => {
  //ctx.request.body用来获取post请求的参数
  const {opinion,src,wechat,openid} = ctx.request.body
  try{
    //knex语法，插入数据到opinions数据表中
    await mysql('opinions').insert({
      opinion,src,wechat,openid,
    })
    // 执行的结果会保存到ctx.state中，也就是从后端返回到前端的数据
    // 执行成功返回的数据，code设为0
    ctx.state.data = {
      code: 0,
      msg: 'success'
    }
    console.log("执行成功")
  }catch(e){
    console.log("执行错误:",e)
    // 执行失败返回的数据，code设为-1
    ctx.state = {
      code: -1,
      data: {
        msg: '添加失败' + e.sqlMessage
      }
    }
  }
}