<template>
  <div class="navbar">
    <div class="container-fluid">
      <h2>SponSync</h2>

    </div>
    <div class="navbar-left">
      <button class="login"><router-link to="/Profile" style="color:white; text-decoration: none;font-weight: bold;">Profile</router-link></button>

      
      
      <br>
      <br>
    </div>
    <div class="navbar-right">
     
      
      
      <button @click="logoutForm" style="color:white; text-decoration: none; font-weight: bold;"> Logout</button>

      
      
   
      
    </div>
    </div>
  
</template>

<script>

export default {
  name: 'InfluencerView',
  components: {
    
  },
  data(){
    return{

    }
  },
  methods:{
    logoutForm()
    {
      
    }
  }


}
</script>

<style scoped>
.navbar{
  display:flex;
  background-color: #EED3D9;
  padding:10px;
  text-align: right;
}
.navbar-left{
  display:flex;
  margin:auto;
  justify-content: left ;
  align-items: left;
  cursor:pointer;
  
}
.navbar-right{
  display:flex;
  cursor:pointer;

  
  
}
</style>
