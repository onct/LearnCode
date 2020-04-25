const {mysql} = require('../qcloud')

module.exports = async (ctx) => {
  const {openid} = ctx.request.body
  try{
    const res = await mysql('records')
        .where("openid",openid).del()
    // 执行成功返回的数据
    ctx.state.data = {
      code: 0,
      msg: 'success'
    }
    console.log("执行成功")
  }catch(e){
    console.log("执行错误:",e)
    // 执行失败返回的数据
    ctx.state = {
      code: -1,
      data: {
        msg: '清除失败' + e.sqlMessage
      }
    }
  }
}