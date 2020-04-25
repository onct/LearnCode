const CONF = {
    port: '5757',
    rootPathname: '/data/wwwroot/www.qinaxun.cn/',
    serverHost: 'https://www.qinaxun.cn/',
    tunnelServerUrl: '',
    tunnelSignatureKey: '27fb7d1c161b7ca52d73cce0f1d833f9f5b5ec89',

    qcloudAppId:'1253727879',
    qcloudSecretId:'AKIDiKg5RM8oIVYLHyIDkBMH3zgZDqKXmD3d',
    qcloudSecretKey:'UjgOYR5tR37xWCxRdrjNkvuc3EekaLuD',
    networkTimeout:30000,

    // 微信小程序 App ID
    appId: 'wxfa8ca84bdebaa05a',

    // 微信小程序 App Secret
    appSecret: 'c615fd1c42719b5ffd049c3f8273aeb0',

    // 是否使用腾讯云代理登录小程序
    useQcloudLogin: false,

    /**
     * MySQL 配置，用来存储 session 和用户信息
     * 若使用了腾讯云微信小程序解决方案
     * 开发环境下，MySQL 的初始密码为您的微信小程序 appid
     */
    mysql: {
        host: 'localhost',
        port: 3306,
        user: 'root',
        db: 'cAuth',
        pass: 'miaode123',
        char: 'utf8mb4'
    },

    cos: {
        /**
         * 地区简称
         * @查看 https://cloud.tencent.com/document/product/436/6224
         */
        region: 'ap-guangzhou',
        // Bucket 名称
        fileBucket: 'qcloudtest',
        // 文件夹
        uploadFolder: ''
    },

    // 微信登录态有效期
    wxLoginExpires: 7200,
    wxMessageToken: 'abcdefgh'
}

module.exports = CONF
