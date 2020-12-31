var x = window.matchMedia("(min-width: 768px)")
var y = document.getElementById('tochange')
var z = document.getElementById('logo')
var j = document.getElementById('home')
var p = window.location.href

// hide logo when small screen
function change(x) {
  if (x.matches) {
    y.className = 'uk-navbar-right';
    z.style.display = 'block';
    j.style.display = 'none';
  } else {
    y.className = 'uk-navbar-center';
    z.style.display = 'none';
    j.style.display = 'flex';
  };
};
change(x) // Call listener function at run time
x.addListener(change) // Attach listener function on state changes
//
 
// change background on scrolling
var myNav = document.getElementById('navbar');
window.onscroll = function () { 
    "use strict";
    if (document.body.scrollTop >= 1 || document.documentElement.scrollTop >= 1 ) {
        myNav.classList.add("nav-colored");
        myNav.classList.remove("nav-transparent");
    } 
    else {
        myNav.classList.add("nav-transparent");
        myNav.classList.remove("nav-colored");
    }
};
//