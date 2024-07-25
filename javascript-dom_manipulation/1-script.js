/*
JS script to change color of the header tag in 1-main.html
when the user clicks on the tag with id red_header
*/
const redHeaderId = document.getElementById('red_header');
const headerTag = document.querySelector('header');
// event on click function
redHeaderId.addEventListener('click', function () {
  headerTag.style.color = '#FF0000';
});
