body, html, #root {
    height: 100%;
    margin: 0;
    padding: 0;
    overflow-x: hidden; 
    display: flex;
    flex-direction: column;
    font-family: 'Roboto', sans-serif; 
  }
  
  .App {
    flex: 1;
    display: flex;
    flex-direction: column;
    margin-top: 64px; /* Add margin to account for the fixed navbar */
  }
  
  .App > div {
    flex: 1;
  }
  
  .active-link {
    background-color: rgba(0, 0, 0, 0.1); /* Slightly faded color of the parent */
    color: inherit; /* Keep the text color the same */
    text-decoration: none; /* Remove the underline */
    padding: 8px 16px; /* Add some padding for better appearance */
    border-radius: 20px; /* Circular shape */
  }
  
  /* Ensure the footer links have the Roboto font */
  footer a {
    font-family: 'Roboto', sans-serif;
  }
  
  /* Reset padding and margin for all elements */
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
  
  /* .main-content {
    padding-top: 64px; Adjust based on your Navbar height
  } */

    