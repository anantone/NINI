% rebase('base.tpl', title='Anthology')

<h1>Open Anthology of N.I.-generated Haikai</h1>


% for item in anthology:
<div
% author = item[1]
% date = item[2]
% str = item[0]
% verses = str.split("\r")
<p><em>
% for i in verses:
{{i}}</br>
% end
</em></p>
% if author and not date:
<p>{{author}}</p>
</br>
% elif author and date:
<p>{{author}}, {{date}}</p>
</br>
% elif date and not author:
<p>{{date}}</p>
% else:
<p> </p>
</br>
</div>
% end

