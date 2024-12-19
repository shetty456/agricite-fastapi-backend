from tortoise.models import Model
from tortoise import fields

class User(Model):
    id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=100)
    last_name = fields.CharField(max_length=100)
    email = fields.CharField(max_length=150, unique=True)
    password = fields.CharField(max_length=255)  # Store hashed passwords
    is_active = fields.BooleanField(default=False)  # Email verification status
    is_superuser = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

    class Meta:
        table = "users"
        unique_together = [("first_name", "last_name")]


class Tag(Model):
    id = fields.IntField(pk=True)
    tag_name = fields.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.tag_name

    class Meta:
        table = "tags"
        ordering = ["tag_name"]


class Module(Model):
    id = fields.IntField(pk=True)
    module_name = fields.CharField(max_length=150, unique=True)
    module_desc = fields.TextField()
    module_image = fields.CharField(max_length=255, null=True)
    tags = fields.ManyToManyField('models.Tag', related_name='modules')  # Tags for filtering
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.module_name

    class Meta:
        table = "modules"
        indexes = [("module_name",)]


class Content(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=150)
    description = fields.TextField()
    image_urls = fields.JSONField(null=True)  # Store array of image URLs
    module = fields.ForeignKeyField('models.Module', related_name='contents')  # Related to Module
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        table = "contents"
        indexes = [("name", "module")]  # Composite index for name and module


class Question(Model):
    id = fields.IntField(pk=True)
    question = fields.TextField()
    question_desc = fields.TextField(null=True)
    image_url = fields.CharField(max_length=255, null=True)
    sub_category = fields.ForeignKeyField('models.Module', related_name='questions')  # Linked to Module
    series = fields.ManyToManyField('models.TestSeries', related_name='questions')  # Questions in test series
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.question

    class Meta:
        table = "questions"
        indexes = [("sub_category", "created_at")]  # Index sub_category for filtering


class Option(Model):
    id = fields.IntField(pk=True)
    option_content = fields.TextField()  # The text of the option
    questions = fields.ManyToManyField('models.Question', related_name='options')  # Many-to-Many relationship

    def __str__(self):
        return self.option_content

    class Meta:
        table = "options"
        indexes = [("option_content",)]  # Index for faster option lookups


class TestSeries(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=150)
    description = fields.TextField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        table = "test_series"
        ordering = ["-created_at"]


class Score(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField('models.User', related_name='scores')  # User related to score
    test_series = fields.ForeignKeyField('models.TestSeries', related_name='scores')  # Test series related to score
    score = fields.IntField()  # The score achieved
    total_score = fields.IntField()  # The total score for the test series
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return f"Score of {self.score} for {self.user} in {self.test_series}"

    class Meta:
        table = "scores"
        indexes = [("user", "test_series")]  # Index for quick lookup by user and test_series
