var x = document.getElementById("id_password1");
x.setAttribute('placeholder', 'Password');
// x.setAttribute('data-toggle', 'tooltip');
// x.setAttribute('data-placement', 'bottom');

var a = document.getElementById("id_full_name");
a.setAttribute('placeholder', 'Full name');

var b = document.getElementById("id_email");
b.setAttribute('placeholder', 'Email adress');


function showPassword() {
  var x = document.getElementById("id_password1");
  var j = document.getElementById("showpassi");
  if (x.type === "password") {
    x.type = "text";
    j.className = "fas fa-eye-slash";
  } else {
    x.type = "password";
    j.className = "fas fa-eye";
  }
}
