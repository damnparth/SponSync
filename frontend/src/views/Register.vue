<template>
    <form>
        <input type="text" placeholder="username" required v-model="username">
        <input type="text" placeholder="first name" required v-model="first_name">
        <input type="text" placeholder="last name" required v-model="last_name">
     
        

    
       
     
        <input type="password" placeholder="password" required v-model="password">
        <!-- <label for="influencer">influencer</label>
        <input type="radio" name="influencer" id="influencer" v-model="userType">
        <label for="sponsor">sponsor</label>
        <input type="radio" name="sponsor" id="sponsor" v-model="userType"> -->
      
        
        
        <select name="userType" id="userType" v-model="userType" required>
            <option value="influencer" >influencer</option>
         <option value="sponsor">sponsor</option>
        </select>
        <br>
       
        <input type="password" placeholder="confirm password" required v-model="confirm">


        <button @click="validateForm">submit</button>

        <p>{{ userType }}</p>

     


        
    </form>
    
  
</template>

<script>
import router from '@/router';
import axios from 'axios';

import Password from 'primevue/password';



export default {
  data(){
    return{
        username:'',
        password:'',
        first_name:'',
        last_name:'',
        userType:'',
        confirm:'',
    }
  },
  components:{Password},
 
  methods:
  {
      validateForm(){
          let isValidated=true;
          const fields=[
            {'username':this.username},
            {'first_name':this.first_name},
            {'last_name':this.last_name},
            {'password':this.password},
            
        ]
      

        if(isValidated)
        this.submitForm();
    },
    submitForm()
    {
        const userdata={
            username: this.username,
            first_name: this.first_name,
            last_name: this.last_name,
            password:this.password,
            userType:this.userType,
            confirm:this.confirm


        }
        axios.post('http://127.0.0.1:8000/userinfo/register/',userdata)
        .then(response=>{
            setTimeout(() => {this.$router.push('/Login')}, 1500)
            

        })
        .catch(error=>{
            console.log(error)
        })
        
    }
  }
}
</script>

<style scoped>
*{
    display: block;
}
form{
    margin-left: 500px;
    margin-top: 150px;
    
}
input{
    margin-bottom: 10px;
    border-radius: 10px;
    height: 30px;
}
button{
    cursor:pointer;
}
label{
    margin-right: 700px;
}
</style>