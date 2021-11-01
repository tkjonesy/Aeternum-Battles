function FadeOut() {
    var element = document.getElementById("fadeout");
    var op = 1;  // initial opacity
    var timer = setInterval(function () {
        if (op <= .1){
            clearInterval(timer);
            element.style.display = 'none';
        }
        element.style.opacity = op;
        element.style.filter = 'alpha(opacity=' + op * 100 + ")";
        op -= 1;
    }, 2000);
}

//992 px non collapsed version
function profileDropdownMargin() {
if (document.getElementById('navbar').clientWidth < 992) {
  document.getElementById('dropdown').style.marginLeft='0px'
}
else {
  document.getElementById('dropdown').style.marginLeft='-95px'
}
}