<template>
<div>
    <div class="contain">
      <div class="row">
        <label class="name">意见与反馈</label>
      </div>
      <div class="row text">
        <div>
          <textarea
            v-model='opinion'
            class = "input"
            maxlength='200'
            placeholder="点击这里填写你的建议、问题反馈、合作等信息，我会认真对待每一条信息~"
          ></textarea>
          <!-- word_count用来保存实时输入字数的长度 -->
          <label class="word-count">{{word_count}}/200</label>
        </div>
      </div>
      <div class="row">
    <div>
      <label class="name">相关截图（选填）</label>
      <label class="img-count">{{img_count}}/2</label>
    </div>
    <!-- v-for是vue的语法，循环语句，循环显示当前上传的照片 -->
    <label v-for="(item, index) in src" :key="index">
      <img class="img" :src="item" >
    </label>
    <!-- v-if是判断语句，判断当前照片数量如果小于2张，就显示添加照片的按钮；反之就不显示了在这里添加点击事件，点击按钮调用uploadPicture方法上传照片 -->
    <label v-if="img_count < 2" @click="uploadPicture">
      <img class="add-img" :src="addimage">
    </label>
    </div>
    <div class="row">
    <div class="name">微信号（选填）</div>
    <input
      v-model='wechat'
      class = "wechat-input"
      maxlength='20'
      placeholder="如果想要详细交流，可以点击这里留下微信号哦~"
        />     
    </div>
    </div>
    <button @click="summit">提交</button>
  </div>
</template>

<script>
import {showModal, post} from '@/util'
export default {
  data () {
    return {
      opinion: '',
      word_count: 0,
      addimage: '/static/images/创作.png',
      img_count: 0,
      src: [],
      wechat: ''
    }
  },
  methods: {
    uploadPicture () {
      // 将this保存到that上面
      let that = this
      wx.chooseImage({
        count: 2,
        sizeType: ['original', 'compressed'],
        sourceType: ['album', 'camera'],
        success (res) {
          // tempFilePath可以作为img标签的src属性显示图片
          const tempFilePaths = res.tempFilePaths
          // 用that.src来调用data函数定义的src变量
          that.src.push(tempFilePaths)
          console.log('that.src', that.src)
        }
      })
    },
    async summit () {
      // 当反馈的字数大于0时，可以提交反馈信息
      if (this.word_count > 0) {
        try {
          // data是要提交给后端的数据，其中包含openid、opinion意见信息、src图片链接、wechat用户微信
          const data = {
            openid: wx.getStorageSync('userinfo').openId,
            opinion: this.opinion,
            src: this.src.join(','),
            wechat: this.wechat
          }
          // 通过这行代码请求请求后端服务器，并传递参数data
          // await我们再ES6知识点中讲过，等后端执行完并获取到返回数据之后，再往下执行
          const res = await post('/weapp/createopinions', data)
          console.log('从后端返回的执行正确的信息是：', res)
          showModal('提交成功', '已将你的反馈提交给了开发者~')
        } catch (e) {
          // 如果执行失败，util.js中的请求方法，会将返回信息的状态变成rejected
          // rejected状态的信息会被当成错误捕捉到
          console.log('从后端返回的执行错误的信息是：', e)
          showModal('提交失败', '服务器出了一点错误~请稍后再试')
        }
        // 当反馈的字数为0时，提示反馈内容不能为空
      } else {
        showModal('提交失败', '反馈内容不能为空哦~')
      }
    }
  },
  watch: {
  // 与需要监控的变量opinion同名的方法
    opinion () {
      this.word_count = this.opinion.length
    },
    src () {
      this.img_count = this.src.length
    }
  }
}
</script>

<style lang='scss'>
.contain{
  background:#FFFFFF;
  font-size:15px;
  .text {
    height: 110px;
  }
  .row{
    border-bottom: 1px #E8E8E8 solid;
    padding: 5px 15px;
    .name {
      width:80%;
      height: 40px;
      line-height: 40px;
    }
    .input {
      width:100%;
      height:85px;
      font-size:14px;
      padding-top:5px;
    }
    .word-count {
      float:right;
      color: #808080;
    }
    .img-count {
      float:right;
      line-height: 40px;
      color: #808080;
    }
    .add-img {
      width:80px;
      height:80px;
    }
    .img {
      width:66px;
      height:66px;
      margin-bottom:7px;
      margin-right: 10px;
    }
    .wechat-input{
      font-size:14px;
    }
  }
}
button {
  margin:20px auto;
  width:90%;
  border-radius: 5px;
  background:#EA5149;
  font-size:16px;
  color:#FFFFFF;
  font-weight:bold;
}

</style>