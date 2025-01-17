# Copyright 2020 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Types internal to TensorFlow.

These types should not be exported. External code should not rely on these.
"""


# TODO(mdan): Is this strictly needed? Only ops.py really uses it.
class NativeObject(object):
  """Types natively supported by various TF operations.

  The most notable example of NativeObject is Tensor.
  """


class TensorSpec(object):
  """Interface for internal isinstance checks to framework/tensor_spec.py.

  This helps to avoid circular dependencies.
  """
