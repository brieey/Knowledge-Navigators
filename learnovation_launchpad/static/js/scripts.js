const signupForm = document.getElementById("signup-form");

signupForm.addEventListener("submit", (e) =>{
    //e.preventDefault();
    const name = document.getElementById("username").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password1").value;
    console.log(name, email, password);

})