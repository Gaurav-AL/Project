var form = document.getElementById('form')
var username = document.getElementById("username")
var email = document.getElementById("email")
var password = document.getElementById("Password")
var dob = document.getElementById("dob")
var error = document.getElementById('error')
var dateObj = new Date()
var month = dateObj.getUTCMonth() + 1; //months from 1-12
var day = dateObj.getUTCDate();
var year = dateObj.getUTCFullYear();
var format = /[ `!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~]/;
   


form.addEventListener("submit",(e) =>{
    let message = []
    if(username.value.length < 2){
        message.push("Username Length Should be greater than 2")
    }
    
    if(format.test(username.value)){
        message.push("Username Contains Special Character")
    }
    if(password.value.length <= 7){
        message.push("Password Length must be greater than 7")
    }
    if(dob.value.split("-")[0] >= year){
        message.push("Date OF Birth IS Wrong or you are GOD!!!")
    }
    if(message.length == 0){
    message.push("Succesfully Login")
    }
    alert(message.join("----and----"))
    
    e.preventDefault();
})
