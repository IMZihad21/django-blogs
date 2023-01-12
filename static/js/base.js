// default fetch function
const fetchAPI = async (apiURL, responseType = "json") => {
  const response = await fetch(apiURL);
  switch (responseType) {
    case "text":
      return await response.text();

    case "blob":
      return await response.blob();

    default:
      return await response.json();
  }
};
