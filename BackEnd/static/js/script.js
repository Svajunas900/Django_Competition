const form1 = document.getElementById("form1");
const form2 = document.getElementById("form2");
const next1 = document.getElementById("next1");
const prev2 = document.getElementById("prev2");


function validateForm1() {
  if (form1.checkValidity()) {
    return true;
  } else {
    
    form1.reportValidity(); 
    return false;
  }
}

next1.addEventListener("click", () => {
  form1.classList.remove("active");
  form1.classList.add("form-prev"); 
  form2.classList.remove("form-next");  
  form2.classList.add("active");
  form2.classList.add("form-next");  
});


prev2.addEventListener("click", () => {
  form2.classList.remove("active");
  form2.classList.add("form-prev"); 
  form1.classList.remove("form-prev");
  form1.classList.add("active");  
});