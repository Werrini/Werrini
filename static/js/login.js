var x = document.getElementById("id_password");
x.setAttribute('placeholder', 'Password');
// x.setAttribute('data-toggle', 'tooltip');
// x.setAttribute('data-placement', 'bottom');

var b = document.getElementById("id_login");
b.setAttribute('placeholder', 'Email adress');


function showPassword() {
  var x = document.getElementById("id_password");
  var j = document.getElementById("showpassi");
  if (x.type === "password") {
    x.type = "text";
    j.className = "fas fa-eye-slash";
  } else {
    x.type = "password";
    j.className = "fas fa-eye";
  }
}
