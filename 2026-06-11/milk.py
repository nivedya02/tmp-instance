# IFID_STATE: eyJzb3VyY2VzIjpbeyJpZCI6IjMwZmI2MTE5LTFmNjQtNDg3Yy1iODA0LWRhODg0MTQ4MmE2OCIsIm5hbWUiOiJtaWxrIiwidHlwZSI6ImRhaXJ5IiwiaXNfYWxsZXJnZW4iOnRydWUsImlzX2RlY2xhcmFibGUiOmZhbHNlfSx7ImlkIjoiNGI4MjlhZTItNjFmOS00Y2I0LWFiZjItZTMxOGFlM2FmZWJkIiwibmFtZSI6ImNvdyBtaWxrIiwidHlwZSI6ImRhaXJ5IiwiaXNfYWxsZXJnZW4iOnRydWUsImlzX2RlY2xhcmFibGUiOnRydWV9XSwiZm9ybXMiOltdLCJyZWxhdGlvbnMiOlt7ImlkIjoiYTdmYWViNDUtYTI1Mi00ZDBjLWEwMDEtNGE1M2JmNjNkMzNlIiwidHlwZSI6IlZhcmlldHlPZiIsImJhc2UiOiIzMGZiNjExOS0xZjY0LTQ4N2MtYjgwNC1kYTg4NDE0ODJhNjgiLCJ2YXJpZXR5IjoiNGI4MjlhZTItNjFmOS00Y2I0LWFiZjItZTMxOGFlM2FmZWJkIn1dLCJjdXN0b21NZXRob2RzIjpbXSwiY3VzdG9tTWF0dGVyU3RhdGVzIjpbXSwiY3VzdG9tU291cmNlVHlwZXMiOltdfQ==

from index import Database, Source, IngredientForm, FormOf, VarietyOf

db = Database()

# Sources & Relations
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

print(db)