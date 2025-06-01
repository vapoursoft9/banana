# banana
<h2>A new lightweight python self hosted database.</h2>
<img src="istock-162487071.jpg"></img>
<p>To change the, ip, and port, you must change the host's values to change the ip in db.py, and you must change the port value to change the port in db.py, run db.py to activate the db.</p>
<p>To use this curl the url with the ip, and port, then add /%, and after that add the content(a word only) you want to add to the data base.</p>
<p>How you can help is by forking this repo to make your own better databases.</p>
<p>This database was made in a day</p>
<style>
  /* Root Variables */
:root {
  --primary-color: #007BFF;
  --secondary-color: #0056b3;
  --text-color: #333;
  --background-color: #f4f4f4;
  --white: #ffffff;
  --max-width: 1200px;
  --shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

/* Base Reset */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Base Styles */
body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background-color: var(--background-color);
  color: var(--text-color);
  line-height: 1.6;
}

/* Header Element Styling */
header {
  background: var(--primary-color);
  color: var(--white);
  padding: 2rem 1rem;
  text-align: center;
  box-shadow: var(--shadow);
}

header h1 {
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
}

header p {
  font-size: 1.1rem;
  opacity: 0.9;
}

/* Navigation */
nav {
  background: var(--secondary-color);
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  padding: 0.75rem;
}

nav a {
  color: var(--white);
  text-decoration: none;
  margin: 0 1rem;
  font-weight: bold;
}

nav a:hover {
  text-decoration: underline;
}

/* Main Content */
main {
  max-width: var(--max-width);
  background: var(--white);
  margin: 2rem auto;
  padding: 2rem;
  box-shadow: var(--shadow);
}

/* Headings */
h1, h2, h3, h4, h5, h6 {
  margin-bottom: 1rem;
  font-weight: 600;
  line-height: 1.2;
}

h1 { font-size: 2.25rem; }
h2 { font-size: 1.75rem; }
h3 { font-size: 1.5rem; }
h4 { font-size: 1.25rem; }
h5 { font-size: 1.1rem; }
h6 { font-size: 1rem; }

/* Paragraphs */
p {
  margin-bottom: 1.25rem;
  font-size: 1rem;
  line-height: 1.7;
  color: var(--text-color);
}

/* Footer */
footer {
  background: #333;
  color: var(--white);
  text-align: center;
  padding: 1rem;
  margin-top: 2rem;
}

/* Responsive Design */
@media (max-width: 768px) {
  nav {
    flex-direction: column;
  }

  nav a {
    margin: 0.5rem 0;
  }

  main {
    padding: 1rem;
  }

  header h1 {
    font-size: 2rem;
  }
}

</style>
