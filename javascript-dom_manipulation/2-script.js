/*
JS script to add the class red to header tag in 2-main.html
when the user clicks on the tag with id red_header
*/
const redHeaderId = document.getElementById('red_header');
const headerTag = document.querySelector('header');
// event on click function
redHeaderId.addEventListener('click', function () {
  headerTag.classList.add('red');
});
