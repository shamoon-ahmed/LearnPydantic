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

We can say **contact : list** , but we don't know what data type is user going to insert in the list and we want string in it. We're just saying that it should be a list. That's it.
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

## Field Validator - @field_validator:

**@field_validator** is a decorator used with Pydantic to validate a certain field. Without @field_validator we would have to type checking, coerce data, apply constraints, etc manually. With **@field_validator**, we write our own logic to validate a certain field, raise custom error messages, etc.

We use **@field_validator** as a decorator above the function and pass the field in 'quotes' that we want to validate

```powershell
from pydantic import BaseModel, field_validator

class Patient(BaseModel):
    email : str

    @field_validator('email')
    def validate_email(value):

        valid_domains = ['piaic.com', 'smiu.edu']

        domain = value.split('@')[-1]

        if domain in valid_domains:
            return value
        raise ValueError('Unregistered Email!')
```

### mode='before' OR mode='after'

**mode** tells Pydantic when to validate and coerce the field.
For instance when converting "30" into 30, we tell Pydantic if we want the raw input "30" so we say mode='before'.
This brings us the unvalidated and non-coerced data. On the other hand mode='after' brings the coerced data.

Remember: By default, mode is after. mode='after'

```powershell
@field_validator('age', mode='before') # setting mode='before' means we want the value before any validation/coersion happens 
    def validate(value):
        if 0 < value < 120:
            return value
        return ValueError('Invalid Age!')
```

So, as @field_validator only allows to validate a single field, we need something that allows validation operation with multiple fields

This is where the next validator comes in

## Model Validator

**@model_validator** allows us to use the entire Pydantic model and validate any field we want.
Just need to pass the mode in the decorator and model in function, and we can write our own custom logic for validation.

Take a look at this code snippet:

```powershell
from pydantic import BaseModel, model_validator

class Patient(BaseModel):
    name : str
    age : int = Field(gt=0, lt=120)

    @model_validator(mode='after')
    def registration_eligibility_for_old(cls, model):
        if model.age >= 60 and 'emergency' not in model.contact_info:
            raise ValueError('Patients aged 60 and above must have an emergency number!')
        return model
```