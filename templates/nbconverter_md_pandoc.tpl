
{% extends 'markdown.tpl'%}


{% block any_cell %}
    {% if 'hide' not in cell['metadata'].get('tags', []) %}
        {{ super() }}
    {% endif %}
{% endblock any_cell %}
