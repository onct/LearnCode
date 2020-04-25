<template>
  <div class="book-card">
    <div class="table" width="98%">
      <div class="tr">
        <!-- 时间 -->
        <div class="date">{{create_time}}</div>
        <!-- 分数 -->
        <div class="busi">
          <!-- 为了页面样式比较整齐，如果当前分数>0，在前面加一个+号; 当前分数=0在前面加一个空格-->
          <label v-if="record.add > 0">+{{record.add}}</label>
          <label v-else-if="record.add == 0">&nbsp;0</label>
          <label v-else>{{record.add}}</label>
        </div>
        <!-- 最后得分 -->
        <div class="mark">
          <!-- 如果当前分数大于0，在分数的前面加一个空格，为了页面样式比较整齐 -->
          <label v-if="record.mark >= 0">&nbsp;{{record.mark}}</label>
          <label v-else>{{record.mark}}</label>
        </div>
        <!-- 备注 -->
        <!-- changeEllipsis方法用来控制ellipsis变量为false或者为true -->
        <div class="net" @click='changeEllipsis'>
          <label v-if="note">{{note}}</label>
          <label v-else class="no-note">点击添加</label>
        </div>
        <!-- 编辑或者取消按钮 -->
        <!-- 当点击添加或者编辑按钮，显示文本框，按钮变成取消按钮 -->
        <!-- 点击取消按钮，触发cancel方法，隐藏文本框，按钮重新变成添加或者编辑按钮 -->
        <label v-if="ellipsis">
          <div class="image" @click='cancel'><image class='img' src='/static/images/quxiao.png'></image></div>
        </label>
        <label v-else>
          <!-- note指的记录备注，默认是record.note。如果重新编辑需要根据编辑的文本实时显示，所以将note做成了变量，src变量用到了三元函数。当文本框中有文字，显示编辑按钮；当文本框中没有文字，不显示按钮 -->
          <div class="image" @click='changeEllipsis'><image class='img' :src="note? src : ''"></image></div>
        </label>
      </div>
    </div>
    <!-- 点击添加或者编辑按钮显示的文本框 -->
    <div class="hide" v-if="ellipsis">
      <button class="btn" @click='addNote'>
        <label v-if="record.note">修改</label>
        <label v-else>添加</label>
      </button>
      <!-- input文本框绑定了note变量，在编辑文本框时，显示的备注文字，会根据文本框中编辑的文字变化 -->
      <input v-model='note'
            class="input"
            maxlength='10'
            placeholder="最多输入10个字">
    </div>
  </div>
</template>

<script>
import {formatTime} from '../utils/index.js'
import {post, showModal} from '@/util'
export default {
  data () {
    return {
      create_time: formatTime(new Date(this.record.create_time)),
      ellipsis: false,
      note: this.record.note,
      src: '/static/images/搜索.png'
    }
  },
  props: ['record'],
  methods: {
    // ellipsis为true时，显示文本框；为false隐藏文本框
    changeEllipsis () {
      this.ellipsis = !this.ellipsis
    },
    // 点击取消按钮时，要改变ellipsis，同时将note重置为修改前的状态
    cancel () {
      this.ellipsis = !this.ellipsis
      this.note = this.record.note
    },
    async addNote () {
      const data = {
        id: this.record.id,
        note: this.note
      }
      try {
        const res = await post('/weapp/updatenote', data)
        console.log('从后端返回的执行正确的信息是：', res)
        // 点击添加或者修改按钮，隐藏掉文本框
        this.ellipsis = false
        // 将从父组件传过来的record中的note值更新为修改后的值
        this.record.note = this.note
      } catch (e) {
        showModal('失败', '请重新提交哦~')
        console.log('从后端返回的执行错误的信息是：', e)
      }
    }
  }
}
</script>

<style lang='scss'>
.book-card{
  background: #FFFFFF;
  margin-bottom:6px;
  .table {
    border: 0px solid darkgray;
    font-size: 15px;
    height: 42px;
    line-height:42px;
    .tr {
      display: flex;
      width: 100%;
    }
    .date{
      width: 40%;
      margin-left: 10px;
    }
    .busi{
      width: 10%;
      font-weight:bold;
    }
    .mark{
      width: 15%;
      margin-left: 20px;
      font-weight:bold;
    }
    .net{
      width: 16%;
      text-align:center;
      width:60px;
      overflow:hidden;
      text-overflow:ellipsis;
      white-space:nowrap;
      font-size: 14px;
      margin-left: 5px;
      line-height:42px;
      .no-note{
        text-decoration:underline;
        color:#C0C0C0;
        font-size: 13px;
      }
    }
    .image{
      padding-top:1px;
      float: right;
      margin-left: 5px;
    }
  }
  .hide{
    background: #F0F0F0;
    font-size: 15px;
    padding: 10px 10px 3px 30px;
    .input{
      width:60%;
      height:30px;
      background:#FFFFFF;
      border:1px solid black;
      border-radius: 5px;
      text-align:center;
    }
    .btn{
      color:white;
      background:#EA5A49;
      padding-left: 15px;
      margin-right:20px;
      border-radius: 5px;
      font-size: 13px;
      line-height: 30px;
      height: 30px;
      width: 18%;
      float:right;
    }
  }
  .img{
    width: 13px;
    height: 13px;
    margin-right: 5px;
  }
}
::-webkit-scrollbar {
  width: 0;
  height: 0;
  color: transparent;
}
</style>