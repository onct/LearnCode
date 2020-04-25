const {mysql} = require('../qcloud')

module.exports = async (ctx) => {
  const {id,note} = ctx.request.body
  try{
    const res = await mysql('records')
                    .where("id",id)
                    .update("note",note)
    // 执行成功返回的数据
    ctx.state.data = {
      code: 0,
      msg: 'success'
    }
  }catch(e){
    // 执行失败返回的数据
    ctx.state = {
      code: -1,
      data: {
        msg: '撤销失败' + e.sqlMessage
      }
    }
  }
}