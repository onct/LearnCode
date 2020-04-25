<template>
<div>
    <!-- 如果在数据库没有查询到记录，show_record为false，提示当前没有记录 -->
    <div v-if='show_record'>
      <div class="prompt">还没有任何记录哦~</div>
    </div>
    <!-- 如果在数据库查询到该用户的记录，show_record默认为true，显示记录表格 -->
    <div v-else>
      <div class="table th">
        <div class="date">时间</div>
        <div class="busi">分数</div>
        <div class="mark">最后得分</div>
        <div class="net">备注</div>
      </div>
      <RecordList :key='index' v-for='(record,index) in records' :record = 'record'></RecordList>
      <p class="text-footer" v-if="!more">
        没有更多数据
      </p>
      <!-- 如果records数据一共不到15条，底部什么也不用显示 -->
      <p class="text-footer" v-else-if="records.length < 15">
      </p>
      <!-- 如果more为true，并且总记录大于15条，底部显示加载中 -->
      <p class="text-footer" v-else>
        加载中···
      </p>
    </div>
  </div>
</template>

<script>
import {get} from '@/util'
import RecordList from '@/components/RecordList'
export default {
  data () {
    return {
      show_record: false,
      userinfo: {},
      records: [],
      page: 0,
      more: true
    }
  },
  components: {
    RecordList
  },
  methods: {
    async getRecords (init) {
      if (init) {
        this.page = 0
        this.more = true
      }
      // 调用后台数据时显示「加载中」提示框
      wx.showToast({
        title: '加载中',
        icon: 'loading'
      })

      //* **需要添加的代码***
      if (this.page === 0) {
        this.records = []
      }
      // 需要传到后台的数据
      const data = {
        openid: this.userinfo.openId,

        //* **需要添加的代码***
        page: this.page
      }
      // 将后台传过来的数据保存到records变量中
      const records = await get('/weapp/getrecords', data)
      // concat是拼接数组的方法，将新查出的数据，拼接到records数组中

      //* **需要编辑的代码***
      // this.records = records.records
      this.records = this.records.concat(records.records)

      //* **需要添加的代码***
      // 每次在数据库中查找15条数据，如果查出的数据不足15条说明这是最后一页了，将more改为false
      if (records.records.length < 15 && this.page > 0) {
        this.more = false
      }
      // 通过records数组的长度来判断show_record变量为false或者true
      if (this.records.length === 0) {
        this.show_record = true
      } else {
        this.show_record = false
      }
      console.log('从后台返回的记录数据：', this.records)
      wx.hideToast()
    }
  },

  onShow () {
    const userinfo = wx.getStorageSync('userinfo')
    // 如果缓存中有userinfo的信息，说明用户登录了。
    if (userinfo.openId) {
      // 将用户信息储存到data的userinfo字段里面，this.userinfo就是指的这个字段。
      this.userinfo = userinfo
    }
    this.getRecords(true)
  },

  onShareAppMessage (e) {
    return {
      title: '真自律',
      path: '/pages/index/main',
      imageUrl: ''
    }
  },
  onReachBottom () {
    // 如果more为false，说明没有更多数据了，不需要再加载getRecords方法，return结束加载
    if (!this.more) {
      return false
    }
    // 加载下一页
    this.page = this.page + 1
    console.log('this.page', this.page)
    this.getRecords()
  },
  onPullDownRefresh () {
    this.getRecords(true)
    wx.stopPullDownRefresh()
  }
}
</script>

<style lang='scss' scoped>
.add{
    margin-top: 20px;
    margin-bottom: 10px;
    text-align:center;
  p{
      font-size: 15px;
  }
}
.th {
  width: 100%;
  height: 30px;
  line-height:30px;
  background: #EA5149;
  color: #FFFFFF;
  font-size: 16px;
  font-weight: bold;
  display: flex;
}
.prompt{
  margin-top: 50px;
  margin-bottom: 30px;
  font-size: 14px;
  color: #888888;
  text-align: center;
}
.date{
  width: 23%;
  padding-left: 60px;
}
.busi{
  width: 10%;
  margin-left: 5px;
}
.mark{
    width: 20%;
  margin-left: 10px;
}
.net{
  width: 20%;
  margin-left: 20px;
}
.text-footer{
  text-align: center;
  font-size: 12px;
  margin-bottom:5px;
  padding-top: 5px;
}
</style>