if (document.fullscreenElement === null) {
  document.documentElement.requestFullscreen();
} else if (document.mozFullScreenElement === null) {
  document.mozCancelFullScreen();
  document.documentElement.requestFullScreen();
} else if (document.webkitFullscreenElement === null) {
  document.webkitExitFullscreen();
  document.documentElement.webkitRequestFullscreen();
} else if (document.msFullscreenElement === null) {
  document.msExitFullscreen();
  document.documentElement.msRequestFullscreen();
} else {
  console.log("Element not found.");
}
