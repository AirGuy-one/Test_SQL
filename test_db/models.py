from django.db import models


class Categories(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category


class TestData(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    cat = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись в бд'
        verbose_name_plural = 'Записи в бд'



