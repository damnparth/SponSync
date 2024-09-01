<template>
  <div>
  <div class="navbar">
    <div class="container-fluid">
      <h2 >SponSync</h2>

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
    <input type="text" placeholder="Search Campaigns" class="search-bar" @keyup="searchCampaigns">
    
    <div class="campaign-pill">
      <h2 style="color: white;">campaign name</h2>
      <button class="campaign-button" >view</button>
      

    </div>
    
    
  
  </div>


  <br>
  <br>
  <br>


  
     
  </div>
  






  
</template>

<script>
import axios from 'axios';



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
      axios.post('http://127.0.0.1:8000/userinfo/logout/')
      .then(Response=>
        {
          this.$router.push('/')
        }

      )
      .catch(Error=>
        {
          console.log(Error)
        }
      );
      
      
    },
    searchCampaigns()
    {
      console.log('hello world')
    }
  }


}
</script>

<style scoped>

.navbar{
  display:flex;
  background-color: #535C91 ;
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
.campaign-pill{
  padding-top: 10px;
  margin-top: 30px;
  border-radius: 20px;
  height: 200px;
  width:600px;
  background-color: #070F2B;
  margin-left: 370px;
 padding-left: 10px;
 
}
.campaign-button{
  border-radius:10px;
  height: 37px;
  width: 70px;
  margin-top:80px;
  margin-left: 460px;
  background-color: #9290C3;
  color: white;
  border: none;
  
  
  
}
</style>
