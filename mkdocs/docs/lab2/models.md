# Django Models Configuration

## Overview

Experiment 2 implements a car ownership management system using Django models. The system manages relationships between owners, cars, driving licenses, and ownership records.

## Model Classes

### Owner Model

```python
from django.db import models

class Owner(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
```

### Car Model

```python
class Car(models.Model):
    license_plate = models.CharField(max_length=10, unique=True)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.make} {self.model} ({self.license_plate})"
```

### DrivingLicense Model

```python
class DrivingLicense(models.Model):
    owner = models.OneToOneField(Owner, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=20, unique=True)
    document_number = models.CharField(max_length=20)
    type = models.CharField(max_length=10)
    issue_date = models.DateField()

    def __str__(self):
        return f"License {self.license_number} ({self.owner})"
```

### Ownership Model

```python
class Ownership(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.owner} owns {self.car}"
```

## Model Relationships

1. Owner - DrivingLicense
   - One-to-One relationship
   - Each owner can have one driving license
   - Cascade deletion when owner is deleted

2. Owner - Car (through Ownership)
   - Many-to-Many relationship
   - Owners can own multiple cars
   - Cars can have multiple owners (over time)
   - Ownership model tracks the relationship period

## Field Types

1. Character Fields
   - `CharField`: For text data with maximum length
   - Used for names, license plates, etc.

2. Date Fields
   - `DateField`: For storing dates
   - Used for birth dates, issue dates, etc.

3. Relationship Fields
   - `OneToOneField`: For one-to-one relationships
   - `ForeignKey`: For many-to-one relationships

## Model Features

1. String Representation
   - Custom `__str__` methods
   - Human-readable object representation

2. Field Constraints
   - Unique constraints
   - Maximum length limits
   - Required/optional fields

3. Cascade Deletion
   - Automatic deletion of related records
   - Data integrity maintenance

4. Data Validation
   - Field type validation
   - Unique constraint checking
   - Required field validation

## Database Schema

```sql
CREATE TABLE Owner (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    last_name VARCHAR(50) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    birth_date DATE NOT NULL
);

CREATE TABLE Car (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    license_plate VARCHAR(10) UNIQUE NOT NULL,
    make VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    color VARCHAR(20) NOT NULL
);

CREATE TABLE DrivingLicense (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    owner_id INTEGER UNIQUE NOT NULL,
    license_number VARCHAR(20) UNIQUE NOT NULL,
    document_number VARCHAR(20) NOT NULL,
    type VARCHAR(10) NOT NULL,
    issue_date DATE NOT NULL,
    FOREIGN KEY (owner_id) REFERENCES Owner(id) ON DELETE CASCADE
);

CREATE TABLE Ownership (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    owner_id INTEGER NOT NULL,
    car_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    FOREIGN KEY (owner_id) REFERENCES Owner(id) ON DELETE CASCADE,
    FOREIGN KEY (car_id) REFERENCES Car(id) ON DELETE CASCADE
);
``` 