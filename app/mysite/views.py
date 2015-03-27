from django.views.generic import TemplateView


class StartSurveyView(TemplateView):
    template_name = 'survey/start_survey.html'

    def get_context_data(self, **kwargs):
        context = super(StartSurveyView, self).get_context_data(
            **kwargs)
        context['heading'] = 'Start survery'
        return context
