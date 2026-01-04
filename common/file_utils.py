# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#   https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""File utility functions."""

import os
from typing import IO, Any


def file_open(filepath: str, mode: str = 'r', **kwargs) -> IO[Any]:
  """Open a file and return a file object.
  
  This is a wrapper around Python's built-in open() function.
  
  Args:
    filepath: Path to the file to open.
    mode: File mode (e.g., 'r', 'w', 'a', 'rb', 'wb').
    **kwargs: Additional arguments to pass to open().
  
  Returns:
    A file object that can be used as a context manager.
  """
  return open(filepath, mode, **kwargs)


def file_exists(filepath: str) -> bool:
  """Check if a file or directory exists.
  
  Args:
    filepath: Path to check.
  
  Returns:
    True if the path exists, False otherwise.
  """
  return os.path.exists(filepath)


def listDir(dirpath: str) -> list[str]:
  """List all files and directories in a directory.
  
  Args:
    dirpath: Path to the directory.
  
  Returns:
    A list of file and directory names in the directory.
  """
  if not os.path.isdir(dirpath):
    raise ValueError(f'Path is not a directory: {dirpath}')
  return os.listdir(dirpath)


def makedirs(dirpath: str, exist_ok: bool = True) -> None:
  """Create a directory and all intermediate directories.
  
  Args:
    dirpath: Path to the directory to create.
    exist_ok: If True, do not raise an error if the directory already exists.
  """
  os.makedirs(dirpath, exist_ok=exist_ok)


# Alias for file_open (used in some parts of the codebase)
Open = file_open

