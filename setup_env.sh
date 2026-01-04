#!/bin/bash
# 设置 PYTHONPATH 以便能够导入 engmod 包
# 使用方法: source setup_env.sh

export PYTHONPATH="/home/gaoch:${PYTHONPATH}"
echo "✓ PYTHONPATH 已设置为包含 /home/gaoch"
echo "  现在可以导入 engmod 包了"

