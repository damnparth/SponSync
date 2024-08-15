<template>
    <form>
        <input type="text" placeholder="username" required v-model="username">
        <input type="text" placeholder="first name" required v-model="first_name">
        <input type="text" placeholder="last name" required v-model="last_name">
        <input type="password" placeholder="password" required v-model="password">
        <input type="radio" name="influencer" id="influencer">
        <input type="radio" name="sponsor" id="sponsor">
        <input type="confirm" placeholder="confirm password" required>
        <button @click="validateForm">submit</button>


        
    </form>
    
  
</template>

<script>
import axios from 'axios';

export default {
  data(){
    return{
        username:'',
        password:'',
        first_name:'',
        last_name:''
    }
  },
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
            password:this.password

        }
        axios.post('http://127.0.0.1:8000/userinfo/register/',userdata)
        .then(response=>{
            if('message'=='hello world')
            console.log('hello')

        })
        .catch(error=>{
            console.log(error)
        })
        
    }
  }
}
</script>

<style>

</style>