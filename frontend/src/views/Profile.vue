<template>
    <div class="profile">
        <h1 style="margin-left: 170px; padding-top: 20px;">hello user</h1>
    </div>
  
</template>

<script>
export default {
    data()
    {
        return{
            username:'',
            first_name:'',
            
        }
    }


}
</script>

<style scoped>
.profile{
    
  border-radius: 15px;
  width: 500px;
  height: 500px;
  background-color:#B5C0D0 ;
  justify-content: center;
  align-items: center;
  margin: auto;
  margin-top: 70px;

}
img{
  width: 200px;
  height:200px;
  border-radius: 100px;

}

</style>