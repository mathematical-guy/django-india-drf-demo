import requests

from django.core.files.base import ContentFile

from myapp.models import Wizard, HouseChoices, GenderChoices


response = requests.get(url="https://hp-api.onrender.com/api/characters")

response_json: list[dict] = response.json()


def make_request_to_wizard_api():
    for wiz in response_json:
        data = {}

        name = wiz.get("name")
        data.update({
            "name": name,
            "house": wiz.get("house", HouseChoices.GRYFFINDOR.value).upper(),
            "gender": wiz.get("gender", GenderChoices.MALE.value).upper(),
        })

        image_url = wiz.get("image", "")

        if image_url:
            image_response = requests.get(url=image_url)
            content = ContentFile(
                name=name,
                content=image_response.content
            )
            data.update({"image": content})


        Wizard.objects.create(**data)
        print(f"ADDED: {name}")