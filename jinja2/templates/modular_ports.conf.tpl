{%- for port in ports %}
{%- with p=port %}
{%- include "ports_config.sub.conf.tpl" %}
{% endwith -%}
{% endfor -%}