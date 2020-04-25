const {mysql} = require('../qcloud')

module.exports = async (ctx) => {
  const {openid} = ctx.request.query
  try{
    const res = await mysql('records')
                      .where("openid",openid)
                      .select('mark')
                      .orderBy('id','desc')
                      .first()
    if(res){
      var mark = res.mark
    }else{
      var mark = 0
    }
    console.log("当前分数",mark)
    // 执行成功返回的数据，将最后这条记录的mark字段也传回到前端
    ctx.state.data = {
      code: 0,
      mark:mark,
      msg: 'success'
    }
    console.log("执行成功")
  }catch(e){
    console.log("执行错误:",e)
    // 执行失败返回的数据
    ctx.state = {
      code: -1,
      data: {
        msg: '获取失败' + e.sqlMessage
      }
    }
  }
}