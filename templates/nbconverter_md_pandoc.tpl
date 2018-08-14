
{% extends 'markdown.tpl'%}


{% block any_cell %}
    {% if 'hide' not in cell['metadata'].get('tags', []) %}
        {{ super() }}
    {% endif %}
{% endblock any_cell %}


{% block input_group %}
    {% if 'hide_input' not in cell['metadata'].get('tags', []) %}
        {{ super() }}
    {% endif %}
{% endblock input_group %}


{% block output_group %}
    {% if 'hide_output' not in cell['metadata'].get('tags', []) %}
        {{ super() }}
    {% endif %}
{% endblock output_group %}
