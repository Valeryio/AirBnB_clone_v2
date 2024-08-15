#!/usr/bin/env python3

from models import storage
from models.state import State

result = storage.all()
print("The result : ", result)
