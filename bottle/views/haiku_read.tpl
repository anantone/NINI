% rebase('base.tpl', title='Gen NI')

<h1>Content generation complete!</h1>

<p>Congratulations! Here is your haiku:</p>
</br>
% str =  haiku[0]
% verses = str.split("\r")
<p><em>
% for i in verses:
{{i}}</br>
% end
</em></p>
</br>
<p>Please, take some time to read it again. Forget about counting syllables, now. Just visualize once more the three miniature moments that you have come up with. Can you see something happening in these very few words? Does this something have any meaning to you? Could it have meaning to someone else? Or would you rather not have wasted your time writing three lines which really, really couldn't mean anything interesting? — If so, please feel free to email a copy of your haiku to nini-haikus@cumulus.cool and you will receive a third-party analysis within 5 business days, which may or may not support your assessment. — You may also read other haikus from our open anthology (see below) or check out the examples provided in our technical white paper.</p>

<p>OPTIONAL: Would you like to add your haiku to our open anthology, so that others may read it? If so, you may add your name and today's date below, and click the Submit button.</p>
<p><em>Please note: only users who submit a haiku are given temporary access to read the anthology. Providing your name or pseudonym is not required. You agree to this use of your haiku, and release me from any liability regarding your copyright as the author of your haiku. This is just a friendly experiment :)</em></p>

<form action="/genie/anthology" method="post">
    Author: <input style="margin:5px;" name="author" type="text" />
    Date: <input style="margin:5px;" name="date" type="date" />
    <input type="hidden" name="haiku" value="{{str}}">
    <input style="margin:5px;" value="Submit" type="submit" />
</form>
