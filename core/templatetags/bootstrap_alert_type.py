from django import template
register = template.Library ()

@register.assignment_tag
def bootstrap_alert_type (tags):
	return 'danger' if tags == 'error' else tags
