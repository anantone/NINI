% rebase('base.tpl', title='Search')

<p>Please enter your search keywords.</p>
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

