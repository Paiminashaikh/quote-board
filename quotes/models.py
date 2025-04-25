from django.db import models

# ✅ Tag options
TAGS = [
    ('Motivational', 'Motivational'),
    ('Love', 'Love'),
    ('Life', 'Life'),
    ('Funny', 'Funny'),
    ('Other', 'Other'),
]

# ✅ Single clean Quote model
class Quote(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)  # ✅ Like field
    tag = models.CharField(max_length=50, choices=TAGS, default='Other')  # ✅ Tag field

    def __str__(self):
        return f"{self.content[:30]}... — {self.author}"
