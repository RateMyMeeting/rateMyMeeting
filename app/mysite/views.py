from django.views.generic import TemplateView
import subprocess

class StartSurveyView(TemplateView):
    template_name = 'survey/start_survey.html'

    def get_context_data(self, **kwargs):
        context = super(StartSurveyView, self).get_context_data(
            **kwargs)
        context['heading'] = 'Start survery'
        return context

class PsView(TemplateView):
    template_name = 'ps.html'

    def get_context_data(self, **kwargs):
        context = super(PsView, self).get_context_data(
            **kwargs)
        output = subprocess.check_output(["ps", "-ef"])
        context['output_list'] = output.split('\n')
        return context
