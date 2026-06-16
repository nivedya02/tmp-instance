# IFID_STATE: eyJzb3VyY2VzIjpbeyJpZCI6IjVlM2Q3Y2Q0LWI4YmMtNDllMy1iZmQ3LTViYTJlYTgxMjQzOSIsIm5hbWUiOiJtaWxrIiwidHlwZSI6ImRhaXJ5IiwiaXNfYWxsZXJnZW4iOnRydWUsImlzX2RlY2xhcmFibGUiOmZhbHNlfSx7ImlkIjoiM2NkMzc5NjQtN2E4OC00Y2U3LTg2YTYtNzFhM2Q4MDJkOTkyIiwibmFtZSI6ImNvdyBtaWxrIiwidHlwZSI6ImRhaXJ5IiwiaXNfYWxsZXJnZW4iOnRydWUsImlzX2RlY2xhcmFibGUiOnRydWV9LHsiaWQiOiIzZjExMjRjZS02MTRhLTQxZGMtOGQ5OC03ZTYzNGE5Y2UzODEiLCJuYW1lIjoid2hlYXQiLCJ0eXBlIjoicGxhbnQiLCJpc19hbGxlcmdlbiI6dHJ1ZSwiaXNfZGVjbGFyYWJsZSI6dHJ1ZX1dLCJmb3JtcyI6W3siaWQiOiJjdXJkIiwibWF0dGVyX3N0YXRlIjoiZGVuc2VfYmxvY2sifSx7ImlkIjoiZmxvdXIiLCJtYXR0ZXJfc3RhdGUiOiJmbG91ciJ9XSwicmVsYXRpb25zIjpbeyJpZCI6ImU5MWI0YjVlLTU3N2UtNGVlYy05NWU0LWI5Mzg1Mjc1YTNmOCIsInR5cGUiOiJWYXJpZXR5T2YiLCJiYXNlIjoiNWUzZDdjZDQtYjhiYy00OWUzLWJmZDctNWJhMmVhODEyNDM5IiwidmFyaWV0eSI6IjNjZDM3OTY0LTdhODgtNGNlNy04NmE2LTcxYTNkODAyZDk5MiJ9LHsiaWQiOiIwZWEwMGNkYi0zYmExLTQwNDItOThlZS1mOGFiNjAyNjlmMzUiLCJ0eXBlIjoiRm9ybU9mIiwib3JpZ2luIjoiM2NkMzc5NjQtN2E4OC00Y2U3LTg2YTYtNzFhM2Q4MDJkOTkyIiwiZm9ybSI6ImN1cmQiLCJwcm9jZXNzaW5nX21ldGhvZHMiOlsiZmVybWVudGF0aW9uIl19LHsiaWQiOiJjNzhhMmM5Yi05NmNhLTQxMzktOTU0MS0zMzgxNmJmM2RiY2MiLCJ0eXBlIjoiRm9ybU9mIiwib3JpZ2luIjoiM2YxMTI0Y2UtNjE0YS00MWRjLThkOTgtN2U2MzRhOWNlMzgxIiwiZm9ybSI6ImZsb3VyIiwicHJvY2Vzc2luZ19tZXRob2RzIjpbIm1pbGxpbmctd2hvbGUiXX0seyJpZCI6IjYwYjVhNDgwLWZmN2YtNGQ0OS1hOWQ5LTVhOTNhNTYwNGU1YyIsInR5cGUiOiJGb3JtT2YiLCJvcmlnaW4iOiIzZjExMjRjZS02MTRhLTQxZGMtOGQ5OC03ZTYzNGE5Y2UzODEiLCJmb3JtIjoiZmxvdXIiLCJwcm9jZXNzaW5nX21ldGhvZHMiOlsibWlsbGluZy1yZWZpbmVkIl19XSwiY3VzdG9tTWV0aG9kcyI6W10sImN1c3RvbU1hdHRlclN0YXRlcyI6W10sImN1c3RvbVNvdXJjZVR5cGVzIjpbXX0=

from index import Database, Source, IngredientForm, FormOf, VarietyOf

db = Database()

milk = db.add(Source(
    name="milk",
    type="dairy",
    is_allergen=True,
    is_declarable=False
))

cow_milk = db.add(Source(
    name="cow milk",
    type="dairy",
    is_allergen=True,
    is_declarable=True
))
db.relate(VarietyOf(base=milk, variety=cow_milk))
db.relate(FormOf(origin=cow_milk, form=curd, processing_method=["fermentation"]))

wheat = db.add(Source(
    name="wheat",
    type="plant",
    is_allergen=True,
    is_declarable=True
))
db.relate(FormOf(origin=wheat, form=flour, processing_method=["milling-whole"]))
db.relate(FormOf(origin=wheat, form=flour, processing_method=["milling-refined"]))

curd = db.add(IngredientForm(id="curd", matter_state="dense_block"))

flour = db.add(IngredientForm(id="flour", matter_state="flour"))

print(db)