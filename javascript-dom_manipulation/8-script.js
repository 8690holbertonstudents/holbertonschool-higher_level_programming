/*
JS script taht fetches and tranlate hello from url
The translation of “hello” must be displayed in the HTML element with ID hello
the script should work when imported from <head> tag
*/
document.addEventListener('DOMContentLoaded', function () {
  const hellolTag = document.getElementById('hello');
  /*
  async function to fetch API
  example from https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
  */
  async function getData() {
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`Response status: ${response.status}`);
      }
      // write to corresponding HTML ID tag when API response is OK
      const json = await response.json();
      if (json.hello) {
        hellolTag.textContent = json.hello;
      }
    } catch (error) {
      console.error(error.message);
    }
  }
  getData();
});
