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

function showNotifications() {
    const container = document.getElementById('notification-container');

    if (container.classList.contains('d-none')) {
        container.classList.remove('d-none');
    } else {
        container.classList.add('d-none');
    }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function removeNotification(removeNotificationURL, redirectURL) {
     const csrftoken = getCookie('csrftoken');
     let xmlhttp = new XMLHttpRequest();

     xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == XMLHttpRequest.DONE) {
            if(xmlhttp.status == 200) {
                window.location.replace(redirectURL);
            } else {
                alert('There was an error')
            }
        }
     };

     xmlhttp.open('DELETE', removeNotificationURL, true);
     xmlhttp.setRequestHeader('X-CSRFToken', csrftoken);
     xmlhttp.send();
}