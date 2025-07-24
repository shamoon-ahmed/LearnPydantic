# Learning Pydantic

Pydantic is a Python library for type and data validation/parsing

## There are different tools (functions/classes) that Pydantic Offers
- **BaseModel** : *contains logic for data/type validation*

```powershell
from pydantic import BaseModel, Field, EmailStr, AnyUrl

class Patient(BaseModel):
    name: str
    age: age
```

- **Field** : *used to define metadata for user to understand better what they need to fill in the field*

```powershell
age : int = Field(title='Age', description='Age of Patient as in the NIC', gt=0, lt=120)
```

- **Custom Types** *like **EmailStr** to validate correct email, **AnyUrl** to validate correct url*

```powershell
class Patient(BaseModel):
    linkedin_url : AnyUrl
    email: EmailStr
```

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
<br>
```powershell
contact : Dict[str, str]
siblings_names : List[str]
```


- **Optional:**
<br>
We use Optional when we are saying some field is optional for the user. If they don't define it, we set a default value instead.
<br>
When using Optional, it's important to set a default value as well
<br>
```powershell
contact : Optional[Dict[str, str]] = None
married : Optional[bool] = False
```

- **Annotated:**
<br>
We use Annotated mostly with Field(), defining the metadata and the data type. That metadata could be a string or a data validation function like Field(), Query(), etc.
<br>
It should look like this. Annotated[datatype, Field()]
<br>
The default value can be defined after Annotated[] like Annotated[] = None OR in the Field(default=)
<br>
```powershell
contact : Annotated[Optional[Dict[str, str]], Field()] = None
married : Annotated[Optional[bool], Field(default=False, description="Should be correct as in the NIC")]
```