const {mysql} = require('../qcloud')

module.exports = async (ctx) => {
  const {openid,page} = ctx.request.query
  try{
    const records = await mysql('records')
                            .select('id','add','mark','note','create_time')
                            .where("openid",openid)
                            .orderBy('id','desc')
                            .limit(15).offset(Number(page) * 15)
    // 执行成功返回的数据
    ctx.state.data = {
      records
    }
  }catch(e){
    // 执行失败返回的数据
    ctx.state = {
      code: -1,
      data: {
        msg: '获取失败' + e.sqlMessage
      }
    }
  }
}