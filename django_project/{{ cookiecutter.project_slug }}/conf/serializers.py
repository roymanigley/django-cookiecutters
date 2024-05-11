from dj_rest_auth.serializers import UserDetailsSerializer

class LoginSerializer(UserDetailsSerializer):

    def to_representation(self, instance) -> dict[str, any]:
        representation = super().to_representation(instance=instance)
        representation.pop('pk')
        representation['is_superuser'] = instance.is_superuser
        representation['permissions'] = [p for g in instance.groups.all() for p in g.permissions.all().values_list('codename', flat=True)]
        representation['permissions'] += instance.user_permissions.all().values_list('codename', flat=True)
        return representation

