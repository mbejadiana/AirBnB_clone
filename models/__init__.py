#!/usr/bin/python3
"""
unique file storage instance
"""

from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
