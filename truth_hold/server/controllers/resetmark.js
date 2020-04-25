const {mysql} = require('../qcloud')

module.exports = async (ctx) => {
  const {openid} = ctx.request.body
  try{
    let add = 0
    let mark = 0
    let note = "清零"
    //往数据表records中添加一条新的记录，mark字段为0，add为0，note备注为"清零"
    await mysql('records').insert({
      openid, add, mark, note
    })
    //执行成功返回到前端的数据
    ctx.state.data = {
      code: 0,
      msg: 'success'
    }
    console.log("执行成功")
  }catch(e){
    console.log("执行错误:",e)
    //执行失败返回到前端的数据
    ctx.state = {
      code: -1,
      data: {
        msg: '清零失败' + e.sqlMessage
      }
    }
  }
}