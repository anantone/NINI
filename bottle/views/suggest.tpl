% rebase('base.tpl', title='Suggestion Box')

<h2>Suggesting a new feature</h2>

% if message:
<p>{{message}}</p>
% else:

<p>Thank you for your willingness to contribute a suggestion! Please enter it below. You have 500 characters and if you provide a valid email address, you will receive an update about your idea.</p>
<form action="/suggest" method="post">
    Your suggested feature: </br><textarea name="suggestion" cols="100" rows="3" maxlength="500"></textarea></br>
    Your email address: <input style="margin:5px;" name="email" type="email" /></br>
    <input style="margin:5px;" value="Submit" type="submit" />
</form>
% end
