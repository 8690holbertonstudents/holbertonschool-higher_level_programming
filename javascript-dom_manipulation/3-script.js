/*
JS script to toggle the class of the header tag in 3-main.html
when the user clicks on the tag with id toggle_header
*/
const toggleHeaderId = document.getElementById('toggle_header');
const headerTag = document.querySelector('header');
// event on click function
toggleHeaderId.addEventListener('click', function () {
  if (headerTag.classList.contains('red')) {
    headerTag.classList.remove('red');
    headerTag.classList.add('green');
  } else {
    headerTag.classList.remove('green');
    headerTag.classList.add('red');
  }
});
