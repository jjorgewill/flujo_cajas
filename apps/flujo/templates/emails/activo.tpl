{% extends "mail_templated/base.tpl" %}

{% block subject %}
   bienvenido

{% endblock %}

{% block html %}

        <h1>Correo de preubas</h1> enviado a <strong> {{nombre}}</strong> con la edad <strong>  {{edad}} </strong>
{% endblock %}