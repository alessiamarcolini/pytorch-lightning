# Copyright The PyTorch Lightning team.
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
# limitations under the License
from typing import Optional

from pytorch_lightning.accelerators.legacy.ddp_hpc_accelerator import DDPHPCAccelerator
from pytorch_lightning.plugins.environments import ClusterEnvironment
from pytorch_lightning.plugins.legacy.ddp_plugin import DDPPlugin


class DDPCPUHPCAccelerator(DDPHPCAccelerator):

    def __init__(self,
                 trainer,
                 cluster_environment: Optional[ClusterEnvironment] = None,
                 ddp_plugin: Optional[DDPPlugin] = None):
        """
        Runs training using DDP (with CPUs) strategy on a cluster

        Example::

            # default
            trainer = Trainer(accelerator=DDPCPUHPCAccelerator())

        """
        super().__init__(trainer, cluster_environment, ddp_plugin)
        self.nickname = 'ddp_cpu'

    def model_to_device(self, model):
        model.cpu()

    def get_device_ids(self):
        device_ids = None
        return device_ids

    def init_device(self, process_idx):
        pass
