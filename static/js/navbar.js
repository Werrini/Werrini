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

// hover logo to red
function hover(element) {
  element.setAttribute('src', "/static/images/logo2.png");
}

function unhover(element) {
  element.setAttribute('src', "/static/images/logo.png");
}
//

var check = document.URL.includes("/blog/");
// active link
for (var i = 0; i < document.links.length; i++) {
    if ( document.URL.includes(document.links[i].href) ){
      if (document.links[i].id === 'home') {
        if (document.URL == document.links[i].href) {
          document.links[i].className += " uk-active"; 
        }
      } else if (!check) {
        document.links[i].className += " uk-active"; 
      } else {
        document.links[i].id += "-active"; 
      }
    };
};
 