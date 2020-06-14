<template>
  <div id="app">
    <a-layout>
     <a-layout-content>
      <router-view />
     </a-layout-content>
    </a-layout>
    
    
  </div>
</template>
<script>
export default {
  name: 'App',
};
</script>

<style href='ant-design-vue/dist/antd.css'></style>
<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width:800px;
  height:400px;
  background: #f0f2f5;
  margin-top:34px;
}

body{
  background: #f0f2f5;
}
</style>
