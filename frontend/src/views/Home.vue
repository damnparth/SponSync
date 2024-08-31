<template>
    

        <div class="navbar">
    <div class="container-fluid">
      <h2>SponSync</h2>

    </div>
    <div class="navbar-left">
      
      
      <br>
      <br>
    </div>
    <div class="navbar-right">
        <button class="login"><router-link to="/Register" style="color:white; text-decoration: none;font-weight: bold;">Register</router-link></button>
        <button class="login"><router-link to="/Login" style="color:white; text-decoration: none;font-weight: bold;">Login</router-link></button>

      

      
    </div>
    </div>
  
</template>

<script>
export default {


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