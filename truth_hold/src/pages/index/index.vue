<template>
  <div>
    <div v-if="showLogin">
      <loginWindow @changeShow="getModel(arguments)"></loginWindow>
    </div>
    <div class="show">
      <div class="button">
        <div class="btn1 right" @click='recall'>撤销</div>
        <div class="btn0" @click='reset'>清零</div>
      </div>
      <div class="mark-text">当前分数</div>
      <div class="mark-text">{{mark}}</div>
    </div>
    <div class="row">
      <div class="button right" @click="addMark(1)">+1</div>
      <div class="button left" @click="addMark(-1)">-1</div>
    </div>
    <div class="row">
      <div class="button right" @click="addMark(+5)">+5</div>
      <div class="button left" @click="addMark(-5)">-5</div>
    </div>
  </div>
</template>

<script>
  import {showModal, post, get} from '@/util'
  import loginWindow from '@/components/loginWindow'
  export default{
    components: {
      loginWindow
    },
    data () {
      return {
        mark: 0,
        userinfo: {},
        showLogin: false
      }
    },
    methods: {
      // addMark(add){
      //   this.mark = this.mark+add
      //   console.log("this.mark" , this.mark)
      // },
      async addMark (add) {
        try {
          const data = {
            openid: this.userinfo.openId,
            add: add
          }
          // 请求后端，找到server/controllers/createrecord.js文件
          const res = await post('/weapp/createrecord', data)
          console.log('从后端返回的执行正确的信息是：', res)
          this.mark = this.mark + add
        } catch (e) {
          showModal('失败', '请重试哦~')
          console.log('从后端返回的执行错误的信息是：', e)
        }
      },
      async getCurrentMark () {
        try {
          const res = await get('/weapp/getmark', {openid: this.userinfo.openId})
          console.log('从后端返回的执行正确的信息是：', res)
          this.mark = res.mark
        } catch (e) {
          showModal('失败', '页面加载失败，请下拉页面重试哦~')
          console.log('从后端返回的执行错误的信息是：', e)
        }
      },
      async resetMart () {
        // 如果当前总分不为0，继续往下执行
        if (this.mark !== 0) {
          // try...catch抓取后端传回的错误
          try {
            // 请求后端，通过'/weapp/resetmart'链接，找到server/controllers/resetmart.js文件
            const res = await post('/weapp/resetmark', {openid: this.userinfo.openId})
            console.log('从后端返回的执行正确的信息是：', res)
            // 将当前页面显示的总分改为0
            this.mark = 0
          } catch (e) {
            showModal('失败', '请重试哦~')
            console.log('从后端返回的执行错误的信息是：', e)
          }
        }
      },
      async recall () {
        try {
          const res = await post('/weapp/deletemark', {openid: this.userinfo.openId})
          console.log('从后端返回的执行正确的信息是：', res)
          this.mark = res.mark
        } catch (e) {
          showModal('失败', e.data.msg)
          console.log('从后端返回的执行错误的信息是：', e)
        }
      },
      reset () {
        var that = this
        wx.showModal({
          content: `确定要清零吗？`,
          success: function (res) {
            if (res.confirm) {
              that.resetMart()
            }
          }
        })
      },
      getModel (val) {
        // 将第一个信息false赋值到showLogin变量中，控制登录弹窗消息
        this.showLogin = val[0]
        // 将第二个信息赋值到userinfo变量中
        this.userinfo = val[1]
        this.getCurrentMark()
      }
    },
    onPullDownRefresh () {
      this.getCurrentMark()
      // 获取完当前分数后，停止下拉刷新的状态
      wx.stopPullDownRefresh()
    },
    onShareAppMessage (e) {
      return {
        title: '真自律',
        path: '/pages/index/main',
        imageUrl: ''
      }
    },
    mounted () {
      const userinfo = wx.getStorageSync('userinfo')
      // 如果缓存中有userinfo的信息，说明用户登录了。
      if (userinfo.openId) {
        // 将用户信息储存到data的userinfo字段里面，this.userinfo就是指的这个字段。
        this.userinfo = userinfo
      } else {
        wx.hideTabBar()
        this.showLogin = true
      }
  
      this.getCurrentMark()
    }

  }
</script>

<style lang='scss'>
.show{
  text-align:center;
  height:266px;
  background: #EA5149;
  margin-bottom:5px;
  color: #FFFFFF;
  font-weight:bold;
  .mark-text{
    font-size: 20px;
    padding:28px;
  }
  .mark{
    font-size: 88px;
  }
  .button{
    margin:0 10px;
    height: 30px;
    line-height:30px;
    text-align:center;
    font-size: 15px;
    font-weight:bold;
    background:#EA5149;
    .btn0{
      width: 60px;
      border-radius: 15px;
      border:1px dashed #feb600;
    }
    .btn1{
      width: 60px;
      border-radius: 15px;
      border:1px dashed #feb600;
    }
  }
}
.row{
  margin: 40px 56px;
  .button{
    width: 70px;
    height: 70px;
    line-height:70px;
    border-radius: 20%;
    border: none;
    text-align:center;
    font-size: 25px;
    color:#FFFFFF;
    font-weight:bold;
  }
}
.right{
  background:#EA5149;
  float: right;
}
.left{
  background:#feb600;
  margin-right:80px;
}
</style>
