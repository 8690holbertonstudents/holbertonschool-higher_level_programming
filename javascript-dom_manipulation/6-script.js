/*
JS script that fetches the character name from url
The name must be displayed in the HTML tag with the ID character
*/
const charId = document.getElementById('character');
/*
async function to fetch API
example from https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
*/
async function getData() {
  const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }
    // retreive name when API response is ok
    const json = await response.json();
    charId.textContent = json.name;
  } catch (error) {
    console.error(error.message);
  }
}
// execute getData
getData();
