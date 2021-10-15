from rest_framework import serializers
from watchlist_app.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = "__all__"  # 각각을 따로 규정할 수도 있지만 이런 식으로 한꺼번에 하는 것도 가능.
        # exclude = ['active'] 이걸 통해 배제할 필드를 지정할 수 있음. 

    def get_len_name(self, object):
        return len(object.name)

    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("name and description should be different")
        return data  # 반드시 validate된 데이터를 리턴하여야 함. 
    

    # field level validator
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("name is too short!")
        else:
            return True

# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("name is too short!")
    

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("name and description should be different")
#         return data  # 반드시 validate된 데이터를 리턴하여야 함. 
    

#     # field level validator
#     # def validate_name(self, value):
#     #     if len(value) < 2:
#     #         raise serializers.ValidationError("name is too short!")
#     #     else:
#     #         return True
