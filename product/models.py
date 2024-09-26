from django.db import models

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Категория",
        help_text="Введите наименование категории",
    )  # Наименование
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание категории", **NULLABLE
    )  # Описание

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"Наименование: {self.name}\n Описание: {self.description}"


class Product(models.Model):

    name = models.CharField(
        max_length=100,
        verbose_name="Продукт",
        help_text="Введите наименование продукта",
    )  # Наименование

    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание товара", **NULLABLE
    )  # Описание

    photo = models.ImageField(
        upload_to="product/image/",
        verbose_name="Фото",
        help_text="Загрузите фото продукта",
        **NULLABLE,
    )  # Изображение(превью)

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию продукта",
        **NULLABLE,
        related_name='products'
    )  # Категория

    purchase_price = models.IntegerField(
        verbose_name="Цена", help_text="Введите цену за покупку"
    )  # Цена за покупку

    creation_date = models.DateField(
        verbose_name="Дата создания", help_text="Введите дату создания"
    )  # Дата создания(записи в БД)

    last_modified_date = models.DateField(
        verbose_name="Дата последнего изменения",
        help_text="Введите дату последнего изменения",
    )  # Дата последнего изменения(записи в БД)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category"]

    def __str__(self):
        return f"Наименование: {self.name}\n Описание: {self.description}\n Цена: {self.purchase_price}"
