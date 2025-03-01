# Django Forms Configuration

## Overview

Experiment 2 implements form handling for the car ownership management system, providing user-friendly interfaces for data input and validation.

## Form Classes

### Owner Form

```python
from django import forms
from .models import Owner

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['last_name', 'first_name', 'birth_date']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'})
        }
```

### Car Form

```python
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['license_plate', 'make', 'model', 'color']
```

### DrivingLicense Form

```python
from .models import DrivingLicense

class DrivingLicenseForm(forms.ModelForm):
    class Meta:
        model = DrivingLicense
        fields = ['owner', 'license_number', 'document_number', 'type', 'issue_date']
        widgets = {
            'issue_date': forms.DateInput(attrs={'type': 'date'})
        }
```

### Ownership Form

```python
from .models import Ownership

class OwnershipForm(forms.ModelForm):
    class Meta:
        model = Ownership
        fields = ['owner', 'car', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'})
        }
```

## Form Features

1. Data Validation
   - Field type validation
   - Required field checking
   - Custom validation rules

2. Widget Customization
   - Date input widgets
   - Select widgets for relationships
   - Custom field rendering

3. Error Handling
   - Field-specific error messages
   - Form-wide error messages
   - Validation error display

4. Form Processing
   - GET/POST handling
   - Data cleaning and normalization
   - Model instance creation/update

## Usage Examples

### View Implementation

```python
def owner_create(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            owner = form.save()
            return redirect('owner_detail', owner_id=owner.id)
    else:
        form = OwnerForm()
    return render(request, 'owner_form.html', {'form': form})
```

### Template Usage

```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
```

## Form Validation Rules

1. Owner Form
   - Last name and first name required
   - Birth date must be in the past

2. Car Form
   - License plate must be unique
   - Make and model required

3. DrivingLicense Form
   - License number must be unique
   - Issue date required
   - Valid license type selection

4. Ownership Form
   - Valid owner and car selection
   - Start date required
   - End date must be after start date if provided 