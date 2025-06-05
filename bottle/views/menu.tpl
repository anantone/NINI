<html>
<head>
<title>
NINI - NIE
</title>
<!--basic responsive design-->
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<!--reload page on browser back button (to make whitepaper joke more efficient!)-->
<meta http-equiv="Cache-Control" content="no-cache">
<script>
window.addEventListener( "pageshow", function ( event ) {
  var historyTraversal = event.persisted ||
                         ( typeof window.performance != "undefined" &&
                              window.performance.navigation.type === 2 );
  if ( historyTraversal ) {
    // Handle page restore.
    window.location.reload();
  }
});
</script>
</head>
<body style="margin:20px;padding:15px;">

<h1 style="text-align: center; padding:3px;">NINI - A NATURAL INTELLIGENCE ENABLER</h1>
<h2 style="text-align: center;"><em>and Code in Place 2025 Final Project by Antoine Bargel</em></h2>
<p style="padding:5px;">Welcome! This prototype enables you to leverage Natural Intelligence for:
<ul><li> gathering information about a topic of your choice.</li>
<li> generating creative, structured, linguistic content.</li>
<li>suggesting further enablement modalities.</li></ul>
Natural Intelligence can best be described as a past-generation form of A.I. To learn more, please read our technically white paper (available after you've tried a feature, or two).</p>
<h3>What would you like to do?</h3>
<ol><li><a href="/search">Search for information</a></li>
<li><a href="/genie/1">Generate creative content</a></li>
<li><a href="/suggest"> Suggest a new feature</a></li>
% if feat and not white:
<li><a href="/whitepaper">Read our technically white paper</a></li>
%elif feat and white:
<li><a href="/paperwhite">Read our <span style="font-family: 'Black Ops One', cursive;">technical</span> white paper</a> (sorry!)</li>
%end
</ol>
</body>
</html>
