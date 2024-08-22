<template>
    <form action="">
        <input type="text" placeholder="username" required v-model="username">
        <input type="password" placeholder="password" required v-model="passText">
        <button @click="validateForm">Submit</button>
        

    </form>
  
</template>

<script>
import axios from 'axios';

export default {
   data()
   {
    return{
        username:'',
        passText:'',
        influencer:'influencer',
        sponsor:'sponsor'
    }

   },
   methods:{
    validateForm()
    {
        let isValidated=true;
        const fields=[
            {'username':this.username},
            {'passText':this.passText}

        ]
        if(isValidated)
    {
        this.submitForm();
    }
    },
    submitForm()
    {
        
        axios.post('http://127.0.0.1:8000/userinfo/login/',{username:this.username, passText:this.passText})
        .then(Response=>
        {
            this.userType=Response.data.userType
            if(this.userType==="influencer"){
                setTimeout(()=>{this.$router.push('/')},3500)
                
            }
            else if(this.userType==="sponsor")
            {
                setTimeout(()=>{this.$router.push('/SponsorView')},3500)
            }
           
            
        }
        )
        .catch(error => {
        console.error('Error:', error); 

    
       
    });
        
       
        
    
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
    
    margin-bottom: 10px;
    border-radius: 10px;
    height: 25px;


}

</style>