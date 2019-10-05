var lines = document.getElementById("divlines");
var txtArea = document.getElementById("edit_area");
window.onload = function() {
    refreshlines();
    txtArea.onscroll = function () {
        lines.style.top = -(txtArea.scrollTop) + "px";
        return true;
    }
    txtArea.onkeyup = function () {
        refreshlines();
        return true;
    }
}

function refreshlines() {
    var nLines = txtArea.value.split("\n").length;
    lines.innerHTML = ""
    for (i=1; i<=nLines; i++) {
        lines.innerHTML = lines.innerHTML + i + "." + "<br />";
    }
    lines.style.top = -(txtArea.scrollTop) + "px";
}