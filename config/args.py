import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--config_file", type=str, default="./config/config.yml", help="Path to the configuration YAML file")
parser.add_argument("--prompts_file", type=str, default="./config/prompt.yml", help="Path to the prompts YAML file")
parser.add_argument("--exp_report_file", type=str, default="./exp/report.csv", help="Path to the experimental results file")
parser.add_argument("--num_gpus", type=str, default="auto", help = "Number of GPUs for distributed inference")
parser.add_argument("--exp", type=str, default=None, help = "Experiment Options (current options: sc, ...)")
parser.add_argument("--use_vllm", type=bool, default=True, help= "Check if you want to use vLLM for inference")
parser.add_argument("--model_cache_dir", type=str, default=None, help= "Assign huggingface cache directory, if needed")
parser.add_argument("--model_branch", type = str, default=None, help= "Used when you want to utilize models other than the main branch in huggingface")

def get_args():
    args = parser.parse_args()
    if args.model_cache_dir:
        os.environ['HF_HOME'] = args.model_cache_dir
    return args