# Copyright 2009 10gen, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Python driver for MongoDB."""

from pymongo.connection import Connection as PyMongo_Connection

ASCENDING = 1
"""Ascending sort order."""
DESCENDING = -1
"""Descending sort order."""

OFF = 0
"""No database profiling."""
SLOW_ONLY = 1
"""Only profile slow operations."""
ALL = 2
"""Profile all operations."""

version = "1.2+"
"""Current version of PyMongo."""

Connection = PyMongo_Connection
"""Alias for :class:`pymongo.connection.Connection`."""
