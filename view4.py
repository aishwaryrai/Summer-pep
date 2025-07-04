class PatientListView(ListView):
    model = Patient
    context_object_name = 'patients'
    template_name = 'clinic/patient_list.html'

class PatientDetailView(DetailView):
    model = Patient
    context_object_name = 'patient'
    template_name = 'clinic/patient_detail.html'

