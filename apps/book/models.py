from django.db import models
class Book(models.Model):
    title=models.CharField(max_length=20)
    pubDate=models.DateTimeField()
    detail = models.CharField(max_length=100, default='')
    def __str__(self): return self.title
    # class Meta
class FamousPeople(models.Model):
    name=models.CharField(max_length=10)
    profile=models.CharField(max_length=50, default='')
    # 在老版本默认CASCADE
    book=models.ForeignKey(Book, on_delete=models.CASCADE)
    def __str__(self): return self.name

class PollManager(models.Manager):
    def with_counts(self):
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT p.id, p.question, p.poll_date, COUNT(*)
                FROM polls_opinionpoll p, polls_response r
                WHERE p.id = r.poll_id
                GROUP BY p.id, p.question, p.poll_date
                ORDER BY p.poll_date DESC""")
            result_list = []
            for row in cursor.fetchall():
                p = self.model(id=row[0], question=row[1], poll_date=row[2])
                p.num_responses = row[3]
                result_list.append(p)
        return result_list
