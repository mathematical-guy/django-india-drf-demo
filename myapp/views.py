from django.http import JsonResponse

from myapp.models import Wizard

from django.views import View
class DjangoWizardListView(View):
    def get(self, request, *args, **kwargs):
        queryset = Wizard.objects.all()
        data = list(queryset.values())
        return JsonResponse(data, safe=False)


from rest_framework.response import Response
from rest_framework.views import APIView

class DRFWizardAPIVIew(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Wizard.objects.all()

        data = queryset.values()
        return Response(data=data)



from rest_framework import serializers

class WizardSerializer(serializers.Serializer):
    name = serializers.CharField()
    house = serializers.CharField()

    # def validate_house(self, house):
    #     DEFAULT_CHOICE = "GRYFFINDOR"
    #     if house != DEFAULT_CHOICE:
    #         raise serializers.ValidationError(
    #             f"Only {DEFAULT_CHOICE} is allowed")
    #     return house

    def validate(self, attrs: dict):
        DEFAULT_CHOICE = "GRYFFINDOR"
        house = attrs.get('house')

        if house != DEFAULT_CHOICE:
            raise serializers.ValidationError(
                f"Only {DEFAULT_CHOICE} is allowed")
        return house

    def create(self, validated_data: dict):
        return Wizard.objects.create(**validated_data)

    def update(self, instance: Wizard, validated_data: dict):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer

class CustomRenderer(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context.get('response').status_code if renderer_context else 200
        result, errors = {}, {}
        if status_code == 200:
            result = data
        else:
           errors = data

        data = {"errors": errors, "data": result, }

        return super(
            CustomRenderer, self
        ).render(
            data=data, accepted_media_type=accepted_media_type,
            renderer_context=renderer_context
        )



class DRFWizardViewSet(ModelViewSet):
    serializer_class = WizardSerializer
    queryset = Wizard.objects.all()
    renderer_classes = [CustomRenderer,]




    # authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAdminUser]



    # def paginate_queryset(self, queryset):
    #     return super().paginate_queryset(queryset=queryset)

    # from rest_framework.authentication import TokenAuthentication, BaseAuthentication
    # from rest_framework.permissions import IsAdminUser

    # class MyAuthentication(BaseAuthentication):
    #     def authenticate(self, request):
    #         from user
    #         User.objects.first()

    # filter_backends = [SearchFilter]
    # search_fields = ['name', ]
    # filterset_fields = ['gender', 'house']


    # def filter_queryset(self, queryset):
    #     query_params = self.request.query_params
    #     gender = query_params.get('gender', None)
    #     house = query_params.get('house', None)
    #
    #     if gender is not None:
    #         queryset = queryset.filter(
    #             gender=gender
    #         )
    #     if house is not None:
    #         queryset = queryset.filter(
    #             house=house
    #         )
    #
    #     return super(
    #         DRFWizardViewSet, self
    #     ).filter_queryset(queryset=queryset)


