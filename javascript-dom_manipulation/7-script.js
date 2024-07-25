/*
JS script that fetches and list movie's name from url
All movie titles must be list in the HTML ul element with id list_movies
*/
const myListulTag = document.getElementById('list_movies');
/*
async function to fetch API
example from https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
*/
async function getData() {
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }
    // retreive all movie's name in a list when API response is OK
    const json = await response.json();
    for (const movie of json.results) {
      const newLiTag = document.createElement('li');
      newLiTag.textContent = movie.title;
      myListulTag.appendChild(newLiTag);
    }
  } catch (error) {
    console.error(error.message);
  }
}
// execute getData
getData();
