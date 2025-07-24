# Learning Pydantic

Pydantic is a Python library for type and data validation/parsing

## There are different tools (functions/classes) that Pydantic Offers
- **BaseModel** : *contains logic for data/type validation*
- **Field** : *used to define metadata for user to understand better what they need to fill in the field*
- **Custom Types** *like **EmailStr** to validate correct email, **AnyUrl** to validate correct url*

## List, Dict, Optional, Annotated

- **List and Dict Concept:**
<br>
For advance type checking, we use List, Dict, Optional, Annotated, etc to validate types
<br>
For instance, we want the user to pass a list with str elements in it. But how do we validate it?
<br>
We can say **contact : list**, but we don't know what data type is user going to insert in the list and we want string in it. We're just saying that it should be a list. That's it.
<br>
Instead we need to import List from typing module to validate it
<br>
We can say **contact : List[str]** to validate the elements inside the list should be in string format. Similarly for different type validations we do the same thing and we import the respective data type from typing.



- **Optional:**
<br>
We use Optional when we are saying some field is optional for the user. If they don't define it, we set a default value instead.
<br>
When using Optional, it's important to set a default value as well