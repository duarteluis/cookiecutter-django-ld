from django.core.management.base import BaseCommand
from django.apps import apps
from django.db import transaction


def is_encrypted_field(field):
    return field.__class__.__module__.startswith("encrypted_model_fields.fields")


class Command(BaseCommand):
    help = "Re-chiffre tous les champs encryptés avec la clé active"

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Démarrage de la rotation des clés..."))

        # Liste des modèles à migrer
        models_to_rotate = [
            ("accounts", "customerprofile"),
            ("accounts", "supplierprofile"),
            ("accounts", "customuser"),
        ]

        for app_label, model_name in models_to_rotate:
            model = apps.get_model(app_label, model_name)
            encrypted_fields = [
                f.name for f in model._meta.fields if is_encrypted_field(f)
            ]

            if not encrypted_fields:
                continue

            with transaction.atomic():
                for obj in model.objects.all():
                    for field in encrypted_fields:
                        # Forcer la re-sauvegarde => re-chiffrement avec nouvelle clé
                        setattr(obj, field, getattr(obj, field))
                    obj.save()

            self.stdout.write(self.style.SUCCESS(f"✓ {model.__name__} mis à jour."))

        self.stdout.write(self.style.SUCCESS("Rotation des clés terminée."))
