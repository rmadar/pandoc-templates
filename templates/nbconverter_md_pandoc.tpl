
{% extends 'markdown.tpl'%}


{% block any_cell %}
    {% if 'hide' not in cell['metadata'].get('tags', []) %}
        {{ super() }}
    {% endif %}
{% endblock any_cell %}


{% block input_group %}
<div class="input_code">
```
{{ cell.source }}
```
</div>
{% endblock input_group %}


{% block stream %}  
<div class="output_code">
```
{{ output.text }}```
</div>
{% endblock stream %}