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

"""Benchmark constants."""
import os
import file_utils

# 获取项目根目录（common 目录的父目录）
_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 数据目录：包含 benchmark 问题的 JSON 文件
DATA_DIR = os.path.join(_PROJECT_ROOT, 'data', 'benchmark')

# 注释库目录：包含 annotated_snippets_v1.json 的目录
LIB_DIR = os.path.join(_PROJECT_ROOT, 'data', 'library')

# Prompt 模板目录：包含 prompt_v0_nosol.txt 等模板文件
PROMPTS_DIR = os.path.join(_PROJECT_ROOT, 'common', 'prompts')

# 系统工件目录：mphclient 可以访问的本地文件路径，用于保存生成的代码文件
SYSTEM_ARTIFACT_DIR = os.path.join(_PROJECT_ROOT, 'artifacts')

# 工作实验目录：实验输出的工作目录
WORKING_EXPERIMENT_DIR = os.path.join(_PROJECT_ROOT, 'experiments', 'working')

# 最终实验目录：最终实验输出目录
FINAL_EXPERIMENT_DIR = os.path.join(_PROJECT_ROOT, 'experiments', 'final')

# 物理文档目录：包含 physics_interfaces.json 和 interface_feature_map.json
PHY_DOC_DIR = os.path.join(_PROJECT_ROOT, 'data', 'docs')

LIB_PATH = os.path.join(LIB_DIR, 'annotated_snippets_v1.json')

BENCHMARK_PROBLEMS = (
    'comsol_82',
    'comsol_75611',
    'comsol_266',
    'comsol_723',
    'comsol_265',
    'comsol_453',
    'comsol_12351',
    'comsol_12677',
    'comsol_12681_gravity',
    'comsol_12681_force',
    'comsol_19275',
    'comsol_1863',
    'comsol_267',
    'comsol_10275',
    'comsol_16635',
)

# VertexAI const
VERTEX_SERVICE_ACCT = 
VERTEX_PROJECT_ID = 
VERTEX_LOCATION = 

ANTHROPIC_PATH = 
OPENAI_PATH = 


def get_api_key(model_type: str) -> str:
  if model_type == 'anthropic':
    return file_utils.file_open(ANTHROPIC_PATH, 'r').read().strip()
  elif model_type == 'openai':
    return file_utils.file_open(OPENAI_PATH, 'r').read().strip()
  else:
    raise ValueError('Unsupported model type: %s' % model_type)
