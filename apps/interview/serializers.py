from rest_framework import serializers
from apps.interview.models import Quiz, Question, UserQuiz, Variant


class QuestionSerializer(serializers.ModelSerializer):
    variants = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = (
            'id',
            'body',
            'question_type',
            'quiz',
            'variants'
        )
        kwargs = {
            'quiz': {'write_only': True},
            'variants': {'read_only': True}
        }

    def get_variants(self, obj):
        variants = []
        for var in obj.variants.all():
            variants.append({
                'text': var.text
            })
        return variants


class VariantSerializer(serializers.Serializer):
    text = serializers.CharField()


class QuestionCreateSerializer(serializers.ModelSerializer):
    variants = VariantSerializer(many=True)

    class Meta:
        model = Question
        fields = (
            'body',
            'question_type',
            'quiz',
            'variants'
        )

    def create(self, validated_data):
        variants = validated_data.pop('variants', [])
        instance = super(QuestionCreateSerializer, self).create(validated_data=validated_data)
        variants_list = []
        for variant in variants:
            variants_list.append(
                Variant(
                    question=instance,
                    **variant
                )
            )
        Variant.objects.bulk_create(variants_list)
        return instance


class QuizSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()

    class Meta:
        model = Quiz
        fields = (
            'id',
            'name',
            'start_date',
            'end_date',
            'description',
            'questions'
        )
        kwargs = {
            'questions': {'read_only': True}
        }

    def get_questions(self, obj):
        questions = obj.questions.all()
        ser = QuestionSerializer(questions, many=True)
        return ser.data


class QuizUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = (
            'id',
            'name',
            'end_date',
            'description',
        )


class SubmitAnswerSerializer(serializers.Serializer):
    question = serializers.IntegerField()
    answer = serializers.CharField()


class SubmitQuizSerializer(serializers.ModelSerializer):
    answers = SubmitAnswerSerializer(many=True)

    class Meta:
        model = UserQuiz
        fields = ('quiz', 'answers', 'user_ident')


class UserQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserQuiz
        fields = (
            'quiz',
            'user',
            'answers'
        )
