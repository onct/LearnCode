import config from './config'
export function showSuccess (text) {
  // wx.showToast是小程序现成的API，其中title是提示的内容,icon是显示的图标
  wx.showToast({
    title: text,
    icon: 'success'
  })
}
export function showModal (title, content) {
  wx.showModal({
    title,
    content,
    showCancel: false
  })
}
function request (url, method, data) {
  // 将wx.request请求API包装成一个Promise对象
  return new Promise(
    (resolve, reject) => {
      // wx.request是微信的API
      wx.request({
        url: config.host + url,
        method: method,
        data: data,
        success: function (res) {
          console.log('请求返回到前端的信息：', res)
          // 当返回信息中res.data.code为0时，说明执行成功，将状态变成resolved
          // 如果为-1说明执行失败，将状态变成rejected
          if (res.data.code === 0) {
            resolve(res.data.data)
          } else {
            reject(res.data)
          }
        }
      })
    })
}
export function get (url, data) {
  // 返回的是一个Promise对象
  return request(url, 'GET', data)
}
// post工具函数
export function post (url, data) {
  // 返回的是一个Promise对象
  return request(url, 'POST', data)
}
