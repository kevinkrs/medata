module.exports = {
  productionSourceMap: true, // NOTE: this is default
  configureWebpack: {
  devtool: 'source-map', 
  },
  pages: {
    popup: {
      template: 'public/browser-extension.html',
      entry: './src/popup/main.js',
      title: 'Popup'
    }
  },
  pluginOptions: {
    browserExtension: {
      components: {
        background: true,
        contentScripts: true,
      },
      componentOptions: {
        
      }
    }
  },
}