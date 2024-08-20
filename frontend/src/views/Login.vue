<template>
    <form action="">
        <input type="text" placeholder="username" required>
        <input type="password" placeholder="password" required>
        <button @click="validateForm">Submit</button>

    </form>
  
</template>

<script>
import axios from 'axios';

export default {
   data()
   {

   },
   methods:{
    validateForm()
    {
        let isValidated=true;
        const fields=[
            {'username':this.username},
            {'password':this.password}

        ]
        if(isValidated)
    {
        this.submitForm();
    }
    },
    submitForm()
    {
        const userData={
            username:this.username,
            password:this.password

        }
        axios.post('http://127.0.0.1:8000/userinfo/login/',userData)
        .then(Response=>
        {
            if('message'=='hello world')
        {
            console.log('hello world')
        }
        }
        )
        .catch(console.error());
        
    
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
    margin-top: 250px;
    
}   
input{
    margin-bottom: 10px;

}

</style>