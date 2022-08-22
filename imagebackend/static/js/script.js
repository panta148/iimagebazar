function show() {
    document.getElementById("overlay").style.display = 'block';
    document.getElementById("mysidebar").style.animation = "expand 0.3s forwards";
}
function closebtn() {
    document.getElementById("overlay").style.display = 'none';
    document.getElementById("mysidebar").style.animation = "collapse 0.3s forwards";
}
function signup() {
    let text = ''
    let data = prompt("Enter your username");
    if (data == null || data == '') {
        text = 'User Cancel the propmt.'

    }
    else {
        text = "Hello " + data + "! How are you today?";

    }
    alert(text);
}