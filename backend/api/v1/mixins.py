from drf_extra_fields.fields import Base64ImageField
from rest_framework import status
from rest_framework.response import Response


class CustomBase64ImageField(Base64ImageField):
    """Настраиваемое поле для предотвращения
       возврата None вместо пустой строки.
    """

    EMPTY_VALUES = ()


class WriteMethodsMixinView:
    """Миксин с методами добавления и удаления объектов в ViewSets."""

    @staticmethod
    def add_obj(serializer):
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )

    @staticmethod
    def remove_obj(field, obj_id, obj_name='Объект'):
        if not field.filter(id=obj_id).exists():
            return Response(
                {'errors': f'{obj_name} с таким ID не найден!'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        field.remove(obj_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
