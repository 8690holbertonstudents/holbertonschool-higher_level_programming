/*
JS script to change text of the header in 5-main.html
when the user clicks on the tag with ID update_header
*/
const updateHeaderId = document.getElementById('update_header');
const headerTag = document.querySelector('header');
// event on click function
updateHeaderId.addEventListener('click', function () {
  headerTag.textContent = 'New Header!!!';
});
