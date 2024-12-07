from django.core.exceptions import ValidationError

def validate_png(image):
    if not image.name.lower().endswith('.png'):
        raise ValidationError('O formato de imagem precisa ser PNG')