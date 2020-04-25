const {mysql} = require('../qcloud')

module.exports = async (ctx) => {
  const {openid,add} = ctx.request.body
  try{
    //查找出最后一条记录
    const res = await mysql('records')
        .where("openid",openid)
        .select('mark')
        .orderBy('id','desc').first()
    //得到最后一条记录的分数
    if(res){
      var mark = res.mark
    }else{
      var mark = 0
    }
    //当前总分 = 最后一条记录的分数 + 本次操作的分数
    mark = mark + add
    console.log("当前分数为：",mark)
    //将openid、本次操作的分数、当前总分
    await mysql('records').insert({
      openid, add, mark
    })
    //执行成功返回到前端的数据
    ctx.state.data = {
      code: 0,
      msg: 'success'
    }
    console.log("执行成功")
  }catch(e){
    console.log("执行错误：",e)
    //执行失败返回到前端的数据
    ctx.state = {
      code: -1,
      data: {
        msg: '添加失败' + e.sqlMessage
      }
    }
  }
}