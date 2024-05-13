function Submit(){
    let name = document.getElementById('name').value
    let email = document.getElementById('email').value
    let phone = document.getElementById('phone_number').value
    let feedback = document.getElementById('text-area').value
    
    if(name == '' || email == '' || phone == ''){
        window.alert("Enter all the fields....")
    }
    else if(feedback == ''){
        window.alert("Enter Feeback....")
    }
    else{
        window.alert('Thank You for your response')
    }
}
function Signup(){
    let username = document.getElementById('username').value
    let firstname = document.getElementById('firstname').value
    let lastname = document.getElementById('lastname').value
    let password = document.getElementById('password').value
    let confirmpassword = document.getElementById('confirmpassword').value
    let email = document.getElementById('email').value
    let mobilenumber = document.getElementById('mobilenumber').value

    if (username == '' || firstname == '' || lastname =='' || password == '' || confirmpassword == '' || email == '' || mobilenumber == ''){
        window.alert('Enter all the fields....')
    }
    else if(password!==confirmpassword){
        window.alert("passwords didn't match, please check your paswords..!")
    }
    else{
        window.alert('Sign Up Successful, Remember login details')
    }
}