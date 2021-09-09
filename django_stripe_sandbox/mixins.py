class ContextObjectInfoMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['OBJECT_NAME'] = self.model.__name__

        QUERYSET_VALUES = {}
        for index, values in enumerate(self.get_queryset().values()):
            QUERYSET_VALUES.update({index: values})
        context['QUERYSET_VALUES'] = QUERYSET_VALUES

        context['OBJECT_VALUES_TO_IGNORE'] = ['abstractmodel_ptr_id']

        return context
