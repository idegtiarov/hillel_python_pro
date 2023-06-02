from django.core.exceptions import BadRequest


class MixinUserFilter():
    ...
    # def get_context_data(self, *args, **kwargs):
    #     data = super().get_context_data(*args, **kwargs)
    #     if data.user != self.request.user:
    #         raise BadRequest
    #     return data
