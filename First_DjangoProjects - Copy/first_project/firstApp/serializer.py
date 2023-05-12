from rest_framework import serializers
from .models import Student


class Att_serializer(serializers.Serializer):
    stuid = serializers.IntegerField()
    stuname = serializers.CharField(max_length=100)
    stumail = serializers.EmailField(max_length=100)
    stuclass = serializers.CharField(max_length=100)

    def create(self,validated_data):  #overriding create method
        return Student.objects.create(**validated_data)

    def update(self,instance,validated_data):  #for put instance nothing data
        instance.stuname = validated_data.get('stuname')
        instance.stumail = validated_data.get('stmail')
        instance.stupass = validated_data.get('stupass')
        instance.save()
        return instance

def email_valid(value):
    if not value.endswith("gmail.com"):
        raise serializers.ValidationError('Not a Vaild Email')


class Att_serializer(serializers.ModelSerializer):
    stumail = serializers.CharField(validators=[email_valid])
    class Meta:
        model = Student
        fields = ['stuid','stuname','stumail','stuclass']

    """""
    # y can valid in sing;le field
    def validate_stuid(self, value):
        if value <=100:
            raise serializers.ValidationError('Not a Valid Roll number')
        return value
    """""
    """""
    # object level validation
    def validate(self, data):
        stuid = data.get('stuid')
        stuname = data.get('stuname')
        stumail = data.get('stumail')
        if stuid <=100 or len(stuname)<=4 or stumail.endswith('gmail.com'):
            raise serializers.ValidationError('Not a Valid Roll number')
        return data
    """""



