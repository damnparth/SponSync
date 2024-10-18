<template>
    <div class="profile">
        <h1 style="margin-left: 170px; padding-top: 20px;">hello {{ username  }}</h1>

        <div class="image-field">
        
        

        </div>
        <div class="biofield">

        <input type="text" placeholder="bio" v-model="bio"> <button @click="submitBio">Submit</button>
        {{ bio }}
        

       </div>

       <div class="email-field">
        <input type="text" placeholder="email" v-model="email"> <button @click="submitEmail">Submit</button>


    
       </div>

        

    </div>
  
</template>

<script>
import axios from 'axios'
export default {
    data()
    {
        return{
            username:'',
            first_name:'',
            bio:'',
            email:''
            
        }
    },
    mounted()
    {
        this.username=sessionStorage.getItem('username')
    },
    methods:{
       submitBio()
       {
        let formData = { bio: this.bio, username:sessionStorage.getItem('username') };
        axios.post('http://127.0.0.1:8000/userinfo/profile/',formData)
        .then(Response=>{
            console.log('hello world')
            
        })
        

       },
       submitEmail()
       {
        let mailData={email:this.email, username}
        axios.post('http://127.0.0.1:8000/userinfo/profile/',mailData)
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
.image-field{
    height: 200px;
    width: 200px;
    background-color: white;
    margin-left: 150px;
}
.biofield{
    margin-left: 150px;
    margin-top: 20px;

}
.email-field{
    margin-left: 150px;
    margin-top: 20px;
}

</style>