<template>
    <div>
        <div class="top">
          <div class="userinfo" >
            <!-- 取userinfo变量中的avatarUrl字段，也就是微信头像的链接 -->
            <img :src="userinfo.avatarUrl" alt="">
          </div>
          <div class="name">
            <!-- 取userinfo变量中的nickName字段，也就是微信昵称 -->
            <label>{{userinfo.nickName}}</label>
            <p class="notice">{{quote}}</p>
          </div>
        </div>
  
        <div class="contain">
            <div class="row" @click="showInstrution">
              <label class="left">
                <img class="img" src="../../../static/images/首页 selected.png">
              </label>
              <label class="name">&nbsp;&nbsp;操作指引</label>
              <label class="right">
                >
              </label>
            </div>
            <div class="row">
              <label class="left">
                <img class="img" src="../../../static/images/社区 black.png">
              </label>
              <label class="name">&nbsp;&nbsp;小程序开发实战课程</label>
              <label class="right">
                >
              </label>
            </div>
            <div class="row" @click='deleteConfirm'>
              <label class="left">
                <img class="img" src="/static/images/创作.png">
              </label>
              <label class="name">&nbsp;&nbsp;清空记录</label>
              <label class="right">
                >
              </label>
            </div>
            <div class="row" @click='showOpinion'>
              <label class="left">
                <img class="img" src="/static/images/创作.png">
              </label>
              <label class="name">&nbsp;&nbsp;意见反馈</label>
              <label class="right">
                >
              </label>
            </div>
        </div>
      </div>
</template>
<script>
import {post, showModal, showSuccess} from '@/util'
export default {
  data () {
    return {
      // 用户信息
      userinfo: {},
      quote: ''
    }
  },
  methods: {
    rankArry () {
      var a = Math.random() + ''
      var rank1 = a.charAt(3)
      var quotes = [
        '不奋发，则心日颓靡；不检束，则心日恣肆',
        '自制是一种秩序，一种对于快乐与欲望的控制',
        '哪怕一点小小的克制，也会使人变得强而有力',
        '做一个自律的人，像优秀的人学习，然后做好自己',
        '真正的自由是在所有时候都能控制自己',
        '每天爱自己多一点！！！',
        '如果连自己都不能控制，有什么资格去谈自己想要的',
        '登峰造极的成就源于自律',
        '自我控制是最强者的本能',
        '立志言为本，修身行乃先'
      ]
      this.quote = quotes[rank1]
    },
    async deleteRecords () {
      try {
        const res = await post('/weapp/deleterecords', {openid: this.userinfo.openId})
        console.log('从后端返回的执行正确的信息是：', res)
        showSuccess('记录已清空~')
      } catch (e) {
        showModal('清空失败', '请重试哦~')
        console.log('从后端返回的执行错误的信息是：', e)
      }
    },
    deleteConfirm () {
      var that = this
      // 用户点击确认后，调用上面添加的deleteRecords方法
      wx.showModal({
        content: `清空之后不能恢复哦~确定要清空吗？`,
        success: function (res) {
          if (res.confirm) {
            that.deleteRecords()
          }
        }
      })
    },
    showOpinion () {
      wx.navigateTo({
        url: '/pages/opinion/main'
      })
    },
    showInstrution () {
      wx.navigateTo({
        url: '/pages/instruction/main'
      })
    }
  },
  onShareAppMessage (e) {
    return {
      title: '真自律',
      path: '/pages/index/main',
      imageUrl: ''
    }
  },
  onShow () {
    this.rankArry()
  },
  mounted () {
    const userinfo = wx.getStorageSync('userinfo')
    if (userinfo.openId) {
      this.userinfo = userinfo
    }
  }
}
</script>
<style lang='scss'>
.contain{
  margin-top: 10px;
  background:#FFFFFF;
  font-size:15px;
  .row{
    padding: 0px 18px;
    border-bottom: 1px #E8E8E8 solid;
    height: 55px;
    line-height: 55px;
    .img {
      float:left;
      width: 20px;
      height: 20px;
      padding-top:16px;
    }
    .name {
      float:left;
    }
  }
  .right {
    float: right;
    color: #C8C8C8;
    line-height:55px;
  }
  .left {
    width:80%;
  }
}  

.top{
  height: 80px;
  width: 100%;
  background:#EA5149;
  padding-top: 30px;
  display: block;
  .userinfo{
    padding-bottom: 5px;
    float: left;
    img{
      width: 120rpx;
      height:120rpx;
      margin: 10rpx;
      border-radius: 1px;
      border: 1px #D0D0D0 solid;
    }
  }
  .name{
    padding-top: 30px;
    padding-left: 5px;
    color: #FFFFFF;
    font-size: 16px;
    float: left;
    .underline{
      border: 1px solid #ffffff;
      border-radius:5px;
      text-align:center;
    }
    .notice{
      color: #D8D8D8;
      font-size: 12px;
    }
    .a-line{
      background:#EA5149;
      border: none;
      display: inline;
      font-size: 16px;
      color: #FFFFFF;
      text-decoration:underline;
    }
  }
}

</style>