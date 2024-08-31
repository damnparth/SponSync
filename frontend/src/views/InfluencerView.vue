<template>
  <div>
  <div class="navbar">
    <div class="container-fluid">
      <h2>SponSync</h2>

    </div>
    <div class="navbar-left">
      <button class="login" @click="viewsNotifs">Notifications</button>
      
      
      
      <br>
      <br>
    </div>
    <div class="navbar-right">
      <button class="login"><router-link to="/Profile" style="color:white; text-decoration: none;font-weight: bold;">Profile</router-link></button>



     
      
      
      <button @click="logoutForm" style="color:white; text-decoration: none; font-weight: bold;"> Logout</button>

      
      
   
      
    </div>

    
    </div>
    <div class="div">
    <input type="text" placeholder="Search Campaigns" class="search-bar">
    
  
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
      axois.post
      
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
.search-bar{
  margin-left: 100px;
  
  margin-top: 20px;
  height: 35px;
  width: 700px;
  padding-left: 500px;
  margin-right: 100px;

}
</style>
