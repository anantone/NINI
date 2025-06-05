% rebase('base.tpl', title='Gen NI')

<h1>Generative Natural Intelligence</h1>
<h2>Step {{step}}/3</h2>
% if message:
<p><em>{{message}}</em></p>
% end
% for prom in prompt:
<p> {{prompt[prom]}} </p>
% end
<form action="/genie/{{step}}" method="post">
    <textarea style="margin:5px;" id="textarea" name="verse_{{step}}" cols="100" rows="1" maxlength="100"></textarea></br>
    <input type="hidden" name="haiku" value="{{haiku}}">
    <input style="margin:5px;" id="button" value="Submit" type="submit" />
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

</form>

