module.exports = {
    publicPath: 'http://localhost:5173/',
    outputDir: '../static/dist',
    indexPath: '../../portaView/index.html',

    configureWebpack: {
        devServer: {
            devMiddleware: {
            writeToDisk: true
            }
        }
    }
};