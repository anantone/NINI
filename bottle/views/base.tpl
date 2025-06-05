<html>
<head>
  <title>{{title or 'No title'}}</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
<style>

textarea {
  max-width: 90%;
}

p {
  font-size: medium;
}

ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333;
}

li {
  float: left;
}

li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

li a:hover {
  background-color: #111;
  font-size: medium;
}
</style>
</head>
<body style="margin:10px;padding:10px">

<ul>
  <li><a class="active" href="/">NINI</a></li>
  <li><a href="/search">Search</a></li>
  <li><a href="/genie/1">Genie</a></li>
  <li><a href="/suggest">Idea Box</a></li>
</ul>



  {{!base}}
</body>
</html>
