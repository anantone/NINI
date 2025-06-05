% rebase('base.tpl', title='Search Results')

% if message:
<p>{{message}}</p>
% end

% if res:

<% if len(res) == 1:
	result = res[0][0]
	url = res[0][1]
	summary = res[0][2] %>

<h2>{{result}}</h2>
<a href="{{url}}">{{url}}</a>
<p>{{summary}}</p>

% else:
	<h3>Your search may refer to:</h3>
	<p><em>(if not, try again with more specific search terms)</em></p>
	<% for i in range(len(res)):
		result = res[i][0]
		url = res[i][1]
		summary = res[i][2] %>
	<h2>{{i+1}}: {{result}}</h2>
	<a href="{{url}}">{{url}}</a>
	<p>{{summary}}</p>
% end
% end
% end

<h3>Search again?</h3>
<form action="/search" method="post">
<textarea id="textarea" rows="1" cols="25" name="searx"></textarea>
<input id="button" value="Search" type="submit" />
<script>
var button = document.getElementById("button");
var textArea = document.getElementById("textarea");

textArea.addEventListener("keydown", function (event) {


    // Checking if key pressed is ENTER or not
    // if the key pressed is ENTER
    // click listener on button is called
    if (event.keyCode == 13) {
    	event.preventDefault()
        button.click();
    }
});
</script>
</form
