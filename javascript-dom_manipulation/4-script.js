/*
JS script to add list elements in 4-main.html
when user clicks on tag with ID add_item
*/
const addId = document.getElementById('add_item');
const myListulTag = document.querySelector('ul.my_list');
// event on click function
addId.addEventListener('click', function () {
  newLiTag = document.createElement('li');
  newLiTag.textContent = 'Item';
  myListulTag.appendChild(newLiTag);
});
