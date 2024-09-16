var elem = document.getElementById("html");

if (elem) { // Check if the element exists
  if (elem.requestFullscreen) {
    elem.requestFullscreen();
  } else if (elem.mozRequestFullScreen) { // Firefox
    elem.mozRequestFullScreen();
  } else if (elem.webkitRequestFullscreen) { // Chrome, Safari, and Opera
    elem.webkitRequestFullscreen();
  } else if (elem.msRequestFullscreen) { // IE/Edge
    elem.msRequestFullscreen();
  } else {
    console.log("Fullscreen API is not supported.");
  }
} else {
  console.log("Element not found.");
}
