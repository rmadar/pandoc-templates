
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


{% block execute_result scoped %}
 {%- for type in output.data | filter_data_type -%}
  {%- if type in ['text/plain'] %}
   <div class="output_code">
   ```
   {{ output.data['text/plain'] | escape_latex }}
   ```
   </div>
   {% else %}
    {{ super() }}
  {% endif %}
{%- endfor -%}
{% endblock execute_result %}